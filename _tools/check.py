#!/usr/bin/env python3
"""Vault check. Run from the vault root.

  python3 _tools/check.py start            mark the start of a run (records the current commit)
  python3 _tools/check.py                  check before a commit (interactive run)
  python3 _tools/check.py --unattended     the same, for a scheduled run: limits and protected fields are enforced

Exit code 0 = no errors, 1 = errors (do not commit until fixed or reported), 2 = the check could not run.
It reads the vault and git only. It never changes a note.
"""
import datetime, os, re, subprocess, sys

try:
    import yaml
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "pyyaml", "--break-system-packages"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        import yaml
    except ImportError:
        print("check: could not run (pyyaml missing)")
        sys.exit(2)

ROOT = os.getcwd()
MARK = os.path.join(ROOT, ".git", "run_start")
STAGES = {"gate", "primer", "triage", "frame", "debate", "evidence", "views", "writeup",
          "decision", "monitoring", "deferred", "dropped"}
REQUIRED = ["type", "ticker", "name", "stage", "track", "updated"]
PROTECTED = ["verdict", "zone", "conviction", "held", "list", "buy_price"]
DOCS = ["Primer", "Abridged", "Triage", "VariantView", "Prior", "MarketRead", "PriceAlone",
        "Debate", "DD", "Scuttlebutt", "Thesis", "Decisions"]
STEP_FILE = {"primer": "Primer.md", "abridged": "Abridged.md", "triage": "Triage.md", "debate": "Debate.md",
             "dd": "DD.md", "scuttlebutt": "Scuttlebutt.md", "writeup": "Thesis.md", "decision": "Decisions.md"}
errors, warns = [], []


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True).stdout


def front(text):
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return yaml.safe_load(parts[1]) or {}


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def items(v):
    if not v:
        return []
    if isinstance(v, list):
        return [str(x) for x in v if str(x).strip()]
    return [x.strip() for x in str(v).split(";") if x.strip()]


def as_date(v):
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})", str(v or ""))
    if not m:
        return None
    try:
        return datetime.date(int(m[1]), int(m[2]), int(m[3]))
    except ValueError:
        return None


if len(sys.argv) > 1 and sys.argv[1] == "start":
    head = git("rev-parse", "HEAD").strip()
    with open(MARK, "w") as f:
        f.write(head)
    print("check: run started at", head[:7])
    sys.exit(0)

UNATTENDED = "--unattended" in sys.argv
today = datetime.date.today()

# settings and limits
try:
    settings = front(read("settings.md")) or {}
except Exception as e:
    settings = {}
    errors.append(f"settings.md: frontmatter cannot be read ({e})")
try:
    monitoring = front(read("monitoring.md")) or {}
except Exception:
    monitoring = {}
lim_cycle = int(settings.get("cycle_items_per_run") or 2)
lim_build = int(settings.get("market_read_builds_per_run") or 3)
lim_earn = int(monitoring.get("max_updates_per_run") or 2)
cap = int(settings.get("max_awaiting") or 10)
stale_days = int(settings.get("frame_stale_days") or 90)

# hubs
hubs, waiting = {}, 0
cdir = os.path.join(ROOT, "companies")
for t in sorted(os.listdir(cdir)):
    d = os.path.join(cdir, t)
    if not os.path.isdir(d):
        continue
    hub = f"companies/{t}/{t}.md"
    if not os.path.exists(os.path.join(ROOT, hub)):
        warns.append(f"{t}: folder has no company page")
        continue
    text = read(hub)
    try:
        fm = front(text)
    except Exception as e:
        errors.append(f"{t}: page frontmatter cannot be read ({str(e).splitlines()[0]})")
        continue
    if fm is None:
        errors.append(f"{t}: page has no frontmatter")
        continue
    hubs[t] = fm
    for k in REQUIRED:
        if fm.get(k) in (None, ""):
            errors.append(f"{t}: required field '{k}' is empty")
    st = str(fm.get("stage") or "").split()[0] if fm.get("stage") else ""
    if st and st not in STAGES:
        errors.append(f"{t}: stage '{st}' is not a known stage")
    if str(fm.get("list") or "") == "buy" and not fm.get("buy_price"):
        errors.append(f"{t}: on the buy list with no buy price")
    if fm.get("buy_price") and str(fm.get("list") or "") != "buy":
        errors.append(f"{t}: has a buy price but is not on the buy list")
    waiting += len(items(fm.get("awaiting")))
    body = text.split("---", 2)[2]
    for doc in DOCS:
        if os.path.exists(os.path.join(d, doc + ".md")) and f"[[{doc}" not in body and f"{doc}.md" not in body:
            warns.append(f"{t}: {doc}.md is not listed on the page")
    steps = fm.get("steps") or {}
    for step, fname in STEP_FILE.items():
        if steps.get(step) and not os.path.exists(os.path.join(d, fname)):
            warns.append(f"{t}: step '{step}' is dated but {fname} is missing")
    has = lambda n: os.path.exists(os.path.join(d, n))
    if has("Debate.md") and not has("VariantView.md"):
        warns.append(f"{t}: debate on file with no frame (order rule; imported or overridden?)")
    if has("Thesis.md") and not (has("VariantView.md") or has("PriceAlone.md")):
        warns.append(f"{t}: thesis on file with no frame or price-alone check (imported or overridden?)")
    fdate = as_date(steps.get("frame"))
    if fdate and (today - fdate).days > stale_days and st not in ("dropped", "deferred"):
        warns.append(f"{t}: frame is {(today - fdate).days} days old (limit {stale_days})")
    u = as_date(fm.get("updated"))
    if u and u > today + datetime.timedelta(days=1):
        warns.append(f"{t}: 'updated' is in the future")
    cp = as_date(fm.get("next_checkpoint"))
    if cp and cp < today:
        warns.append(f"{t}: next checkpoint {cp} has passed")
    fdir = os.path.join(d, "files")
    if os.path.isdir(fdir):
        for fn in os.listdir(fdir):
            if os.path.getsize(os.path.join(fdir, fn)) > 10 * 1024 * 1024:
                errors.append(f"{t}: files/{fn} is over 10 MB")

