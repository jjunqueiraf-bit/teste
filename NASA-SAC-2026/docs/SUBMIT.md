# Submission: checklist, demo and every form field

**Challenge: Space Mission Design Game · São Paulo · deadline Sun 15 Nov 2026, 23:59 local**

Rules here come from the official Project Submission Guide as read by the team
lead in a browser (this machine cannot reach spaceappschallenge.org), backed by
the NASA Space Apps guide PDFs archived in this folder.

---

## ⏰ Code freeze

Anything saved after the deadline is ineligible, and the clock is the Local
Event's, not yours. Work back from 23:59 with real buffer:

| Time | What happens | Owner |
|---|---|---|
| **20:00** | **Code freeze.** Last commit, last push, last release. Nothing touches `index.html` after this. | Adult team lead |
| 20:15 | Download the release file fresh and play one full mission offline | Crew |
| 20:30 | Open every link you are about to paste in a **private window**, signed out | Crew |
| 21:00 | Paste all fields, tick both boxes, **click Submit for Judging** | Adult team lead |
| 21:05 | Reload the page. It must say *submitted*, not *saved*. Screenshot it. | Adult team lead |
| 21:05–23:59 | Buffer. You may keep re-submitting improvements; the last one is judged. | — |

Confirm the São Paulo cutoff with your Local Lead — it can be earlier than the
global one, and the Local Event's clock is the one that counts.

---

## The mandatory checklist

| # | Requirement | Status | What is left, and who does it |
|---|---|---|---|
| 1 | **Answers an official NASA challenge**, not Invent Your Own | ✅ **Done** | Game, README and title screen all name **Space Mission Design Game**. Confirm the team page has the same challenge selected. *Adult team lead* |
| 2 | **Uses a NASA data source from the challenge**, visibly cited | ✅ **Done** | DONKI (132 real CMEs, real speed / half-angle / class), NASA Image and Video Library (10 photos with NASA IDs), NASA's six-step mission design process, CubeSat 101. All listed on the in-game **DATA, SOURCES & CREDITS** screen and in the NASA Data field below. **Still to check:** that at least one of these appears on the challenge's own Resources tab. *Crew* |
| 3 | **Presented primarily in English** | ✅ **Done** | Game, README and all docs are English. Keep the form fields English too. |
| 4 | **Demo: ≤30s video OR ≤7 slides** | ✅ **Built** | The 7-slide deck is made and ready to export. No audio, so no subtitle requirement. *Adult lead: export and host it* |
| 5 | **AI use declared and AI content labelled** | ✅ **Done in the build** | In-game credits screen, README, and the Use of AI field below. The two orbital diagrams carry an **AI-ASSISTED DIAGRAM** watermark; the six crew portraits carry an **AI-GENERATED IMAGE** watermark. **Still to do:** paste the declaration into the form. *Adult team lead* |
| 6 | **All sources, tools, images and materials cited** | ✅ **Done** | New **DATA, SOURCES & CREDITS** screen in the game (title screen → link, and from the debrief), plus `docs/NASA-SOURCES.md` and the References field below. |
| 7 | **All links public, no password** | ✅ **Done for the game** | Repo public; **GitHub Pages live and verified** from a clean signed-out browser — HTTP 200, 633 ms, byte-identical to the build, all assets render, no JS errors. Still to host: the demo PDF. *Adult team lead* |
| 8 | **Team registered, 2–6 participants, same Local Event** | ⚠️ **Verify** | Six crew. Check all six are confirmed on the team page at the São Paulo event. **You cannot add anyone after submission closes.** *Adult team lead — do this first* |
| 9 | **Submitted by 15/11 23:59 São Paulo** | ⚠️ **Not yet** | See the code-freeze table above. *Adult team lead* |

### Risks, in the order they would sink the entry

