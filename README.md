# AI workspace

## Layout

```
ai-workspace/
├── README.md
├── tsbuddy-ai/                  # Separate product repository
├── learning/
│   ├── inbox/                   # Course notes, links, transcripts
│   ├── curriculum/              # Python + 12 cogs
│   ├── exercises/               # Practice based on real project changes
│   └── progress/                # Attempts and learning evidence
├── career/
│   ├── profile/
│   ├── opportunities/
│   └── interview-practice/
└── learning-app/                # Future gamified learning app
```

`tsbuddy-ai/` and `learning-app/` are separate clones, ignored by this
repository's git and synced through `repos.txt`. Everything under `learning/`
and `career/` is tracked here; each of those folders keeps a `.gitkeep` so it
survives a fresh clone while empty.

## Sync all repositories

Run from any directory on this machine:

```bash
ai-workspace pull    # Default: download committed changes, fast-forward only
ai-workspace push    # Upload existing commits to each configured upstream
ai-workspace status  # Show local state; ahead/behind uses the last fetched state
```

Commit your work before switching machines, then run `ai-workspace push`.
On the other machine, run `ai-workspace pull`.

Repositories are listed in `repos.txt`. Each nested folder must contain its own
clone. Missing clones are reported; this command does not create them.
Pull skips dirty repositories. Errors do not prevent processing the remaining
repositories, but any missing or failed repository makes the command exit nonzero.
The command never creates commits, stashes changes, forces pushes or resets files.
Push transfers existing commits only; it leaves uncommitted changes untouched.

Install the CLI on another Linux machine after cloning this workspace:

```bash
mkdir -p "$HOME/.local/bin"
ln -s "$HOME/ai-workspace/bin/ai-workspace" "$HOME/.local/bin/ai-workspace"
```

Ensure `~/.local/bin` is on your PATH, or run `~/ai-workspace/bin/ai-workspace`
directly. This Bash script uses GNU `readlink -f` and Bash `mapfile`.
