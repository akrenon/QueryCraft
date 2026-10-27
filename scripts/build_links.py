#!/usr/bin/env python3
"""Build correctly encoded search links for one query across several engines.

Usage:
    python3 build_links.py --engine google --engine shodan "your query"
    python3 build_links.py --all "your query"
    python3 build_links.py --list

Only builds URLs. It never sends a request.
"""

import argparse
import base64
import sys
from urllib.parse import quote, quote_plus

# Each entry: engine id -> (display name, function that turns a query into a URL)
ENGINES = {
    "google": ("Google", lambda q: "https://www.google.com/search?q=" + quote_plus(q)),
    "bing": ("Bing", lambda q: "https://www.bing.com/search?q=" + quote_plus(q)),
    "duckduckgo": ("DuckDuckGo", lambda q: "https://duckduckgo.com/?q=" + quote_plus(q)),
    "yandex": ("Yandex", lambda q: "https://yandex.com/search/?text=" + quote_plus(q)),
    "baidu": ("Baidu", lambda q: "https://www.baidu.com/s?wd=" + quote_plus(q)),
    "brave": ("Brave Search", lambda q: "https://search.brave.com/search?q=" + quote_plus(q)),
    "mojeek": ("Mojeek", lambda q: "https://www.mojeek.com/search?q=" + quote_plus(q)),
    "shodan": ("Shodan", lambda q: "https://www.shodan.io/search?query=" + quote_plus(q)),
    "censys": ("Censys Platform", lambda q: "https://platform.censys.io/search?q=" + quote_plus(q)),
    "fofa": (
        "FOFA",
        lambda q: "https://en.fofa.info/result?qbase64="
        + quote(base64.b64encode(q.encode("utf-8")).decode("ascii"), safe=""),
    ),
    "crtsh": ("crt.sh", lambda q: "https://crt.sh/?q=" + quote_plus(q)),
    "github": ("GitHub code search", lambda q: "https://github.com/search?type=code&q=" + quote_plus(q)),
    "grepapp": ("grep.app", lambda q: "https://grep.app/search?q=" + quote_plus(q)),
    "urlscan": ("urlscan.io", lambda q: "https://urlscan.io/search/#" + quote(q, safe="")),
    "virustotal": ("VirusTotal", lambda q: "https://www.virustotal.com/gui/search/" + quote(q, safe="")),
    "wayback": ("Wayback Machine", lambda q: "https://web.archive.org/web/*/" + quote(q, safe=":/*")),
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("query", nargs="?", help="the search query, quoted as one argument")
    parser.add_argument("--engine", "-e", action="append", default=[], help="engine id, repeatable")
    parser.add_argument("--all", action="store_true", help="build links for every engine")
    parser.add_argument("--list", action="store_true", help="list supported engine ids")
    args = parser.parse_args()

    if args.list:
        for key, (name, _) in ENGINES.items():
            print(f"{key:12} {name}")
        return 0

    if not args.query:
        parser.error("a query is required")

    selected = list(ENGINES) if args.all else args.engine
    if not selected:
        parser.error("pass --engine at least once, or --all")

    unknown = [e for e in selected if e not in ENGINES]
    if unknown:
        print("Unknown engine id(s): " + ", ".join(unknown), file=sys.stderr)
        print("Run with --list to see supported ids.", file=sys.stderr)
        return 2

    for key in selected:
        name, build = ENGINES[key]
        print(f"{name}: {build(args.query)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
