# Final assessment

Sunday 15 November 2026. Challenge: **Space Mission Design Game**, São Paulo.
Submissions close 23:59 local — **confirm the São Paulo cutoff, which may be earlier
than the global portal.**

---

## 1. What changed in this last pass

Everything the team asked for, plus what testing turned up.

| Asked for | Done |
|---|---|
| Each astronaut votes every step, majority wins, ties to the fastest | Yes — and the same rule now settles the mission choice instead of a coin flip |
| Different colours per world | The whole page turns rust-red on Mars, cool grey on the Moon |
| Situations easier to understand, using real past events | Opportunity (2018) on the power choice, Mars Climate Orbiter (1999) on the rocket check |
| More maths, and name the scientists | Equations on three steps; Hohmann (1925); Kulcinski, Wittenberg and Schmitt (1986) |
| Comparison pictures for the decisions | Side-by-side bars for mass, power, cost, lift and speed on every step |
| Make the Earth comms visible and clear | Rebuilt as two people with an animated signal between them |
| Hold attention better | Colour change per world, animated signal, comparison bars, named people, real disasters |

## 2. Against the Space Mission Design Game brief

The brief asks for a game **for 1 to 4 players** that teaches **real aerospace
trade-offs** by letting players **design and simulate a complete mission end to
end**, naming: objectives, spacecraft design, instruments, launch vehicles,
budgets, power, mass, communications and orbital constraints.

| Named in the brief | In the game |
|---|---|
| 1 to 4 players | Crew size, character pick, **a vote every phase** |
| Mission objectives | Six illustrated story panels |
| Spacecraft design | Power, instruments, radio, rocket |
| Scientific instruments | Pick 2 of 4, each costing mass, watts and money |
| Launch vehicles | Three rockets, 300 / 1000 / 4000 kg |
| Budgets | $600M cap, enforced |
| Power | Watts made vs used, enforced |
| Mass | Kilograms vs lift capacity, enforced |
| Communications | Three options setting how fast science gets home |
| Orbital constraints | Launch windows, Hohmann transfer, 26-month cycle |
| Design **and simulate** | Design → verify → journey → operate → deliver → home |

**Eleven for eleven.**

## 3. Handbook test table (p.9) — all verified by automation

| Test | Result |
|---|---|
| A complete mission runs, returns a result, explains, restarts | **PASS** |
| An invalid design cannot launch; the limit and the fix are clear | **PASS** (2 reasons shown) |
| Distinguishes stored data from data delivered to Earth | **PASS** |
| Poor instrument choice explained | **PASS** |
| Double-clicks do not spend twice or skip a stage | **PASS** |
| Restart clears mission state | **PASS** |
| Second device / access without setup surprises | **PASS** (one offline file) |
| First-time player reaches a result without coaching | **Lucca played and was fine** — one data point, not yet written up |

Plus, from this pass:
- No page scroll at 360×640, 390×844 or 1280×800; nothing important clipped
- Every visible button has an accessible name
- Five complete playthroughs across crew sizes, worlds, lengths and difficulties:
  all finished, four different endings, zero JavaScript errors

## 4. Science and sources

Everything checkable is checked, and disagreements are stated rather than hidden.

- **132 real DONKI coronal mass ejections** drive the radiation model, using the
  real speed, NASA's halfAngle geometry and NASA's own class
- **Walter Hohmann, 1925** — the transfer orbit
- **Kulcinski, Wittenberg and Schmitt, 1986** — the first paper linking lunar
  helium-3 to fusion. Schmitt is the Apollo 17 astronaut in the photograph the
  player saw two steps earlier
- **Opportunity, silenced 10 June 2018** by a planet-wide dust storm — attached
  to the solar-versus-nuclear choice
- **Mars Climate Orbiter, 1999** — newtons versus pound-force, arrived at ~57 km
  instead of 140–150 km. Orbiter cost ~$125M; published programme-loss figures
  run higher, and the game says so
- Maths shown as equations: 1/distance² for sunlight, distance ÷ speed of light
  for signal delay, mass ≤ lift capacity

## 5. What is still missing — none of it is code

1. **Write up a child testing it.** Lucca played and was fine; that needs to
   become a sentence a judge can read: who played, what confused them, what they
   could explain afterwards. This is the Impact lens, scored first.
2. **Demo video**, 60–90 seconds, narrated by the children.
3. **One-page data explainer** — the content is already in `NASA-SOURCES.md`.
4. **AI disclosure** in the submission. This code was written by an AI assistant
   working to the team's direction; the handbook (p.11) requires that to be
   stated.
5. **Confirm one listed NASA source on the challenge's Resources tab.** Three
   sources used here came from the list the team supplied, but this container
   cannot reach spaceappschallenge.org to verify it.

## 6. On holding attention

What was added: the page changes colour with the world, the radio signal
animates between two faces, comparison bars make choices visually obvious, real
disasters give stakes, and named people give the science a human face.

What would help most next, and costs nothing to build: **shorten the story from
six panels to four**. A first run is now title → crew → setup → characters →
vote → 6 story panels → 5 design steps → verify → journey → 6 phases → debrief.
That is a lot before the first decision. The SHORT mission setting already helps;
cutting two story panels would help more.

## 7. Verdict

The build answers the brief completely and passes every functional test. The
science is real, sourced, and honest about what is disputed.

**The remaining work is evidence, not engineering.** An hour spent writing down
what Lucca and two others did — what confused them, what they could explain
afterwards — is worth more to the score than anything further that could be
built today.
