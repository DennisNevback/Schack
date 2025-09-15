//* Include the scripts
/*
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
  brython(0);
  console.clear();
});
*/

// Include the scripts dynamically
let myPath = [...document.querySelectorAll('script')]
  .map(({ src }) => src)
  .filter(x => x.includes('/start.js'))[0]
  .slice(0, -8);

let libs = [
  'jquery.js',
  'bootstrap.bundle.min.js',
  'brython.js',
  'brython_stdlib.js'
];

function loadScript(src, callback) {
  let script = document.createElement('script');
  script.src = src;
  script.onload = callback;
  document.head.appendChild(script);
}

(function loadLibs(i = 0) {
  if (i >= libs.length) {
    if (typeof brython !== 'undefined') brython(0);
    return;
  }
  loadScript(myPath + libs[i], () => loadLibs(i + 1));
})();
