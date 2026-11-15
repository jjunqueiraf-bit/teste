# How to save the game and submit it

Written for the team. Two parts: **saving your work**, then **submitting it**.

> **Check your clock first.** The global portal accepts projects until 23:59
> Sunday 15 November, local time. Your São Paulo event may set an **earlier**
> cutoff. Use whichever comes first, and aim to finish two hours before it.

---

# PART 1 — Saving the version

## The game is one file
Everything — the code, the NASA photographs, the astronaut portraits, your
Construct artwork, the 132 real solar-storm records — is inside a single file:

```
NASA-SAC-2026/index.html
```

Nothing else is needed to play it. No internet, no install, no account.
Double-click it and it runs.

## A. Save a copy you can hand over (do this first, it takes a minute)
1. Download `index.html` from GitHub (open the file, press the **Download raw
   file** button).
2. Rename it with today's date, e.g. **`mission-trainer_20261115_1800.html`**.
3. Put it in a folder on the laptop called `demo`.
4. **Open it and play one full mission.** If it works from that folder with the
   Wi-Fi switched off, it will work for a judge.
5. Copy that same file onto a second device or a USB stick. The handbook asks
   for a backup that someone else can open.

## B. Keep the history on GitHub
The project lives at **github.com/jjunqueiraf-bit/teste**, under `NASA-SAC-2026/`.
Every change so far is already saved and pushed there.

To save a new change from a computer with git:
```
cd NASA-SAC-2026
git add -A
git commit -m "say what you changed"
git push
```

**Under-13s must not create GitHub accounts.** An adult pushes on the team's
behalf — that is what the handbook says, and it is a GitHub rule, not ours.

## C. Make a release the judges can download
On GitHub: **Releases → Draft a new release → tag `v1.0` → attach
`index.html` → Publish**. That gives you one permanent link to a file that
cannot change afterwards.

## D. Before you call it final
- [ ] Open the saved file **with Wi-Fi off** and finish a mission
- [ ] Open it on a **second device**
- [ ] Try a **deliberately bad design** (small rocket, big dish, launch next
      month) and check it says CANNOT LAUNCH with reasons
- [ ] Try **collecting and never sending** and check it ends with the science
      stranded
- [ ] Press **PLAY AGAIN** and confirm it starts clean

---

# PART 2 — Submitting to NASA Space Apps

## What a submission needs
Submissions are made on your **team page** on spaceappschallenge.org, under the
**Project** tab. Fill in the real fields the site shows you — the list below is
what to have ready, not a claim about the exact form layout. **Open the page
early and read the actual fields**, because they are the authority, not this
document.

Have ready:

| Thing | What we have |
|---|---|
| Project name | Junior Astronaut Mission Trainer — Space Mission Design Game |
| Short summary | See the paragraph below |
| How it works | `README.md` |
| NASA data used | `docs/NASA-SOURCES.md` |
| Link to play it | The published page, or the GitHub release |
| Link to the code | github.com/jjunqueiraf-bit/teste |
| Demo video | **Still to record — see below** |
| AI use statement | **Must be written — see below** |

### A summary you can paste and edit
> A mission-design game for 1 to 4 players, aged 7 to 12. Players choose a
> destination, then design the mission: when to launch, where the power comes
> from, which two instruments to carry, how the evidence gets home, and which
> rocket can lift it. A design that breaks its mass, power, cost or launch
> window limits cannot launch, and the game says why. In flight, the crew vote
> each phase, and science only counts once it has been transmitted to Earth —
> collect everything and send nothing and the mission fails. Solar storms come
> from 132 real coronal mass ejections in NASA's DONKI database, using each
> event's real speed and angular width.

## The demo video
The handbook asks for a short, screen-only recording with captions. Aim for
**60–90 seconds**. Record the screen, not the room, and **keep the children's
faces and full names out of the video** — the handbook is explicit about that.

A running order that fits in 90 seconds:
1. **(10s)** Title, then the mission choice. "We picked Mars, to go and get a
   rock that might hold signs of ancient life."
2. **(20s)** The launch-window step. Show the diagram. "You cannot go to Mars
   on any day. Earth takes 365 days to orbit, Mars takes 687, so they only line
   up every 26 months."
3. **(15s)** Pick a power source and an instrument. Point at the comparison
   bars. "The nuclear battery is heavier and costs more, but it keeps working
   in a dust storm. Opportunity died in one in 2018."
4. **(15s)** BUILD & VERIFY failing. "Too heavy for this rocket, so it does not
   launch. That is a real design review."
5. **(20s)** One or two phases of flight. Show the Earth message with the delay.
   "This took 19 minutes to arrive. Nobody on Earth is watching us live."
6. **(10s)** The ending. "Science only counts when it reaches Earth."

**One of the children should narrate it.** That matters more than polish: it
shows the team understands the work.

Recording: use whatever screen recorder is already on the laptop. Test a
10-second clip first and play it back before recording the real one.

## The AI statement
This game's code was written by an AI assistant working to the team's
instructions and decisions. The handbook (p.11) says AI use is allowed **with
disclosure**. Write it plainly in the project description, something like:

> The team designed the game, chose the missions, made the pixel art and the
> astronaut characters, and decided every rule. The code was written with an AI
> assistant, under the team's direction. All NASA data and sources are listed in
> the project.

Do not leave this out, and do not bury it.

## Before you press submit
- [ ] Confirm the **São Paulo deadline** as well as the global one
- [ ] Open the challenge's **Resources tab** and confirm at least one of the
      NASA sources we used is listed there (Global Awards eligibility)
- [ ] Check every link you pasted **actually opens**, signed out, on a second
      device
- [ ] Write one sentence about a child who played it: who, what confused them,
      what they could explain afterwards
- [ ] Press submit, then **reload the page and confirm it says submitted, not
      saved**. A draft is not an entry.
- [ ] Screenshot the confirmation

## If something breaks at the last minute
Fall back to the saved file from Part 1A. It is self-contained and offline, so
it cannot be broken by a website being down or Wi-Fi failing at the venue.
