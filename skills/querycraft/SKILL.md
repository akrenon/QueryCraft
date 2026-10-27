---
name: querycraft
description: Builds, explains and refines OSINT search queries. Use when the user wants a Google dork, a Bing, DuckDuckGo, Yandex or Baidu query with operators, a Shodan, Censys, FOFA, ZoomEye or Netlas search, a crt.sh, Wayback Machine, urlscan.io or GitHub code search, wants to translate a query from one engine to another, asks why a dork returns nothing, or says things like "find exposed X", "search for hosts running Y", "dork for Z", "build a Shodan query", "convert this to Censys", "rewrite this query for FOFA".
---

# QueryCraft

Turn an investigation goal into working search queries for the right engines, explain every operator used, and give the user ready-to-click links. Answer in the language the user writes in.

## Engines covered

| Group | Engines | Typical use |
| --- | --- | --- |
| Web search | Google, Bing, DuckDuckGo, Yandex, Baidu, Brave Search, Mojeek | Pages, documents and files indexed on the open web; regional coverage (Yandex for Russian and CIS content, Baidu for Chinese content) |
| Internet scanners | Shodan, Censys Platform (CenQL), FOFA, ZoomEye, Netlas, ONYPHE, Criminal IP, Hunter.how | Open ports, service banners, software versions, network ranges, technology fingerprints |
| Certificates and DNS | crt.sh, Censys certificates, SecurityTrails, DNSDumpster | Subdomain discovery through certificate transparency, historical DNS records, related infrastructure |
| Web archives | Wayback Machine (incl. CDX API), archive.today, Common Crawl index | Past versions of pages, removed content, old URLs and endpoints |
| Code and source search | GitHub code search, GitLab search, grep.app, PublicWWW | Configuration leaks in public repositories, websites sharing a tracking ID or script |
| Threat intelligence | urlscan.io, VirusTotal, GreyNoise (GNQL), AlienVault OTX | Phishing pages, malicious infrastructure, scanner and botnet noise, indicators of compromise |
| Image search and geolocation | Yandex Images, Google Lens, Bing Visual Search, TinEye | Image provenance, verification of photos and videos, locating landmarks and places |

Operator support changes over time. When a search tool is available, check the engine's official documentation for unusual operators before relying on them.

## Workflow

1. **Pin down the goal.** Work out what the user is looking for (documents, pages, hosts, services, certificates, a technology fingerprint), which scope applies (a domain, an organisation, an ASN, a country, a time window) and why. Ask one short question only when the goal is too vague to build a useful query; otherwise state the assumption and continue.
2. **Pick the engines.** Use the "Typical use" column above. Content on web pages and files points to web search engines. Open ports, banners and software versions point to internet scanners. Subdomains and infrastructure history point to certificate and DNS sources. Removed or changed content points to web archives. Suggest a second engine when it covers a blind spot of the first (Yandex for Russian and CIS content, Bing for its `ip:` operator, FOFA or ZoomEye for better coverage of Asian networks, crt.sh for certificates a scanner has not seen).
3. **Build the query.** Start with a precise primary query, then give one broader and one narrower variant. Quote values that contain spaces or special characters. Keep Google queries under its 32 word limit.
4. **Explain it.** One line per operator: what it does in this query and why it is there.
5. **Link it.** Output a direct search link for each engine, with the query fully URL-encoded (spaces, quotes, colons and other special characters). Check each link once before output; when an engine expects a special format (FOFA, for example, takes the query base64-encoded), say so instead of guessing.
6. **Flag limits.** Mention operators that are unreliable or deprecated, filters that need a paid plan, and typical reasons for zero results.

## Output format

For each engine, use this structure:

```
**<Engine>**
<query in a code block>
Link: <search URL>
- <operator>: <what it does here>
Variants: broader <query> / narrower <query>
Notes: <limits, plan requirements, pitfalls>
```

When the user asks to convert a query between engines, show the source query, the converted query and every operator that has no direct equivalent.

## Related skills in this plugin

- `explain-query`: break down an existing query the user pastes.
- `research-log`: record queries, dates and result counts for reproducible research.
- `own-surface-review`: guided review of the user's own external footprint.

## Troubleshooting zero or noisy results

- Remove operators one at a time to find the one that kills the result set.
- Google silently ignores some operator combinations and personalises results; test in a private window and check whether `site:` alone returns anything.
- Shodan and Censys index banners and responses, not page content you see in a browser; match on what the service actually returns.
- Field names differ between Censys Legacy Search and the Censys Platform; convert old queries before blaming the data.
- Scanner counts are snapshots; add a time filter to separate current exposure from historical records.

## Responsible use

QueryCraft is for passive discovery: building queries against public search indexes. Apply these rules:

- Build queries for the user's own assets, assets in an authorised engagement scope, or aggregate research (counting exposure across many hosts). For queries that single out a specific third party organisation's systems with the aim of finding weaknesses, ask about the scope once and continue when the user confirms a legitimate context.
- Do not build queries meant to locate, profile or track a private individual (home address, daily movements, family members, identifying a person from a photo).
- When a query is likely to surface credentials, keys, personal data or other sensitive files, say so, advise against opening or using the data, and point to responsible disclosure to the owner or the competent CERT.
- Do not log in to, test or interact with systems found through a query. Query building ends at the search result.
