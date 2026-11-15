# Space Mission Design Game

**NASA Space Apps Challenge 2026 · São Paulo · 14–15 Nov 2026**
Challenge: [Space Mission Design Game](https://www.spaceappschallenge.org/2026/challenges/space-mission-design-game/)

A browser game for **1 to 4 players**, ages 7–12. You design a complete space
mission — objectives, launch window, power, instruments, communications, rocket
and budget — then fly it and find out which of your decisions was the one that
broke it. **Every choice costs something else**, including doing nothing.

> **Use of AI.** The team chose the challenge, designed both missions, decided
> every rule and balance figure, drew the pixel art and tested the game. The
> code was written with an AI assistant working under the team's direction, and
> the two orbital diagrams are AI-assisted and carry a visible watermark saying
> so. The full declaration is on the game's own **DATA, SOURCES & CREDITS**
> screen, reachable from the title screen.

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
Six selectable crew: **TAYLER, DELAYTINHO, HENRY, CHARLES, NELSON and LUTERO**.
Each has a different specialism and wears one of four suit colours in play.

Each player picks one at the start; duplicates lock out. The crew rotates duty
one astronaut per sol — the on-duty astronaut appears in the HUD and is named in
every mission log entry, so each player gets their own turns in the record.

The portraits are **AI-generated illustrations**, commissioned by the team and
then edited by them. Each full portrait carries a visible **AI-GENERATED IMAGE**
watermark, as the rules require, and the crew-select screen says so in text as
well, because a 52-pixel thumbnail cannot carry a legible watermark of its own.
No NASA logo, Space Apps patch, mission identifier or national flag appears on
any of them: all were removed.

Portraits are embedded as base64, so the single file still works offline.

> **Note on the under-18 rule.** The NASA Space Apps Terms and Conditions bar
> any image, video, audio or other likeness of a person under 18 from a
> submitted project. A build using fully generic pixel astronauts instead of
> these portraits is kept at `art/crew/` and can be restored in one commit.

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
| TAYLER | Engineer | Power systems (+40%) | Not a medic |
| DELAYTINHO | Geologist | Finding good ground (+38%) | Stays out too long |
| HENRY | Flight surgeon | Keeping the crew alive (+45%) | Slows the mission |
| CHARLES | Radiation officer | Shielding (+45%) | Heavy on power |
| NELSON | Systems operator | Wastes nothing (costs -18%) | Never pushes |
| LUTERO | Rover pilot | Covering ground (+30%) | Light on shielding |

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

## Every action has to earn its phase
The flight loop used to be two buttons. It is not any more:

- **Power** — drilling costs 22 W and transmitting 18 W, more than the outpost
  makes in a phase. You cannot run two science actions back to back without
  recharging, and an action you cannot power is greyed out with the numbers shown.
- **Life support** — the crew consumes it every phase whatever you do. Below 45
  they tire and **collect and transmit less**, so neglect costs output long
  before it costs lives.
- **Shielding** — decays every phase on its own as soil settles and seals age.
  Let it reach zero during a strong CME and the mission ends immediately.

So a run is a judgement call: you cannot afford every upkeep action *and* all
the science, and which one you skip depends on the design you flew.

## Seven ways a mission can end
| Ending | Cause |
|---|---|
| **FLAWLESS MISSION** | All science delivered, early, crew in good shape |
| **WELCOME HOME, HEROES** | All science delivered |
| **PARTIAL SUCCESS** | 60%+ delivered when the window closed — real science, not the whole answer |
| **DATA STRANDED** | Plenty collected, too little sent |
| **MISSION INCOMPLETE** | Too many phases went on upkeep |
| **BLACKOUT** | Power reached zero |
| **CREW EVACUATED** | Life support reached zero |
| **RADIATION EMERGENCY** | Shielding at zero when a strong CME arrived |

Each ending names what to change next time. All eight are reachable and were
observed in testing.

## Team artwork (Construct)
Three assets from the team's Construct project are used:
- **cockpit.jpg** — the flight-deck window, shown during the journey (tinted
  warm for the Mars run)
- **ship.png** — the pixel shuttle, flown across the star field in transit
- **start.png** — the START button on the title screen
- **control.png** — the astronaut NPC, cropped head-and-shoulders, who is now
  the face of Mission Control in the radio panel
- **landing.gif** — the 16x16 landing animation, played full-screen between the
  journey and the first day of work
- **rover.png** — the 30x30 mission rover, driving the surface on both worlds
- **astro_anim_*.png** — the hand-animated astronaut from the team's Pixilart
  video, lifted out of the 1900x1900 export, keyed to transparency and
  recoloured into the four suit colours

### The animated astronaut
The Pixilart video was a 10 second, 300 frame, 1900x1900 MP4 with the sprite
occupying a small part of the frame. Rather than embed video, the sprite region
was cropped, the frames de-duplicated down to the real **54 frame** loop, the
white keyed out by flood fill from the border (so the white suit survives), and
the gold visor recoloured into cyan, green, gold and red while keeping its
shading. Four strips, about 26 KB in total, embedded like everything else.

In play, the **astronaut on duty** is drawn with this larger, more detailed
animation while off-duty crew keep the compact 30px suits — so the person
actually working stands out.

Originals in `art/crew/`.

> **Not used: `fundo1`.** It carries a visible *shutterstock.com* watermark, so
> it is third-party licensed material and cannot ship. The submission form
> requires you to confirm that every external resource is listed and that you
> hold permission for any copyrighted material — so it stays out.
>
> **The crew portraits were edited before shipping.** Every Space Apps patch,
> every national flag and every original name tag was removed, and a visible
> AI-generated watermark added, so that no NASA branding or mission identifier
> appears inside AI-generated content.

## The journey
Launching no longer drops you straight onto the surface. The ship crosses a
star field toward a growing destination while the cockpit view and an astronaut
explain how long the crossing takes and why:

- **Moon** — about 3 days, 384,400 km, and you can still turn round
- **Mars** — about 259 days on the Hohmann path, no turning round, no resupply,
  longer in the capsule than a school year

## Side-by-side panels
On screens 760px and wider, the NASA photograph sits beside the text rather
than above it, so a reader sees the picture and the explanation together.
Narrow screens still stack.

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

## The rover
The team's 30x30 rover drives the surface on both worlds, bumping over the
rocks with a small dust puff behind it, and heads out to the sample site when
the crew choose to collect. It faces whichever way it is travelling.

Each mission also carries one radio message about the real machine it is based on:

- **Moon** — the Lunar Roving Vehicle. The Apollo 17 crew covered about **36 km**
  in theirs, still the furthest anyone has driven anywhere off Earth, and Gene
  Cernan reached **18 km/h**, the unofficial lunar speed record.
- **Mars** — Curiosity and Perseverance. Because a command from Earth takes
  minutes to arrive, they drive themselves for much of the day. Perseverance is
  the rover that drilled the Sapphire Canyon core this mission goes to fetch.

## Radio traffic
Every phase brings one message between the crew on the surface and the
teammates who stayed on Earth, shuffled per run so replays differ.

**The crew are named and placed.** Whoever you did not pick for the flight crew
is holding the desk back home, so the link reads
`LUTERO · EARTH → TAYLER` or `TAYLER · MARS → LUTERO`, with both portraits
shown. Nobody appears in two places at once.

**The delay is real and calculated, not decorative.** Each run picks an
Earth-Mars distance between 80 and 370 million km (the real range is roughly 55
to 400 million), divides by the speed of light, and shows the result on every
message:

- *"sent from Earth 19 minutes 34 seconds ago · LUTERO cannot see what you are doing now"*
- *"this will reach LUTERO in 19 minutes 34 seconds · any answer takes that much more"*

On the Moon the same calculation gives **1.3 seconds** over 384,400 km, so the
contrast between the two destinations is visible rather than asserted.

Each message also carries a real difficulty of working off-world, with the
explanation behind a disclosure:

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

### Pictures that answer the question
Each design step shows something that explains *that* decision:

| Step | Image |
|---|---|
| When do we launch? | A drawn orbital diagram — Earth at launch, the transfer arc, and where Mars will be in 259 days (a separate Earth–Moon version for the lunar run) |
| Where does the power come from? | Mars 2020's MMRTG (PIA23306) |
| What science do we carry? | PIXL finding vivianite and greigite (PIA26640) |
| How does the evidence get home? | The Deep Space Network at Goldstone (PIA23214) |
| Which rocket? | Mars 2020 lifting off on an Atlas V (KSC-20200730) |

The launch-window diagram is drawn rather than photographed, because NASA's
image library has no picture that shows *why you must wait*. It is captioned
"drawn for this game" so it is never mistaken for a NASA photograph. It is
geometrically honest: the transfer arc is half an ellipse with the Sun at one
focus, and Mars is placed 136 degrees short of the arrival point, which is how
far it travels in 259 days of its 687-day year.

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
The full, owner-assigned version is in **`docs/SUBMIT.md`**. In short:
- [x] Answers an official challenge — Space Mission Design Game
- [x] Real NASA data (DONKI, Image and Video Library), cited in-game
- [x] Everything in English
- [ ] Under-18 likeness rule — see the note under *Astronaut crew*
- [x] AI use declared in-game, in this README and in the submission text
- [x] Credits screen listing every source, tool and image
- [ ] Demo: 30-second video **or** 7 slides — draft in `docs/SUBMIT.md`
- [ ] Links tested signed out
- [ ] Submitted for judging before the São Paulo cutoff

## Files
```
index.html              the whole game, standalone
docs/SUBMIT.md          submission checklist + every form field, drafted
docs/ASSESSMENT.md      where the project stands against the rules
docs/challenge-brief.md the NASA challenge
docs/MISSIONS.md        mission science + sources + honest caveats
docs/PROJECT-CONTEXT.md event facts, constraints, decisions
data/                   raw DONKI pull + built event deck
tools/                  balance simulator and Playwright verifier
```
