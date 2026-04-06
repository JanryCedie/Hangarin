const CACHE_NAME = 'hangarin-cache-v2';
const assetsToCache = [
    '/',
    '/login/',
    '/static/css/bootstrap.min.css',
    '/static/css/ready.css',
    '/static/css/custom.css',
    '/static/js/core/jquery.3.2.1.min.js',
    '/static/js/core/popper.min.js',
    '/static/js/core/bootstrap.min.js',
    '/static/js/ready.min.js',
    '/static/img/icon-192.png',
    '/static/img/icon-512.png'
];

// Install Event - Pre-caching core assets
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(assetsToCache);
        })
    );
});

// Activate Event - Clean up old caches
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cache) => {
                    if (cache !== CACHE_NAME) {
                        return caches.delete(cache);
                    }
                })
            );
        })
    );
});

// Fetch Event - Better caching strategies
self.addEventListener('fetch', (event) => {
    const request = event.request;
    const url = new URL(request.url);

    // Strategy 1: Cache-First for static assets (images, CSS, JS)
    if (url.origin === location.origin && (url.pathname.startsWith('/static/') || url.pathname.startsWith('/images/'))) {
        event.respondWith(
            caches.match(request).then((cachedResponse) => {
                if (cachedResponse) return cachedResponse;
                return fetch(request).then((networkResponse) => {
                    return caches.open(CACHE_NAME).then((cache) => {
                        cache.put(request, networkResponse.clone());
                        return networkResponse;
                    });
                });
            })
        );
        return;
    }

    // Strategy 2: Network-First for HTML pages (so user sees updates when online)
    event.respondWith(
        fetch(request).catch(() => {
            return caches.match(request);
        })
    );
});
