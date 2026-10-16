# Release checklist — the gates, in order

The first that fails stops the release. A book's `release.py` runs them; this is the list it implements.

1. **The run.** Every runnable block ran at the pinned record and kept its promise; no block changed since its last run; outputs live in data, never in source.
2. **The guards.** Every guard the book names exists in the record's test tree and its count is read from there.
3. **The audit.** The book's own rules: forbidden words; references to pages that exist; at most three `[AUTHOR]` questions per chapter; no repeated paragraph; glossary citations true; evidence files exist; counts match lists.
4. **The lint.** `tools/style_lint.py --strict` on every language.
5. **The translation check.** Every translated page matches its English page in shape, front matter and code bytes; vocabulary from the style sheet.
6. **The verification.** Every chapter has a fresh-reader verification report newer than its last substantive edit, and its findings were applied or refused with a reason.
7. **The author's approval.** `status: published`, set by the author, on every page (a release); otherwise the manifest and the colophon say **proof copy** and count the pages by stage (draft, in review, published). A page never moves stage without the author's word, and the house registry records the pages he moved.
8. **The artefacts.** The reader, the agents' form (`book.json` against its schema, `llms` files), the PDF, the ePub; each with size and hash in the manifest, with the book's commit and the record's commit.
9. **The memo.** The phase memo filed (`templates/memo.md`), nothing reported done that the build did not prove.
