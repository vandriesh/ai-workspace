# Starting point: experienced in TypeScript, writes no Python unaided

Vitalie built tsbuddy in TypeScript (React Router v7, Vite, Prisma monorepo). On 2026-09-28 they said they could not write `Corpus.search` from an empty file without AI; all 9 tsbuddy-ai commits are co-authored by Claude. Reading fluency may exist, but writing starts from zero, so every lesson must end with them producing Python, not just reading it.

**Evidence:** self-report, plus the commit history.

**Implications:** map each new construct to its TypeScript equivalent and to where that instinct misleads. Start with small, pure functions from tsbuddy-ai that plain `python3` can check without installs, and build up to the full `Corpus.search`.
