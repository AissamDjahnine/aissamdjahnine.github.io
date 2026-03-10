#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen


THESIS_URL = "https://theses.hal.science/tel-05263492"
OUTPUT_PATH = Path(__file__).resolve().parents[1] / "_data" / "thesis_stats.json"


def fetch_html(url: str) -> str:
    req = Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/123.0.0.0 Safari/537.36"
            )
        },
    )
    with urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def parse_metric(html: str, label: str) -> int:
    pattern = re.compile(
        rf'<div class="metrics-views col-6">\s*<span>\s*([\d\s]+)\s*</span>\s*<span>{label}</span>',
        re.IGNORECASE | re.MULTILINE,
    )
    match = pattern.search(html)
    if not match:
        raise RuntimeError(f"Could not find metric for label: {label}")
    return int(re.sub(r"\s+", "", match.group(1)))


def main() -> None:
    html = fetch_html(THESIS_URL)
    views = parse_metric(html, "Consultations")
    downloads = parse_metric(html, "Téléchargements")

    payload = {
        "views": views,
        "downloads": downloads,
        "source_url": THESIS_URL,
        "updated_at": datetime.now(timezone.utc).date().isoformat(),
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
