# Where this project stands

Re-assessed Sunday 15 Nov 2026, after the pivot to **Space Mission Design Game**.
Deadline 23:59 Sunday São Paulo time — confirm the local cutoff, which may be earlier.

Scored against the Space Mission Design Game brief and the team handbook's five
judging lenses (p.11) and test table (p.9).

---

## 1. Against the Space Mission Design Game brief

The published brief asks for a game *"for 1 to 4 players"* that teaches
*"the complex, real-world trade-offs of aerospace engineering by letting users
design and simulate a complete mission from end to end"*, naming: mission
objectives, spacecraft design, scientific instruments, launch vehicles, budgets,
power, mass, communications and orbital constraints.

| Named in the brief | In the game | How |
|---|---|---|
| 1 to 4 players | **Yes** | Crew size, character select, duty rotates each phase |
| Mission objectives | **Yes** | Six story panels establish the science question |
| Spacecraft design | **Yes** | Power source, instruments, radio, rocket |
| Scientific instruments | **Yes** | Pick exactly 2 of 4; each costs mass, power, money |
| Launch vehicles | **Yes** | Three rockets, 300 / 1000 / 4000 kg capacity |
| Budgets | **Yes** | $600M cap; a design over budget cannot launch |
| Power | **Yes** | Watts made vs watts used; over-draw blocks launch |
| Mass | **Yes** | Kilograms vs rocket capacity; over blocks launch |
| Communications | **Yes** | Three options; sets how fast science reaches Earth |
| Orbital constraints | **Yes** | Launch windows — 26 months, Hohmann transfer, 259 days |
| Design **and simulate** end to end | **Yes** | Design → verify → fly → deliver → home |

**Nine of nine named elements, plus the player count.** This is the strongest
part of the submission.

## 2. Handbook test table (p.9)

| Test | Result |
|---|---|
| A complete mission runs, returns a result, explains, restarts | **PASS** |
| **An invalid design cannot launch; limit and redesign route clear** | **PASS** — blocks on mass, power, cost or launch window, each with the number and the fix |
| **Distinguishes stored data from data delivered to Earth** | **PASS** — collect-and-never-send loses with the science stranded, and says so |
| Poor instrument choice explained | **PASS** — warnings name what the missing instrument would have told you |
| Double-clicks do not spend twice or skip a stage | **PASS** |
| Restart clears mission state | **PASS** |
| Second device / access without setup surprises | **PASS** — one offline file |
| First-time player reaches a result without coaching | **UNTESTED** |

Seven of eight. The eighth needs a child, not code.

## 3. Five judging lenses (p.11)

| Lens | Status |
|---|---|
| **Creativity** | **Strong** — design-then-fly, crew specialisms, radio traffic |
| **Relevance** | **Strong** — every element the brief names, structured on NASA's own six-step process |
| **Validity** | **Strong, one check outstanding** — real DONKI data, traceable rules, tested outcomes, sources documented; confirm a listed source appears on the Resources tab |
| **Presentation** | **Partial** — honest claims and readable captions, but no demo video |
| **Impact** | **Missing** — no named learner, no observed misconception |

## 4. Playthrough length

Measured end to end, automated: **42 clicks across 10 screens**.
At a realistic reading pace that is **3 to 4 minutes** — inside the handbook's
3–5 minute target. Breakdown: 6 story panels, 5 design steps, 1 verification,
4 flight phases, 1 debrief.

---

## What changed since the last assessment

Resolved:
- **Challenge identity** — was the biggest risk; the project is now built for
  Space Mission Design Game and matches its brief point by point
- **Game shape** — design and simulate end to end, not outpost survival
- **Two handbook pass conditions** that were previously N/A now pass
- **Length** — was 12–36 turns, now 4–8 phases and 3–4 minutes total
- **Mobile** — the choices were unreachable; the page no longer scrolls
- **Consequences** — now shown before committing and explained after
- **Editorialising removed** — the Exxon / Blue Origin / Amazon aside is gone

Still open, in priority order:
1. **No child has tested it** — the Impact lens, and the last failing pass condition
2. **No demo video**
3. **No one-page data explainer packaged** (content drafted in `MISSIONS.md` and `NASA-SOURCES.md`)
4. **Authorship / AI disclosure** not yet written into the submission
5. **Resources tab unverified** — see below

## On the NASA source requirement
The handbook (p.7) makes at least one listed NASA source a Global Awards gate.
Three of the sources this project uses came from the resource list supplied for
this challenge, and all three do real work in the game:
- **Design and Develop Science Missions** — its six-step process is the design
  progress bar; its four segments are the verification summary
- **CubeSat 101** — anchors the mass and cost scales
- **DONKI** — 132 real CME events drive the radiation model

That almost certainly satisfies the gate. **It still needs one human check:**
open the challenge's Resources tab and confirm at least one of these is listed
there. This container cannot reach spaceappschallenge.org — DNS and TLS both
fail through the proxy — so it is the one thing I cannot verify for you.

---

## Where to spend the remaining hours

| # | Task | Time | Why |
|---|---|---|---|
| 1 | Confirm a listed NASA source on the Resources tab | 10 min | Awards eligibility |
| 2 | Three children play it cold; write down what confused them | 60 min | Impact lens + the last pass condition |
| 3 | Fix the top one or two confusions | 60 min | Driven by evidence, not guesswork |
| 4 | One-page data explainer | 30 min | Content already drafted |
| 5 | 60–90 s demo video, narrated by the children | 60 min | Presentation + authorship |
| 6 | AI disclosure line in the submission | 10 min | Handbook p.11 |
| 7 | Submit two hours early, confirm *submitted* not saved | 30 min | Handbook p.10 |

## What not to do
- No new features. The brief is fully covered; more surface means more to explain.
- No platform port.
- Do not skip the child test to polish the game further. The game is no longer
  the weak part.

## Honest summary
The build now answers the challenge brief completely and passes seven of the
handbook's eight functional tests. Three months ago this would be a finished
project.

What is missing is **evidence that it teaches anyone** — and the handbook scores
that explicitly, in the lens listed first. One afternoon of three children
playing it, with notes on what confused them and what they could explain
afterwards, is worth more than anything else that could be built today.
