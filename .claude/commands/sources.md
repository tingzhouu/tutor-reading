---
description: Discover and manage high-quality reading sources
allowed-tools: Bash(cat:*), Bash(echo:*), WebFetch, WebSearch
---

# Source Discovery and Management

Help the user build and refine their personal reading ecosystem.

## What to Do

If no arguments ($ARGUMENTS is empty), show current recommended sources organized by topic (from the CLAUDE.md source list) and ask if they want to explore any area.

If arguments are provided:
- `explore [topic]` → search for new quality sources on that topic, verify they're active and high-quality
- `check [source name or URL]` → evaluate a specific source's quality (check recent posts, frequency, depth)
- `add [url]` → evaluate and add a source to their personal list

## When Exploring New Sources

Search for sources and evaluate them on:
1. **Recency** — are they still actively publishing? (Check last post date)
2. **Signal-to-noise** — are most posts substantive or is it mostly filler?
3. **Practitioner vs. pundit** — does the author actually build/do things?
4. **Originality** — do they have unique perspectives or just aggregate others?

Present findings as a short list with honest assessments. Don't recommend anything you wouldn't actually want to read yourself.
