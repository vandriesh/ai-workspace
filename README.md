# AI workspace

## Layout

```
ai-workspace/
├── README.md
├── tsbuddy-ai/                  # Separate product repository
├── learning/                    # Teaching workspace for Python AI engineering
│   ├── MISSION.md               # Why, and what success looks like
│   ├── RESOURCES.md             # Trusted sources and communities
│   ├── NOTES.md                 # How I prefer to be taught
│   ├── lessons/                 # One short HTML lesson per skill
│   ├── reference/               # Cheat sheets and the 12 cogs map
│   ├── exercises/               # Practice code, checked by tests
│   ├── learning-records/        # What I have shown, not just covered
│   ├── assets/                  # Shared lesson stylesheet and quiz widget
│   └── inbox/                   # Course notes, links, transcripts
├── career/
│   ├── profile/
│   ├── opportunities/
│   └── interview-practice/
└── learning-app/                # The workshop app and its lessons: a step-by-step rebuild of tsbuddy-ai
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

Install the CLI on another macOS or Linux machine after cloning this workspace:

```bash
mkdir -p "$HOME/.local/bin"
ln -s "$HOME/ai-workspace/bin/ai-workspace" "$HOME/.local/bin/ai-workspace"
ln -s "$HOME/ai-workspace/learning-app/bin/workshop" "$HOME/.local/bin/workshop"
```

The second link installs the workshop app's command; start a study session with
`workshop`.

Ensure `~/.local/bin` is on your PATH, or run `~/ai-workspace/bin/ai-workspace`
directly. The script runs on the Bash 3.2 that ships with macOS and needs
nothing else installed; `readlink -f` requires macOS 12.3 or later.
