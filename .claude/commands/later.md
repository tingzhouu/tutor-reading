---
description: Save an article to read later
allowed-tools: Read, Write, Edit, WebFetch
---

# Save for Later

The user wants to save an article to their read-later queue.

## Step 1: Parse Input

The user should provide a URL in $ARGUMENTS. If no URL is provided, ask for one.

## Step 2: Get Article Info

If a URL is provided, try to fetch the page to extract the title. If fetching fails or is slow, just ask the user for a title or use the URL domain as a fallback.

Infer the topic from the title/URL. Valid topics: `software-engineering`, `ai-ml`, `using-ai`, `finance`, `self-improvement`, `health`, `other`.

## Step 3: Save to Queue

Read `data/read-later.json` and append a new entry:

```json
{
  "added": "YYYY-MM-DD",
  "title": "Article Title",
  "url": "https://...",
  "topic": "topic-tag",
  "note": "Optional user note or empty string"
}
```

Write the updated array back to `data/read-later.json`.

## Step 4: Confirm

Confirm it's saved with the title and topic. Keep it brief — one line is enough. If the user included a note with the URL, save that too.
