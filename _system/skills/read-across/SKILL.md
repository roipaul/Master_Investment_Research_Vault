---
name: "read-across"
description: "Carry what earlier research on adjacent companies established into new work: map adjacent companies, collect a what-we-already-know pack before a primer or thesis, and file reusable learnings into shared industry and business-model notes. Use for /read-across."
---

# Read-across

Each company the user researches teaches something about its rivals, its customers, its suppliers and other businesses built the same way. This skill makes that knowledge reusable. It keeps a map of which companies are adjacent, files what was learned into shared notes, and hands new work a short pack of what is already known, so that a new primer or thesis builds on earlier research instead of starting from the filings alone.

The user is an experienced equity analyst running his own and his family's money. Two rules protect the new work from the old:

- **Facts carry over; judgments do not.** Facts, patterns and benchmarks feed the primer. An earlier verdict or view reaches only the debate and the thesis, labelled as a hypothesis to test on the new company's own evidence.
- **A learning describes the company it came from, or the industry. It never describes the new company.** Facts about the new company still come only from its own filings.

## Modes

- `/read-across TICKER` — **Collect.** Build the pack before a gate, primer, debate or thesis.
- `/read-across TICKER file` — **File.** After a primer, debate, due diligence, earnings update or decision review, move the reusable learnings into the shared notes.
- `/read-across TICKER extract` — **Extract.** Pull learnings out of an older company's existing documents, once. Collect calls it when it meets an adjacent company with documents but no learnings on file.
- `/read-across TICKER confirm` — record the user's confirmation, edit or rejection of proposed patterns and lessons, and of proposed analogues. Only he can run this.

## Knowledge base (start)

Run the `research-kb` read step. Read the hub, `Prior.md` if it exists, and the shared notes the hub names. If the vault is unreachable, say so, work from what is in the conversation, and send the files at the end.

## The map of adjacent companies

Each hub carries three fields, added if missing:

- `industry:` the slug of its industry note, `themes/<industry>.md`.
- `model_tags:` one to three business-model tags from the list in `themes/README.md` (for example: franchise network, marketplace, distributor, branded consumer product, capital-equipment maker, commodity producer, lender, subscription software, logistics network). Add a tag to that list only when none fits, and log it there.
- `adjacent:` a list of `ticker`, `relation`, `basis` (one line, with its source) and, for analogues, `confirmed`.

Three relations count as adjacent. Same owner and same policy regime do not; those stay with the entity and policy notes.

| Relation | How it is found |
|---|---|
| Competitor, or same industry | The primer's industry sections and the filings; any hub with the same `industry` |
| Customer or supplier | The primer's customers and suppliers sections and the filings |
| Business-model analogue | A shared `model_tags` entry. Propose at most three, with one line on why the comparison teaches something. An analogue is used only after the user confirms it |

Write every relation to **both** hubs. A relation found in a filing is written as it is found. Do not infer a customer or supplier link the filings do not state.

## What a learning is

A learning is one short, dated, sourced item that would help research on another company. It is one of four kinds:

| Kind | Example | Filed |
|---|---|---|
| Fact | A cost position, a share figure, a contract term, how a channel takes inventory | Automatically, if it has a primary source |
| Benchmark | Margins, returns, payout, working-capital days of a named company for a named period | Automatically, if it has a primary source |
| Pattern | How a kind of customer, regulator or competitor has behaved more than once | **Proposed**; it waits for the user |
| Open question | Something this work could not answer that an adjacent company might | Automatically |

A lesson from a resolved view or a reviewed decision is a pattern, and is proposed in the same way.

Not a learning: a company detail with no bearing elsewhere, a price, a valuation, a verdict, a zone, a conviction level, or anything without a source.

Learnings live in the shared notes, never in a company's folder: the industry note `themes/<industry>.md`, and for something true of a business model, `themes/model-<tag>.md`. Each note has one table, appended to and never rewritten:

`L# | Date | Kind | Learning | Applies to | From (company and document) | Original source | Data through | Status`

**Status** is one of: current, proposed, superseded by L#, answered by L# (for an open question), rejected.

