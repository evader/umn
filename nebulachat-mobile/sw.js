self.addEventListener('install', function(e) {
  console.log('NebulaChat Service Worker Installed');
});
self.addEventListener('fetch', function(e) {
  console.log('Fetching:', e.request.url);
});