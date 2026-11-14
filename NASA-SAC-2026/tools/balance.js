// Balance simulator: is the game winnable, and how hard?
const ACTIONS = [
  { id: 'harvest', e: { prog: +14, pwr: -16, life: -6 } },
  { id: 'shield',  e: { shd: +20, pwr: -10, life: -4 } },
  { id: 'solar',   e: { pwr: +24, shd: -10, life: -3 } },
  { id: 'life',    e: { life: +22, pwr: -11 } },
  { id: 'hold',    e: { life: -4, pwr: -3 } },
];

const SEV_POOL = [].concat(Array(94).fill(1), Array(27).fill(2), Array(11).fill(3));

function run(policy, seed, cfg) {
  let S = { pwr: cfg.pwr0, life: cfg.life0, shd: cfg.shd0, prog: 0 };
  let rnd = seed;
  const nx = () => ((rnd = (rnd * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff);
  for (let sol = 1; sol <= cfg.maxSol; sol++) {
    const sev = SEV_POOL[(nx() * SEV_POOL.length) | 0];
    const a = policy(S, sol, sev);
    for (const k in a.e) S[k] += a.e[k];
    const raw = sev * cfg.sevMul;
    const blocked = Math.round(raw * (S.shd / 100));
    const hit = Math.max(0, raw - blocked);
    S.life -= hit;
    S.shd -= sev * cfg.shdDrain;
    for (const k of ['pwr', 'life', 'shd']) S[k] = Math.max(0, Math.min(100, S[k]));
    S.prog = Math.max(0, Math.min(100, S.prog));
    if (S.prog >= 100) return { win: true, sol };
    if (S.life <= 0) return { win: false, why: 'life', sol };
    if (S.pwr <= 0) return { win: false, why: 'power', sol };
  }
  return { win: false, why: 'timeout', prog: S.prog };
}

// a sensible kid strategy: fix whatever is lowest, otherwise push the goal
const smart = (S) => {
  if (S.life < 30) return ACTIONS[3];
  if (S.pwr < 25) return ACTIONS[2];
  if (S.shd < 25) return ACTIONS[1];
  if (S.pwr < 20) return ACTIONS[2];
  return ACTIONS[0];
};
const greedy = () => ACTIONS[0];
const random = () => ACTIONS[(Math.random() * ACTIONS.length) | 0];

function rate(policy, cfg, n = 400) {
  let w = 0, why = {};
  for (let i = 0; i < n; i++) {
    const r = run(policy, i * 7919 + 13, cfg);
    if (r.win) w++; else why[r.why] = (why[r.why] || 0) + 1;
  }
  return { winRate: (w / n * 100).toFixed(1) + '%', fails: why };
}

const current = { pwr0: 62, life0: 70, shd0: 46, maxSol: 20, sevMul: 7, shdDrain: 2 };
console.log('=== CURRENT TUNING ===');
console.log('smart :', JSON.stringify(rate(smart, current)));
console.log('greedy:', JSON.stringify(rate(greedy, current)));
console.log('random:', JSON.stringify(rate(random, current)));

console.log('\n=== CANDIDATE TUNINGS (target: smart ~60-75%, greedy low, random low-ish) ===');
const cands = [
  { name: 'A longer+softer', pwr0: 70, life0: 75, shd0: 50, maxSol: 24, sevMul: 6, shdDrain: 2 },
  { name: 'B softer rad   ', pwr0: 70, life0: 78, shd0: 55, maxSol: 24, sevMul: 5, shdDrain: 2 },
  { name: 'C generous     ', pwr0: 75, life0: 80, shd0: 55, maxSol: 26, sevMul: 5, shdDrain: 1 },
  { name: 'D mid          ', pwr0: 72, life0: 78, shd0: 52, maxSol: 25, sevMul: 5, shdDrain: 2 },
];
for (const c of cands) {
  console.log(c.name, '| smart', rate(smart, c).winRate,
    '| greedy', rate(greedy, c).winRate,
    '| random', rate(random, c).winRate,
    '| smart fails', JSON.stringify(rate(smart, c).fails));
}
