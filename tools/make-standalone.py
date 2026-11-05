"""Build the GitHub Pages copy (index.html) from the Claude artifact source (splitter/index.html).

The artifact source is written without <html>/<head>, because Claude's viewer adds them.
This wraps it into a normal standalone page. Run from the repo root:

    python tools/make-standalone.py
"""
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
src = (root / 'splitter' / 'index.html').read_text(encoding='utf-8')
cut = src.index('<style>')
head_bits, body = src[:cut].strip(), src[cut:]
# this marker only means something inside Claude's viewer
head_bits = head_bits.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
reset = (':root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
         'body{margin:0;font:14px system-ui,-apple-system,"Segoe UI",sans-serif}img{max-width:100%}[hidden]{display:none!important}')
out = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
       '<meta name="description" content="Split flat 3D-printed wall art into bed-sized pieces with puzzle joints.">\n'
       + head_bits + '\n<style>' + reset + '</style>\n</head>\n<body>\n' + body.rstrip() + '\n</body>\n</html>\n')
(root / 'index.html').write_text(out, encoding='utf-8', newline='\n')
print('wrote index.html', len(out), 'bytes')
