---
description: Find high-quality content to read right now
allowed-tools: Bash(python:*), Bash(cat:*), Bash(echo:*), WebFetch, WebSearch
---

# Find Something Great to Read

The user wants reading recommendations. They have limited time and want to make it count.

## Step 1: Determine Context

If the user provided arguments ($ARGUMENTS), use those to focus the search. Examples:

- `/read ai` → focus on AI developments
- `/read 10 min` → short reads only
- `/read finance deep` → in-depth finance content
- `/read surprise me` → something outside their usual topics

If no arguments, pick a balanced mix across their interests.

## Step 2: Check Reading Log

Read `data/reading-log.json` to see what they've read recently. Avoid recommending similar content to what they read in the last week. Use the log to identify topics they haven't covered recently.

## Step 3: Pull from Substack Feed

Run the Substack fetcher to get recent posts from their subscribed newsletters:

```bash
python scripts/fetch_substacks.py --days 7
```

If a topic filter is relevant:

```bash
python scripts/fetch_substacks.py --days 7 --topic ai
```

This returns a JSON array of recent posts. Filter out any marked `already_read: true`. Pick the most interesting-looking posts from the results — don't just list everything the script returns. Use your judgment about what looks substantive based on titles and subtitles.

## Step 4: Supplement with Web Search

If the Substack feed doesn't have enough variety, or the user asked for a topic not well covered by their subscriptions, supplement with web search. Search for:

- Recent posts from known quality sources (see CLAUDE.md for the source list)
- Specific topic searches like "[topic] engineering blog post 2026"
- Look for content published in the last 1-4 weeks for freshness

The Substack feed is the primary source. Web search fills gaps.

## Step 5: Present a Reading Menu

Present 5-7 recommendations as a curated menu. For each item:

**Title** — Source Name
_Estimated read time · Topic tag_
One sentence on why this is worth their time specifically.

Group by reading time:

- ☕ Quick (5-10 min)
- 📖 Medium (15-25 min)
- 🧠 Deep (30+ min)

Mark which ones came from their Substack feed vs. discovered via search.

## Step 6: Let Them Choose

After presenting, ask what catches their eye. If they pick something, fetch the URL and give a brief "what to watch for" primer (2-3 sentences) to prime their reading — key questions the article addresses, or context that makes it more valuable.

Don't summarize the content — the whole point is for them to read it themselves.
