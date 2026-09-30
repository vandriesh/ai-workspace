# How does tsbuddy-ai decide which docs the model reads? Name one weakness.

From lesson 1 (score a doc with sets). The target answer is about 60 seconds.

## Attempt 1 (2026-09-29, written)

> The scorer functionality runs scoring against all files by calculating the score using a specific formula:
> - The title of the document gives 3 points.
> - The summary and the body give 1.5 and 1 point respectively.
>
> By comparing all the scores we can sort the documents by high score and return the top documents.

**Covered:** every doc gets a score, and the docs are sorted, with the top ones returned. The weights are in the right order.

**Missing or imprecise:**
- **Name the technique.** It's keyword (lexical) retrieval, with no vectors yet: the query and each doc become sets of lowercase words.
- **The unit is off.** The title doesn't give 3 points; each query word the title shares gives 3.0.
- **The model's part.** The top five come back as id, title and summary, and the model decides which ones to open with `read_doc`. The agent does its own retrieval, and that answers the "which docs the model reads" part.
- **No weakness named, though the question asked for one.** For example, there's no stemming (`exports` ≠ `export`) and no synonyms (`download` vs `export`).
- **Why start here (a bonus point).** It's cheap and deterministic, and it's the baseline embeddings have to beat on the evals.

## Attempt 2 (2026-09-29, written, same session)

> First we retrieve the keywords and compare against title, summary, and body from the documents. The title, summary, and body have different weights if the word exists in respective field. At the end the highest-score document will be read and will be sent to the user.

**Better:** the unit is right now: the weight applies per word found in a field.

**Still missing or wrong:**
- **Wrong: nothing retrieved is sent to the user.** The top five go to the *model* as id, title and summary. The model picks which pages to open with `read_doc`, and their text becomes its context. The model then writes the answer for the user, "based only on the documents" it read (`ANSWER_PROMPT` in `app/agent.py`), and lists the doc ids it used. Getting that flow right is what RAG means.
- **Vocabulary.** "Retrieve" means fetching *documents*. The keywords are extracted from the query, not retrieved.
- **Still no weakness named, and no "why".**

## Attempt 3 (2026-09-30, written, shortly after reading the model answer)

> the words from query are transformed into a set of lower case words; each word from the query shared by document's title score 3, summary - 1.5, body - 1. the model calls the tool and get top 5 documents, decide which doc to read and use to write the answer. I'm using the keywords because it's cheap and deterministic; this is a baseline the embeddings will have to beat

**Right now:** the scoring unit, the model's role (it calls the tool, chooses what to read, and writes the answer) and the reason for starting with keywords.

**Still missing:**
- **The weakness, for the third time.** The question has two parts, and the second is always dropped.
- **The label.** Open with "keyword retrieval, no vectors yet".
- **The docs become word sets too,** not only the query.

**Caveat:** this came minutes after reading the model answer, so it shows short-term recall. The cold repeat next session is the real check.

**Weakness, when asked for it separately:**

> the weakness is it is exact match and won't match e.g. export with exports.

Correct. The term for the missing step is *stemming*. The second weakness to have ready is synonyms: "download my hours" misses a page that says "export", and that one is what embeddings address.

## Model answer (about 60 seconds)

> It's keyword retrieval, with no vectors yet. The query and each doc become sets of lowercase words, and each query word a doc shares scores 3 in the title, 1.5 in the summary and 1 in the body, so a doc that's *about* the topic outranks one that mentions it in passing. The search is a tool: the model calls `search_docs`, gets the top five as id, title and summary, and decides which pages to open with `read_doc`. Then it writes the answer from those pages and returns the ids it used. I started with keywords because it's cheap and deterministic, and it's the baseline embeddings have to beat on the evals. The main weakness is that it only matches exact words: "exports" misses "export", and "download my hours" misses a page that says "export".

**Next:** ask again cold at the start of the next session, without this file open.
