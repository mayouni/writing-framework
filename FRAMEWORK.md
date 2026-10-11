# The AYOUNI Writing Framework

Version 0.1 · 2026-10-11 · Mansour Ayouni, with the sessions that wrote the Softanza book.

## 0. What this is

A way of writing books in which a human author and software agents hold the pen together, and the page reads as one voice: the author's. It is built from a study of how the author writes when he writes alone (*Beginning Ring Programming*, 2020; the study is `../books/ring-book/style/STYLE-ANALYSIS.md`), from what the two AYOUNI books of 2026 learned about writing with agents, and from the publisher's copyedit of the first book, which showed which of his habits are voice and which are noise.

The framework has four parts: the **twelve commitments** every AYOUNI book keeps; the **two hands**, which say what the author writes and what the agents do; the **noise list** and the **author's calls**; and the **mechanics**, with the briefs, checklists and tools that enforce what can be enforced. A book instantiates the framework in its own `CLAUDE.md` (its shape, its vocabulary, its evidence) and pins the version it follows.

The one test, before any rule: *would he have run it, would he have said where it stops, and is the particular true?* If a page passes those three it is his, whoever typed it.

## 1. One voice, two hands

The author's voice, as the study found it, is a teacher at the keyboard who runs the thing before he explains it, quotes the machine's answer, leaves the reader a defect to fix, says where he stops, puts true pieces of his own life into the data, picks up a metaphor and puts it down, lifts the stakes once a chapter from real conviction, counts and names what he teaches, opens with a roadmap and closes with a bridge. It is also a writer whose sentences needed a second hand: calques, intensifiers, hedges, ellipses, superlatives and slips that an editor cut by the hundred.

The agents are the second hand, and more: they can run every block of a book at every build, count every assertion, read a library's test tree, find the sentence that says more than its evidence, translate the whole book and check the translation, and keep forty chapters in one shape. They cannot know what happened in Regueb in 1986, whether the daughter drew the map, what the author believes, or which metaphor he wants to live with. When they fill those holes they invent, and an invented particular is the one thing that breaks the voice beyond repair.

So the division is not "human writes, agent polishes". It is: **the author gives the true, the chosen and the believed; the agents give the run, the count, the check and the shape; and the joints between them are written down** (section 3). A page may be drafted by an agent from the record and be his, if every particular in it is true and sourced and every choice in it is his or marked as waiting for him.

## 2. The twelve commitments

Each commitment names the habit (H1–H12 in the study), what the agents do with it, what only the author does, and how it is checked.

**C1 · Run it, then read it.** The unit of teaching is a thing the reader can run, then its exact answer, then the reading of that answer. Code before explanation; principle extracted after. The machine's message is quoted, never paraphrased; when it complains, the complaint is the lesson.
*Agents:* run every block at every build and print its verdict under it; refuse a page whose code did not run; keep output out of source files (it is read from the run). *Author:* chooses what to run and in what order. *Check:* the proof line; no paragraph of abstract nouns without a run or a figure within reach (the voice reader flags it).

**C2 · Leave a defect in the reader's hands.** Every chapter hands over something real and unfinished, named as such: a bug left on purpose, a homework with stakes, a chart not drawn, a question the author could not answer. Show the wrong version before the right one when the wrong one teaches. Reject correct code for a reason of taste and give the reason.
*Agents:* never fix a defect the author left; never smooth a limit into a success; check that each chapter's exercise is a real defect and not a demonstration. *Author:* decides which defect. *Check:* the chapter checklist, item 2.

**C3 · Say where you stop.** The limit is a fixed part of every chapter and of the book: what is built, what is designed, what is absent, in the book's stage words; the loss printed beside every win; "I don't know" written where it is true; the scope of every claim ("at this bank", "at this commit"). An overclaim found later is not a sin; an overclaim left standing is.
*Agents:* read every claim against the record and classify it (verified / wrong / unsupported / overclaim); narrow rather than delete; carry stage words from code, not from documents. *Author:* owns the stage of his own designs. *Check:* the fresh-reader verification (brief `briefs/fresh-verifier.md`); the limit section present and non-empty.

**C4 · The true particular.** A name, a date, a place, a person, a memory, a sentence of the author's appears only if it is true and in the record (or given by him in the session). Family and friends by their consent. The reader's own life may be addressed; the author's is never composed. A hole where a particular belongs is marked `[AUTHOR: …]` and stays visible until he fills it; it is never filled by an agent with a plausible one.
*Agents:* write the marker; batch the questions (three per chapter at most); when the author delegates the answer, apply the answer policy (`briefs/answer-policy.md`), whose first rule is "the record decides; nothing is invented". *Author:* fills the holes; this is the part of the book only he can write. *Check:* grep for `[AUTHOR`; the particulars audit (every proper name and date traced).