1. **The crew portraits are AI-generated likenesses of the team's children —
   this is the team's accepted risk, taken with the facts in front of them.**
   - **Fixed:** every NASA Space Apps patch, every Brazilian flag and every
     original name tag has been removed, the names are now TAYLER, DELAYTINHO,
     HENRY, CHARLES, NELSON and LUTERO, and each portrait carries a visible
     **AI-GENERATED IMAGE** watermark. The crew-select screen states in text
     that the portraits are AI-generated, because a 52-pixel thumbnail cannot
     carry a legible watermark.
   - **Still open:** the rule says a project may not include *"any images,
     video, audio, or other likeness to persons under 18 years old."* These
     were rendered **from photographs of the children**, so they are
     AI-generated likenesses of real minors, which is what *other likeness*
     covers — renaming the characters does not change what the image is. An
     AI-generated face of a person who does not exist would not be caught by
     this; these are not that.
   - **The one-commit undo:** a complete build using generic pixel astronauts
     (no faces at all) was tested and works. If a judge or Local Lead raises
     it, that build can ship in minutes. Ask and it will be restored.
2. **The children cannot narrate the demo.** A voice is audio likeness of a
   minor. The deck has no audio, which avoids this entirely.
3. **Nothing is published.** Every link in the form has to resolve for a
   stranger with no account.

---

## PART 1 — Save and publish the build

### The game is one file

```
NASA-SAC-2026/index.html     (~549 KB)
```

Code, 10 NASA photographs, the team's pixel art, the landing animation, the
rover and 132 real coronal mass ejections — all inside it. No internet, no
install, no account. Double-click and it runs.

### ✅ The repository is public

Verified signed-out, with no token: the repo, the raw game file and the docs
all return 200. You are no longer blocked.

⚠️ **One consequence is now live.** The repository's **git history** is public
too, and **20 earlier commits of `index.html` still contain the original
portraits** — with the NASA Space Apps patches, the Brazilian flags and the
children's real first names. A judge will not read your git history, but it is
there. The history can be rewritten so only the current version exists; it
takes a few minutes and a force-push. Ask if you want it.

### Which link goes in "Link to Final Project"

### ✅ Use this one

```
https://jjunqueiraf-bit.github.io/teste/NASA-SAC-2026/index.html
```

Verified from a clean browser, signed out, no token: HTTP 200 in 633 ms,
byte-identical to the build, all six portraits render, 132 DONKI events and ten
NASA photographs present, the credits screen opens, **no failed requests and no
JavaScript errors.** A judge clicks it and the game is playing.

| Option | Link | What a judge gets |
|---|---|---|
| **Pages** ⭐ | the URL above | **The game, playing, in one click.** Live and tested. |
| Repo | `https://github.com/jjunqueiraf-bit/teste` | Works. They must find and download the file themselves. Good as a *source code* link. |
| Release | `v1.0` | **Still an unpublished draft with no file attached.** Optional now that Pages works — finish it or discard it. |
| ~~Raw file~~ | `raw.githubusercontent.com/...` | **Do not use.** GitHub serves it as `text/plain`, so a judge sees a wall of base64. Verified. |

### Steps left

1. ~~Make the repo public~~ — **done.**
2. ~~Turn on GitHub Pages~~ — **done and verified.**
3. **Host the demo deck.** `docs/Space-Mission-Design-Game-demo.pdf` → Google
   Drive, set **Anyone with the link**. That is your **Link to Project Demo**,
   and it is the last link you need.
4. **Optional:** finish or discard the `v1.0` release draft. It is currently
   unpublished with no file attached, so it is invisible to the public either
   way. Notes are ready at `docs/release-notes-v1.0.md`.
5. Copy `index.html` to a USB stick as the venue fallback.

### Build checks before freeze

- [ ] Opens and completes a mission offline
- [ ] Opens on a second device
- [ ] A bad design (small rocket, big dish, launch next month) says **CANNOT
      LAUNCH** and gives reasons
- [ ] Collecting and never sending ends with the science stranded
- [ ] **PLAY AGAIN** starts clean
- [ ] Title screen → **DATA, SOURCES & CREDITS** opens and lists everything
- [ ] No Space Apps patches, no flags, no real names anywhere on screen

