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
Six selectable characters, one per team member: **Theo, Davi, Henrique, Caio,
Nathan and Luca**. Luca's portrait carries the Brazil flag but no name tag.

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

## Mission setup
Before launch, pick:
- **Length** — Quick (12 sols, ~3-5 min demo) / Standard (24) / Expedition (36).
  Progress per action scales with length, so a short run is still a real mission.
- **Difficulty** — Cadet / Astronaut / Commander. Changes starting margins,
  a per-sol crew oxygen draw, and how hard radiation lands.

Verified winnable at every combination (smart play, 10 runs each):

|            | Cadet | Astronaut | Commander |
|------------|-------|-----------|-----------|
| Quick      | 100%  | 100%      | 70%       |
| Standard   | 100%  | 100%      | 30%       |
| Expedition | 100%  | 80%       | 60%       |

## Crew specialisms
Each astronaut is genuinely better at one job and genuinely worse at another,
so **who is on duty changes what today's best move is**:

| Astronaut | Role | Good at | Weak at |
|---|---|---|---|
| Theo | Engineer | Power systems (+40%) | Not a medic |
| Davi | Geologist | Finding good ground (+38%) | Stays out too long |
| Henrique | Flight surgeon | Keeping the crew alive (+45%) | Slows the mission |
| Caio | Radiation officer | Shielding (+45%) | Heavy on power |
| Nathan | Systems operator | Wastes nothing (costs -18%) | Never pushes |
| Luca | Rover pilot | Covering ground (+30%) | Light on shielding |

Action cards show the numbers *after* the on-duty astronaut's specialism, so
players can see the difference rather than being told about it.

Verified: every astronaut can win solo at every difficulty, and none dominates.

## Situational scenes
The surface reacts to what is happening that sol:
- **Solar storm** (severity 3 or a direct hit) — the sky pulses red, off-duty
  crew break off and huddle against the habitat
- **Dust storm** (Mars) — drifting butterscotch haze across the scene
- **Lunar night** (Moon) — everything darkens, solar output stops
- **Choosing an action** walks the on-duty astronaut to that job: the arrays
  for solar work, the habitat for shielding or life support, out along the
  mission line to push progress

## Events
Two kinds, and the game never confuses them:

**Real space weather** (badged `REAL EVENT · ARCHIVED`) — drawn from the 132
DONKI records. Each uses three real fields:
- **speed** (218-1048 km/s) sets radiation intensity
- **halfAngle** (10-46 deg) sets geometry: 64 glancing, 36 partial, 32 direct hits
- **NASA class** (S slow / C common / O occasional) is shown as NASA records it

**Outpost situations** (badged `OUTPOST SITUATION · NOT NASA DATA`) — five per
mission: lunar night, dust storms, comms blackout, a rich regolith seam, water
ice found. These are in-game scenarios, deliberately *not* dressed as NASA
records. Each carries a "Did you know?" line and, like every action, each one
costs something.

## The mission arc
The game follows NASA's own six-step process (see `docs/NASA-SOURCES.md`),
shaped as five questions a mission team has to answer:

1. **Define the mission** — why go at all (illustrated story panels)
2. **Define how to get there** — launch window, power, instruments, radio, rocket
3. **Define how to collect the evidence** — your instruments set your collection rate
4. **Define how to deliver it to Earth** — your radio sets your send rate
5. **Come home** — only what reached Earth counts

### Collected is not delivered
The flight phase tracks two separate numbers:
- **Collected** — science sitting in the spacecraft's memory (striped on the gauge)
- **Sent** — science that actually reached Earth (solid, and the only way to win)

A player who collects everything and never transmits **loses**, and the debrief
tells them why. Verified: that strategy ends with 231 units stranded and 0
delivered.

Your design choices decide the flight:
| Choice | Effect in flight |
|---|---|
| Instruments | Collection rate — drill + spectrometer collect 23/turn, camera + weather station 14 |
| Radio | Send rate — orbiter relay 34, big dish 25, small antenna 10 |
| Power source | Recharge — RTG 24 steady, solar 32 on a good day but 14 in dust or night |

The radio you chose before launch is often what decides the mission.

### Mission length
Short **4 phases**, Standard **6**, Extended **8** — a run takes a few minutes,
not twenty. Collection and send rates scale with length, so every setting is
winnable (verified 6/6 at all three) and the time goes into learning rather
than repetition.

