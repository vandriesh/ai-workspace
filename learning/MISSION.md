# Mission: Python AI engineering, proven on tsbuddy-ai

## Why
Get hired as an AI Engineer, with Amdaris's Senior AI Engineer role as the reference target. tsbuddy-ai is the evidence, but today it is a project AI built; an interviewer will probe it until it is clear who understands it. The goal is to make it a project Vitalie built with AI and can defend and extend line by line.

## Success looks like

### First: Python basics
- Finish the Python Tutorial ch. 3–5 and the Exercism concept exercises, then pass lesson 1's tests without AI.

### Then: the map
- Draw tsbuddy-ai as blocks from memory (the 12 cogs and how they connect) and walk through one request end to end.
- For each cog, explain in AI-engineering language what it is for and **when it is needed, and when it isn't** (e.g. RAG without a vector database).
- Hold a conversation in the field's vocabulary. The details come later.

### Later: depth
- Write tsbuddy-ai's core pieces from an empty file, without AI, until the tests pass: `Corpus.search`, the Pydantic request and answer models, one LangGraph tool.
- Explain each of the 12 cogs as tsbuddy-ai implements it: what it does, why this choice, what to measure next.
- Ship one measured improvement personally, e.g. keyword vs embedding retrieval compared by evals, with the numbers.
- Pass a mock Senior AI Engineer interview (Python coding and AI system design) built from real interview reports.

## Constraints
- 2–4 hours a week.
- Experienced TypeScript developer; writes no Python unaided yet.
- Interview format unknown; to be researched before the mock interviews.
- Works on macOS and Linux, synced through `ai-workspace`.

## Out of scope
- Azure-specific services.
- Model training, fine-tuning and ML maths, unless the interview research shows they are expected.
- Python corners the service does not need: threading and the GIL, metaclasses, `__slots__`.
