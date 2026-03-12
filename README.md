# Reading Tutor

A Claude Code project that acts as your personal reading curator and discussion partner. Built to replace low-signal Reddit browsing with high-quality, substantive reading.

## Setup

1. Make sure you have [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) installed
2. Clone or copy this directory somewhere on your machine
3. `cd` into the project directory
4. Run `claude` to start a session

## Commands

| Command | What it does |
|---------|-------------|
| `/read` | Find high-quality content to read right now |
| `/read ai` | Find content on a specific topic |
| `/read 10 min` | Find quick reads |
| `/discuss` | Discuss something you just read |
| `/discuss [url]` | Discuss a specific article |
| `/log` | View your reading history and stats |
| `/log best` | See your highest-rated reads |
| `/log topic ai` | Filter log by topic |
| `/sources` | Browse recommended sources |
| `/sources explore [topic]` | Discover new quality sources |

## How It Works

- **CLAUDE.md** contains the tutor's personality, your interest profile, and quality heuristics
- **Slash commands** in `.claude/commands/` define the four interaction modes
- **Reading log** in `data/reading-log.json` tracks what you've read over time

## Customization

- Edit **CLAUDE.md** to adjust your interest profile or add/remove quality sources
- The reading log builds over time — the tutor uses it to avoid repeats and notice gaps
- Add new commands in `.claude/commands/` for any workflows you want (e.g., a `/weekly-review` command)

## Tips

- Start each reading session with `/read` and let it curate for you
- After reading something, always do `/discuss [url]` — this is where the real value is
- Check `/log` weekly to see your patterns
- When you find a great new blog or newsletter, run `/sources check [url]` to evaluate it
