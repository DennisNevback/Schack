// Include the scripts
let myPath = [...document.querySelectorAll('script')]
  .map(({ src }) => src)
  .filter(x => x.includes('/start.js'))[0]
  .slice(0, -8)
let _scripts = [
  'jquery.js',
  'bootstrap.bundle.min.js',
  'brython.js',
  'brython_stdlib.js'
].map(x => `<script src="${myPath}${x}"></script>`).join('\n');
document.write(_scripts);
setTimeout(function start() {
  if (!('brython' in window)) { setTimeout(start, 10); return; }
  brython(1);
  console.clear();
});