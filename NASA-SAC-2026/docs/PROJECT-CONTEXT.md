# NASA Space Apps 2026 — Project Context

## Identity
- **Event:** NASA Space Apps Challenge 2026 — **14–15 Nov 2026** (live now)
- **Theme:** The Next Frontier
- **Local event:** São Paulo
- **Challenge:** Space Mission Design Game (1–4 players; design and simulate a complete mission end to end)
- **Source:** https://www.spaceappschallenge.org/2026/challenges/junior-astronaut-mission-trainer/
- **Full brief:** `docs/challenge-brief.md`

## Origin
Project began as a ChatGPT/Codex project (`NASA SAC 2026`, local folder
`g-p-6aceeccfe768819195579b9fe42dfa94` on Windows). Migrating to Claude Code.
Prior files/threads NOT yet transferred.

## The deliverable
Browser-playable prototype for ages 7–12: run a lunar or Martian outpost,
balance life support / radiation shielding / power / food / comms delay.
Every choice costs something else. No free "safe" option.

## Hard constraints (from brief)
- Browser-playable, **no download, no account**
- 2–3 core resources, not 5–6
- Real NASA data, attributed in-tool
- Must label archived data as archived — never present static as live
- Ship: working prototype + 1-page data explainer + demo video

## Judging angles
1. In-game choices tied to real-world consequences
2. Replayability — varied events, learn from failure without punishment
3. Data explainer judges can verify

## Environment status (verified 14 Nov 2026)
- Cloud container, **ephemeral** — nothing survives without a git push
- Network: NASA hosts opened on personal Default env —
  `api.nasa.gov`, `osdr.nasa.gov`, `images-api.nasa.gov`
- `api.nasa.gov` DEMO_KEY works but rate-limits at 30/hr (hit it)
- DONKI `/CME` → 200, **133 real events** captured for 1 Oct–14 Nov 2026
- DONKI `/FLR` → returned a NASA-side 404 on one window; retest with a real key
- `images-api.nasa.gov` → 200, Artemis south pole imagery available

## Captured data
- `data/donki-cme-2026-10-01_to_11-14.json` — 133 real CME events
- `data/nasa-images-artemis-south-pole.json` — NASA imagery search results

## Open decisions (BLOCKING build)
1. **Site:** Moon south pole (Artemis topicality) vs Mars (comms-delay mechanic is real)
2. **Stack:** single-file no-build HTML/JS vs React — must deploy static
3. **Data mode:** curated real archive shipped with game (recommended) vs live API calls
