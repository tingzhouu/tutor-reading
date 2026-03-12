#!/usr/bin/env python3
"""Fetch recent posts from configured Substack newsletters.

Usage:
    python scripts/fetch_substacks.py                # fetch all, last 7 days
    python scripts/fetch_substacks.py --days 14      # fetch all, last 14 days
    python scripts/fetch_substacks.py --topic ai     # fetch only AI substacks
    python scripts/fetch_substacks.py --limit 3      # max 3 posts per newsletter
"""

import json
import argparse
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests


PROJECT_ROOT = Path(__file__).parent.parent


def load_config():
    config_path = PROJECT_ROOT / "data" / "substacks.json"
    if not config_path.exists():
        print(f"Error: config not found at {config_path}")
        sys.exit(1)
    with open(config_path) as f:
        return json.load(f)


def load_reading_log():
    log_path = PROJECT_ROOT / "data" / "reading-log.json"
    if not log_path.exists():
        return []
    with open(log_path) as f:
        return json.load(f)


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}


def fetch_archive(base_url, limit=5):
    """Fetch posts from a Substack archive API, using the site's base URL directly."""
    base_url = base_url.rstrip("/")
    url = f"{base_url}/api/v1/archive?sort=new&search=&offset=0&limit={limit}"
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json()


def fetch_posts(substacks, days=7, limit=5, topic=None):
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    reading_log = load_reading_log()
    read_urls = {entry.get("url", "") for entry in reading_log}

    results = []

    for sub in substacks:
        if topic and sub.get("topic") != topic:
            continue

        name = sub.get("name", sub["url"])
        base_url = sub["url"]
        print(f"Fetching: {name}...", file=sys.stderr)

        try:
            posts = fetch_archive(base_url, limit=limit)

            for post in posts:
                title = post.get("title", "Untitled")
                subtitle = post.get("subtitle", "")
                slug = post.get("slug", "")
                post_date_str = post.get("post_date", "")
                canonical_url = post.get("canonical_url", "")
                word_count = post.get("wordcount", 0) or post.get("word_count", 0)

                # Build URL if not provided
                if not canonical_url and slug:
                    canonical_url = f"https://{subdomain}.substack.com/p/{slug}"

                # Parse date and filter by cutoff
                post_date = None
                if post_date_str:
                    try:
                        post_date = datetime.fromisoformat(
                            str(post_date_str).replace("Z", "+00:00")
                        )
                        if post_date < cutoff:
                            continue
                    except (ValueError, TypeError):
                        pass

                # Estimate read time
                read_mins = max(1, (word_count or 1000) // 250)

                already_read = canonical_url in read_urls

                results.append({
                    "title": title,
                    "subtitle": subtitle,
                    "url": canonical_url,
                    "source": name,
                    "topic": sub.get("topic", "general"),
                    "date": post_date.isoformat() if post_date else "",
                    "read_minutes": read_mins,
                    "already_read": already_read,
                })

        except Exception as e:
            print(f"  Error fetching {name}: {e}", file=sys.stderr)
            continue

    # Sort by date descending
    results.sort(key=lambda x: x.get("date", ""), reverse=True)
    return results


def main():
    parser = argparse.ArgumentParser(description="Fetch recent Substack posts")
    parser.add_argument("--days", type=int, default=7, help="Look back N days (default: 7)")
    parser.add_argument("--limit", type=int, default=5, help="Max posts per newsletter (default: 5)")
    parser.add_argument("--topic", type=str, help="Filter by topic")
    args = parser.parse_args()

    config = load_config()
    posts = fetch_posts(config["substacks"], days=args.days, limit=args.limit, topic=args.topic)

    # Output as JSON to stdout (for Claude Code to consume)
    print(json.dumps(posts, indent=2))


if __name__ == "__main__":
    main()
