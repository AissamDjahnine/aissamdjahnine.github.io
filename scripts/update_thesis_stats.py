#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor, Request, build_opener


THESIS_URL = "https://theses.hal.science/tel-05263492"
OUTPUT_PATH = Path(__file__).resolve().parents[1] / "_data" / "thesis_stats.json"


def make_request(url: str) -> Request:
    return Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/123.0.0.0 Safari/537.36"
            )
        },
    )


def read_text(opener, url: str) -> str:
    with opener.open(make_request(url), timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def anubis_pow(random_data: str, difficulty: int) -> tuple[str, int]:
    prefix = "0" * difficulty
    nonce = 0
    while True:
        # ponytail: single-threaded is enough for HAL's current difficulty; add workers if it gets slow.
        digest = hashlib.sha256(f"{random_data}{nonce}".encode()).hexdigest()
        if digest.startswith(prefix):
            return digest, nonce
        nonce += 1


def pass_anubis(opener, html: str, url: str) -> str:
    match = re.search(
        r'<script id="anubis_challenge" type="application/json">(.+?)</script>',
        html,
        re.DOTALL,
    )
    if not match:
        return html

    data = json.loads(match.group(1))
    challenge = data["challenge"]
    started_at = time.monotonic()
    digest, nonce = anubis_pow(challenge["randomData"], data["rules"]["difficulty"])
    elapsed_ms = int((time.monotonic() - started_at) * 1000)
    query = urlencode(
        {
            "id": challenge["id"],
            "response": digest,
            "nonce": nonce,
            "redir": url,
            "elapsedTime": elapsed_ms,
        }
    )
    return read_text(
        opener,
        f"https://theses.hal.science/.within.website/x/cmd/anubis/api/pass-challenge?{query}",
    )


def fetch_html(url: str) -> str:
    opener = build_opener(HTTPCookieProcessor())
    html = read_text(opener, url)
    return pass_anubis(opener, html, url)


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
