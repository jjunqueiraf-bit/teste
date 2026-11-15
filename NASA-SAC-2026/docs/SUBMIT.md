# Recording and posting the project

Everything in Part 2 and Part 3 of this file is taken from NASA Space Apps' own
published guides. **Read the "Where these rules come from" note at the bottom
before you rely on a number** — the live site was unreachable while this was
written, so the year-specific dates must be confirmed by the team.

Three parts: **save the build**, **record the demo**, **post the submission**.

> **The clock.** The portal closes at **23:59 on Sunday 15 November, São Paulo
> local time** — that is tonight. Your São Paulo Local Lead may set an earlier
> cutoff. Use whichever comes first and aim to be finished two hours before it.
> You can re-submit as many times as you like until it closes; only the last
> submission is judged. **So submit something early, then improve it.**

---

# ⚠️ Three things that must be fixed before you post

A judge checks these first. If a project fails any one of them it is scored
**1 (Poor) and not evaluated any further** — no appeal, no partial credit.

### 1. The six astronaut portraits must come out

The character art for Theo, Davi, Henrique, Caio, Nathan and Luca breaks three
separate rules at once:

- It is a **likeness of a person under 18**. The Terms & Conditions say demos
  and final projects may not include images, video, audio or other likeness of
  anyone under 18. Six recognisable faces are in the build right now.
- Each suit carries a **"NASA International Space Apps Challenge" patch**.
  AI-generated content "may not use, contain, or modify any NASA branding or
  design elements (such as the NASA logos, flags, or mission identifiers)."
  That patch is a mission identifier, and it is visibly distorted.
- They are **AI-generated images with no watermark**. AI-generated images and
  videos "must be amended to include a visible watermark indicating they are
  AI-generated."

**The fix:** swap the six portraits for generic pixel astronauts in the four
suit colours the team already drew (`art/crew/astro_anim_*.png`,
`art/crew/control.png` — no faces, no name tags, no patches), and replace the
first names with callsigns the players choose at the start. It is about fifteen
minutes of work. Keep the personal version as a private family build — it just
cannot be the one you submit or film.

### 2. The demo is **30 seconds**, not 60–90

An earlier version of this file said 60–90 seconds. That was wrong. The limit
is **a video of 30 seconds or less, OR a deck of 7 slides or fewer** (title and
ending slides count). Judges stop watching at 30 seconds. A 90-second video
fails the minimum check.

### 3. The README names the wrong challenge

`README.md` still says *"Junior Astronaut Mission Trainer"* and links to that
challenge page. You are submitting to **Space Mission Design Game**. "Responds
to the challenge selected" is a minimum requirement, and the judges read your
links. Change the title and the link before you paste the repo URL anywhere.

---

# PART 1 — Save the build

## The game is one file

Everything — code, the NASA photographs, your Construct and Pixilart artwork,
the 132 real coronal mass ejections — is inside:

```
NASA-SAC-2026/index.html
```

No internet, no install, no account. Double-click it and it runs.

## A. Save a copy you can hand over

1. Download `index.html` from GitHub (open the file, press **Download raw file**).
2. Rename it with the date: `mission-design-game_20261115_1800.html`.
3. Put it in a folder called `demo` on the laptop.
4. **Open it and play one full mission with the Wi-Fi switched off.** If it
   works from that folder offline, it will work for a judge.
5. Copy it to a second device or a USB stick.

## B. Push the history to GitHub

```
cd NASA-SAC-2026
git add -A
git commit -m "say what you changed"
git push
```

**Under-13s must not create GitHub accounts** — that is GitHub's rule, not
ours. An adult pushes on the team's behalf.

## C. Cut a release judges can download

GitHub → **Releases → Draft a new release → tag `v1.0` → attach `index.html`
→ Publish**. One permanent link to a file that cannot change afterwards.

## D. Last checks on the build

- [ ] Opens and completes a mission **offline**
- [ ] Opens on a **second device**
- [ ] A deliberately bad design (small rocket, big dish, launch next month)
      says **CANNOT LAUNCH** and gives reasons
- [ ] Collecting and never sending ends with the science stranded
- [ ] **PLAY AGAIN** starts clean
- [ ] No faces, names or Space Apps patches anywhere on screen

---

# PART 2 — Record the demo

## The rules, exactly

| | |
|---|---|
| Format | **Video ≤ 30 seconds** OR **slide deck ≤ 7 slides** (pick one) |
| Where it lives | **Not on the Space Apps site.** The portal does not accept video or document uploads. Host it on YouTube, Google Drive, GitHub, Dropbox or OneDrive and paste a link. |
| Access | **Publicly accessible.** No sign-in, no permission request, no registration. Test it in a private browsing window. |
| Language | Slides **must be in English**. A video may be spoken in any language **but must carry English subtitles**. |
| People | No images, video, audio or likeness of anyone **under 18**. |
| AI content | Declared; AI images/video need a visible watermark; AI code/data acknowledged in the descriptive text. No NASA branding inside AI-generated content. |
| Content | No profanity or inappropriate language. |