## Collect

1. **Find the adjacent companies.** Use the hub's `adjacent`, any hub that lists this ticker, hubs with the same `industry`, and confirmed analogues. For a company with nothing on file yet, match the competitor, customer and supplier names from its gate note or filings against the `companies/` folder.
2. **Rank and cap at five:** direct competitor, then customer or supplier, then same industry, then confirmed analogue; within a rank, the more recent work first. Name any left out.
3. **Extract where needed.** If an adjacent company has a primer or thesis but its hub has no `learnings_filed` date, run Extract on it first, at most two a run, and list the rest as waiting.
4. **Apply the age rule.** A fact or pattern whose data is more than 12 months old, or a benchmark that depends on a price and is more than six months old, is marked "as of <date>". It may be cited with that date and must be re-checked before it is stated as current.
5. **Write the pack** to `companies/<TICKER>/Prior.md`, one to two pages, as a dated section:

```
1. Adjacent companies used, with the relation and why; any left out
2. Facts to reuse: each with its L#, date, original source and status
3. Benchmarks: name | metric | value | period | source
4. Open questions inherited from earlier work
5. To test against this company's filings: earlier learnings the new
   filings could confirm or contradict
6. Hypotheses from earlier judgments (debate and thesis only): each written
   as "earlier judgment on <company>, to be tested here", with what would
   show it does or does not hold for this company
7. Proposed analogues and proposed patterns awaiting the user
8. Gaps: adjacent work that is missing, stale or still to extract
```

If nothing adjacent is on file, write a three-line pack that says so. That is a normal result for the first company in an industry.

**Who uses which sections**

| Work | Uses |
|---|---|
| Pre-primer gate | One line: how many adjacent companies are on file and the single most relevant learning |
| Full primer | Sections 2 to 5 only, never section 6 |
| Debate and thesis | All sections. Each item in section 6 must be answered for this company on its own evidence, and may turn out not to apply |

## File

1. Read the document just written and list the candidate learnings, with the kind of each.
2. **Check each against the notes.** If the learning is already there, add "confirmed again by <company>, <date>" to the existing row's log line instead of filing a duplicate.
3. **File facts, benchmarks and open questions** that have a primary source. A candidate without one is not filed.
4. **Propose patterns and lessons.** Give them status `proposed`, and add "confirm learnings: /read-across TICKER confirm" to the hub's `awaiting`. In Confirm, record his wording where he changes it.
5. **Handle conflicts.** Where the new company's primary filing contradicts an earlier learning, the newer primary source wins. Mark the old row superseded with the new L#, never delete it, and add "re-check: L# superseded" to the `awaiting` field of the company it came from.
6. **Answer open questions.** If this work answers an inherited question, mark it answered with the L# that answers it.
7. Update the map on both hubs, and set `learnings_filed` to today on this hub.

**Extract** is File run over an older company's existing primer, thesis, debate and earnings files. It files nothing that the documents do not support, and proposes patterns in the same way.

## Output

- `companies/<TICKER>/Prior.md` (frontmatter: `type: document`, `doc: prior`, `tickers`, `updated`, `data_through`, `sources: [skill:read-across]`). Each Collect adds a dated section.
- The shared notes, appended to.
- Hub fields: `industry`, `model_tags`, `adjacent`, `learnings_filed`, and any `awaiting` line; a dated `## Log` line.

Commit per `research-kb` (message `<TICKER>: read-across <date> — <one line>`).

Reply in a few lines. For Collect: the adjacent companies used, the three most useful things already known, anything to test, and what is waiting on him. For File: how many learnings were filed by kind, any conflict, and any pattern or analogue proposed.

## Standards

- Plain English. Every learning carries its date, the document it came from and its original source.
- Never state or adjust the user's views. An earlier view of his is quoted with its date and labelled as earlier.
- The pack is short. If it runs past two pages, it is carrying company detail that belongs in the company's own documents.
- Quotes under 15 words, one per source; paraphrase otherwise. Summarise broker material and never copy it.
- No price target, fair value, buy/sell or sizing language.