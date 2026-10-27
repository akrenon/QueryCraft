# QueryCraft

QueryCraft helps Claude build, explain and fix search queries for OSINT work. I built it because I kept rewriting the same dorks and scanner queries by hand, mixing up syntax between engines and losing track of what I had already searched.

It covers web search engines, internet scanners, certificate and DNS sources, web archives, code search, threat intelligence platforms and image search.

## Install

In Claude Code:

```
/plugin install querycraft --marketplace akrenon/QueryCraft
```

## What it does

**querycraft** turns an investigation goal into queries for the right engines. Each query comes with a short explanation of every operator, a broader and a narrower variant, notes on plan limits, and a direct search link.

**explain-query** takes a query you already have and breaks it down part by part. If it returns nothing or far too much, you get a corrected version.

**research-log** records each query with date, engine, exact query string and result count, so the research can be repeated and described in a report.

**own-surface-review** walks through what public sources show about your own domains and IP ranges, in a fixed order, and sorts the findings by what needs action.

## Examples

- "Build a Shodan query for my company's IP range and explain each filter"
- "Translate this Censys query into Shodan syntax"
- "Why does this Google dork return zero results?"
- "What do public sources show about my own domain?"

The skills answer in the language you write in.

## Link builder

`scripts/build_links.py` turns a query into correctly encoded search links. Claude uses it automatically when a shell is available. You can also run it yourself:

```
python3 scripts/build_links.py --list
python3 scripts/build_links.py --engine google --engine shodan "your query"
python3 scripts/build_links.py --all "your query"
```

It only builds URLs and never sends a request. It needs Python 3 and nothing else.

## Setup

None. QueryCraft needs no API keys and does not connect to any search engine on its own. You run the queries yourself, or Claude runs them with tools you have already connected.

## Responsible use

QueryCraft is meant for passive discovery against public search indexes: your own assets, systems you are authorised to assess, and research that looks at exposure across many hosts at once. It will not help locate or profile private individuals. When a query is likely to surface credentials or personal data, it says so and points to responsible disclosure instead of collecting the data. Nothing found through a query should be accessed or tested without permission.

## License

Apache License 2.0, see [LICENSE](LICENSE) and [NOTICE](NOTICE).

Made by [AKRENON](https://akrenon.com).
