#!/usr/bin/env python3
"""
build_universe.py — ETL: CSV → rwa_universe.json

Reads data/rwa_tokens.csv (2,257 rows from backend data team)
and merges rows by symbol into data/rwa_universe.json (955 tokens).

Native tokens in data/native_rwa.json take priority on symbol collision.

Usage:
  python3 scripts/build_universe.py
"""

import csv
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(PROJECT_DIR, "data")

CSV_PATH = os.path.join(DATA_DIR, "rwa_tokens.csv")
OUTPUT_PATH = os.path.join(DATA_DIR, "rwa_universe.json")
NATIVE_PATH = os.path.join(DATA_DIR, "native_rwa.json")

# ── Chain index → chain name mapping ──
INDEX_TO_CHAIN = {
    "1":        "ethereum",
    "56":       "bsc",
    "501":      "solana",
    "42161":    "arbitrum",
    "5000":     "mantle",
    "70000080": "linea",
    "195":      "tron",
    "607":      "aptos",
    "143":      "tron_test",   # mapped but likely unused
    "988":      "oasys",
    "9745":     "etherlink",
    "42220":    "celo",
    "43114":    "avalanche",
}

# ── Tag → category mapping ──
# Priority order: first match wins
# Check order matters: leveraged (48) must precede stablestock (38)
# because leveraged ETFs carry both tags
TAG_PRIORITY = [
    (48, "leveraged"),
    (36, "xstock"),
    (37, "ondo_tokenized"),
    (39, "rstock"),
    (40, "prestock"),
    (38, "stablestock"),
    (33, "gold"),
    (34, "gold"),
]

# Categories where has_nav is True
HAS_NAV_CATEGORIES = {"gold"}

def parse_tags(raw: str) -> list:
    """Parse '[36, 28, 29, 13]' → [36, 28, 29, 13]."""
    raw = raw.strip().strip('"').strip("[]")
    tags = []
    for t in raw.split(","):
        t = t.strip()
        if t:
            try:
                tags.append(int(t))
            except ValueError:
                pass
    return tags


def classify(tags: list) -> str:
    """Map tags → category. Returns category string (priority order)."""
    for tag, cat in TAG_PRIORITY:
        if tag in tags:
            return cat
    return "xstock"  # fallback


def build():
    if not os.path.exists(CSV_PATH):
        print(f"ERROR: CSV not found at {CSV_PATH}")
        sys.exit(1)

    # Read CSV
    rows = []
    with open(CSV_PATH, encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if len(row) < 5:
                continue
            chain_index = row[0].strip().strip('"')
            address = row[1].strip().strip('"')
            symbol = row[2].strip().strip('"')
            name = row[3].strip().strip('"')
            tags_raw = ",".join(row[4:])  # tags may contain commas in name
            tags = parse_tags(tags_raw)
            rows.append({
                "chain_index": chain_index,
                "address": address,
                "symbol": symbol,
                "name": name,
                "tags": tags,
            })

    print(f"Read {len(rows)} rows from CSV")

    # Group by symbol → merge chains/addresses
    universe = {}
    for row in rows:
        sym = row["symbol"]
        chain_name = INDEX_TO_CHAIN.get(row["chain_index"], f"chain_{row['chain_index']}")
        category = classify(row["tags"])

        if sym not in universe:
            universe[sym] = {
                "name": row["name"],
                "category": category,
                "asset_backed": True,
                "has_nav": category in HAS_NAV_CATEGORIES,
                "source": "csv",
                "chains": [],
                "addresses": {},
            }

        entry = universe[sym]
        if chain_name not in entry["chains"]:
            entry["chains"].append(chain_name)
        if chain_name not in entry["addresses"]:
            entry["addresses"][chain_name] = row["address"]

    print(f"Merged into {len(universe)} unique tokens")

    # Category stats
    from collections import Counter
    cat_count = Counter(v["category"] for v in universe.values())
    for cat, cnt in sorted(cat_count.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {cnt}")

    # Chain stats
    chain_count = Counter()
    for v in universe.values():
        for c in v["chains"]:
            chain_count[c] += 1
    print(f"\nChain distribution:")
    for ch, cnt in sorted(chain_count.items(), key=lambda x: -x[1]):
        print(f"  {ch}: {cnt}")

    # Multi-chain tokens
    multi = [(s, len(v["chains"])) for s, v in universe.items() if len(v["chains"]) > 1]
    if multi:
        print(f"\nMulti-chain tokens ({len(multi)}):")
        for sym, nc in sorted(multi, key=lambda x: -x[1])[:10]:
            chains = universe[sym]["chains"]
            print(f"  {sym}: {nc} chains ({', '.join(chains)})")

    # Load native tokens to identify collisions
    native = {}
    if os.path.exists(NATIVE_PATH):
        with open(NATIVE_PATH) as f:
            native = json.load(f)
        collisions = set(universe.keys()) & set(native.keys())
        if collisions:
            print(f"\nSymbol collisions (native wins): {', '.join(sorted(collisions))}")
            for sym in collisions:
                del universe[sym]

    # Write output
    with open(OUTPUT_PATH, "w") as f:
        json.dump(universe, f, indent=2, ensure_ascii=False)

    total = len(universe) + len(native)
    size_kb = os.path.getsize(OUTPUT_PATH) / 1024
    print(f"\nWrote {OUTPUT_PATH}")
    print(f"  {len(universe)} CSV tokens + {len(native)} native = {total} total")
    print(f"  File size: {size_kb:.0f} KB")


if __name__ == "__main__":
    build()
