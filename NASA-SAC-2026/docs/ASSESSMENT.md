# Where this project stands

Assessed 14 Nov 2026, ~22:30 São Paulo. Deadline 23:59 Sun 15 Nov (confirm the
local São Paulo cutoff — it may be earlier than the global portal).

Scored against two documents: the challenge brief (`challenge-brief.md`) and the
team preparation handbook's five judging lenses (p.11) and test table (p.9).

---

## 1. Against the challenge brief

| Brief requirement | Status | Note |
|---|---|---|
| Kids 7–12 run a lunar or Martian outpost | **Strong** | Both missions playable |
| Balance competing demands | **Strong** | Power / life support / shielding |
| 2–3 core resources, not 5–6 | **Strong** | Exactly 3 — the brief explicitly prefers this |
| Choices play out over a mission timeline | **Strong** | 12 / 24 / 36 sols |
| No choice is free | **Strong** | Even "shelter and wait" costs oxygen |
| Real NASA data, attributed in-tool | **Strong** | 132 DONKI events, IDs + links shown |
| Archived data labelled as archived | **Strong** | Badged everywhere |
| Browser, no download, no account | **Strong** | One 482 KB offline file |
| Working prototype | **Strong** | Verified end-to-end |
| **Judging angle 1** — choices tied to real-world consequence | **Strong** | Damage derives from real CME speed + halfAngle |
| **Judging angle 2** — replayability | **Strong** | 132 events, 2 missions, 6 specialists, 9 setup combos |
| **Judging angle 3** — short data explainer shipped with it | **MISSING** | Content exists in `MISSIONS.md`, not packaged as a deliverable |
| Food production as a demand | Not included | Deliberate — brief prefers 3 resources |
| Communication delay as a demand | Not included | Mars comms appears as an event, not a managed resource |

## 2. Against the handbook's five judging lenses (p.11)

| Lens | What it asks for | Status |
|---|---|---|
| **Impact** | A named learner, a specific misconception, an observed improvement | **MISSING — nothing tested with a real child** |
| **Creativity** | A clear, enjoyable way to expose an engineering decision | **Strong** |
| **Validity** | Required listed NASA source, a traceable rule, a tested outcome | **At risk** — rules traceable and tested, but DONKI is unverified against the chosen challenge's Resources tab |
| **Relevance** | Mapped to the full challenge brief | **At risk** — challenge identity unresolved |
| **Presentation** | Short working demo, readable captions, honest claims | **Partial** — honest claims yes, no demo video |

## 3. Handbook test table (p.9)

| Test | Result |
|---|---|
| A complete mission runs, returns a result, explains, restarts | **PASS** (verified) |
| Double-clicks do not spend twice or skip a stage | **PASS** (verified) |
| Restart clears mission state | **PASS** (verified) |
| Second device / access without setup surprises | **PASS** — single file, works from `file://` |
| First-time player reaches a result without coaching | **UNTESTED** |
| Mass / budget limit blocks an invalid design | **N/A** to this game's shape |
| Distinguishes stored data from data delivered to Earth | **N/A** to this game's shape |

Those last two N/As matter — see risk 1.

---

## The three real risks

### Risk 1 — the challenge may be the wrong one (HIGHEST)
The repo README and the handbook both name **Space Mission Design Game**. The
brief we built against is **Junior Astronaut Mission Trainer**, which does not
appear in the published 2026 list; the only match found was a page labelled 2027.

They want different games. Space Mission Design Game asks players to *design and
simulate a mission end to end* — instruments, launch vehicle, budget, mass,
communications, orbit. This game is outpost survival. It has no design stage, no
budget or mass check, no launch decision and no downlink choice.

**Action: open the team page and confirm the selected challenge. 5 minutes.**
Everything below is worth less if this is wrong.

### Risk 2 — nothing has been tested with a child
"Impact" is a judging lens and a pass condition, and it is the one thing no
amount of building can substitute for. The handbook even scripts it (p.9):
ask before play *"If you collect a great image but cannot send it, did the
mission succeed?"*, and after play *"You have energy for one more observation
or a downlink — what would you do and why?"* Record the answer, not whether
they enjoyed it.

### Risk 3 — authorship
The handbook says the children author the game and the explanation, and that AI
assistance is disclosed. This code is AI-written. That does not disqualify the
work, but it must be declared, and the children need to be able to explain the
decisions. The surest fix is for them to narrate the demo video themselves.

---

## Where to spend the remaining time

| # | Task | Time | Why |
|---|---|---|---|
| 1 | Confirm the challenge on the team page | 5 min | Unblocks everything |
| 2 | Open its Resources tab, note one listed NASA source | 10 min | Global Awards eligibility gate (handbook p.7) |
| 3 | Three children play it cold; write down what confused them | 60 min | The only way to earn the Impact lens |
| 4 | Fix the top one or two confusions | 60 min | Driven by 3, not by guesswork |
| 5 | One-page data explainer | 30 min | Judging angle 3; content already drafted |
| 6 | 60–90 s demo video, narrated by the children | 60 min | Presentation lens + authorship |
| 7 | AI disclosure line in the submission | 10 min | Handbook p.11 |
| 8 | Submit, confirm *submitted* not saved, 2 h early | 30 min | Handbook p.10 |

Everything above the line is worth more than any new feature.

## What NOT to do now
- Do not port to another platform (MakeCode Arcade, Unity). The NASA photographs
  cannot survive a 16-colour 160×120 screen, and it risks a working entry.
- Do not add more resources. The brief explicitly prefers three.
- Do not add a third mission. The handbook asks for one; you already have two.

## Honest summary
The **build** is in good shape — arguably ahead of what the brief asks, with
real data used in a way judges can verify, and balance proven by simulation
rather than asserted.

The **evidence around the build** is thin. There is no record of a child
learning anything, no demo, and no packaged explainer. Those are exactly what
three of the five judging lenses score.

A weaker game with a tested learner and a clear two-minute demo would likely
score higher than this one submitted as-is.