---

## PART 2 — The demo

### Rules

| | |
|---|---|
| Format | **Video ≤30 seconds** OR **≤7 slides** including title and intro slides. Pick one. |
| Hosting | **Not on the Space Apps site** — it takes JPG/PNG/GIF up to 10 MB but no video or documents. Host on YouTube, Drive or GitHub and paste one link. |
| Access | Public. No sign-in, no permission request. Test in a private window. |
| Language | Slides **must be English**. A video may be spoken in Portuguese **but must carry English subtitles**. |
| People | **No image, video, audio or likeness of anyone under 18.** |
| Limit | Over 30 seconds or over 7 slides = **not eligible for Global Judging.** |

### ✅ Recommended: the 7 slides

Safer tonight — no audio, no subtitles, no timing risk. Seven slides, English,
big visuals, few words.

| # | Slide | Content |
|---|---|---|
| 1 | **Title** | *Space Mission Design Game* · team name · all member names · challenge: Space Mission Design Game · NASA Space Apps 2026, São Paulo |
| 2 | **The problem** | "Children are taught that space is amazing. They are not taught that it is a budget." One line on who it is for: 1–4 players, ages 7–12. |
| 3 | **What you do** | Screenshot of a design step. The five decisions: launch window, power, two instruments, radio, rocket. |
| 4 | **The moment it teaches** | Screenshot of **BUILD & VERIFY refusing to launch**, with the reasons listed. Caption: "Too heavy for this rocket. That is a real design review." *This is your strongest slide — do not cut it.* |
| 5 | **NASA data made this possible** | Screenshot of a real CME event in play, plus the credits screen. Name DONKI (132 real events: real speed, half-angle, NASA class), the Image and Video Library (10 photos with NASA IDs), and NASA's six-step mission design process. |
| 6 | **The user experience** | Screenshot of the crew voting and of the Earth message arriving 19 minutes late. Caption: "Science only counts once it reaches Earth." |
| 7 | **What it becomes** | One offline HTML file → any classroom with no network. Next: more destinations, a teacher's sheet, Portuguese subtitles. |

### Alternative: the 30-second video

NASA's own model is 0:00 who you are and the challenge · 0:05 name it and the
problem · 0:10 how it works and the NASA data · 0:20 the future · 0:30 stop.

**76 words — about 30 seconds read at a normal pace. Time it. If you run over,
cut the last line.**

> **0:00** Team *[name]*, São Paulo. This is the Space Mission Design Game.
>
> **0:04** Children aged seven to twelve design a real mission — and find out why it fails.
>
> **0:09** Moon or Mars. Choose a launch window, a power source, two instruments, a radio, a rocket.
>
> **0:16** Break the mass or power budget and it will not launch — and it tells you why.
>
> **0:22** Real NASA storm data hits you in flight. Science only counts once it reaches Earth.
>
> **0:28** One file. No internet. Any classroom.

| Time | On screen |
|---|---|
| 0:00 | Title screen, then the mission vote |
| 0:04 | A crew picking Mars |
| 0:09 | The launch-window step with the orbit diagram |
| 0:16 | **BUILD & VERIFY refusing to launch**, reasons listed |
| 0:22 | A solar storm hitting, then the Earth message arriving late |
| 0:28 | The ending screen |

Record the **screen only**, not the room. Test a 10-second clip first and check
the text is readable at the size YouTube will show it.

---

## PART 3 — Every form field, drafted

Paste these, then edit in the team's own voice. Everything below is in English,
as required.

### Project Name

```
Space Mission Design Game
```

### High-Level Project Summary

