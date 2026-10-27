---
name: research-log
description: Keeps a reproducible log of OSINT queries. Use when the user wants to record which queries were run, on which engine, when and with how many results, wants to export a query log for a report or data article, or says "log this query", "add to my research log", "document my searches", "start a query log".
---

# Research log

Make OSINT work reproducible: anyone reading the log should be able to rerun each query and compare results. Answer in the language the user writes in.

## Log format

Keep one row per query run with these columns:

| Column | Content |
| --- | --- |
| date | Date and time the query was run, ISO 8601 with time zone |
| engine | Engine name, and plan level for scanners if known |
| query | The exact query string, unmodified |
| link | Direct search link |
| purpose | One line on what the query was meant to find |
| results | Result count as the engine reported it, or "not checked" |
| notes | Filters applied in the UI, pagination limits, anything that affects reproducibility |

## Steps

1. **Pick the storage.** Use what the user names. Otherwise prefer a spreadsheet the user can keep editing; fall back to a CSV file with the columns above. Append to an existing log rather than starting a new one when the user refers to "my log".
2. **Record faithfully.** Copy the query exactly. Take result counts only from the user or from a tool result; never estimate or invent a count. Mark unknown values as "not checked".
3. **Keep sensitive data out.** Log the query and the count, not the content of results. Do not store credentials, personal data or file contents surfaced by a query, even when the user pastes them.
4. **Summarise on request.** When the user asks for a summary or methods section, describe engines, date range, number of queries and how counts were obtained, in plain prose suitable for a report.
