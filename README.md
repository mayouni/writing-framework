# The AYOUNI Writing Framework

How Mansour Ayouni's books are written with agents so that they read in one voice: his. Version 0.3, 2026-10-15.

| File | What it is |
|---|---|
| `FRAMEWORK.md` | the framework: the twelve commitments, the two hands, the joints, the noise list, the author's calls, the mechanics |
| `CLAUDE.md` | what a session does with this folder when it works on a book |
| `DECISIONS.md` | every change to the framework, with its reason |
| `briefs/` | the briefs given to agents: `voice-reader.md`, `fresh-verifier.md`, `fixer.md`, `answer-policy.md`, `translator.md` |
| `checklists/` | `chapter.md` (the twelve commitments as questions), `noise.md` (what to cut), `release.md` (the gates) |
| `tools/` | `style_lint.py` (noise and sentence profile over Markdown pages), `docx_to_text.py` (Word to text, for a study) |
| `templates/` | `chapter.md`, `memo.md`, `decisions.md` |

The study the framework is built from: `../books/ring-book/style/` (the analysis, seven close readings, the copyedit comparison, the metrics).
The first application plan: `../books/softanza-book/sessions/2026-10-11-writing-framework-plan.md`.

## Use it from a book

```bash
python ../../writing-framework/tools/style_lint.py src/en            # the noise and the profile, per page
python ../../writing-framework/tools/style_lint.py src/en --strict   # exit 1 over the thresholds
python ../../writing-framework/tools/style_lint.py src/fr --lang fr  # a first French noise list; English is the full one
```

A fresh-reader pass on a chapter: give an agent `briefs/voice-reader.md` (how it sounds) or `briefs/fresh-verifier.md` (whether it is true to the record), the chapter, and nothing else; then a second agent `briefs/fixer.md` with the report. The author's open questions are answered by him, or on his word by `briefs/answer-policy.md`.
