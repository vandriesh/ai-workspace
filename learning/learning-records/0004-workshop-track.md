# Mission: the depth track is a workshop that rebuilds tsbuddy-ai

On 2026-09-30 Vitalie asked for lessons in the style of Kent C. Dodds' Epic Workshop: code mostly in place, emoji comments marking the part to write, tests to check it, and a diff against the solution. They then asked that the lessons rebuild the current assistant step by step, in about ten lessons.

**Decided:**
- The app lives in its own repository, `learning-app` (the `workshop` command). The lessons are in the same repository, in `workshops/tsbuddy-guide/`. I first put them in `ai-workspace`; Vitalie asked for them to be part of the app's repository.
- `workshops/tsbuddy-guide/README.md` holds the ten-lesson plan. Each lesson is one part of tsbuddy-ai and one or two of the 12 cogs. Lesson 1 (keyword search) is written; lessons 2 to 10 are planned.
- The two cogs tsbuddy-ai has not built, embeddings and a vector database, are the capstone after lesson 10.

**Implications:**
- Write one lesson at a time, just ahead of Vitalie, shaped by what the previous lesson showed.
- Every lesson opens with where its cog sits, what it is for and when it is not needed, so the map builds up lesson by lesson (see LR 0002).
- Tests use stub models only. No API key is ever needed or committed.
- From lesson 2 the exercises need packages, so lesson 2 starts with uv and a `.venv` in the workshop's folder.

**Not settled:** whether the Tutorial chapters and Exercism come before the workshop, as `MISSION.md` says, or alongside it as each lesson's "read first". Asked on 2026-09-30.
