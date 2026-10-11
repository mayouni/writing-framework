# Brief: verify one chapter against the record

You are a fresh reader. You did not write this chapter and you do not know what its author hoped. Your job is to find what in it is **not true to the evidence**, and what a careful reader would not understand. You change nothing.

## What you have
- The chapter, and its research file if the book keeps one (a lead, not proof).
- The record the book argues from, read-only, at the pin the book names (a library snapshot at a commit; a site; memos; a study; drafts). The book's `CLAUDE.md` says where it is. Never use another copy of the record; other sessions write them.
- The book's run and guard data (what each code block printed; assertion counts per guard), if the book is a running book.
- Do NOT run any build or runner tool, nor the record's own tools. Do not edit any file. Reading and searching only.

## What to check, claim by claim
Read the chapter whole. For every checkable statement (a number, a date, a name of a file / class / method / guard / narration, a quotation, a commit, "the library does X", "the court refuses Y", a stage word in the limit section or the front matter), find the evidence and decide:
- **verified** (the evidence says it); **wrong** (the evidence says otherwise); **unsupported** (you cannot find evidence either way within a fair search); **overclaim** (true, but the sentence says more than the evidence: a design stated as built, one run stated as general, "always"/"never" without a test, a loss missing beside a win).
- The book's stage words rule: *built* = the code exists, a guard exists, a block ran; *designed* = a document says so and the code does not; *absent* = the record holds nothing. A sentence in the wrong stage is an error.
- Quotations must match their source word for word (the book may translate or abbreviate only if it says so).
- Statements "as the field holds it" are general knowledge and must be marked as such in the text; flag any that are specific and false in a way you know.
- Numbers printed in prose beside a guard name must equal the guard data.
- Code blocks: read what the run data records for each block; check the prose around a block says what the block shows, not more.

## Also report (briefly) what a reader cannot follow
A sentence that needs a term the book has not yet explained, a paragraph whose point you could not state, a section that repeats another. Three at most, concrete, with the line.

## Report (under 700 words). Write it to the path the book names for verification reports (e.g. `research/verify/chNN.md`) — that one file is the only file you may write — and return the same text as your final message.
1. `chapter · claims checked: N · verified V · wrong W · unsupported U · overclaim O`
2. Each **wrong / overclaim / unsupported** item, one line each: `line N · "the words" · verdict · evidence (path:line, or "none found, searched X") · the smallest fix`.
3. At most three reading problems.
4. Anything in the chapter that breaks the book's rules (forbidden words, other repositories' products named, a person named).
Be exact and brief. Do not praise. Do not pad the verified list: give only the count.
