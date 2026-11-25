const { chromium, devices } = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const u of ['https://iaclatam.com/','https://iaclatam.com/productos/bentley-openroads/','https://iaclatam.com/que-es-bim/','https://iaclatam.com/mx/inicio/']) {
    const ctx = await b.newContext({...devices['Pixel 7']});
    const p = await ctx.newPage(); let bytes=0, reqs=0, imgBytes=0, js=0;
    p.on('response', async r => { reqs++; try{ const l=+(r.headers()['content-length']||0); bytes+=l; const t=r.request().resourceType(); if(t==='image') imgBytes+=l; if(t==='script') js++; }catch(e){} });
    await p.addInitScript(() => { window.__lcp=0; window.__cls=0;
      new PerformanceObserver(l=>{for(const e of l.getEntries()) window.__lcp=e.startTime}).observe({type:'largest-contentful-paint',buffered:true});
      new PerformanceObserver(l=>{for(const e of l.getEntries()) if(!e.hadRecentInput) window.__cls+=e.value}).observe({type:'layout-shift',buffered:true}); });
    const t0=Date.now();
    try { await p.goto(u,{waitUntil:'load',timeout:60000}); } catch(e){ console.log(u,'ERR',e.message.slice(0,80)); continue; }
    await p.waitForTimeout(3000);
    const m = await p.evaluate(()=>{const n=performance.getEntriesByType('navigation')[0];
      return {ttfb:Math.round(n.responseStart), dcl:Math.round(n.domContentLoadedEventEnd), load:Math.round(n.loadEventEnd), lcp:Math.round(window.__lcp), cls:+window.__cls.toFixed(3),
      ld:document.querySelectorAll('script[type="application/ld+json"]').length, hscroll: document.documentElement.scrollWidth>window.innerWidth, viewport: !!document.querySelector('meta[name=viewport]')}});
    console.log(u, JSON.stringify({...m, reqs, js, kb:Math.round(bytes/1024), imgKb:Math.round(imgBytes/1024)}));
    await ctx.close();
  }
  await b.close();
})();
