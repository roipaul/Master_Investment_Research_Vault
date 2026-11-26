---
name: "research-portals"
description: "Pull broker research (Bernstein, CLSA), Capital IQ transcripts, financials, filings and insider data, and Xueqiu posts through the built-in browser when a research step needs estimates, channel checks or chatter."
---

# Research portals

The user has his own logins to Bernstein, CLSA and Capital IQ, and reads Xueqiu. The other research skills (desk-dd, thesis-debate, earnings-update, thesis-update, variant-view, scuttlebutt) call this one when a question needs any of these:

- broker estimates of KPIs the company does not disclose;
- channel checks;
- a call transcript, consensus or insider data;
- Chinese investor or merchant chatter.

## Ground rules

- **Browser.** Use the built-in browser and load the `built-in-browser` skill first.
- **Sign-ins.** The user signs in himself. Never type passwords, never bypass a CAPTCHA, and reject non-essential cookies.
- **Blocked sites.** If a page needs access to another host (for example a CDN), call `request_access` for that host.
- **Dropped sessions.** If the browser session drops, retry once. Then tell the user and ask for exports (PDF or xlsx) rather than looping.
- **Reading.** Read pages as text, not screenshots. Do heavy parsing one report per call, because batches time out.
- **What gets written down.** Facts, estimates and dates, each with the broker, report title, date and URL. Quotes stay under 15 words, one per source. Never put report text in the vault or the Project, and never write account identifiers.
- **Labels.** A broker number is an estimate and a channel check is the broker's finding. Label them that way, not as facts.

## Which source for which need

| Need | First source | Check against |
|---|---|---|
| KPIs the company does not disclose (GMV, take rate, segment losses) | Bernstein and CLSA estimate tables; consensus | Official or third-party data (statistics bureau, industry data, the company's reported lines) |
| Industry events and fee changes (shopping festivals, merchant fees) | CLSA and Bernstein channel checks | Platform notices; merchant posts |
| Transcripts, consensus, financial history, filings | Capital IQ | The company's own releases and filings |
| Insider transactions and ownership | Capital IQ | EDGAR Forms 3/4/144 and 13D/G; HKEX disclosure of interests |
| What merchants and Chinese investors say | Xueqiu | Scuttlebutt sources |

## Bernstein

1. Open the ticker page: `https://www.bernsteinresearch.com/brweb/ticker.aspx?id=<id>#/`.
2. List the reports, newest first.
3. Open each report as HTML at `/brweb/ViewResearchHtml.aspx?cid=<cid>&downloadid=<id>` and read it with `get_page_text`.
4. Pull:
   - quarterly estimate tables (take rate, GMV, segment profit);
   - channel-check findings;
   - accounting changes the analyst flags, such as reclassifications into contra-revenue.

## CLSA

1. Open the company page: `https://www.clsa.com/member/company/?clsa_id=<id>&option=company-page`.
2. Reports are PDFs at `/member/reports/<id>.pdf`.
3. Many of these PDFs use CID fonts, so plain text extraction returns garbage. Instead:
   - fetch the PDF from inside the signed-in tab;
   - map each font's ToUnicode CMap in JavaScript;
   - decode one report per call.
4. Keep the parser on `window` so the rest of the session can reuse it.

## Capital IQ (CIQ Pro)

1. **Find the company.** Look up its MI key with search.
2. **Unblock the app.** It needs site access to `cdn.spgi.spglobal.com` before it renders. Reject cookies.
3. **Avoid the menu pages.** These routes render slowly or stay blank:
   - `#company/transcripts?id=`
   - `#company/insiderActivity?Id=`
   - `#company/investmentresearch?id=&type=1`

   Use the APIs the app calls instead, which you can find with `read_network_requests`.
4. **Transcripts.** Call `/apisv3/docviewer-service/api/v1/metadata/bff?mid=<mid>&isPropDoc=false`. It returns `docFetchMetadata.downloadUrl`, which holds the text. Search the text for the line items in question, such as unexplained losses or accounting changes.
5. **Insider activity.** Always reconcile it against the primary filings.
6. **If it fails twice,** ask the user for exports.

## Xueqiu (雪球)

- **Post pages** (`xueqiu.com/<uid>/<postid>`) read normally with `get_page_text`.
- **Search** needs a login in the page itself. Instead, fetch `/query/v1/search/status.json?q=<query>` from a xueqiu.com tab. Only page 1 returns data.
- **Search terms** should be Chinese product, fee and rule names, for example 全站推, 退款, 技术服务费, 广告.
- **Weighing posts.** Posts are slanted voices: investors talking their book, or merchants with a grievance. Count before you characterise, as in `scuttlebutt`.

## Output

1. **Sell-side and terminal check.** Write a dated section in the calling skill's document. For each question, give:
   - what each source says;
   - the range of estimates;
   - where the brokers disagree;
   - which official data could settle it.
2. **Implied-KPI cross-check.** When brokers' estimates of an undisclosed KPI diverge, show what each estimate implies for the linked KPI, given the line the company does report. For example: reported ad-revenue growth ÷ each GMV estimate → implied take-rate change. Put an official benchmark beside it. If a sheet is in use, build this as a tab.
3. **Rule changes.** When a KPI steps, date the platform and regulatory rule changes around it and say whether the step laps in four quarters.
4. **IR questions.** Add any IR questions the reports raise: one topic each, with the figure and its source.
5. **Hub.** Record the portal ids (Bernstein ticker id, CLSA id, Capital IQ MI key) in the hub frontmatter as `portals:`, so the next run goes straight there.