---
description: Discuss and deepen understanding of something you just read
allowed-tools: Bash(cat:*), Bash(echo:*), WebFetch, WebSearch
---

# Discuss What You've Read

The user wants to discuss content they've just read. This is where shallow reading becomes deep understanding.

## Step 1: Get the Content

If the user provided a URL ($ARGUMENTS), fetch it and read it.
If they pasted text or described what they read, work with that.
If neither, ask what they just read.

## Step 2: Start the Discussion

DON'T just summarize back to them — they already read it. Instead, do one of these depending on what fits:

### Challenge Their Understanding
Ask a probing question that tests whether they got the core argument, not just the surface:
- "What's the strongest counterargument to the author's main claim?"
- "If you had to explain the key insight to a colleague in 30 seconds, what would you say?"
- "What assumption is the author making that they never explicitly state?"

### Connect to Their World
Draw connections to their professional context or other things they've read:
- "How does this relate to [topic from reading log]?"
- "Would this approach work in a payments/fintech context? Why or why not?"
- "What would you change about your current workflow based on this?"

### Go Deeper
Point them toward the deeper layer:
- "The author mentions X but doesn't go into detail — that's actually a rabbit hole worth exploring because..."
- "This builds on [earlier idea/paper] — the key evolution is..."
- "The interesting tension here is between X and Y..."

## Step 3: Have a Real Conversation

This should feel like talking with a well-read friend at a coffee shop, not a book report. Be opinionated. Disagree with the author if warranted. Push back on the user's takes if they're surface-level.

Keep the discussion going for as long as the user is engaged. Ask follow-ups. Make them articulate their thinking.

## Step 4: Wrap Up and Log

When the discussion winds down:
1. Offer a brief synthesis: "Here's what I think you got out of this..."
2. Suggest 1-2 follow-up reads that connect to what they just discussed
3. Offer to log it: ask for their 1-5 rating and update `data/reading-log.json`
