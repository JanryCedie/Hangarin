// Hangarin PWA Service Worker v2
const CACHE_NAME = 'hangarin-cache-v2';
const urlsToCache = [
  '/',
  '/static/img/icon-192.png',
  '/static/img/icon-512.png',
  '/static/todo/css/todo.css', // Update based on your actual CSS path
  'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css',
  'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css'
];

// Install Event
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

// Activate Event
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.filter(cacheName => cacheName !== CACHE_NAME)
          .map(cacheName => caches.delete(cacheName))
      );
    })
  );
});

// Fetch Event (Offline Logic)
self.addEventListener('fetch', event => {
  // Strategy: Network First, falling back to Cache
  event.respondWith(
    fetch(event.request)
      .then(response => {
        // If the request was successful, clone it and put it in the cache
        if (response && response.status === 200 && response.type === 'basic') {
          const responseToCache = response.clone();
          caches.open(CACHE_NAME)
            .then(cache => {
              cache.put(event.request, responseToCache);
            });
        }
        return response;
      })
      .catch(() => {
        // If the network request fails, look for a match in the cache
        return caches.match(event.request);
      })
  );
});
