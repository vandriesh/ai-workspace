# Python AI Engineering Resources

Every URL checked on 2026-09-28. O'Reilly pages block automated fetches; the book details were confirmed through the authors' own sites.

## Knowledge

- [Docs: _The Python Tutorial (3.14)_ — Python Software Foundation](https://docs.python.org/3/tutorial/index.html)
  The official tour of the language, written "for programmers that are new to the Python language, not beginners". The chosen basics course: ch. 3–5 (types, variables, control flow, functions, data structures), then 6, 8, 9 (modules, exceptions, classes). Use for: the basics, and whenever Python semantics differ from JS.
- [Cheat sheet: _Learn Python in Y Minutes_ — learnxinyminutes.com](https://learnxinyminutes.com/python/)
  Python 3 in one annotated file: datatypes, collections, control flow, functions, modules, classes, generators, decorators. Use for: a 20-minute map before the tutorial, and quick syntax lookups.
- [Practice: _Python track_ — Exercism](https://exercism.org/tracks/python)
  Free, not-for-profit. Concept exercises in learning order plus ~140 practice exercises; every solution runs against tests, with optional human mentoring. Track actively maintained ([exercism/python](https://github.com/exercism/python), last push 2026-09-22). Use for: drilling the basics with instant feedback, alongside the tutorial.
- [Docs: _Static Typing with Python_ — Python Typing Team](https://typing.python.org/en/latest/)
  Checker-neutral guides, reference and the formal typing spec: narrowing, generics, Protocols (structural typing, like TS interfaces). Use for: where typing differs from TS. To pick a checker, see Pyright's [mypy comparison](https://github.com/microsoft/pyright/blob/main/docs/mypy-comparison.md) (mypy skips unannotated functions by default; Pyright infers return types).
- [Docs: _uv_ — Astral](https://docs.astral.sh/uv/)
  Replaces pip, pip-tools, virtualenv and pyenv; `pyproject.toml` + `uv.lock` is package.json + lockfile. Use for: the tsbuddy-ai migration, starting from [From pip to a uv project](https://docs.astral.sh/uv/guides/migration/pip-to-project/).
- [Docs: _Ruff_ — Astral](https://docs.astral.sh/ruff/)
  One tool for linting and formatting, configured in `pyproject.toml`. Use for: your ESLint + Prettier; browse the rules reference to choose rule sets beyond the defaults.
- [Docs: _pytest_ — pytest-dev](https://docs.pytest.org/en/stable/)
  Fixtures, parametrize, `conftest.py`, "Good Integration Practices". Use for: where Jest/Vitest habits do not carry over (fixtures replace beforeEach, parametrize replaces `test.each`).
- [Docs: _Coroutines and Tasks_ (asyncio) — Python Software Foundation](https://docs.python.org/3/library/asyncio-task.html)
  `TaskGroup`, cancellation, `asyncio.timeout()`, `shield`, `to_thread`. Use for: concurrency in FastAPI handlers and graph nodes. Read [A Conceptual Overview of asyncio](https://docs.python.org/3/howto/a-conceptual-overview-of-asyncio.html) first; the event loop differs from Node's.
- [Docs: _Models_ — Pydantic](https://pydantic.dev/docs/validation/latest/concepts/models/)
  Validation vs coercion, strict mode, `model_validate`/`model_validate_json`, nested/generic models, extra fields. Use for: mapping Zod knowledge, and the structured-output `Answer` model.
- [Docs: _Settings Management_ (pydantic-settings) — Pydantic](https://pydantic.dev/docs/validation/latest/concepts/pydantic_settings/)
  `BaseSettings`, `.env`, prefixes, nested settings, secrets. Use for: config questions; pair with FastAPI's [Settings and Environment Variables](https://fastapi.tiangolo.com/advanced/settings/) for the `lru_cache` + dependency-override pattern.
- [Docs: _FastAPI Tutorial – User Guide_ — FastAPI](https://fastapi.tiangolo.com/tutorial/)
  Dependencies, response models, testing. Its [Server-Sent Events](https://fastapi.tiangolo.com/tutorial/server-sent-events/) page documents a built-in `EventSourceResponse` since 0.135.0 (untested here; tsbuddy-ai uses sse-starlette). Use for: dependency injection, the nearest thing to NestJS providers.
- [Docs: _LangGraph Persistence_ — LangChain](https://docs.langchain.com/oss/python/langgraph/persistence)
  Checkpointers (`InMemorySaver`, `SqliteSaver`, `PostgresSaver`), per-thread state, stores. Use for: choosing a checkpointer before adding interrupts.
- [Docs: _LangGraph Interrupts_ — LangChain](https://docs.langchain.com/oss/python/langgraph/interrupts)
  `interrupt()` + `Command(resume=...)`, approve/reject routing, the checkpointer + `thread_id` requirement. Use for: the human-approved write action; compare with LangChain's [HumanInTheLoopMiddleware](https://docs.langchain.com/oss/python/langchain/human-in-the-loop).
- [Repo docs: _pgvector README_ — pgvector](https://github.com/pgvector/pgvector)
  Distance operators, HNSW vs IVFFlat, filtered and hybrid search. Use for: the embeddings experiment; Python examples in [pgvector-python](https://github.com/pgvector/pgvector-python).
- [Article: _Introducing Contextual Retrieval_ — Anthropic (Sep 2024)](https://www.anthropic.com/engineering/contextual-retrieval)
  Measured comparison of embeddings, BM25, hybrid and reranking by top-20 retrieval failure rate. Use for: a model for the keyword-vs-embeddings eval; evidence BM25 still wins on exact identifiers.
- [Guide: _AI Evals: Everything You Need to Know_ — Hamel Husain & Shreya Shankar](https://hamel.dev/blog/posts/evals-faq/)
  Error analysis, binary pass/fail over 1–5 scales, validating an LLM judge against human labels, RAG evals. Actively updated (Sep 2026). Use for: auditing the LLM-as-judge harness.
- [Article: _Product Evals in Three Simple Steps_ — Eugene Yan (Nov 2025)](https://eugeneyan.com/writing/product-evals/)
  Label 50–100 failures, one evaluator per dimension checked against held-out labels, then automate. Use for: a checklist when calibrating the judge.
- [Article: _Demystifying evals for AI agents_ — Anthropic (Jan 2026)](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
  Code/model/human graders, grading end state vs transcript, pass@k vs pass^k. Use for: evaluating multi-step tool use and the write action.
- [Article: _Building effective agents_ — Anthropic (Dec 2024)](https://www.anthropic.com/engineering/building-effective-agents)
  Workflows vs agents and five composable patterns. Use for: justifying architecture choices in interviews.
- [Article: _Writing effective tools for agents — with agents_ — Anthropic (Sep 2025)](https://www.anthropic.com/engineering/writing-tools-for-agents)
  Tool naming, useful return context, pagination/truncation, evaluating tools. Use for: refining `list_docs`/`search_docs`/`read_doc`.
- [Docs: _LangChain & LangGraph integration_ — Langfuse](https://langfuse.com/integrations/frameworks/langchain)
  `CallbackHandler`, `session_id`, `user_id`, tags. Page shows SDK v3; tsbuddy-ai pins v4, so check the v3→v4 upgrade guide. Use for: tracing, then the [evaluation docs](https://langfuse.com/docs/evaluation/overview) for datasets and experiments.
- [Book: _AI Engineering_ — Chip Huyen (O'Reilly, Dec 2024)](https://huyenchip.com/books/)
  Foundation models, evaluation (2 chapters), prompting, RAG and agents, finetuning, inference, architecture, user feedback. Use for: the map of the role and interview prep; chapter summaries in [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book).

## Wisdom (Communities)

- [Python Discord](https://www.pythondiscord.com/)
  Largest Python Discord, volunteer-staffed help channels, published code of conduct. Use for: "is this idiomatic?" and typing/asyncio debugging.
- [Discussions on Python.org](https://discuss.python.org/)
  Official forum with Python Help, Typing, Packaging and Async-SIG categories. Use for: deeper typing, packaging and asyncio questions.
- [LangChain Forum](https://forum.langchain.com/)
  Official forum with LangGraph help sections; moderate traffic. Use for: checkpointer and interrupt questions (search first).
- [Latent Space Discord](https://www.latent.space/p/community)
  Community around the Latent Space podcast; weekly paper club, city meetups. Use for: how practitioners do AI engineering.
- [MLOps Community](https://mlops.community/)
  Practitioner Slack, meetups and conferences on production agents. Use for: evals, observability and deployment in production.

## Gaps

- **Video courses:** Coursera's _Python for Everybody_ was considered and rejected: it is aimed at non-programmers (about 2 months at 10 h a week). Udemy courses are paid and beginner-paced; none recommended.
- **Python for JS/TS developers:** no high-trust guide found. `tsbuddy-ai/docs/python-notes.md` fills this, grounded in the real code. Paid fallback: _Effective Python, 3rd ed._ (Slatkin, 2024), https://effectivepython.com/
- **Pydantic vs Zod:** only SEO comparison posts; learn from the Pydantic docs.
- **Choosing an embedding model:** no current vendor-neutral primer.
- **Human approval for agent writes (UX, audit, security):** nothing authoritative beyond the LangGraph/LangChain docs and Anthropic's posts.
- **Evals book:** _Evals for AI Engineers_ (Shankar & Husain, O'Reilly) is in Early Release, print due 2026-10-31. Revisit then.
