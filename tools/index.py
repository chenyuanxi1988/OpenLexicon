"""Generate or check the headword index and inclusive UTF-8 byte ranges."""
import argparse
import csv
import io
import json
import string
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / 'index'


def make_index():
    groups = defaultdict(list)
    with (ROOT / 'OpenLexicon.jsonl').open('rb') as stream:
        start = 0
        for line, raw in enumerate(stream, 1):
            record = json.loads(raw)
            headword = record['term_en']
            initial = headword[0].lower()
            group = initial if initial in string.ascii_lowercase else 'other'
            end = start + len(raw)
            groups[group].append((headword, record['id'], line, start, end - 1))
            start = end
    result = {}
    for group, rows in groups.items():
        buffer = io.StringIO()
        writer = csv.writer(buffer, delimiter='\t', lineterminator='\n')
        writer.writerow(('headword', 'id', 'line', 'start_byte', 'end_byte'))
        writer.writerows(sorted(rows, key=lambda row: row[0].casefold()))
        result[DIRECTORY / (group + '.tsv')] = buffer.getvalue().encode()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    expected = make_index()
    stale = set(DIRECTORY.glob('*.tsv')) - expected.keys()
    if args.check:
        if stale or any(not p.exists() or p.read_bytes() != data for p, data in expected.items()):
            raise SystemExit('Index differs from JSONL. Run python3 tools/index.py.')
        return
    DIRECTORY.mkdir(exist_ok=True)
    for path, data in expected.items():
        path.write_bytes(data)
    for path in stale:
        path.unlink()


if __name__ == '__main__':
    main()
