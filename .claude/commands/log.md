---
description: View or manage your reading log
allowed-tools: Bash(cat:*), Bash(echo:*), Bash(jq:*), Bash(wc:*)
---

# Reading Log

Manage the reading log stored in `data/reading-log.json`.

## What to Do

If no arguments ($ARGUMENTS is empty), show a summary:
- Total articles read
- Articles this week / this month
- Topic breakdown (how many per topic)
- Recent entries (last 5)
- Average rating
- Longest streak of consecutive days with a reading logged
- Topics they haven't touched recently (gentle nudge)

If arguments are provided:
- `stats` → detailed statistics and trends
- `topic [name]` → filter by topic
- `best` → show highest rated articles (4-5 stars)
- `recent [N]` → show last N entries
- `add` → manually add an entry (prompt for details)

## Presentation

Keep it clean and scannable. Use a simple text table or list format. 
When showing trends, be encouraging but honest — if they haven't read anything in a week, note it without being preachy.

The goal is to build a sense of progress and pattern awareness, not guilt.
