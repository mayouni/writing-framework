#!/usr/bin/env python3
"""style_lint — the noise list and the sentence profile of the AYOUNI Writing Framework, over Markdown pages.

    python style_lint.py <file-or-folder>...            # a report per page and a total
    python style_lint.py src/en --strict                # exit 1 when a page is over a threshold
    python style_lint.py src/en --json out.json         # the counts as data
    python style_lint.py src/en --profile ring          # compare with the Ring book's profile (default) or 'none'

What it reads: the prose of a page. Front matter, code fences, tables, headings and figure captions are skipped.
What it counts (FRAMEWORK.md §4 and §5): calques and homophones, intensifiers, hedge stacks, trailing ellipses and colon lead-ins,
superlatives and self-advertising, unbacked absolutes (counted, not judged), forbidden words, emojis, long sentences, exclamations and
whether they follow a run (a code fence or an output line within the two previous blocks), em dashes, and the pronoun profile.
It changes nothing. A count is a thing to look at, not a verdict; the thresholds under --strict are the Ring book's profile with room.
"""
import json, re, sys
from pathlib import Path

CALQUES = {
    r"\b(a|the|this|that|whole|your|my|our|his|her)\s+hole\b": "hole → whole",
    r"\bhole\s+(program|book|chapter|file|code|list|thing|system|solution|point|story|world)\b": "hole → whole",
    r"\bstaff\b(?!\s+(member|members|of the|turnover))": "staff → stuff?",
    r"\bwitch\b": "witch → which",
    r"\bfellow\s+(me|the|this|these|those|him|her|them|along)\b": "fellow → follow",
    r"\b(more|less|better|rather|other|bigger|smaller|higher|lower|greater|larger|longer|shorter|faster|slower|easier|harder|simpler|older|newer|cheaper|earlier|later)\s+(\w+\s+)?then\b": "then → than",
    r"\bquiet\s+(like|simple|basic|the|a|an|good|different|clear|easy|hard|long|short)\b": "quiet → quite",
    r"\bin the same time\b": "in the same time → at the same time",
    r"\bfrom one hand\b|\bfrom the other hand\b": "from one hand → on one hand",
    r"\bobeys? to\b": "obey to → obey",
    r"\ban? (useful|important|interesting|good|bad|new) information\b": "an information → a piece of information",
    r"\bin plus of\b": "in plus of → besides",
    r"\bmay be\b(?=\s+(in|a|the|not|you|we|it|this|that|because|if|later|one|two|three|more|some|for))": "may be → maybe",
    r"\bimbricated\b": "imbricated → nested",
    r"\bcash (miss|misses|memory)\b": "cash → cache",
}
INTENSIFIERS = r"\b(very|really|simply|obviously|obvious|dead simple|as simple as that|very simple|so easy|very easy|pretty much|basically|literally|extremely|incredibly)\b"
HEDGES = r"\b(maybe, and probably|somehow|kind of|sort of|a little bit|more or less|in a way|I guess|I think that|it seems that|probably, and)\b"
SUPERLATIVES = r"\b(one of the most|for the first time|first ever|the first (\w+ )?to|unprecedented|revolutionary|game[- ]changing|paradigm shift|world[- ]class|state[- ]of[- ]the[- ]art|cutting[- ]edge|groundbreaking|the best (\w+ )?(in|of) the world|never before)\b"
ABSOLUTES = r"\b(the root cause of all|all (the )?problems|every programmer|no other (language|system|tool|platform)|nothing else|always|never|everyone|nobody|impossible|cannot fail|guaranteed)\b"
FORBIDDEN = {
    r"\bsubstrate\b": "substrate (never)",
    r"(?<!decision-)(?<!decision )\bmakers?\b": "maker → crafter",
    r"\bleverage\b": "leverage → use",
    r"\butili[sz]e[sd]?\b": "utilize → use",
    r"\bbest practices?\b": "best practice → what worked",
    r"\bstakeholders?\b": "stakeholders → be specific",
    r"\bdevelopers?\b": "developer → programmer (the book's word)",
    r"\bin order to\b": "in order to → to",
}
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿\U0001F000-\U0001F2FF]")
FENCE = re.compile(r"^(```|~~~)", re.M)

PROFILES = {
    "ring": dict(median=16, long_pct=3.3, excl_per_k=2.4, q_per_k=3.3, colon_per_k=15.2, dash_per_k=0.5),
    "none": None,
}
STRICT = dict(long_pct=6.0, excl_per_k=4.0, dash_per_k=4.0, intens_per_k=4.0, forbidden=0, calques=0, emoji=0, superl_per_k=1.0)