# what this run changed
base = open(MARK).read().strip() if os.path.exists(MARK) else "HEAD"
changed = {}
for line in git("diff", "--name-status", base).splitlines() + git("diff", "--name-status", "--cached", base).splitlines():
    p = line.split("\t")
    if len(p) >= 2:
        changed[p[-1]] = p[0][0]
for line in git("ls-files", "--others", "--exclude-standard").splitlines():
    changed[line] = "A"

deleted = [f for f, s in changed.items() if s == "D" and f.endswith(".md")]
for f in deleted:
    errors.append(f"{f}: a note was deleted (notes are never deleted unless Paul asks)")

n_cycle = len([f for f in changed if (re.match(r"cycles/[^/]+\.md$", f) and f != "cycles/index.md")
               or (re.match(r"macro/[^/]+\.md$", f) and f != "macro/where-we-stand.md")])
n_build = len([f for f, s in changed.items() if s == "A" and f.endswith("/MarketRead.md")])
n_earn = len([f for f, s in changed.items() if s == "A" and re.match(r"companies/[^/]+/earnings/[^/]+\.md$", f)])
new_hubs = [f for f, s in changed.items() if s == "A" and re.match(r"companies/([^/]+)/\1\.md$", f)]

over = []
if n_cycle > lim_cycle:
    over.append(f"cycle items {n_cycle} against a limit of {lim_cycle}")
if n_build > lim_build:
    over.append(f"market-read first builds {n_build} against a limit of {lim_build}")
if n_earn > lim_earn:
    over.append(f"earnings updates {n_earn} against a limit of {lim_earn}")
for o in over:
    (errors if UNATTENDED else warns).append("run limit passed: " + o)

if waiting > cap:
    msg = f"waiting list {waiting} against a cap of {cap}: no new names"
    if new_hubs:
        (errors if UNATTENDED else warns).append(msg + f"; this run started {len(new_hubs)} ({', '.join(new_hubs)})")
    else:
        warns.append(msg)

# protected fields, scheduled runs only
if UNATTENDED:
    for f in changed:
        m = re.match(r"companies/([^/]+)/\1\.md$", f)
        if not m or changed[f] == "A":
            continue
        old = git("show", f"{base}:{f}")
        try:
            ofm = front(old) or {}
        except Exception:
            continue
        nfm = hubs.get(m[1], {})
        for k in PROTECTED:
            if str(ofm.get(k)) != str(nfm.get(k)):
                errors.append(f"{m[1]}: '{k}' changed in a scheduled run ({ofm.get(k)!r} to {nfm.get(k)!r})")
    if "settings.md" in changed:
        try:
            ofm = front(git("show", f"{base}:settings.md")) or {}
            if str(ofm.get("dials")) != str(settings.get("dials")):
                errors.append("settings.md: the confirmed dials changed in a scheduled run")
        except Exception:
            pass

for e in errors:
    print("ERROR  ", e)
for w in warns:
    print("warning", w)
print(f"check: {len(errors)} errors, {len(warns)} warnings; limits this run: cycle {n_cycle}/{lim_cycle}, "
      f"market-read builds {n_build}/{lim_build}, earnings {n_earn}/{lim_earn}; waiting {waiting}/{cap}"
      + ("; scheduled run" if UNATTENDED else ""))
sys.exit(1 if errors else 0)