**C5 · One metaphor at a time.** A metaphor is picked up to do one job and put down; it is not sustained for ornament. A metaphor that is kept (the court, the doors, the twin; the happy path, the clay, the millstone) must be load-bearing (it explains what no code there explains), must be mapped once, term by term, where it is introduced, and must keep its names stable across the book. Metaphors of the field that the book refuses (construction, the factory) are refused by name and with a reason.
*Agents:* keep the names stable; flag a decorative metaphor (one that could be deleted without loss of meaning); never introduce a sustained metaphor. *Author:* chooses the ruling metaphors and the ones to refuse. *Check:* the metaphor audit (voice reader, section 4).

**C6 · I, we, you — and the tool that answers.** "I" is the witness and the opinion ("in my case", "I would reject it because"); "we" is the pair at the keyboard inside a worked example; "you" is the reader with the editor open. Questions are beats put to the reader or to the machine, each answered within the page. The tool may be addressed and may answer (its error message is its voice). Imperatives are the spine: run, save, try, look.
*Agents:* keep the pronouns' jobs; turn roadmap "we" into "I"/"you"; never add "I feel" or "I remember" sentences. *Author:* decides the personification (Ring was "she"; see the author's calls). *Check:* pronoun counts per page against the book's profile.

**C7 · Long, then short.** A long cumulative sentence (triads are welcome) is followed by a verdict of a few words. Half the paragraphs may be one sentence. The colon introduces code, output, a definition and a punchline; the dash is rare. "And" and "But" may open a sentence. Exclamations exist and are earned: after a run or a reveal, never on an abstract sentence; about two per thousand words. Repetition is emphasis when it is deliberate.
*Agents:* the lint (`tools/style_lint.py`) counts sentence lengths, exclamations and their placement, dashes and colons, and reports drift from the profile. *Author:* nothing to decide. *Check:* the lint report.

**C8 · Count and name.** What a chapter teaches is a counted set with a name (three commandments, six doors, nine elements, three stage words), and the name is reused exactly. The count is honest: a set of seven is not sold as five; a list is not padded to a round number. Mixed grammar inside one list is a tic.
*Agents:* check that a stated count matches the list; keep the names exact across languages. *Author:* names the sets. *Check:* the audit (`book_audit`-style count checks).

**C9 · Roadmap and bridge.** A chapter opens with what it will do, in the first person, in a few sentences, not seven. A section ends by handing over to the next. A chapter closes on a bridge, a release, a homework or a personal coda, not on a summary of what was just said. The preface is written last, from the book that exists, by the author.
*Agents:* keep the shape; flag a chapter whose opening has no roadmap or whose close is a summary. *Author:* the codas (C4). *Check:* the chapter checklist.

**C10 · Lift the stakes once, and own it.** Each chapter rises at least once from the technical point to what it means for people, the craft or the country, from conviction. Such a claim is either backed in the page or marked as belief ("this is my view, not a scientific truth"). "For the first time", "the root cause of all", "unprecedented" require a source or go.
*Agents:* flag unbacked absolutes and superlatives; never add a stake. *Author:* the stake and its marking. *Check:* the lint's absolutes list; the verifier's "overclaim" class.

**C11 · The questioner's record.** The book argues from a record it can point at: a library at a pinned commit, memos with dates, a study with numbered rulings, decisions logged with their reasons, requests filed to the people who own what the book needs. Numbers are read at build time, never composed; a number that cannot be read is written `null` and said so. Every phase ends with a memo (by / subject / why / did / state / waiting / next / note), and nothing is reported done that the build did not prove.
*Agents:* keep the record (data files, memos, decisions, verification reports, book.json); file requests instead of editing other repositories. *Author:* rules on the decisions. *Check:* the memo; the status page; the manifest.

**C12 · Plan large, ship what runs.** The plan may hold thirty chapters; the book ships what ran, and says in its preface what it owes. A chapter is done only when its code runs on the build, its guards resolve, its translation exists, and the author has read it and said so.
*Agents:* the status page prints which of the four each chapter has; the release manifest calls the book a proof copy while a page is unread. *Author:* marks `read`. *Check:* the release gates.

## 3. The joints between the hands

What makes the two hands one voice is a small set of written things that pass between them:

| Joint | What it is | Who writes it | Who reads it |
|---|---|---|---|
| The brief | the book's contract: structure, shape of a chapter, voice, rules that override everything | author | every session, first |
| `[AUTHOR: …]` | a hole only the author can fill, in the page where it belongs | agent | author |
| The decision log | every choice taken on the author's delegation, with the alternatives and the reason | agent | author, who overrules by editing |
| The memo | one per phase, in the fixed form | agent | author |
| The verification report | a fresh reader's claim-by-claim verdict on a chapter | agent (one who did not write it) | a second agent, then the author |
| The run and the court | the verdict under every block, read from data | the build | the reader |
| The status page and manifest | what each chapter has of the four conditions; what a release contains | the build | everyone |
| `status: read` | the author's reading, set by him only | author | the build |

