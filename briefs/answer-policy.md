# Brief: answer the author's open questions on his behalf

Only when the author has said so, in his words, for this book. Every `[AUTHOR: …]` marker is a question the record could not answer. An answer taken under this policy is a DELEGATED decision: it is logged as one, the page is not marked `read`, and the author can overrule it by editing the page. Nothing here lets anyone write a sentence and call it the author's.

## The rules

**D1. The record decides; nothing is invented.** Never put in the author's mouth a memory, a motive, a fact about a person, a date or a feeling that no file holds. When a question asks for one ("is there an earlier moment", "what did it cost you", "who held the phone", "which goes first"), the answer is *the record does not hold it*: the chapter says what the record holds, in one plain sentence where the gap is, and does not fill it. The marker goes; the gap stays visible in the text.

**D2. "May the chapter say X, with its caveat?" is yes, with the caveat printed in the same place.** A loss, a gap or a "not run" is printed beside the claim.

**D3. "Is this sentence yours?" cannot be answered for him.** Print the sentence attributed to its source (the site, the design document, the memo, the study), by name and date, never as his own words. A principle the chapter states in its own bold sentence stays the chapter's, in the book's voice.

**D4. A contract the code does not meet is told as designed, not hidden.** State what the code does now and label the other as *designed*, with the stage word. Never write that something is built that the code does not do.

**D5. Unreviewed foreign-language text is never printed as reviewed.** Print it only with the line that no native speaker has read it, or not at all. Never write a sentence in those languages to fill a gap.

**D6. People are not named.** A person named in a record is not named in the book. The chapter says "the record names the person" and prints the date and the sentence.

**D7. Content of a source that is not public** is printed only as the book already prints it (read from its file on a date, the source unnamed where the book's rules say so), and no more than the chapter needs.

**D8. The author's own text is not edited.** Where a question asks to correct a chapter he wrote, the answer is: his chapter keeps his wording; the other chapters say in one sentence what the record shows more exactly, and the exact wording is listed once in the memo under "for the author" so he can edit it himself.

**D9. A choice between two presentations** ("show it as a running block or describe it", "open on X or Y") is answered by the option that keeps the chapter's runs unchanged. Do not touch any code fence; if an answer would need a code change, do not make it: write the need in your report.

**D10. A name, a title, a number or a label:** choose the option already in the text or most directly supported by the record, say so in your report, and print the alternative nowhere.

**D11. The preface stays a working page** until the author writes it.

## What you do for each marker
1. Read the marker and the paragraph around it, and the chapter's decision and limit sections if the answer touches them.
2. Pick the answer by the rules. Make the smallest edit that states it: usually delete the marker and, where the answer changes the claim, adjust the sentence or add one.
3. Make the same edit in every language of the book, keeping the same number of paragraphs, headings and list items.
4. After your edits no `[AUTHOR` may remain in your files, in any language.

## What you do not do
Edit a code fence; edit front matter keys other than stage text when an answer changes a stage claim; run the build or the runner; mark a page `read`; write the forbidden words; name a person.

## Report
For each marker, one line: `chapter · short question · answer (rule) · what you changed`. Then anything that needs a code change or a run, and anything the rules could not settle.
