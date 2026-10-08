// AltaCoco Scan Station — offline shell. Network first, cache as fallback, only for /trade/.
const CACHE = 'scan-station-v2';
const SHELL = ['/trade/', '/trade/manifest.webmanifest', '/trade/icon-192.png', '/trade/apple-touch-icon.png',
  '/trade/firebase-config.js', '/trade/firebase-bundle.js'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys()
    .then(keys => Promise.all(keys.filter(k => k.startsWith('scan-station-') && k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  if (e.request.method !== 'GET' || url.origin !== location.origin || !url.pathname.startsWith('/trade')) return;
  e.respondWith(
    fetch(e.request).then(res => {
      if (res.ok) { const copy = res.clone(); caches.open(CACHE).then(c => c.put(e.request, copy)); }
      return res;
    }).catch(() => caches.match(e.request, {ignoreSearch: true})
      .then(r => r || (e.request.mode === 'navigate' ? caches.match('/trade/') : undefined)))
  );
});