An agent never sets `read`, never answers an `[AUTHOR]` marker except under the delegated policy, never edits the author's own text (a chapter he wrote is reported on, not edited), never names a person, never invents a particular.

## 4. The noise list (cut) and the author's calls (never decided by an agent)

**Cut, by tool where possible:** calques and homophones (hole/whole, staff/stuff, witch/which, fellow/follow, then/than, "from one hand", "in the same time", "obeys to", "yet" for "and"); intensifiers and reassurance (very, really, simply, just, dead simple, obvious, "as simple as that" before the run); stacked hedges and apologies; trailing ellipses; colon lead-ins to an unnamed figure; superlatives and self-advertising ("one of the most", "maybe for the first time", "unprecedented"); unbacked absolutes ("the root cause of all"); scope inflation in promises; run-on roadmaps; repeated listings; emojis; and the AYOUNI forbidden words (substrate; maker outside "decision-maker"; revolutionary, game-changing, paradigm shift; leverage, utilize, best practice, stakeholders; "developer" for programmer; the names of other repositories' products).

**The author's calls, listed for him and left as they are until he rules:** the tool as "she"; the reader's pronoun; the flourishes an editor would cut ("Ready? Please give me your hand…", "What the hell is this?!"); a phrase of his the record calls his ("for the first time in computer science history"); how much of his biography goes into a chapter; the name of a ruling metaphor; which exercise is the defect; a title.

## 5. Mechanics

**Words.** Plain words a non-native reader parses; no idiom that needs a culture to decode, except the author's own, which is used without explanation and never translated into a joke. Foreign words (Hausa, Arabic, French) are welcome when true. Code names in prose are bare, with `()` for functions. Numbers read from a run carry their date and commit; others are spelled out under ten. Dates are written in full. No emojis in prose.

**Sentences.** Profile from the Ring book: median 16 words, a quarter under 10, one in thirty over 40; colons 15 per 1,000 words, dashes under 1, exclamations about 2, questions about 3. A book may set its own profile in its `CLAUDE.md`; the lint reports against it.

**Paragraphs.** Short; one-sentence paragraphs for verdicts and hand-overs. A paragraph of abstract nouns with no run, figure or example within reach is rewritten or cut.

**Figures.** A diagram of the logic before the code when the chapter teaches logic; a figure that carries an argument gets a caption that labels it, not one that instructs. Numbers in figures are read at build from the record and say where from.

**Headings.** Sentence case; the book's fixed headings reused exactly in every chapter and in every language.

**Languages.** A translation is of the final English, page for page, same shape, same counts, code byte-identical; it is checked mechanically (`check_fr`-style) and bannered as a translation of a draft until the English is read. Vocabulary is the project's own glossary.

**Tools and briefs** (this folder): `tools/style_lint.py` (the noise and the profile), `tools/docx_to_text.py` (Word to text, for studies like the Ring book's), `briefs/voice-reader.md` (how a chapter sounds, with evidence), `briefs/fresh-verifier.md` and `briefs/fixer.md` (claim by claim against the record, then the smallest fix), `briefs/answer-policy.md` (delegated answers that invent nothing), `briefs/translator.md`; `checklists/chapter.md`, `checklists/noise.md`, `checklists/release.md`; `templates/chapter.md`, `templates/memo.md`, `templates/decisions.md`.

## 6. How a book uses the framework

1. The book's `CLAUDE.md` names the framework version, the book's shape (its fixed elements), its stage words, its evidence (the record it argues from, pinned), its vocabulary, and the profile it wants if it differs.
2. Before drafting: the brief is read whole; research is written from the record; the shape is instantiated.
3. Drafting: one voice; every particular sourced or marked `[AUTHOR]`; every block run.
4. After drafting: lint; voice read (a fresh reader with `briefs/voice-reader.md`); verification (a fresh reader with `briefs/fresh-verifier.md`, then a fixer); the author's reading; translation and its check; audit; release.
5. Every change to this framework is a decision logged in `DECISIONS.md` here, with its reason; books cite the version they follow.

## 7. What the framework does not do

It does not write the author's conviction, his memories or his jokes. It does not choose his metaphors. It does not make a page `read`. It does not promise clarity; it makes the second hand's work checkable, so that the author's first hand can stay as free as it was in 2019, with someone to catch the hole in "the hole program".
