# NASA Space Apps Challenge 2026 — Build a Junior Astronaut Mission Trainer

**Source:** https://www.spaceappschallenge.org/2026/challenges/junior-astronaut-mission-trainer/
**Captured:** 14 Nov 2026
**Local event:** São Paulo
**Difficulty:** Intermediate · Beginner/Youth
**Subjects:** Games · Planets & Moons · Software · Space Exploration · Sun
**Page tabs:** Details · Resources (datasets/links) · Teams · Event

---

## 1. The challenge in one line
Design and build an interactive game or app where kids aged 7–12 run a lunar or Martian outpost and balance competing demands — life support, radiation shielding, power, food production, communication delay — so they experience the trade-offs that make a mission succeed or fail.

## 2. Problem being solved
- Kids' space content tends to be either too abstract (posters, facts) or too technical.
- Students see mission *outcomes*, rarely the *decision logic* behind them.
- Pure education loses attention; pure entertainment loses accuracy. The gap is translation.

## 3. Background (NASA context)
- NASA is building a sustained Moon presence (Artemis) and extending toward Mars.
- Outpost crews must split limited power across life support, comms and science; weigh radiation exposure against objectives; and absorb resource costs that compound over time.
- Mission planners make these calls using real data — the same data the game should use.

## 4. Objectives
- Players manage an outpost and make real decisions on: **life support, radiation shielding, power budget, food production, communication delay**.
- Choices play out over a simulated mission timeline.
- No choice is free: e.g. trade oxygen reserves for a research opportunity; reinforce shielding against a solar event at the cost of tonight's power.
- Deliverable: a **working prototype** that makes the trade-off mechanic clear enough that a young player leaves understanding a real deep-space constraint.
- Format is open: survival/resource management, narrative decision tree, mission-control dashboard, or other; browser, mobile or desktop. Creative "outposts" beyond Moon/Mars are allowed if the teaching goal stays central.

## 5. NASA data sources to use
| Dataset | What it gives the game |
|---|---|
| **DONKI** (Space Weather Database of Notifications, Knowledge, Information) | Real solar flares / CMEs / radiation-risk events → drive shielding decisions |
| **OSDR** (Open Science Data Repository) | Astronaut radiation dosimetry, health and biology findings → consequences of exposure |
| **Artemis & Mars surface mission data** | Environmental conditions at the chosen site (temperature, light/sol length, terrain, photos) |

Guidance: real data over invented numbers; attribute sources inside the tool; if live API calls aren't feasible, embed a curated real dataset — but don't present static data as live. Check the **Resources** tab for added datasets.

## 6. Design considerations
**Audience & accessibility**
- Ages 7–12, but able to flex to siblings, parents, classrooms.
- Plain language; explain unavoidable terms (radiation dose, microgravity, sol) in context.
- Low barrier: browser-playable, no download, no account.

**Pitfalls to avoid**
- A "safe" option with no cost.
- Visual polish replacing mechanical accuracy.
- Too many systems — 2–3 core resources (life support, power, shielding) beat 5–6.

## 7. What makes a solution stand out (judging angles)
1. Links in-game choices to **real-world consequences** — e.g. shielding decision tied to current space weather.
2. **Replayability** — varying events/mechanics so kids try strategies and learn from failure without feeling punished.
3. A short **data explainer** with the prototype: which NASA datasets were used and why, so judges can verify the science.

## 8. Build checklist (derived)
- [ ] Pick site (Moon south pole / Mars) and 3 core resources
- [ ] Define the trade-off loop (each action costs ≥1 other resource)
- [ ] Pull DONKI events (live API or curated archive) as the event engine
- [ ] Map OSDR findings to health consequences in kid-friendly language
- [ ] Use real site data/photos for environment
- [ ] In-game source attribution + "live vs archived" label
- [ ] Randomized event deck for replayability
- [ ] Browser build, no login
- [ ] 1-page data explainer + demo video for submission

---
*Space Apps is funded by NASA's Science Mission Directorate via Booz Allen Hamilton, Mindgrub and SecondMuse. Questions: Space Apps Connect.*