**One link only** in the Demo field — you are choosing one format, not both.

## How to handle the narration

The children cannot be heard or seen in the demo; a voice is a likeness. Two
clean ways round it, in order of preference:

1. **No voice at all.** Screen recording of the game with **English text
   captions burned on**. The game's own screens are already in English, it
   sidesteps the subtitle rule completely, and it is the fastest to produce.
2. **An adult narrates in English.** Also fine. If the adult narrates in
   Portuguese, English subtitles are then mandatory.

Either way the children's work is still front and centre — it is their art,
their rules and their design decisions on screen. Credit them by first name in
the *written* Hackathon Journey field, which is not a demo and not a likeness.

## A 30-second script that fits

NASA's own pitch model ("30 Seconds of Glory") splits the time like this:
0:00 who you are and which challenge · 0:05 name the solution and the problem ·
0:10 how it works, show it, say which space-agency data made it possible ·
0:20 what it could become · 0:30 stop.

Here is that model filled in. It is **76 words**, which is about 30 seconds read
at a normal pace. Time yourself; if you run over, cut the last line first.

> **0:00** Team *[your team name]*, São Paulo. This is the Space Mission Design Game.
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

### What to show under each line

| Time | On screen |
|---|---|
| 0:00 | Title screen, then the mission vote |
| 0:04 | A crew picking Mars |
| 0:09 | The launch-window step, with the orbit diagram visible |
| 0:16 | **BUILD & VERIFY refusing to launch**, reasons listed — this is the single best shot you have |
| 0:22 | A solar storm hitting, then the Earth message arriving late |
| 0:28 | The ending screen |

Record the **screen only**, not the room. Do a 10-second test clip and play it
back before you record the real one — check the text is readable at the size
YouTube will show it.

## If you choose slides instead

Seven slides, English, strong visuals, few words:

1. Team name, challenge (**Space Mission Design Game**), member callsigns
2. The problem and who it is for
3. How the game works — the five design decisions
4. A screenshot of BUILD & VERIFY refusing to launch
5. The NASA data, named: DONKI, the Image and Video Library, the mission-design
   process
6. What a player walks away understanding
7. What it becomes with more time

Slides are the safer choice if you are short on time tonight — no audio, no
subtitles, no timing risk.

---

# PART 3 — Post the submission

You submit on **your team page** at spaceappschallenge.org, under the
**Project** tab → **Edit Project**. Fill in the fields the site actually shows
you; the list below is what to have written and ready to paste.

## The form fields

**Project Title**
> Space Mission Design Game — design the mission, then find out why it fails

**High-Level Project Summary** *(what you built, how it answers the challenge, why it matters)*
> A mission-design game for 1 to 4 players, aged 7 to 12. Players choose a
> destination, then design the whole mission: when to launch, where the power
> comes from, which two instruments to carry, how the evidence gets home, and
> which rocket can lift it. A design that breaks its mass, power, cost or
> launch-window limits cannot launch — and the game explains which limit it
> broke. In flight the crew vote each phase, and science only counts once it has
> been transmitted to Earth: collect everything, send nothing, and the mission
> fails. It runs from a single file with no internet, so it works in a classroom
> with no network.

**Link to Final Project** — the GitHub release from Part 1C, or the repo.
Must open with no login.

**Link to Project "Demo"** — one link, the video or the deck. Must open with no
login. **Test it signed out.**

**Detailed Project Description** *(what it does, how it works, tools used)*
Draw from `README.md` and `docs/MISSIONS.md`. Say plainly: single HTML file,
Canvas 2D, no framework, no server; pixel art drawn by the team in Pixilart and
Construct; NASA photographs embedded with their NASA IDs.

**Space Agency Data** *(the field that decides Global Award eligibility)*
Paste from `docs/NASA-SOURCES.md`. Name each one and say what it changed:
> - **DONKI (api.nasa.gov/DONKI/CME)** — 132 real coronal mass ejections from
>   1 Oct–14 Nov 2026. Each in-game storm uses that event's real speed
>   (218–1048 km/s), real half-angle (10–46°) and NASA's own S/C/O class.
> - **NASA Image and Video Library (images-api.nasa.gov)** — seven credited
>   photographs shown with title, date and NASA ID, including PIA26368 (the
>   "leopard spots" rock) and as17-145-22157 (Apollo 17 scooping regolith).
> - **"Design and Develop Science Missions", NASA Access to Space for All,
>   26 Mar 2025** — the six-step design process is the progress bar across the
>   top of the game; the four mission segments are how BUILD & VERIFY reports
>   back.
> - **CubeSat 101, NASA CubeSat Launch Initiative** — anchors the mass and cost
>   scales so the numbers are the right order of magnitude.

**Hackathon Journey** *(what you learned, what went wrong, who to thank)*
This is where the children's names belong — it is written text, not a likeness.
Say what surprised them: that you cannot fly to Mars on any day you like, that
the heavier battery is the one that survives a dust storm, that data sitting on
the surface is worth nothing.

