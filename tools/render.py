"""Render the reading copy from JSONL, or verify it with --check."""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def entry_lines(record, ordinal):
    title = f"{ordinal}. **{record['term_en']}** — {'；'.join(record['terms_zh'])}"
    if record['part_of_speech']:
        title += f" *({record['part_of_speech']})*"
    lines = [title, '']
    for sense in record['senses']:
        prefix = f"{sense['number']}." if sense['number'] else '-'
        chinese = '；'.join(sense['terms_zh'])
        gloss = f"**{chinese}：** " if chinese else ''
        lines.append(f"   {prefix} {gloss}{sense['definition_en']}")
        for key, label in [('labels', 'Sense labels'), ('jurisdictions', 'Sense jurisdiction')]:
            if sense.get(key):
                lines.append(f"      - *{label}:* {'; '.join(sense[key])}")
        if 'source' in sense:
            source = sense['source']
            lines.append(f"      - *Source:* [{source['citation']}]({source['url']}) · {sense['review_status']} · {source['checked']}")
    for key, label in [('language', 'Language'), ('abbreviation_expansions', 'Expands to'),
                       ('labels', 'Labels'), ('jurisdictions', 'Jurisdiction')]:
        value = record[key]
        if value:
            display = value if isinstance(value, str) else '; '.join(value)
            lines.append(f'   - *{label}:* {display}')
    targets = dict.fromkeys(ref['target_term'] for ref in record['cross_references'])
    if targets:
        lines.append('   - *See also:* ' + '; '.join(targets))
    return lines + ['']


def render(records):
    counts = Counter(r['record_type'] for r in records)
    senses = sum(len(r['senses']) for r in records)
    refs = sum(len(r['cross_references']) for r in records)
    lines = ['# OpenLexicon', '', '*An English-first bilingual legal lexicon drafted for learning legal English.*', '',
             f"- **Entries:** {len(records):,} ({counts['main_entry']:,} main entries + {counts['abbreviation_appendix']} abbreviations)",
             f'- **Senses:** {senses:,}', f'- **Cross-references:** {refs:,}',
             '- **Review:** Source-checked senses carry a citation. Other senses await review.',
             '- **Version:** 2.2 · 2026-11-24',
             '- **License and provenance:** [SOURCES.md](SOURCES.md)', '', '---', '']
    def sort_key(record):
        term = record['term_en'].casefold()
        return re.sub(r'[^a-z0-9]', '', term), term
    groups = {}
    for record in sorted(records, key=sort_key):
        group = record['term_en'][0].upper()
        if record['record_type'] == 'abbreviation_appendix':
            group = 'Abbreviations'
        elif group not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            group = 'OTHER'
        groups.setdefault(group, []).append(record)
    ordinal = 0
    for group in sorted(groups, key=lambda g: (len(g) > 1, g == 'Abbreviations', g)):
        lines.extend([f'## {group}', ''])
        if group == 'Abbreviations':
            ordinal = 0
        for record in groups[group]:
            ordinal += 1
            lines.extend(entry_lines(record, ordinal))
    return '\n'.join(lines).rstrip('\n') + '\n'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    with (ROOT / 'OpenLexicon.jsonl').open(encoding='utf-8') as stream:
        output = render(list(map(json.loads, stream)))
    target = ROOT / 'OpenLexicon.md'
    if args.check:
        if target.read_bytes() != output.encode():
            raise SystemExit('Reading copy differs from JSONL. Run tools/render.py.')
    else:
        target.write_bytes(output.encode())