```
The Space Mission Design Game is a browser game for 1 to 4 players, aged 7 to
12, that teaches real aerospace trade-offs by making players design a complete
mission and then fly it.

Players vote on a destination, then make five decisions that a real mission team
has to make: when to launch, where the power comes from, which two instruments
to carry, how the evidence gets back to Earth, and which rocket can lift it. A
design that breaks its mass, power, cost or launch-window limits CANNOT LAUNCH,
and the game names the limit it broke. In flight, the crew vote every phase
while real NASA space-weather data attacks the outpost, and science only counts
once it has been transmitted home: collect everything, send nothing, and the
mission fails.

It answers the challenge by refusing to let a player win without understanding
the trade-off. There is no free action, no infinite budget, and no way to skip
the physics. It runs from a single HTML file with no internet, no install and no
account, so it works in a classroom with no network.
```

### Link to Project Demo

```
[one link — the 7 slides or the 30-second video, hosted publicly, tested signed out]
```

### Link to Final Project

```
[the GitHub release URL for index.html]
```

### Detailed Project Description

```
WHAT IT DOES
The player runs a mission end to end, in the order a real mission team works:
define the mission, decide how to get there, decide how to collect the evidence,
decide how to deliver it to Earth, and come home.

1. DEFINE THE MISSION. Two real missions, voted on by the crew. Moon: harvest
helium-3, following the real $6.9M NASA contract awarded to Interlune in May
2026. Mars: recover the Sapphire Canyon core that Perseverance drilled in July
2024 and that NASA announced in Nature in September 2025 as a potential
biosignature — a sample still sitting on Mars because Mars Sample Return lost
its funding in January 2026. Six illustrated panels, each built on a real NASA
photograph, explain why we would go, what was actually found, what is still
disputed, and who pays for it.

2. DESIGN IT. Five steps, following NASA's own six-step mission design process.
Launch window (the 26-month Mars synodic period versus a Moon launch available
most weeks), power source (an MMRTG's steady 110 W against solar panels that
make more on a good day and nothing in a dust storm), two instruments from four,
communications, and the launch vehicle. Each option shows its mass, power, cost
and capability side by side, so the trade-off is visible rather than described.

3. BUILD AND VERIFY. The design is checked against mass, power, budget and
launch window. If it fails, it does not launch, and the game lists every limit
it broke and by how much. This is the moment the game exists for.

4. FLY IT. The crew vote on one action each phase. Power, life support and
shielding all decay whether you act or not. Solar storms arrive from 132 real
coronal mass ejections. Science collected is tracked separately from science
transmitted, and only transmitted science counts.

5. COME HOME. Eight different endings, each naming what to change next time.

HOW IT WORKS
One self-contained HTML file. Canvas 2D for the surface scenes, no framework, no
server, no build step, no account, no network. Every image, animation and data
record is embedded as base64, so the file runs from file:// offline. Tested at
360x640 through 1280x800 with no page scrolling during play.

BENEFITS AND GOALS
Most space education tells children that space is amazing. This teaches them
that it is a budget. A child who finishes one mission can explain why you cannot
launch to Mars on any day you like, why the heavier battery is sometimes the
right one, and why data sitting on a planet's surface is worth nothing. It is
designed to be handed to a teacher as a single file and used in a room with no
internet.

TOOLS AND LANGUAGES
HTML, CSS and vanilla JavaScript with the Canvas 2D API. Pixel art drawn by the
team in Pixilart and Construct. Playwright for automated testing across five
full playthroughs. Python and Node scripts for asset processing and for
simulating game balance before tuning it.
```

### Use of AI

```
AI was used, and here is exactly how.

The team chose the challenge, designed both missions, decided every game rule
and every balance figure, drew all the pixel art and animation, playtested the
game and made every creative decision.

AI-ASSISTED CODE: the game's code was written with an AI assistant working under
the team's direction. This is acknowledged here, in the project's README, and on
the game's own DATA, SOURCES & CREDITS screen, reachable from the title screen.

AI-ASSISTED IMAGES: two orbital diagrams (why a Mars launch must wait for its
transfer window, and why the Moon is reachable almost any week) were generated
as code with AI assistance. Both carry a visible "AI-ASSISTED DIAGRAM" watermark
in the corner of the image, and both are captioned in-game as drawn for this
game so they can never be mistaken for NASA photographs.

AI-GENERATED CREW PORTRAITS: the six astronaut character portraits are
AI-generated illustrations, commissioned and then edited by the team. Each
carries a visible "AI-GENERATED IMAGE" watermark, and the character-select
screen states in text that they are AI-generated, because the small thumbnails
used elsewhere in the game are too small for a legible watermark.

NOT AI-GENERATED: all pixel art, the rover, the astronaut animation, the landing
sequence and the user interface art were hand-drawn by the team in Pixilart and
Construct.

No AI-generated content in this project uses, contains or modifies any NASA
branding or design element. No NASA logo, Space Apps patch, mission identifier
or national flag appears in any image in this project; all were removed.
```

