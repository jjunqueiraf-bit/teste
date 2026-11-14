// Mirrors the live model in index.html exactly, so tuning here transfers.
const fs = require('fs');
const html = fs.readFileSync('/home/user/teste/NASA-SAC-2026/index.html', 'utf8');
const deck = JSON.parse(html.match(/const EVENTS_FALLBACK = (\[.*?\]);/s)[1]);

const LENGTHS = { quick: 12, std: 24, long: 36 };

const ACTIONS = [
  { id: 'prog',  e: { prog: +18, pwr: -14, life: -6 } },
  { id: 'shd',   e: { shd: +20, pwr: -8, life: -4 } },
  { id: 'pwr',   e: { pwr: +26, shd: -10, life: -3 } },
  { id: 'life',  e: { life: +22, pwr: -9 } },
  { id: 'hold',  e: { life: -4, pwr: -3 } },
];
// ops pool, matching the live effects (every one costs something)
const OPS = [
  { e: { pwr: -7 } }, { e: { pwr: -12 } }, { e: { pwr: -5, life: -3 } },
  { e: { prog: +10, pwr: -6 } }, { e: { life: +16, pwr: -6 } },
];

function geomMult(a) { a = a || 20; return a >= 30 ? 1.0 : a >= 20 ? 0.72 : 0.42; }

function run(sols, d, seed) {
  let S = { pwr: d.pwr, life: d.life, shd: d.shd, prog: 0 };
  const pk = Math.pow(24 / sols, 0.6);
  let r = seed;
  const nx = () => ((r = (r * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff);
  const scale = e => { const o = { ...e }; if (o.prog > 0) o.prog = Math.round(o.prog * pk); return o; };

  for (let sol = 1; sol <= sols; sol++) {
    // same policy a thoughtful kid converges on
    let a = S.life < 30 ? ACTIONS[3] : S.pwr < 28 ? ACTIONS[2] : S.shd < 28 ? ACTIONS[1] : ACTIONS[0];
    const ae = scale(a.e);
    for (const k in ae) S[k] += ae[k];

    if (sol > 1 && nx() < 0.34) {
      const o = scale(OPS[(nx() * OPS.length) | 0].e);
      for (const k in o) S[k] += o[k];
    } else {
      const ev = deck[(sol - 1) % deck.length];
      const sev = ev.severity || 1;
      const raw = Math.round(sev * 6 * geomMult(ev.halfAngle) * d.rad);
      const blocked = Math.round(raw * (S.shd / 100));
      S.life -= Math.max(0, raw - blocked);
      S.shd -= sev * 2;
    }
    S.life -= (d.drain || 0);
    for (const k of ['pwr', 'life', 'shd']) S[k] = Math.max(0, Math.min(100, S[k]));
    S.prog = Math.max(0, Math.min(100, S.prog));
    if (S.prog >= 100) return 1;
    if (S.life <= 0 || S.pwr <= 0) return 0;
  }
  return 0;
}

const rate = (sols, d, n = 400) => {
  let w = 0;
  for (let i = 0; i < n; i++) w += run(sols, d, i * 7919 + 13);
  return w / n;
};

// deck lacks halfAngle? check
console.log('deck halfAngle present:', deck.filter(e => e.halfAngle != null).length, '/', deck.length);

// targets: cadet .88-1.0, astro .60-.78, cmdr .28-.50, at every length
function score(set) {
  let pen = 0;
  const T = { cadet: [0.88, 1.0], astro: [0.60, 0.78], cmdr: [0.28, 0.50] };
  for (const [name, d] of Object.entries(set)) {
    for (const sols of Object.values(LENGTHS)) {
      const r = rate(sols, d, 250);
      const [lo, hi] = T[name];
      if (r < lo) pen += (lo - r) * 2;
      if (r > hi) pen += (r - hi);
    }
  }
  return pen;
}

let best = null;
for (const cr of [0.45, 0.55, 0.65])
for (const ar of [0.95, 1.05, 1.15])
for (const mr of [1.25, 1.4, 1.55])
for (const mlife of [62, 66, 70])
for (const mshd of [36, 42, 48])
for (const mdrain of [0, 1]) {
  const set = {
    cadet: { pwr: 82, life: 86, shd: 62, rad: cr, drain: 0 },
    astro: { pwr: 70, life: 74, shd: 48, rad: ar, drain: 1 },
    cmdr:  { pwr: 58, life: mlife, shd: mshd, rad: mr, drain: mdrain },
  };
  const s = score(set);
  if (!best || s < best.s) best = { s, set, cr, ar, mr, mlife, mshd, mdrain };
}

console.log('\nbest penalty', best.s.toFixed(3));
console.log(JSON.stringify(best.set, null, 1));
console.log('\n          quick   std   long');
for (const [name, d] of Object.entries(best.set)) {
  const r = Object.values(LENGTHS).map(s => (rate(s, d, 1500) * 100).toFixed(0).padStart(4) + '%');
  console.log('  ' + name.padEnd(7), r.join('  '));
}
