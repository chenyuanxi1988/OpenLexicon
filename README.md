# OpenLexicon

OpenLexicon is an English-first bilingual legal lexicon drafted for learning legal English. **本词典为学习法律英语而起草。** English headwords and explanations are accompanied by working Chinese translations.

**[Read the dictionary → OpenLexicon.md](OpenLexicon.md)**

## Version 2

- **Date:** 2026-10-11
- **Entries:** 8,227 — 8,109 main entries and 118 abbreviations.
- **Senses:** 8,633.
- **Cross-references:** 8,790.
- **License:** CC BY-SA 4.0, subject to the qualifications below.

## Files

- `README.md` — this introduction.
- `OpenLexicon.md` — the complete human-readable dictionary, alphabetically grouped. Internal record IDs are not displayed.
- `OpenLexicon.jsonl` — one JSON object per line for search, analysis, and reuse. Stable `id` values connect `cross_references[].target_id` to dictionary records.

For ordinary reading, open `OpenLexicon.md`. Use an editor's search function to find an English headword or Chinese term. Use `OpenLexicon.jsonl` when exact fields, stable IDs, sense metadata, or reference links are needed.

## What changed in Version 2

Fifteen case-insensitive duplicate-headword groups were consolidated into canonical entries. Sixteen duplicate records were merged while their distinct meanings and English wording were retained as separate senses. Capitalization conventions, source-specific labels, and jurisdiction scope are kept at the relevant sense where needed. One exactly repeated IDPC definition was displayed once instead of twice, with no distinct meaning removed. Thirteen cross-reference target IDs were redirected to retained canonical records.

This release also includes a limited set of reviewed Chinese-translation and part-of-speech corrections, including the descriptive translation used for `Master of the Rolls` and `MR`. Chinese remains a working editorial layer, not a completed jurisdiction-wide terminology review.

## Scope and sources

The English text is retained from the supplied clean dictionary. This release is not an independent certification of legal accuracy, translation accuracy, or originality, and it is not legal advice.

Oxford University Press, *A Dictionary of Law*, 10th edition (2022), was used as a reference for some headwords and senses. This does not mean that every entry comes from that work or that this release reproduces or certifies its text.

## License

Project contributions that OpenLexicon is entitled to license are offered under [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/). Rights in any third-party materials are unaffected. Reusers remain responsible for identifying applicable rights, giving attribution, indicating changes, and complying with the license where it applies.
