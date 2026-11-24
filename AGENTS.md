# Using OpenLexicon

Read the JSONL at a known Git commit. It is UTF-8, with one complete record per line. The Markdown file is a generated reading copy. The release has no service to call or install.

## Lookup and citation

1. Match a stable ID or case-folded headword first. For aliases, try an abbreviation expansion and then the expanded headword. Search both record and sense translations for a Chinese term. Treat partial matches as candidates. Read the full record before answering.
2. Keep different senses separate. Take the jurisdiction from the sense when given, then from the record. If neither supplies it, report “jurisdiction unverified”. The same headword can have different tests under different rules.
3. Return the headword, sense number (or ordinal for an unnumbered sense), English explanation and Chinese translation. Give the citation, link and checked date where present. A sense without a source is inherited and unreviewed. Never infer a source from a nearby entry.
4. Cite OpenLexicon by commit, stable ID and sense. A GitHub permalink to the corresponding JSONL line is useful for provenance even when the browser cannot render the large file. Read the official authority separately for legal argument. If no match is found, report the unsuccessful lookup.
5. A cross-reference is a navigation hint. Resolve its target ID and compare the target headword with the displayed label. Historical differences include inflections and mistaken links. If the names or jurisdictions differ, search both headwords and check the underlying authority before asserting a relationship.

## Editing

Keep IDs permanent. Add new records after the highest allocated ID. Preserve distinct meanings and keep jurisdiction-specific sources at sense level. Write definitions independently from the cited authorities and indicate the precise provision or judgment paragraph. Use the existing source-checked records as examples. This status records an AI-assisted comparison with the cited source, without implying review by counsel. Record changes in CHANGELOG.md. Run the renderer and its check before committing. Keep private source materials and account details outside the public repository.
