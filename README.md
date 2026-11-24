# OpenLexicon

OpenLexicon is an English-first bilingual legal lexicon drafted for learning legal English. **本词典为学习法律英语而起草。** English headwords and explanations are accompanied by working Chinese translations.

**[Read the dictionary → OpenLexicon.md](OpenLexicon.md)**

## Version 2.2 · 2026-11-24

8,231 headwords (8,113 main entries and 118 abbreviations), 8,651 senses and 8,764 cross-references. The release contains 36 individually source-checked senses. The other senses await provenance and legal review. Read [source and licence notes](SOURCES.md) before reuse.

## Find and cite an entry

[OpenLexicon.jsonl](OpenLexicon.jsonl) is the master dictionary. Browse the Markdown above or download the raw JSONL if GitHub's preview is limited. With a local checkout, the following commands require only Python 3:

```sh
git rev-parse HEAD
python3 tools/lookup.py "summary judgment"
python3 tools/lookup.py lex-4331
python3 tools/lookup.py 商业秘密
```

The lookup returns the JSONL line number and original record, including all senses. Cite the commit printed by Git, the stable ID and the sense number. For example, **OpenLexicon 2.2, lex-4331, sense 2** identifies the U.S. federal summary-judgment sense. Its legal authority is Fed. R. Civ. P. 56(a). Sense 1 is the England and Wales rule.

[AI retrieval and editing rules](AGENTS.md) · [Sources and reuse](SOURCES.md) · [Change history](CHANGELOG.md) · [Development plan](DEVELOPMENT_PLAN.md)

Edit the JSONL and run `python3 tools/render.py` to refresh the reading copy. Run `python3 tools/render.py --check` to verify that the copy matches the master.

## What changed in Version 2

Fifteen case-insensitive duplicate-headword groups were consolidated into canonical entries. Sixteen duplicate records were merged while their distinct meanings and English wording were retained as separate senses. Capitalization conventions, source-specific labels, and jurisdiction scope are kept at the relevant sense where needed. One exactly repeated IDPC definition was displayed once instead of twice, with no distinct meaning removed. Thirteen cross-reference target IDs were redirected to retained canonical records.

This release also includes a limited set of reviewed Chinese-translation and part-of-speech corrections, including the descriptive translation used for `Master of the Rolls` and `MR`. Chinese remains a working editorial layer, not a completed jurisdiction-wide terminology review.

## Scope and sources

The English text is retained from the supplied clean dictionary. This release is not an independent certification of legal accuracy, translation accuracy, or originality, and it is not legal advice.

Oxford University Press, *A Dictionary of Law*, 10th edition (2022), was used as a reference for some headwords and senses. This does not mean that every entry comes from that work or that this release reproduces or certifies its text.

## License

Project contributions that OpenLexicon is entitled to license are offered under [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/). Rights in any third-party materials are unaffected. Reusers remain responsible for identifying applicable rights, giving attribution, indicating changes, and complying with the license where it applies.
