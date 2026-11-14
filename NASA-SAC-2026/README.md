# Junior Astronaut Mission Trainer

**NASA Space Apps Challenge 2026 · São Paulo · 14–15 Nov 2026**
Challenge: [Build a Junior Astronaut Mission Trainer](https://www.spaceappschallenge.org/2026/challenges/junior-astronaut-mission-trainer/)

A browser game for ages 7–12. You run a real outpost and discover that
**every choice costs something else** — including doing nothing.

## Play it
Open `index.html`. That's it. No install, no build, no account, no server.
Works offline from `file://` — all data is embedded.

## Two missions, both real
| | |
|---|---|
| **Moon — Harvest Helium-3** | NASA awarded Interlune a $6.9M contract in May 2026 to extract helium-3 from lunar soil. Payload "Prospect Moon", targeting 2028. |
| **Mars — Recover Sapphire Canyon** | Perseverance drilled a core in July 2024 that NASA announced as a *potential biosignature* in Sept 2025. It is still on Mars — Mars Sample Return was defunded 23 Jan 2026. |

1–4 players vote on the mission; majority flies. Then a briefing screen shows
what is already done, what the focus is today, what we honestly don't know,
and **who actually pays** for it.

## Astronaut crew
Six selectable characters: Theo, Davi, Henrique, Caio, Nathan, plus a nameless
astronaut any player can claim and name themselves (defaults to "Astronaut").

Each player picks one at the start; duplicates lock out. The crew rotates duty
one astronaut per sol — the on-duty astronaut appears in the HUD and is named in
every mission log entry, so each player gets their own turns in the record.

Portraits are embedded as base64, so the single file still works offline.

> **Note for submission:** the handbook (p.11) says to keep minors' recognizable
> names and faces out of submission materials. These are illustrations, not
> photos, but they do pair real first names with likenesses. Decide whether this
> build is the public submission or the local version the team plays.

## Real NASA data
- **132 real coronal mass ejections** from NASA's **DONKI** database,
  1 Oct – 14 Nov 2026. Each in-game storm shows its real event ID, real speed
  (218–1048 km/s) and links to the actual DONKI record.
- Severity tiers derived from the **real speed distribution**, not invented.
- Data is **archived and labelled as archived** in-game. Nothing is presented
  as live. (A browser game cannot hold an API key safely, and a rate-limited
  live call would break during judging.)

## Three resources, one rule
Power · Life Support · Shielding. Every action gives one and takes another.
Even "shelter and wait" costs oxygen — there is no free option, because there
isn't one in space either.

Radiation damage is computed from the real CME speed tier against your
shielding level. Fast storm + thin shield = the crew pays.

## Balance (verified, not guessed)
`tools/` contains the simulator used to tune the game:
- Sensible play ("fix the lowest bar, else push the goal") wins **~65%**
- Mindless resource-grabbing wins **0%**
- Random play wins **~2%**

Verified against the real page with Playwright: **8/12 wins** with sensible play.

## Pixel art

### Astronaut sprites (in use)
Four animated suits from Pixilart, **30×30, 8 frames, 100 ms per frame**:
cyan, green, gold, red — assigned to players 1–4 in join order.

Source GIFs were RGB on a white background with no alpha. Since the suit is
*also* white, a plain colour-key would have punched holes through the body.
Instead `tools/` flood-fills transparency inward from the border, so only
white reachable from outside the black outline is cleared. Strips live in
`art/astro_<colour>.png` (240×30) and are embedded as base64 — about 5 KB total.

The scene redraws on `requestAnimationFrame` while the game screen is visible:
off-duty crew idle at the left of the regolith, the on-duty astronaut walks
right as mission progress climbs.

### Adding more sprites
Keep **30×30** and integer scaling so pixels stay crisp. Export PNG with
transparency where possible; if the background is opaque white, reuse the
flood-fill in `tools/`. Register in `SUITIMG` or draw via `sprite()` in
`drawScene()`. Canvas is already `image-rendering: pixelated`.

## Submission checklist
- [x] Working browser prototype, no download, no account
- [x] Real NASA data, attributed in-tool, archived clearly labelled
- [x] 3 core resources, no free action
- [x] Replayability — 132-event shuffled deck, two missions
- [x] Mission context with real evidence and real funders
- [ ] 1-page data explainer (content is in `docs/MISSIONS.md`)
- [ ] Demo video
- [ ] Real Pixilart sprites

## Files
```
index.html              the whole game, standalone
docs/challenge-brief.md the NASA challenge
docs/MISSIONS.md        mission science + sources + honest caveats
docs/PROJECT-CONTEXT.md event facts, constraints, decisions
data/                   raw DONKI pull + built event deck
tools/                  balance simulator and Playwright verifier
```
