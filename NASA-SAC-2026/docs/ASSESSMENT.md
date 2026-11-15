# Final assessment

Sunday 15 November 2026. Challenge: **Space Mission Design Game**, São Paulo.
Submissions close 23:59 São Paulo time — **Local Event clock, and anything saved
after it is ineligible.** Code freeze 20:00, submit 21:00. See `SUBMIT.md`.

---

## 0. Eligibility — the pass/fail gate

A judge checks these before scoring anything. Fail one and the project is scored
**1 (Poor) and not evaluated further.**

| # | Requirement | Status | Owner |
|---|---|---|---|
| 1 | Answers an official challenge, not Invent Your Own | ✅ **Done** — Space Mission Design Game, in the title screen, README and docs | Adult lead confirms the team page matches |
| 2 | NASA data used, and visible | ✅ **Done** — DONKI, Image and Video Library, NASA's six-step process, CubeSat 101, all on the in-game credits screen | Crew: confirm one appears on the challenge Resources tab |
| 3 | Primarily in English | ✅ **Done** | — |
| 4 | Demo ≤30s video or ≤7 slides | ⚠️ **Missing** — both drafted in `SUBMIT.md`; slides recommended | Crew + adult |
| 5 | AI use declared, AI content labelled | ✅ **Done in the build** — credits screen, README, watermarked diagrams | Adult pastes the declaration into the form |
| 6 | Every source, tool and image cited | ✅ **Done** — new credits screen + References draft | — |
| 7 | All links public, no password | ⚠️ **Missing** — nothing published yet | Adult lead |
| 8 | Team registered, 2–6, same Local Event | ⚠️ **Verify first** — cannot add members after close | Adult lead |
| 9 | Submitted by the deadline | ⚠️ **Not yet** | Adult lead |

### Risks closed in this pass

- **Likenesses of under-18s.** The six illustrated portraits of the children
  are out of the build. Crew are now generic pixel astronauts by callsign —
  ORION, VEGA, RIGEL, LYRA, ATLAS, NOVA — recoloured from the team's own
  astronaut sprite. No face, no name tag, no patch. The personalised version was
  handed over as a private family build and is **not in this repository**.
- **NASA branding inside AI-generated art.** The patch went with the portraits.
  Nothing AI-generated in the build now carries a NASA logo, flag or identifier.
- **Unwatermarked AI images.** Both orbital diagrams now carry a visible
  **AI-ASSISTED DIAGRAM** watermark.
- **Wrong challenge name.** Title screen, document title, README and the page
  banner all now say Space Mission Design Game.
- **Demo length.** Earlier guidance in this repo said 60–90 seconds. The limit
  is 30 seconds or 7 slides, and judges stop at the limit.

### Risks still open

1. **The old portraits are in this repository's git history**, inside earlier
   commits of `index.html`. Not visible to a judge, but public. History can be
   rewritten on request.
2. **The children cannot narrate the demo** — a voice is audio likeness of a
   minor. Use burned-in English captions, or an adult narrating.
3. **The demo does not exist yet.** It is the one piece of pure missing work,
   and it is often the first thing a judge opens.
4. **Nothing is published.** Every link must resolve for a stranger with no
   account.

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

1. **The demo.** ≤30 second video or ≤7 slides. Both drafted in `SUBMIT.md`;
   the slides are the safer choice tonight. Not narrated by the children.
2. **Publish the links.** GitHub release for the game, public host for the
   demo, both tested signed out in a private window.
3. **Write up a child testing it.** One player tried it and was fine; that needs
   to become a sentence a judge can read — who played, what confused them, what
   they could explain afterwards. It belongs in the Detailed Description, and it
   is the Impact lens, which is scored first.
4. **Confirm the team page**: challenge set to Space Mission Design Game, all
   six members confirmed at the São Paulo event.
5. **Confirm one listed NASA source on the challenge's Resources tab.** The
   sources used here came from the list the team supplied, but this container
   cannot reach spaceappschallenge.org to verify it.

Everything else — the AI declaration, the credits, the citations, the English,
the removal of the children's likenesses — is now in the build and drafted in
`SUBMIT.md` ready to paste.

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

The build answers the brief completely, passes every functional test, and now
clears every eligibility gate that can be cleared in code. The science is real,
sourced, and honest about what is disputed. Five full playthroughs across crew
sizes, worlds, lengths and difficulties all finish, with four different endings
and zero JavaScript errors.

**The remaining work is evidence and publishing, not engineering.** Three things
decide whether this scores: the demo exists and is inside the limit, every link
opens for a stranger, and someone clicks Submit for Judging before the São Paulo
cutoff. An hour on the seven slides and a written note about a child playing it
is worth more than anything else that could be built today.