### NASA Data

```
DONKI — Space Weather Database Of Notifications, Knowledge, Information
https://api.nasa.gov/DONKI/CME
132 real coronal mass ejections recorded between 1 October and 14 November 2026.
This is not decoration: every solar storm in the game uses that event's real
speed (218-1048 km/s) to set radiation intensity, its real half-angle (10-46
degrees) to decide whether the hit is glancing, partial or direct, and NASA's
own S/C/O class, shown to the player as NASA records it. The deck of 132 is
shuffled per run, so no two missions face the same weather. Archived rather than
live, and labelled as archived in-game, because a browser game cannot hold an
API key safely and a rate-limited call would fail during judging.

NASA Image and Video Library
https://images-api.nasa.gov
Ten photographs, each displayed in-game with its title, date and NASA ID:
as17-145-22157 (Harrison Schmitt scooping lunar samples, Apollo 17),
art002e021278 (Earthset from Orion), KSC-20231121-PH-ULA01_0002 (Astrobotic
lander encapsulation), PIA26368 (the 'leopard spots' rock), PIA26344
(Perseverance selfie with Cheyava Falls), PIA24485 (the delta in Jezero Crater),
PIA26640 (PIXL finding vivianite and greigite), PIA23306 (Mars 2020's MMRTG),
PIA23214 (the Deep Space Network at Goldstone), KSC-20200730-PH-FMX01_0042 (Mars
2020 lifting off on an Atlas V). Each photograph is attached to the decision it
explains, not used as wallpaper.

"Design and Develop Science Missions" — Julie Levri, Flight Systems Engineer,
NASA Access to Space for All, Systems Engineering Webinar Series, 26 March 2025
https://www.nasa.gov/wp-content/uploads/2025/04/250323-design-and-develop-science-mission.pdf
The six steps across the top of every design screen are NASA's six steps:
Identify Need & Goals, Define Concept, Define Requirements, Design, Build &
Verify, Implement. BUILD & VERIFY summarises the player's mission back to them
in NASA's four mission segments: launch, space, ground and user.

CubeSat 101 — NASA CubeSat Launch Initiative
https://www3.nasa.gov/sites/default/files/atoms/files/nasa_csli_cubesat_101_508.pdf
Sets the mass and cost scales so the numbers a player sees are the right order
of magnitude.
```

### Space Agency Partner Data and Other References

