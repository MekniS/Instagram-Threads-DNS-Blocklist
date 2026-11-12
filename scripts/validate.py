#!/usr/bin/env python3
"""Validate simple AdGuard domain blocking rules and detect duplicates."""
import pathlib
import re
import sys

path = pathlib.Path(__file__).resolve().parents[1] / 'blocklist.txt'
pattern = re.compile(r'^\|\|([a-z0-9](?:[a-z0-9.-]*[a-z0-9])?)\^$')
seen = set()
errors = []
for num, raw in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
    line = raw.strip()
    if not line or line.startswith('!'):
        continue
    match = pattern.fullmatch(line)
    if not match:
        errors.append(f'line {num}: invalid rule: {line}')
        continue
    domain = match.group(1)
    if any(not label or len(label) > 63 or label.startswith('-') or label.endswith('-') for label in domain.split('.')) or '.' not in domain:
        errors.append(f'line {num}: invalid domain: {domain}')
    if domain in seen:
        errors.append(f'line {num}: duplicate: {domain}')
    seen.add(domain)
if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f'Valid: {len(seen)} unique domain rules')