## Two worlds that look like two worlds
The scenes are built separately, from the physical differences rather than a
palette swap:

**The Moon** has no atmosphere, so the sky stays black even in daylight, stars
are hard points, and shadows are pitch black. **Earth hangs in the sky** with a
visible night side. The Sun is small and fierce. Crater rims ring the horizon
and boulders throw sharp shadows across grey regolith. The habitat is a dome
with soil piled over it.

**Mars** has a thin dusty atmosphere that scatters light, so the sky is
**butterscotch, not black**, and daytime stars are washed out. The Sun is small
and pale because Mars is half again as far from it. Mesas recede into haze on
the horizon, rocks are strewn across rust-red ground, and the habitat is a
lander on legs with regolith banked against it.

Weather sits on top of that: lunar night darkens everything and kills the
panels; a Martian dust storm thickens the haze.

## Radio traffic
Every phase brings one message between the crew on the surface and Mission
Control on Earth, shuffled per run so replays differ. Each carries a real
difficulty of working off-world, with the explanation behind a disclosure:

- signal delay, and deciding alone because nobody is watching live
- lunar dust wrecking visors and seals
- dosimeters and career radiation limits
- how little you can feel through a pressurised glove
- ~200 degree temperature swings between sunlight and shadow
- recycling about 90% of water, including breath and sweat
- repairing with only what you launched with
- a 24 h 39 min Martian day pulling the crew out of step with Earth
- losing line of sight and working through the gap
- filling the buffer faster than it can be sent

## Mission story (the explainer)
After the mission vote, a six-panel illustrated sequence runs before play. Each
panel pairs a **real NASA photograph** (credited with title, date and NASA ID)
with one of the chosen astronauts speaking in a comic-style bubble, then a short
explanation. A different crew member narrates each panel.

Both missions follow the same arc:
1. **Why we go** - the problem on Earth
2. **The discovery** - what was actually found, and how
3. **The evidence / what is already happening** - contracts, instruments, dates
4. **Why it matters on Earth** - the concrete payoff today, not just someday
5. **Who pays for it** - government money vs private money, and why both
6. **What is hard** - the honest limits, leading into the trade-off loop

### Real NASA images used
| File | NASA ID | Subject |
|---|---|---|
| moon_scoop | as17-145-22157 | Harrison Schmitt scooping lunar samples, Apollo 17 |
| moon_earth | art002e021278 | Earthset seen from Orion |
| moon_private | KSC-20231121-PH-ULA01_0002 | Astrobotic lander encapsulation |
| mars_spots | PIA26368 | The 'leopard spots' rock |
| mars_selfie | PIA26344 | Perseverance selfie with Cheyava Falls |
| mars_jezero | PIA24485 | The delta in Jezero Crater |
| mars_pixl | PIA26640 | PIXL finding vivianite and greigite |

Pulled from the NASA Image and Video Library, compressed and embedded so the
single file still runs offline. Originals in `art/nasa/`.

## Private sector
A dedicated panel in each mission explains that governments fund what is too
risky or too slow for a business - the science, the first landers, the proof -
while private money turns one mission into an industry. Named with real roles:
Interlune, Vermeer, Astrobotic, Intuitive Machines, SpaceX, and buyers Bluefors
and Maybell Quantum. It also states plainly that Blue Origin is funded by Jeff
Bezos rather than Amazon, and that Exxon has no role in space.

## Cause and consequence at every step
The result readout explains *why*, not just what. Each action carries its own
reason ("baking helium-3 out of regolith needs heat, and heat needs power"), and
radiation outcomes are explained from the real numbers - the cloud's width, your
shielding level, and why the damage lands on life support.

## Screen layout
The game screen is built to fit **one screen with no page scrolling**, so a
player never loses sight of the outpost or of what their last decision did.

Permanently pinned: the scene, the on-duty astronaut and sol counter, the four
gauges, and a **result readout** showing what the crew just did and what the
storm cost. Only the action list scrolls, and only on small phones; CONFIRM is
pinned within thumb reach.

On screens 900px and wider it becomes two columns - scene and status on the
left, event and choices on the right - with nothing scrolling at all.

Verified at 360x640, 390x844, 820x1180, 1280x800 and 1280x620: zero page
scroll, scene and result always visible, CONFIRM always on screen.

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
