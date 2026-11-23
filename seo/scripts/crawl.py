"""Rastrea una lista de URLs y guarda datos SEO en JSON.
Uso: python3 crawl.py urls.txt salida.json"""
import os, sys, json, re, ssl, urllib.request, concurrent.futures as cf
from html.parser import HTMLParser
CA = "/root/.ccr/ca-bundle.crt"
ctx = ssl.create_default_context(cafile=CA if os.path.exists(CA) else None)
class NoRedir(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k): return None
opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx), NoRedir)
UA = "Mozilla/5.0 (compatible; SEO-audit-script)"
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.d={"title":"","desc":None,"canonical":None,"robots":None,"h1":[],"h2":0,"hreflang":[],"lang":None,"imgs":0,"noalt":0,"jsonld":[],"text":[],"links":[],"og":0}
        s.stack=None; s.skip=0; s.buf=""
    def handle_starttag(s,t,a):
        a=dict(a)
        if t=="html": s.d["lang"]=a.get("lang")
        if t in("script","style","noscript"):
            s.skip+=1
            if t=="script" and a.get("type")=="application/ld+json": s.stack="ld"; s.buf=""
        if t=="title": s.stack="title"; s.buf=""
        if t=="h1": s.stack="h1"; s.buf=""
        if t=="h2": s.d["h2"]+=1
        if t=="meta":
            n=(a.get("name") or "").lower(); p=(a.get("property") or "").lower()
            if n=="description": s.d["desc"]=a.get("content","")
            if n=="robots": s.d["robots"]=a.get("content","")
            if p.startswith("og:"): s.d["og"]+=1
        if t=="link":
            r=(a.get("rel") or "").lower()
            if r=="canonical": s.d["canonical"]=a.get("href")
            if r=="alternate" and a.get("hreflang"): s.d["hreflang"].append((a["hreflang"],a.get("href")))
        if t=="img":
            s.d["imgs"]+=1
            if not (a.get("alt") or "").strip(): s.d["noalt"]+=1
        if t=="a" and a.get("href"): s.d["links"].append(a["href"])
    def handle_endtag(s,t):
        if t in("script","style","noscript"):
            s.skip=max(0,s.skip-1)
            if s.stack=="ld": s.d["jsonld"].append(s.buf); s.stack=None
        if t=="title" and s.stack=="title": s.d["title"]=s.buf.strip(); s.stack=None
        if t=="h1" and s.stack=="h1": s.d["h1"].append(re.sub(r"\s+"," ",s.buf).strip()); s.stack=None
    def handle_data(s,x):
        if s.stack: s.buf+=x
        if not s.skip: s.d["text"].append(x)
def fetch(u):
    r={"url":u}
    try:
        req=urllib.request.Request(u,headers={"User-Agent":UA})
        try: resp=opener.open(req,timeout=40); code=resp.status; body=resp.read().decode("utf-8","replace")
        except urllib.error.HTTPError as e: code=e.code; r["location"]=e.headers.get("Location"); body=""
        r["status"]=code
        if body:
            p=P(); p.feed(body); d=p.d
            words=len(re.findall(r"\w+"," ".join(d["text"])))
            types=[]
            for j in d["jsonld"]:
                types+=re.findall(r'"@type":\s*"([^"]+)"',j)
            r.update(title=d["title"],desc=d["desc"],canonical=d["canonical"],robots=d["robots"],h1=d["h1"],h2=d["h2"],hreflang=d["hreflang"],lang=d["lang"],imgs=d["imgs"],noalt=d["noalt"],schema=sorted(set(types)),words=words,og=d["og"],links=[l for l in d["links"] if "iaclatam.com" in l or l.startswith("/")],bytes=len(body))
    except Exception as e: r["error"]=str(e)[:200]
    return r
urls=[l.strip() for l in open(sys.argv[1]) if l.strip()]
with cf.ThreadPoolExecutor(4) as ex: res=list(ex.map(fetch,urls))
json.dump(res,open(sys.argv[2],"w"),ensure_ascii=False)
print(len(res),"done")
