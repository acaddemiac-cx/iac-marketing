"""Resume el JSON de crawl.py. Uso: python3 analyze.py salida.json"""
import json,sys,collections as C
R=json.load(open(sys.argv[1]))
ok=[r for r in R if r.get("status")==200]
print("status:",C.Counter(r.get("status",r.get("error","?")[:40]) for r in R))
for r in R:
    if r.get("status")!=200: print("  NON200",r["url"],r.get("status"),r.get("location"),r.get("error",""))
def sec(u):
    p=u.replace("https://iaclatam.com/","")
    return "mx" if p.startswith("mx/") else "ec" if p.startswith("ec/") else "tag" if p.startswith("tag/") else "co"
print("\nlang attrs:",C.Counter((sec(r["url"]),r.get("lang")) for r in ok))
print("hreflang present:",sum(1 for r in ok if r["hreflang"]),"/",len(ok))
print("robots meta:",C.Counter(r.get("robots") for r in ok).most_common(6))
nonself=[r for r in ok if r.get("canonical") and r["canonical"].rstrip("/")!=r["url"].rstrip("/")]
print("canonical missing:",sum(1 for r in ok if not r.get("canonical")),"non-self:",len(nonself))
for r in nonself[:15]: print("   ",r["url"],"->",r["canonical"])
print("noindex:",[r["url"] for r in ok if r.get("robots") and "noindex" in r["robots"]][:20])
# titles
tc=C.Counter(r["title"] for r in ok)
dups=[(t,n) for t,n in tc.items() if n>1]
print("\ndup titles groups:",len(dups),"pages:",sum(n for t,n in dups))
for t,n in sorted(dups,key=lambda x:-x[1])[:15]: print("  ",n,"x",repr(t))
L=[len(r["title"]) for r in ok]
print("title len >65:",sum(1 for x in L if x>65),"<30:",sum(1 for x in L if x<30))
print("missing desc:",sum(1 for r in ok if not r.get("desc")))
dc=C.Counter(r["desc"] for r in ok if r.get("desc")); dd=[(t,n) for t,n in dc.items() if n>1]
print("dup desc groups:",len(dd),"pages:",sum(n for t,n in dd))
for t,n in sorted(dd,key=lambda x:-x[1])[:8]: print("  ",n,"x",repr(t[:110]))
print("desc >160:",sum(1 for r in ok if r.get("desc") and len(r["desc"])>160),"<70:",sum(1 for r in ok if r.get("desc") and len(r["desc"])<70))
print("\nH1 count:",C.Counter(len(r["h1"]) for r in ok))
print("no H1 by sec:",C.Counter(sec(r["url"]) for r in ok if not r["h1"]))
print("multi H1 examples:",[(r["url"],r["h1"][:3]) for r in ok if len(r["h1"])>1][:6])
hc=C.Counter(r["h1"][0] for r in ok if r["h1"]); print("dup H1:",[(h,n) for h,n in hc.items() if n>1][:12])
print("\nimgs total:",sum(r["imgs"] for r in ok),"noalt:",sum(r["noalt"] for r in ok))
print("schema types:",C.Counter(t for r in ok for t in r["schema"]).most_common(20))
print("words by sec (median):",{s:sorted(r["words"] for r in ok if sec(r["url"])==s)[len([1 for r in ok if sec(r["url"])==s])//2] for s in ["co","mx","ec","tag"]})
thin=[(r["words"],r["url"]) for r in ok if r["words"]<400 and sec(r["url"])!="tag"]
print("thin <400 words:",len(thin),sorted(thin)[:15])
print("og tags missing:",sum(1 for r in ok if r["og"]==0))
print("bytes median:",sorted(r["bytes"] for r in ok)[len(ok)//2])
