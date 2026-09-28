# Teaching notes

- **Sequencing (2026-09-28):** wants to start with the basics (types, variables, functions, loops) from an external course, at a fast pace ("senior JS developer"). Chosen: the official Python Tutorial ch. 3–5 plus Exercism concept exercises. Don't re-teach what the tutorial covers; add short retrieval quizzes on the TS-instinct traps per chapter, and use lesson 1 as the check that the basics transferred.
- **Order:** Python basics → the map → depth. Wants the mind map and vocabulary before implementation details, but only after the basics (see LR 0002). Open every cog lesson with where it sits in the whole system.
- **Revisit (2026-09-28):** `%` with negative operands. Got `//` flooring right (`-9 // 4 = -3`) but answered `-9 % 4 = -2` and `7 % -3 = 1` (JS remainder instinct); had also briefly confused `%` with the integer part. Put one negative-`%` item in the ch. 3 quiz.
- **Time:** 2–4 h a week. Keep lessons to ~25 minutes so a week holds several, plus review.
- **AI during exercises:** not answered yet. Default: off (no agent, no autocomplete) while writing exercise code; hints come from the teacher on request. Ask again after lesson 1.
- **Machines:** macOS and Linux. On macOS, `python3` is 3.9.4 and `/opt/homebrew/bin/python3.13` exists; no uv or pytest installed. Linux Python version unknown. Until the tooling lesson (uv), exercises must run with plain `python3` ≥ 3.9 and no installs.
- **Confidence:** doubts they will meet a Senior bar and sees tsbuddy-ai mainly as a CV mention. Keep progress visible: each lesson ends in a passing test or a change in tsbuddy-ai they can point to.
- **Interviews:** will research the format and wants mock interviews. Each cog closes with an out-loud interview rep; store answers in `career/interview-practice/`.
- **Existing material:** `tsbuddy-ai/docs/python-notes.md` is the TS→Python explainer (no better public guide exists). Build on it; quiz from it rather than re-teaching it.
- **Git:** sometimes commits on the Linux machine from a patch. Keep `ai-workspace` changes small and self-contained.
