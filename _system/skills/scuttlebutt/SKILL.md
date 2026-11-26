---
name: "scuttlebutt"
description: "Mine public posts (forums, review and complaint sites, employee boards, video transcripts) for what a company's customers, channel, workers or developers say, mapped to the debate questions, plus a shortlist of creators and communities to approach for interviews."
---

# Scuttlebutt from public posts

The user has no expert network. This workflow is the substitute: it reads what the people inside a business's ecosystem already say in public, maps it to the questions the thesis debate left open, and builds a list of people he can approach himself for short paid interviews.

It produces evidence and a contact list. It does not contact anyone, does not collect phone numbers or private details, and does not work around blocked sites.

## Inputs

1. **The questions.** From the thesis debate scorecard (preferred) or the primer's Section 5. Keep the question numbers so findings map back.
2. **The constituencies.** Pick the two or three groups that can answer them. Candidates: end customers or consumers; business customers and the people who run the product day to day (admins, procurement, clinicians, plant engineers); channel — dealers, distributors, installers, contractors, resellers, franchisees; supply side — suppliers, gig workers, drivers, couriers, hosts, merchants; employees and former employees; developers and integrators; patients and providers; regulators' public comment files.
3. **The vocabulary.** Product, plan, fee, feature and programme names and slang in the language the constituency uses. Pull them from the primer and a first round of searching; the research is only as good as the search terms.

## Step 1 — Mine the posts (parallel subagents, one per constituency)

Pick sources by constituency and market:

| Constituency | Global / US / Europe | Japan | Korea | Taiwan | China |
|---|---|---|---|---|---|
| Consumers | Reddit, Trustpilot, Amazon and app-store reviews, BBB, CFPB complaints, YouTube transcripts, X | 価格.com, 5ch, X, YouTube | 네이버 카페, 클리앙, 뽐뿌, YouTube | PTT, Dcard, Mobile01 | 黑猫投诉, 知乎, 小红书, 贴吧, 抖音/快手/B站 transcripts, app-review mirrors |
| Business users | G2, Capterra, TrustRadius, Gartner Peer Insights, Reddit r/sysadmin-type subs, trade forums, Stack Overflow, GitHub issues | ITreview, Qiita | 블라인드 industry boards | PTT tech boards | 知乎, CSDN, 脉脉 |
| Channel / contractors / franchisees | Trade forums (e.g. contractor, dealer, pool, HVAC, auto-dealer boards), Facebook groups, franchise-review sites, YouTube trade channels | 業界 forums, X | 네이버 카페 (업종별) | Mobile01, Facebook groups | 贴吧, 快手/抖音 trade creators, 卡车之家-type trade sites, 雪球 (Xueqiu) merchant and operator posts |
| Supply side / gig workers | Reddit driver/host/courier subs, UberPeople-type forums, YouTube | X, YouTube | 블라인드, 네이버 카페 | PTT | 抖音/快手 creators, 贴吧, 黑猫 |
| Employees | Glassdoor, Blind, Indeed, Fishbowl, LinkedIn posts | OpenWork, 転職会議 | 블라인드, 잡플래닛 | 面試趣, Qollie | 脉脉, 看准网 |
| Developers | GitHub, Hacker News, Stack Overflow, Discord/forum archives | Qiita, Zenn | OKKY | iThome | CSDN, V2EX, 掘金 |

Brief each subagent with: the question list and the specific sub-questions for that constituency (what they pay, how it changed by year, which alternatives they also use, whether they bypass the company, volume and price conditions, service quality, switching); the vocabulary; the rule "evidence only, with URL and date, at most one quote under 15 words per post, no opinions"; and the instruction to report what was blocked.

Ask for a tally, not just anecdotes: how many posts say X over what period. Say which way the sample skews (complainers, one region, one segment) and what was not found.

Xueqiu (雪球) is mined in the main thread with the built-in browser, not by a subagent, because its search needs the user's browser. The method is in `research-portals`:

- read post pages as text;
- for search, fetch `/query/v1/search/status.json?q=<term>` from a xueqiu.com tab (page 1 only);
- search in Chinese with fee, tool and rule names.

Xueqiu mixes investors talking their book with merchants describing their costs. Tally the two separately.

## Step 2 — Build the interview shortlist

For each constituency, 15–30 creators or active posters, in tiers:

- **Tier A — discuss the company directly**: handle, platform, follower count with date, role/base if stated, profile or post URL, what they said (paraphrased, dated), suggested angle for an interview.
- **Tier B — large reach in the constituency**: same fields, even if they have not named the company.
- **Communities**: forums, subreddits, hashtag threads, official-account comment sections, trade associations, regional groups — with a note on ownership bias (a community run by a competitor or a vendor).

Contact routes only if public (a business-inquiry note, a public account, a newsletter); never personal numbers or addresses.

## Step 3 — Synthesis

Write `<Company>_<TICKER>_<Constituency>_Voice.md`:

1. **Scope and bias** — sources read, sources blocked, how the sample skews.
2. **By debate question** — what the posts show (with counts), what it implies for the bull or bear side, and any regulatory read-across (a practice a regulator has already made a peer unwind is a risk flag).
3. **Other constituencies** — in a few lines if also mined.
4. **Interview targets** — the tiered list and communities.
5. **Questions to ask** — five to eight per constituency, phrased for a 20-minute call, ordered from the deciding question down.

Save to the project with `project_write`, send the working files (evidence tally and creator table), and give the user the two or three findings that move a question in the reply.

## Standards

- Count before you characterise: "7 posts" beats "many users".
- Label inference. A feature seen in posts is not a disclosed policy.
- Quotes under 15 words, one per source; paraphrase otherwise.
- Say when the evidence is from a constituency with a grievance and whether the silent majority would likely differ.