# Lesson 1: wrote the scorer; doesn't yet see the model's role in retrieval

On 2026-09-29 Vitalie finished lesson 1. `words()` and `score()` pass all 9 tests on Python 3.9 and 3.13.

**Shown:**
- **`words()`** was idiomatic on the first try, identical to tsbuddy-ai's.
- **`score()`:** the first version counted shared words with a JS-style loop. After a prompt, it was rewritten correctly with `&` and `len`. So Vitalie can apply set operators once reminded, but doesn't reach for them yet.
- **A bug the original tests missed:** it unioned the summary into the body, compensating for lesson question 4, which was misread. That question was rewritten, and a test for field independence was added.

**Interview rep, three attempts:**
- Vitalie can describe the scoring, and fixed the per-word unit after feedback.
- Their second attempt said the top document "is sent to the user". So Vitalie doesn't yet see that retrieval feeds the model's context and the model writes the answer, which is RAG's core idea.
- They didn't name a weakness in either attempt.
- On 2026-09-30, a third attempt, made right after reading the model answer, got the model's role and the "why" right. The weakness was missing for the third time: Vitalie answers the "how" and drops the second part of the question.
- This is expected, because the map comes after the basics. Details are in `career/interview-practice/0001-how-does-retrieval-work.md`.

**Implications:**
- In the map lesson, draw the request flow first: user → model → `search_docs` / `read_doc` → context → answer.
- Re-ask the retrieval question cold next session, and check that both parts of the question get answered.
- Quiz set operators (`&`, `|`, `-`) in the ch. 5 quiz.

**Still to ask:** the lesson's quiz score, and whether Copilot and Full Line completion were off while they wrote it.
