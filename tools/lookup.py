"""Find exact ID, headword, Chinese translation or abbreviation expansion."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query')
    query = parser.parse_args().query.strip().casefold()
    found = False
    path = Path(__file__).resolve().parents[1] / 'OpenLexicon.jsonl'
    with path.open(encoding='utf-8') as stream:
        for line, raw in enumerate(stream, 1):
            record = json.loads(raw)
            names = [record['id'], record['term_en'], *record['terms_zh'],
                     *record['abbreviation_expansions'], *record.get('aliases', [])]
            for sense in record['senses']:
                names.extend(sense['terms_zh'])
            if any(query == name.casefold() for name in names):
                print(json.dumps({'line': line, 'record': record}, ensure_ascii=False))
                found = True
    if not found:
        raise SystemExit('No exact match.')


if __name__ == '__main__':
    main()
