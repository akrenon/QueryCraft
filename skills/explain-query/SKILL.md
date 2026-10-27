---
name: explain-query
description: Explains an existing OSINT search query piece by piece. Use when the user pastes a Google dork, a Shodan, Censys, FOFA or other search query and asks what it does, why it returns nothing, why it returns too much, or how to adapt it. Also triggers on "explain this query", "what does this dork do", "why does this search find nothing".
---

# Explain a query

Take a query the user already has and make it understandable and fixable. Answer in the language the user writes in.

## Steps

1. **Identify the engine.** Infer it from the syntax. If the syntax fits several engines, name the candidates and explain for the most likely one.
2. **Break it down.** Split the query into its parts (operators, field filters, quoted strings, boolean logic, grouping). For each part give one line: what it matches and how it narrows or widens the result set.
3. **State the overall intent** in one or two plain sentences: what kind of result the whole query is designed to find.
4. **Check it.** Point out syntax errors, operators the engine no longer supports or treats as unreliable, filters that need a paid plan, logic that cancels itself out, and quoting problems. When a search tool is available and an operator looks unusual, check the engine's official documentation.
5. **Suggest fixes.** If the user reported zero or noisy results, give a corrected version and one broader or narrower variant, and say which change matters most.

## Boundaries

Explaining a query is fine whatever its origin, including queries copied from public collections. Apply the responsible use rules of the `querycraft` skill when the user asks to adapt a query toward a specific third party target or toward a private individual.
