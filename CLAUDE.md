# CLAUDE.md — the AYOUNI Writing Framework

This folder is the writing framework of the AYOUNI books. It is not a book. Read `FRAMEWORK.md` whole before touching prose in any book of `../books/`.

## When you work on a book

- The book's own `CLAUDE.md` and brief come first; this framework is what they instantiate. Where they are silent, the framework rules.
- Before drafting or revising a chapter: run `tools/style_lint.py` on it after; give it to a fresh reader with `briefs/voice-reader.md` when the voice is in question, with `briefs/fresh-verifier.md` when the facts are; apply fixes through `briefs/fixer.md`.
- Never: set `status: read`; answer an `[AUTHOR: …]` marker except under `briefs/answer-policy.md` on the author's word; invent a name, date, place, memory or sentence of the author's; name a person from a record; edit a chapter the author wrote himself (report on it); add a sustained metaphor; add a stake.
- Always: write "AI model" / "AI agent" where the bare word is ambiguous (AWF-10); size type by semantic level (AWF-09: book > part > chapter > section > body; a heading above the text it heads; labels at 12px or more; one scale, checked at build); say where the chapter stops; print the loss beside the win; keep the counted sets' names exact; read numbers, never compose them; end a phase with a memo (`templates/memo.md`), and report to the author in that memo format in every substantive message, not only at a phase's end (AWF-11).

## When you change the framework

- A change is a decision: add a row to `DECISIONS.md` with the reason and the date, and bump the version in `FRAMEWORK.md` (0.x while the author has not ruled on the author's calls list).
- Evidence first: a new rule cites a passage of the Ring book study, a copyedit finding, or a book's verification result.
- The author's rules bind here too: no "substrate"; "crafter", never "maker" (outside "decision-maker"); never the names of other repositories' products; no emojis in anything a reader sees.
