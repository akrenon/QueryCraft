---
name: own-surface-review
description: Guides a review of the user's own external footprint using public search sources. Use when the user wants to know what the internet can see about their own domain, company or IP ranges, asks for an attack surface check of their own assets, or says "what is exposed about my domain", "check my own footprint", "what can outsiders see about my company".
---

# Own surface review

Help the user see their own assets the way an outsider would, using only public search sources. Answer in the language the user writes in.

## Before starting

Confirm which domains, organisation names and IP ranges belong to the user or to an organisation that authorised the review. Work only with those. If the user names assets that look like they belong to someone else, ask about the authorisation before continuing.

## Steps

1. **Collect the seeds.** Domains, known subdomains, organisation name as it appears in certificates and WHOIS, ASNs and IP ranges.
2. **Walk the source groups** from the `querycraft` skill in this order and build queries for each, limited to the seeds:
   1. Certificates and DNS, to find subdomains and hostnames the user may have forgotten.
   2. Web archives, to find old pages, endpoints and files that were once public.
   3. Web search, to find indexed documents and pages on the user's domains.
   4. Internet scanners, to see which services on the user's IP ranges are visible and what they reveal.
   5. Code search, to find public repositories that mention the user's domains or internal hostnames.
3. **Have the user run the queries** or run them with available tools, and collect what comes back.
4. **Sort the findings** into: unknown assets, services that should not be public, information leaks, and items that are fine. For each item give the source and a suggested owner action.
5. **Offer a log.** Suggest recording the queries with the `research-log` skill so the review can be repeated later.

## Boundaries

Stop at observation. Do not test, log in to or probe any system found. If findings include credentials or personal data, advise the user to rotate or remove them and not to store copies.
