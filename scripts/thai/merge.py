#!/usr/bin/env python3
"""Merge a local translation draft, reviewed terminology and explicit overrides.

Usage: python3 scripts/thai/merge.py /path/to/draft.jsonl
Draft records: {"key": [context, English], "translation": Thai}.
The script preserves existing keys and never translates command identifiers.
"""
import json
import re
import sys
from pathlib import Path
from validate import CATALOGS, read

path = CATALOGS / 'th.tsv'
rows = read(path)
for line in Path(sys.argv[1]).read_text().splitlines():
    entry = json.loads(line)
    rows[tuple(entry['key'])] = entry['translation']

# Correct repeated terminology in the machine-assisted draft. These corrections
# are scoped to matching English terms to avoid changing unrelated messages.
terms = {
    'artboard': {'แผงภาพศิลป์': 'อาร์ตบอร์ด'},
    'bicubic': {'บิซิฟิค': 'ไบคิวบิก', 'กราดเรียบ': 'ไล่ระดับสีเรียบ'},
    'gradient': {'กรัเดียนต์': 'ไล่ระดับสี', 'กรัดเอนท์': 'ไล่ระดับสี', 'กราด': 'ไล่ระดับสี'},
    'panel': {'ป้าย': 'แผง'},
    'anchor': {'จุดติดตั้ง': 'จุดยึด', 'จุดตั้งต้น': 'จุดยึด'},
    'noise': {'เสียงรบกวน': 'นอยส์'},
    'pin': {'ปิน': 'หมุด'},
    'guide': {'เส้นทาง': 'เส้นไกด์'},
    'override': {'การยึดติด': 'ค่าที่ปรับทับ', 'การยึดตัว': 'ค่าที่ปรับทับ'},
    'camera raw': {'RAW กล้อง': 'Camera Raw'},
    'paragraph': {'ข้อความแบบย่อย': 'ข้อความแบบย่อหน้า'},
    'layer': {'ชั้นภาพ': 'เลเยอร์', 'ชั้นวิดีโอ': 'เลเยอร์วิดีโอ'},
    'breeze': {'ลมเบา': 'Breeze', 'ลมด้าน': 'Breeze '},
    'frame': {'ฟรม': 'เฟรม'},
    'pressure': {'ความดัน': 'แรงกด'},
    'flame': {'ไฟลาม': 'เปลวไฟ'},
    'jitter': {'การสั่นของ': 'ความแปรผันของ', 'การสั่นสะเทือน': 'ความแปรผัน'},
    'vignette': {'การยุบตัว': 'ขอบมืด'},
    'shortcut': {'ช็อตคีย์': 'แป้นพิมพ์ลัด', 'การตั้งค่าเร็ว': 'แป้นพิมพ์ลัด', 'การตั้งค่าสั้น': 'แป้นพิมพ์ลัด', 'ชุดสั้น': 'รายการแป้นพิมพ์ลัด'},
    'font': {'ตัวอักษร': 'ฟอนต์'},
    'effect': {'ผลลัพธ์': 'เอฟเฟกต์'},
}
for key, target in rows.items():
    source = key[1]
    for term, replacements in terms.items():
        if term in source.lower():
            for old, new in replacements.items():
                target = target.replace(old, new)
    target = target.replace('พื้นนที่', 'พื้นที่').replace('ด้้วย', 'ด้วย')
    rows[key] = target

# Camera Raw shares reviewed wording with the common image-editing labels.
for key in list(rows):
    if key[0] == 'cameraRaw' and ('', key[1]) in rows:
        rows[key] = rows['', key[1]]

overrides = read(Path(__file__).with_name('overrides.tsv'))
for key, target in overrides.items():
    if key in rows:
        rows[key] = target
    if not key[0] and ('cameraRaw', key[1]) in rows:
        rows['cameraRaw', key[1]] = target

header = '# Thai localization for PhotoCraft (MIT OR Apache-2.0).\n# Context<TAB>English source<TAB>Thai translation. See docs/localization-th.md.\n'
path.write_text(header + ''.join('\t'.join((*key, target)) + '\n' for key, target in sorted(rows.items())))
print(f'Wrote {len(rows)} entries to {path}')
