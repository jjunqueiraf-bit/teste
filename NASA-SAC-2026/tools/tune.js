// Grid-search a tuning where thinking wins and spamming loses.
const SEV_POOL = [].concat(Array(94).fill(1), Array(27).fill(2), Array(11).fill(3));

function mkActions(t) {
  return [
    { id: 'harvest', e: { prog: +t.pg, pwr: -t.hc, life: -6 } },
    { id: 'shield',  e: { shd: +20, pwr: -8, life: -4 } },
    { id: 'solar',   e: { pwr: +t.sg, shd: -10, life: -3 } },
    { id: 'life',    e: { life: +22, pwr: -9 } },
    { id: 'hold',    e: { life: -4, pwr: -3 } },
  ];
}

function run(policy, seed, t, A) {
  let S = { pwr: t.pwr0, life: t.life0, shd: t.shd0, prog: 0 };
  let rnd = seed;
  const nx = () => ((rnd = (rnd * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff);
  for (let sol = 1; sol <= t.maxSol; sol++) {
    const sev = SEV_POOL[(nx() * SEV_POOL.length) | 0];
    const a = policy(S, A);
    for (const k in a.e) S[k] += a.e[k];
    const raw = sev * t.sevMul;
    const blocked = Math.round(raw * (S.shd / 100));
    const hit = Math.max(0, raw - blocked);
    S.life -= hit;
    S.shd -= sev * t.shdDrain;
    for (const k of ['pwr', 'life', 'shd']) S[k] = Math.max(0, Math.min(100, S[k]));
    S.prog = Math.max(0, Math.min(100, S.prog));
    if (S.prog >= 100) return 'win';
    if (S.life <= 0) return 'life';
    if (S.pwr <= 0) return 'power';
  }
  return 'timeout';
}

const smart  = (S, A) => S.life < 30 ? A[3] : S.pwr < 28 ? A[2] : S.shd < 28 ? A[1] : A[0];
const greedy = (S, A) => A[0];
const random = (S, A) => A[(Math.random() * A.length) | 0];

function rate(policy, t, A, n = 500) {
  let w = 0;
  for (let i = 0; i < n; i++) if (run(policy, i * 7919 + 13, t, A) === 'win') w++;
  return w / n * 100;
}

const results = [];
for (const pg of [18, 20, 22, 25])
for (const hc of [10, 12, 14])
for (const sg of [26, 30, 34])
for (const maxSol of [20, 24])
for (const sevMul of [4, 5, 6])
for (const shd0 of [50, 60]) {
  const t = { pg, hc, sg, maxSol, sevMul, shdDrain: 2, pwr0: 70, life0: 75, shd0 };
  const A = mkActions(t);
  const s = rate(smart, t, A), g = rate(greedy, t, A), r = rate(random, t, A);
  // want: smart high, greedy clearly lower, random lower still
  if (s >= 55 && s <= 80 && g <= s - 30 && r <= s - 25) {
    results.push({ t, s: +s.toFixed(1), g: +g.toFixed(1), r: +r.toFixed(1),
                   score: s - Math.abs(68 - s) * 2 - g - r });
  }
}
results.sort((a, b) => b.score - a.score);
console.log('viable tunings found:', results.length);
console.log('\n=== TOP 6 ===');
results.slice(0, 6).forEach(x => {
  const t = x.t;
  console.log(
    `prog+${t.pg} harvCost${t.hc} solar+${t.sg} sols${t.maxSol} rad x${t.sevMul} shd0 ${t.shd0}` +
    `  ->  smart ${x.s}%  greedy ${x.g}%  random ${x.r}%`);
});
