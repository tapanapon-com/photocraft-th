#!/usr/bin/env python3
"""Exercise a running isolated Thai build using its authenticated control API.
Start it with --control 7983, --control-token-file TOKEN, and an automation
write root for the generated demo files. Run: smoke.py TOKEN [port].
"""
import json
import socket
import sys
from pathlib import Path

connection = socket.create_connection(('127.0.0.1', int(sys.argv[2]) if len(sys.argv) > 2 else 7983), timeout=60)
stream = connection.makefile('rwb')
sequence = 0

def request(method, params=None):
    global sequence
    sequence += 1
    stream.write((json.dumps({'id': sequence, 'method': method, 'params': params or {}}) + '\n').encode())
    stream.flush()
    reply = json.loads(stream.readline())
    if not reply.get('ok'):
        raise RuntimeError(f'{method}: {reply}')
    return reply.get('result')

def command(command_id, **params):
    return request('engine.execute', {'command': command_id, 'params': params})

request('auth', {'token': Path(sys.argv[1]).read_text().strip()})
command('prefs.set', path='interface.language', value='th')
request('ui.resize', {'width': 1400, 'height': 900})
command('file.new', name='ทดลองภาษาไทย — PhotoCraft', width=960, height=540)
command('layer.new.layer', name='พื้นหลัง')
command('edit.fill', color='#142c40')
command('type.create', x=64, y=160, text='PhotoCraft', size=66, font='Inter', color='#ffffff', name='ชื่อโปรแกรม')
command('type.create', x=64, y=250, text='สร้างสรรค์ภาพในภาษาไทย', size=36, font='Noto Sans Thai', color='#56dac4', name='ข้อความภาษาไทย')
command('type.create', x=64, y=325, text='เลเยอร์ • มาสก์ • แปรง • สี', size=24, font='Noto Sans Thai', color='#d5e7ef', name='เครื่องมือแต่งภาพ')
request('ui.set', {'fit': True})
request('app.save', {'path': 'photocraft-th-demo.pcraft'})
request('ui.screenshot', {'path': 'photocraft-th-workspace.png'})
# Switch twice without changing the saved document, then reopen its native file.
command('prefs.set', path='interface.language', value='en')
command('prefs.set', path='interface.language', value='th')
command('file.close')
request('app.open', {'path': 'photocraft-th-demo.pcraft'})
request('app.save', {'path': 'photocraft-th-demo.png'})
print(json.dumps({'status': 'passed', 'menu': request('ui.menu.list')}, ensure_ascii=False))