**References** *(everything you used — code, text, images, even open ones)*
Every NASA source above, plus Pixilart and Construct, plus the AI declaration.
If you cannot show you have permission to use something, take it out.

## The AI declaration

Required, and judged. Put it in the Detailed Project Description **and** in
References so nobody misses it:

> The team designed the game, chose both missions, drew the pixel art and the
> animations, and decided every rule. The game's code was written with an AI
> assistant working under the team's direction, and this is declared here as
> required. All NASA data and sources used are listed in the References field.

If any image in the final build is AI-generated, it needs a **visible
watermark** saying so — which is one more reason the six portraits should go.

## The two boxes you must tick

The form will not submit without them. You are confirming, in substance:

1. You have read and agree to the Project Submission Guide and the Participant
   Terms and Conditions.
2. The project is your team's **original work**, every external resource —
   code, text, images, even open-source ones — is listed in **References**, and
   you have used no copyrighted material you do not have permission for.

Tick those honestly. The Shutterstock background from the Construct pack is
exactly the kind of thing box 2 is about: it is licensed to someone else and
must not be in the build.

## Team rules

- Everyone must be **registered and identified on the team's Project Page**.
- **Maximum six** team members, minimum one. You have six — that is the cap.
- You **cannot add members after submission closes**. Do this first, not last.

## Final checklist before you press Submit

- [ ] The six face portraits and the Space Apps patches are **out of the build
      and out of the demo**
- [ ] The README names **Space Mission Design Game**
- [ ] Demo is **≤ 30 seconds** or **≤ 7 slides**
- [ ] Demo link and project link both open **in a private window, signed out**
- [ ] Everything on the page and in the linked materials is **in English**
      (video in Portuguese → English subtitles)
- [ ] All six members registered and listed on the Project Page
- [ ] AI use declared in writing
- [ ] References lists every source, including Pixilart and Construct
- [ ] No profanity anywhere, including in the code comments judges might read
- [ ] Press **Submit** — then **reload the page and confirm it says submitted,
      not saved**. A draft is not an entry.
- [ ] Screenshot the confirmation
- [ ] Confirm the **São Paulo cutoff** with your Local Lead as well as the
      global one

## After you submit

Local judges pick **1–3 projects per location** to advance as *Global
Nominees*. Those go to NASA and partner-agency judges, who pick *Global
Finalists*, who go to an executive committee for **10 Global Awards**: Best Use
of Science, Best Use of Data, Best Use of Technology, Galactic Impact, Best
Mission Concept, Most Inspirational, Best Storytelling, Global Connection,
Art & Technology, and Local Impact.

Judges score **holistically 1–5** on five criteria: **Impact, Creativity,
Validity, Relevance, Presentation**. Relevance explicitly rewards NASA data
being *integral* to the project rather than decorative — which is why the
Space Agency Data field is worth writing carefully.

**Best Mission Concept** ("the most plausible concept and design") and **Best
Storytelling** are the two this project is built to win. Say so, in those words,
in the Detailed Project Description.

## If something breaks at the last minute

Fall back to the saved file from Part 1A. It is self-contained and offline, so
a dead Wi-Fi link at the venue cannot touch it.

---

## Where these rules come from

`www.spaceappschallenge.org` could not be reached from the machine this was
written on — DNS and TLS both fail there, through every route tried. Nothing
below was invented or recalled from memory; each rule comes from a document
actually retrieved and read:

| Source | What it gave |
|---|---|
| **Space Apps 2025 Judging Guidelines** (NASA Space Apps S3) | The minimum-requirements checklist: English, responds to the challenge, **≤ 7 slides or ≤ 30 seconds**, links password-unrestricted, NASA data used, AI declared with the branding and watermark rules. The 1–5 criteria and the ten awards. |
| **Space Apps 2022 Project Submission Guide** (NASA Space Apps S3) | The exact project-form fields, the two agreement checkboxes, the six-member cap, the file-hosting rules, the "30 Seconds of Glory" pitch model. |
| **Space Apps 2021 Project "Demo" Guide** (NASA Space Apps S3) | Demo format rules and the seven-slide content outline. |
| **github.com/nasa/spaceapps** | Confirms registration and Terms & Conditions apply; the repo itself is only a README and Discussions — no submission rules live there. |
| **The GO Team message to participants** | Names the current guides: Project Submission, Judging and Awards, Participant FAQs, Space Apps Connect. |

**What the team must still confirm on the live site**, because it is
year-specific and the 2026 pages could not be opened:

1. The exact 2026 São Paulo submission deadline.
2. Whether the 2026 form fields match the list above.
3. The challenge's own **Resources tab** — check at least one NASA source you
   used is listed there.
4. The current Participant Terms and Conditions, especially the under-18 clause.
5. Whether the Brazilian Space Agency (AEB) is a 2026 Space Agency Partner, in
   which case Brazilian open data would also count toward eligibility.

Open `https://www.spaceappschallenge.org/resources/project-submission-guide/`
and the 2026 challenge page on a phone and check these five. It takes five
minutes and it is the difference between a valid entry and a wasted weekend.
