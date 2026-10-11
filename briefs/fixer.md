# Brief: apply a reader's report to a chapter

A fresh reader checked one chapter (for its facts with `fresh-verifier.md`, or for its voice with `voice-reader.md`) and wrote a report. Its items are claims. The reader is a model like you; it can be wrong. You decide each item yourself, from the evidence.

## For each item
1. Open the evidence it cites (the record at the pin, the run data, the drafts, the page itself). A few minutes per item, not more.
2. If you **confirm** it: make the smallest edit that makes the sentence true to the evidence (or the voice true to the framework), in the book's voice: first person, plain words, short sentences, long-then-short. Prefer *narrowing* a claim to what the evidence says over deleting it. Where a claim is general knowledge, mark it as the book marks such claims.
3. If you **cannot confirm** it: leave the text and say so in your report with what you looked at.
4. Make the same edit in every language the book has (same-named file), in that language's style sheet. The translated page keeps the same number of paragraphs, headings, list items and table rows.
5. Reading problems: fix them only when the fix is one sentence (define a term where it first appears). Skip the rest and say so.

## Rules (they bind you)
- The answer policy's first rules hold: invent nothing; attribute a sentence to its source; stage words are the book's; no person named; no other repository's product named; the forbidden words stay out.
- **Do not edit any code fence**, and do not edit a chapter the author wrote himself (report instead). Front matter: change the text of stage values and the names in evidence lists only when an item requires it and the named thing exists; change no other key.
- A number printed in prose beside a guard must equal the guard data; if you add one, read it there.
- Where the report shows the record has changed since the chapter was drafted (a site that now says otherwise), state the present reading with its date, or state what the source said when the chapter was drafted, with its date. Prefer the present reading.
- Do NOT run the build, the runner, the printers or the release; you may run the book's checkers (`check_fr`-style, the audit, the lint) and must fix any error they report in your files.
- Edit only your chapter's files. Use small scripts: read bytes, replace an exact string asserted to occur once, write bytes back (files use LF).
- Do not mark a page `read`.

## Report (your final message, under 500 words)
`item · confirmed / not confirmed · what you changed (or why not)`, one line each; then `confirmed C · not confirmed N · reading problems fixed R`; then anything you could not settle.
