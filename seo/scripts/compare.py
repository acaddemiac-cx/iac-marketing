"""Compara un rastreo nuevo con el anterior, tarea por tarea del plan SEO.

Uso: python3 compare.py crawl_anterior.json crawl_nuevo.json sitemap_actual.txt
(los JSON salen de crawl.py; sitemap_actual.txt = una URL por línea)
"""
import json, re, sys, collections as C

old = {r["url"]: r for r in json.load(open(sys.argv[1]))}
new = {r["url"]: r for r in json.load(open(sys.argv[2]))}
sitemap = {l.strip() for l in open(sys.argv[3]) if l.strip()}
B = "https://iaclatam.com"
s = lambda u: u.replace(B, "")
ok = [r for r in new.values() if r.get("status") == 200]
idx = [r for r in ok if "noindex" not in (r.get("robots") or "")]
def sec(u):
    p = s(u)
    return "mx" if p.startswith("/mx/") else "ec" if p.startswith("/ec/") else "co"
def st(u):
    r = new.get(B + u)
    return r and (r.get("status"), r.get("location"), r.get("robots"))
out = C.OrderedDict()
def say(k, v): out[k] = v; print(f"{k}: {v}")

say("URLs en sitemap", len(sitemap))
say("estado de URLs", dict(C.Counter(r.get("status") for r in new.values())))
say("T02 tags indexables", sum(1 for r in idx if "/tag/" in r["url"]))
for u in ["/gracias-solidworks/", "/ig/", "/taller-ia-2/"]: say("T03 " + u, st(u))
for u in ["/mx/", "/ec/", "/servicios/", "/productos/", "/mx/servicios/", "/mx/productos/", "/ec/servicios/", "/ec/productos/"]:
    say("T05 en sitemap " + u, B + u in sitemap)
say("T08 nofollow", [s(r["url"]) for r in ok if "nofollow" in (r.get("robots") or "")])
# hreflang
hl = [r for r in idx if r.get("hreflang")]
say("T09 páginas indexables con hreflang", f"{len(hl)} de {len(idx)}")
codes = C.Counter(c for r in hl for c, _ in r["hreflang"])
say("T09 códigos usados", dict(codes))
noself, nonrecip, badtarget = [], [], []
for r in hl:
    m = {c: h for c, h in r["hreflang"]}
    if r["url"] not in m.values() and (r.get("canonical") or "") not in m.values(): noself.append(s(r["url"]))
    for c, h in m.items():
        t = new.get(h)
        if t is None: continue
        if t.get("status") != 200: badtarget.append((s(r["url"]), c, s(h), t.get("status")))
        elif h != r["url"] and r["url"] not in {x for _, x in t.get("hreflang", [])}: nonrecip.append((s(r["url"]), c, s(h)))
say("T09 sin autorreferencia", noself[:15]); say("T09 sin retorno", nonrecip[:15]); say("T09 destino no 200", badtarget[:15])
say("T10 lang por sección", dict(C.Counter((sec(r["url"]), r.get("lang")) for r in ok if "/tag/" not in r["url"])))
say("T12 'Asisitida'", [s(r["url"]) for r in ok if "Asisitida" in r.get("title", "")])
say("T12 mx microsoft-365", (new.get(B + "/mx/productos/microsoft-365/") or {}).get("title"))
tc = C.defaultdict(list)
for r in idx: tc[r["title"]].append(s(r["url"]))
dups = {t: v for t, v in tc.items() if len(v) > 1}
say("T13 títulos duplicados (grupos/páginas)", (len(dups), sum(len(v) for v in dups.values())))
for t, v in list(dups.items())[:20]: print("    ", repr(t), v)
say("T14 títulos <30", [(s(r["url"]), r["title"]) for r in idx if len(r["title"]) < 30])
say("T15 títulos >65", len([r for r in idx if len(r["title"]) > 65]))
say("T16 sin descripción", [s(r["url"]) for r in idx if not r.get("desc")])
dc = C.defaultdict(list)
for r in idx:
    if r.get("desc"): dc[r["desc"]].append(s(r["url"]))
dd = {t: v for t, v in dc.items() if len(v) > 1}
say("T17 descripciones duplicadas (grupos/páginas)", (len(dd), sum(len(v) for v in dd.values())))
for t, v in list(dd.items())[:12]: print("    ", v)
say("T17 descripciones >160", [s(r["url"]) for r in idx if r.get("desc") and len(r["desc"]) > 160])
say("T18 sin H1", [s(r["url"]) for r in idx if not r.get("h1")])
say("T18 varios H1", [(s(r["url"]), r["h1"]) for r in idx if len(r.get("h1") or []) > 1])
ev = ["/live-conversatorio/", "/live-solidworks/", "/live-bim/", "/live-staad-pro/", "/live-projectwise-bundle/", "/live-ia/", "/live-synchro-y-primavera/", "/cata-de-vinos-solidworks-2026/", "/innovation-day-bentley/", "/taller-ia/", "/congreso-inteligencia-artificial/", "/concurso-academico-bim-2026/"]
say("T19 eventos", {u: (st(u), (new.get(B + u) or {}).get("words")) for u in ev})
cats = [p + c for p in ["/", "/mx/", "/ec/"] for c in ["productos/infraestructura-aguas/", "productos/manufactura/", "productos/inteligencia-artificial/"]]
say("T20 palabras categorías", {u: ((new.get(B + u) or {}).get("words"), (old.get(B + u) or {}).get("words")) for u in cats})
say("T21 hubs", {u: st(u) for u in ["/servicios/", "/productos/", "/mx/servicios/", "/mx/productos/", "/ec/servicios/", "/ec/productos/"]})
oldposts = [u for u in old if re.search(r"\.com/[^/]+/$", u) and u in old and old[u].get("schema") and "Article" in old[u]["schema"]]
moved = C.Counter()
for u in oldposts:
    r = new.get(u) or {}
    moved["301" if r.get("status") == 301 else "404/410" if r.get("status") in (404, 410) else "noindex" if "noindex" in (r.get("robots") or "") else "igual"] += 1
say("T22 artículos (todos) estado", dict(moved))
for u in ["/implemetancion-de-agentes-de-ia-para-el-2026/", "/entro-automatizacion-ecosistema-bots-iac/", "/hardware-para-ejecturar-synchro-4d/"]: say("T23 " + u, st(u))
say("T24 imágenes sin alt (en páginas indexables)", (sum(r["noalt"] for r in idx), sum(r["imgs"] for r in idx)))
# enlaces internos
targets = C.defaultdict(set)
for r in ok:
    for l in r.get("links", []):
        l = l.split("#")[0]
        if l.startswith("/"): l = B + l
        if l.startswith(B) and "wp-content" not in l and "cdn-cgi" not in l and "?" not in l: targets[l].add(s(r["url"]))
unknown = sorted(l for l in targets if l not in new and l.rstrip("/") + "/" not in new)
bad = [(s(l), new[l]["status"], sorted(targets[l])[:3]) for l in targets if l in new and new[l].get("status") in (404, 410)]
red = [(s(l), s(new[l].get("location") or ""), sorted(targets[l])[:3]) for l in targets if l in new and new[l].get("status") == 301 and not re.search(r"/\d{4}/\d\d/\d\d/$", l)]
say("T04 enlaces internos a 404", bad)
say("T04 enlaces internos a redirecciones", red[:25])
json.dump(unknown, open(sys.argv[2] + ".unknown.json", "w"))
say("enlaces internos sin revisar (rastrear aparte)", len(unknown))