def blocks_of(text):
    """The page as blocks: ('code', s) for fences, ('skip', s) for front matter/tables/headings/captions, ('prose', s) otherwise."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4:]
    out, i = [], 0
    parts = re.split(r"(^(?:```|~~~).*?^(?:```|~~~)\s*$)", text, flags=re.S | re.M)
    for part in parts:
        if part.startswith(("```", "~~~")):
            out.append(("code", part)); continue
        for para in re.split(r"\n\s*\n", part):
            p = para.strip()
            if not p:
                continue
            if p.startswith(("#", "|", "<!--", "![", "*Figure", "*Fig", "<figure", "<div", "<svg")) or re.match(r"^\*[^*\n]{3,120}\*$", p):
                out.append(("skip", p))
            elif re.match(r"^(    |\t)", para):
                out.append(("code", p))
            else:
                out.append(("prose", p))
    return out


def sentences(p):
    p = re.sub(r"`[^`]*`", "CODE", p)
    p = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", p)
    return [s.strip() for s in re.split(r"(?<=[.!?…])\s+(?=[A-Z«\"'(\[])", p) if len(s.split()) > 1]


def lint_text(text):
    blocks = blocks_of(text)
    prose = [b[1] for b in blocks if b[0] == "prose"]
    joined = "\n\n".join(prose)
    low = joined.lower()
    sents = [s for p in prose for s in sentences(p)]
    words = re.findall(r"[A-Za-zÀ-ÿ'’]+", joined)
    N = max(1, len(words))
    k = 1000.0 / N
    lens = sorted(len(s.split()) for s in sents) or [0]
    long_s = [s for s in sents if len(s.split()) > 40]
    # exclamations: after a run or not
    excl_total, excl_cold = 0, []
    for idx, (kind, p) in enumerate(blocks):
        if kind != "prose":
            continue
        n = p.count("!")
        if not n:
            continue
        excl_total += n
        prev = [b[0] for b in blocks[max(0, idx - 2):idx]]
        after_run = "code" in prev or bool(re.search(r"(prints|printed|gives|returns|answers|complains|says|shows|output|verdict|kept|raised|ran|run it|execute)", p.lower()))
        if not after_run:
            excl_cold.append(p[:90])
    findings = {}
    def grab(pattern, label, flags=re.I):
        hits = [m.group(0) for m in re.finditer(pattern, joined, flags)]
        if hits:
            findings[label] = hits
        return len(hits)
    calq = sum(grab(pat, "calque: " + why) for pat, why in CALQUES.items())
    intens = grab(INTENSIFIERS, "intensifiers")
    hedges = grab(HEDGES, "hedge stacks")
    superl = grab(SUPERLATIVES, "superlatives")
    absol = grab(ABSOLUTES, "absolutes (to judge)")
    forb = sum(grab(pat, "forbidden: " + why) for pat, why in FORBIDDEN.items())
    emoji = len(EMOJI.findall(joined))
    ell = sum(1 for p in prose if re.search(r"(\.\.\.|…)\s*$", p))
    colon_lead = 0
    for idx, (kind, p) in enumerate(blocks):
        if kind == "prose" and p.rstrip().endswith(":") and idx + 1 < len(blocks) and blocks[idx + 1][0] == "prose":
            colon_lead += 1
    pron = {w: len(re.findall(r"\b" + w + r"\b", low)) for w in ("i", "we", "you")}
    pron["i"] = len(re.findall(r"\bI\b", joined))
    return dict(
        words=N, sentences=len(sents), median=lens[len(lens) // 2], q1=lens[len(lens) // 4], q3=lens[3 * len(lens) // 4],
        long=len(long_s), long_pct=round(100 * len(long_s) / max(1, len(sents)), 1),
        excl=excl_total, excl_per_k=round(excl_total * k, 1), excl_cold=excl_cold,
        questions=joined.count("?"), q_per_k=round(joined.count("?") * k, 1),
        colon_per_k=round(joined.count(":") * k, 1), dash_per_k=round((joined.count("—") + joined.count(" - ") + joined.count("–")) * k, 1),
        calques=calq, intensifiers=intens, intens_per_k=round(intens * k, 1), hedges=hedges, superlatives=superl, superl_per_k=round(superl * k, 2),
        absolutes=absol, forbidden=forb, emoji=emoji, ellipses=ell, colon_leads=colon_lead,
        one_sentence_paras=sum(1 for p in prose if len(sentences(p)) == 1 and len(p.split()) > 3), paragraphs=len(prose),
        pronouns=pron, findings=findings, long_examples=[s[:120] for s in long_s[:3]],
    )


def over(r):
    out = []
    if r["long_pct"] > STRICT["long_pct"]: out.append(f"long sentences {r['long_pct']}% > {STRICT['long_pct']}%")
    if r["excl_per_k"] > STRICT["excl_per_k"]: out.append(f"exclamations {r['excl_per_k']}/k > {STRICT['excl_per_k']}")
    if r["dash_per_k"] > STRICT["dash_per_k"]: out.append(f"dashes {r['dash_per_k']}/k > {STRICT['dash_per_k']}")
    if r["intens_per_k"] > STRICT["intens_per_k"]: out.append(f"intensifiers {r['intens_per_k']}/k > {STRICT['intens_per_k']}")
    if r["superl_per_k"] > STRICT["superl_per_k"]: out.append(f"superlatives {r['superl_per_k']}/k > {STRICT['superl_per_k']}")
    if r["forbidden"] > STRICT["forbidden"]: out.append(f"forbidden words {r['forbidden']}")
    if r["calques"] > STRICT["calques"]: out.append(f"calques {r['calques']}")
    if r["emoji"] > STRICT["emoji"]: out.append(f"emoji {r['emoji']}")
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    strict = "--strict" in sys.argv
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    jpath = sys.argv[sys.argv.index("--json") + 1] if "--json" in sys.argv else None
    prof = PROFILES.get(sys.argv[sys.argv.index("--profile") + 1] if "--profile" in sys.argv else "ring")
    files = []
    for a in args or ["."]:
        p = Path(a)
        files += sorted(p.rglob("*.md")) if p.is_dir() else [p]
    files = [f for f in files if f.suffix == ".md"]
    if not files:
        print("no .md files"); sys.exit(2)
    rows, totals, bad = [], dict(words=0, sentences=0, long=0, excl=0, calques=0, intensifiers=0, superlatives=0, forbidden=0, emoji=0, hedges=0, ellipses=0, colon_leads=0), 0
    print(f"{'page':44s} {'words':>6} {'med':>4} {'>40':>5} {'!/k':>5} {'?/k':>5} {':/k':>5} {'—/k':>5} {'int/k':>6} {'calq':>5} {'sup':>4} {'abs':>4} {'forb':>5} {'…':>3}")
    for f in files:
        r = lint_text(f.read_text(encoding="utf-8", errors="replace"))
        r["file"] = str(f)
        rows.append(r)
        for kk in totals:
            totals[kk] += r.get(kk, 0)
        flags = over(r)
        if flags:
            bad += 1
        print(f"{f.name[:44]:44s} {r['words']:6d} {r['median']:4d} {r['long_pct']:5.1f} {r['excl_per_k']:5.1f} {r['q_per_k']:5.1f} {r['colon_per_k']:5.1f} {r['dash_per_k']:5.1f} {r['intens_per_k']:6.1f} {r['calques']:5d} {r['superlatives']:4d} {r['absolutes']:4d} {r['forbidden']:5d} {r['ellipses']:3d}" + ("   <- " + "; ".join(flags) if flags else ""))
        if verbose:
            for label, hits in r["findings"].items():
                print(f"      {label}: {', '.join(sorted(set(hits)))[:200]}")
            for s in r["excl_cold"][:3]:
                print(f"      exclamation on an abstract sentence: {s}")
            for s in r["long_examples"]:
                print(f"      long: {s}")
    W = max(1, totals["words"])
    print(f"\n{len(files)} pages · {totals['words']} prose words · {totals['sentences']} sentences · long {100 * totals['long'] / max(1, totals['sentences']):.1f}% · "
          f"exclamations {totals['excl'] * 1000 / W:.1f}/k · intensifiers {totals['intensifiers'] * 1000 / W:.1f}/k · superlatives {totals['superlatives']} · "
          f"calques {totals['calques']} · forbidden {totals['forbidden']} · emoji {totals['emoji']} · hedge stacks {totals['hedges']} · trailing ellipses {totals['ellipses']} · colon lead-ins {totals['colon_leads']}")
    if prof:
        print(f"profile (Ring book): median {prof['median']} · long {prof['long_pct']}% · ! {prof['excl_per_k']}/k · ? {prof['q_per_k']}/k · : {prof['colon_per_k']}/k · — {prof['dash_per_k']}/k")
    if jpath:
        Path(jpath).write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
        print("wrote", jpath)
    if strict and bad:
        print(f"STRICT: {bad} page(s) over a threshold"); sys.exit(1)


if __name__ == "__main__":
    main()
