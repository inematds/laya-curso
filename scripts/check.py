"""Validate generated navigation, manifest and stable learning ids (stdlib only)."""
import json
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.ids=[];self.links=[];self.topics=[];self.manifest='';self.reading=False;self.svgs=0;self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if 'data-inema-topic' in a:self.topics.append(a['data-inema-topic'])
  if tag=='svg' and a.get('role')=='img':self.svgs+=1
  for name in ['href','src']:
   if a.get(name):self.links.append(a[name])
  if tag=='script' and 'data-inema-manifest' in a:self.reading=True
 def handle_data(self,data):
  if self.reading:self.manifest+=data
 def handle_endtag(self,tag):
  if tag=='script':self.reading=False
pages={p:Page(p.read_text()) for p in ROOT.rglob('*.html') if 'assets' not in p.parts}
errors=[];expected=None;total=0
for path,page in pages.items():
 if len(page.ids)!=len(set(page.ids)):errors.append(f'duplicate ids: {path}')
 try:
  manifest=json.loads(page.manifest)
  if expected is None:expected=manifest
  assert manifest==expected
 except Exception:errors.append(f'invalid manifest: {path}')
 for link in page.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  dest=(path.parent/unquote(u.path)).resolve() if u.path else path
  if dest.is_dir():dest=dest/'index.html'
  if not dest.exists():errors.append(f'missing {path.relative_to(ROOT)} -> {link}')
  if u.fragment and dest in pages and unquote(u.fragment) not in pages[dest].ids:errors.append(f'missing anchor {link}')
 if path.name.startswith('modulo-'):
  assert len(page.topics)==6 and page.svgs>=1,path
  assert len(path.read_text().splitlines())>=500,path
  total+=len(page.topics)
 for track in expected['tracks']:
  for mod in track['modules']:
   target=ROOT/mod['href']
   assert len(pages[target].topics)==mod['topics']
assert total==48,total
assert not errors,'\n'.join(errors)
print(f'OK: {len(pages)} páginas, 8 módulos, {total} tópicos, links/âncoras/manifestos válidos.')
