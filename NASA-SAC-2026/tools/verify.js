const { chromium } = require('playwright');
const OUT = '/tmp/claude-0/-home-user/d76167c4-7d3d-5872-a48b-bfac51b722e2/scratchpad/shots/';

// Play the REAL page with the "fix the lowest bar, else push the goal" rule.
async function play(p, missionIdx, shot) {
  await p.goto('file:///home/user/nasa-sac-2026/index.html');
  await p.waitForTimeout(700);
  await p.click('text=START');
  await p.waitForTimeout(150);
  await p.click('text=SOLO');
  await p.click('#pgo');
  await p.waitForTimeout(250);
  const btns = await p.$$('#voteui button');
  await btns[missionIdx].click();
  await p.click('#vgo');
  await p.waitForTimeout(250);
  await p.click('text=BEGIN MISSION');
  await p.waitForTimeout(300);

  for (let t = 0; t < 40; t++) {
    if (await p.$('#s-end.on')) break;
    const S = await p.evaluate(() => ({ pwr: S.pwr, life: S.life, shd: S.shd, prog: S.prog }));
    let i = 0;                                  // 0 harvest/drive 1 shield 2 solar 3 life 4 hold
    if (S.life < 30) i = 3;
    else if (S.pwr < 28) i = 2;
    else if (S.shd < 28) i = 1;
    const acts = await p.$$('#actions button');
    if (!acts.length) break;
    await acts[i].click();
    await p.waitForTimeout(60);
    const go = await p.$('#actGo');
    if (await go.isDisabled()) break;
    await go.click();
    await p.waitForTimeout(110);
  }
  const ended = !!(await p.$('#s-end.on'));
  let outcome = 'no ending';
  if (ended) outcome = (await p.textContent('#endbody h1')).trim();
  if (shot) await p.screenshot({ path: OUT + shot, fullPage: true });
  return outcome;
}

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 900, height: 1100 }, deviceScaleFactor: 2 });
  const errs = [];
  p.on('pageerror', e => errs.push(e.message));

  let wins = 0, n = 12;
  for (let i = 0; i < n; i++) {
    const r = await play(p, i % 2, i === 0 ? 'win-moon.png' : null);
    if (r.includes('SUCCESS')) wins++;
    if (i < 4) console.log(`run ${i} (${i % 2 ? 'mars' : 'moon'}):`, r);
  }
  console.log(`\nsmart-play win rate in the REAL game: ${wins}/${n}`);
  console.log('ERRORS:', errs.length ? errs : 'none');
  await b.close();
})();