```
ORBITAL MECHANICS AND PHYSICS USED IN THE GAME
- Earth orbits the Sun in 365 days, Mars in 687, so a low-energy alignment
  recurs about every 26 months. A Hohmann transfer takes about 259 days and
  needs about 3.6 km/s. Walter Hohmann, 1925.
- An MMRTG produces roughly 110 W and keeps producing it at night and through
  dust storms. Mars receives about 43% of the sunlight Earth does, before dust.
- Light travels at 299,792 km/s. Every message delay in the game is the real
  Earth-to-destination distance divided by that figure: about 1.3 seconds to the
  Moon, up to about 20 minutes to Mars.
- Kulcinski, Wittenberg and Schmitt, 1986 — the first paper linking lunar
  helium-3 to fusion power. Harrison Schmitt is the Apollo 17 astronaut in the
  photograph the player sees two steps earlier.

REAL EVENTS CITED IN THE GAME
- Opportunity, silenced 10 June 2018 by a planet-wide dust storm (attached to
  the solar-versus-nuclear power decision).
- Mars Climate Orbiter, 1999 — newtons versus pound-force (attached to the
  design verification step).
- NASA award to Interlune, May 2026, $6.9M, payload "Prospect Moon".
- Perseverance / Cheyava Falls / Sapphire Canyon, NASA and Nature, September
  2025, described in-game as a potential biosignature, not as proof.
- Mars Sample Return defunded, 23 January 2026.

TOOLS AND SOFTWARE
- Pixilart — all pixel art and animation, drawn by the team.
- Construct — the cockpit view, ship, buttons and astronaut sprite, made by
  the team.
- HTML, CSS, vanilla JavaScript, Canvas 2D API. No frameworks, no libraries, no
  third-party code is included in the final file.
- Playwright (automated testing), Python with Pillow and NumPy (image
  processing), Node.js (balance simulation). Development tools only; none ships
  in the submitted file.

IMAGES AND MEDIA
- All photographs are NASA, public domain, each listed above with its NASA ID.
- All pixel art, animation, the rover, the lander animation and the interface
  art are the team's own original work.
- The two orbital diagrams are AI-assisted and visibly watermarked.
- No stock photography, no third-party licensed art, no music, no sound.
- A Shutterstock-watermarked background that came with a template was
  identified and deliberately excluded from the build.

HONESTY NOTE
In-game outpost events (lunar night, dust storms, comms blackout, a rich
regolith seam, water ice) are written scenarios, not NASA records, and the game
never badges them as data. Only the DONKI space-weather events carry the
"REAL EVENT - ARCHIVED" badge.
```

### The two checkboxes

The form will not submit without both. You are confirming that you have read and
agree to the Project Submission Guide and the Participant Terms and Conditions,
and that the project is your team's **original work** with every external
resource listed in References and no copyrighted material you lack permission
for. The References field above is written to make both true. Then click
**Submit for Judging** — saving a draft is not entering.

---

## PART 4 — Final checks before you click

- [ ] All six members confirmed on the team page, same Local Event
- [ ] Challenge on the team page reads **Space Mission Design Game**
- [ ] Every form field filled, all in English
- [ ] Demo is ≤30 seconds or ≤7 slides
- [ ] Demo link and project link open **in a private window, signed out**
- [ ] AI declaration pasted into Use of AI
- [ ] References lists every tool and source
- [ ] No Space Apps patches, flags or real names in the build or the demo
- [ ] No profanity anywhere, including code comments
- [ ] Click **Submit for Judging**, reload, confirm it says submitted
- [ ] Screenshot the confirmation

## If something breaks at the last minute

Fall back to the offline file from Part 1. It is self-contained, so dead Wi-Fi
at the venue cannot touch it.

---

## How this project will be judged

Judges score holistically 1–5 on **Impact, Creativity, Validity, Relevance and
Presentation**, after a pass/fail check of the minimum requirements above.
Relevance explicitly rewards NASA data being *integral* rather than decorative —
which is why the NASA Data field is worth the length it has.

Local judges advance 1–3 projects per location as Global Nominees; those go to
NASA and partner-agency judges for Global Finalist, then to an executive
committee for ten Global Awards. **Best Mission Concept** ("the most plausible
concept and design") and **Best Storytelling** are the two this project is built
for.

## Reference documents in this folder

Archived from NASA Space Apps' own servers, because the live site is unreachable
from the build machine:

- `Final_Space_Apps_2025_Judging_Guidelines_for_web.pdf` — the minimum-requirements
  checklist and the 1–5 criteria
- `Space_Apps_2022_Project_Submission_Guide.pdf` — form fields and the pitch model
- `Space_Apps_2021_Project_Demo_Guide.pdf` — demo formats
- `Space_Apps_2022_Judging_and_Awards_Guide.pdf` — the award ladder

Year-specific details were supplied by the team lead from the live 2026 guide.
