# Brief: translate a page

The translation is of the English page, page for page, in the same voice (first person, the author's) and with the same structure. It is bannered as a translation of a draft until the English page is published by the author; then it is re-read against the final English.

**Translated:** every sentence of prose; the title; the stage words' text; the headings (the book's fixed headings have one fixed translation each, in the book's style sheet); the cells of a table; the text of every `[AUTHOR: …]` marker; list items.

**Never changed, byte for byte:** every code fence, including comments and the strings it prints (the code is the run's); the front matter keys and every value except `title` and the stage texts; the names of the record (classes, methods, files, guards, commits); backtick spans; numbers (written in the target language's convention in prose); quotations of the tool's own messages, which stay in their language, in quotation marks; proper names.

**Shape:** the same number of paragraphs, list items, table rows and `[AUTHOR` markers; a bold sentence stays bold; a heading keeps its number.

**Vocabulary:** the project's own glossary first (the site's words, the book's style sheet), then the plainest word, kept the same on every page. Terms with two senses in English (commit as the governed act and commit in git; plane and plan) get two words and the style sheet says which.

**Voice:** plain, short sentences, no inflation, the loss printed beside the win; the warmth is in the stories, never in adjectives. Typography of the target language (French: « », the comma decimal in prose, spaced thousands).

**Checks:** the book's mechanical checker (`check_fr`-style: front matter, fences byte-identical, headings, counts) must pass; a word-to-look-at warning is read, not ignored.

**Report:** per page, the terminology choices you made that the style sheet did not settle, so they can be added to it.
