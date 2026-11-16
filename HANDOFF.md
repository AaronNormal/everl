# Everl: design handoff

**For:** the next Claude (or designer) picking up the Everl app and everl.com redesign.
**Last updated:** 16 Nov 2026

Everl is a social app for meeting people nearby, in person. You flip a switch to "available", and people nearby with the same interests can see you. From there you meet up for a pint, padel, karaoke, a pub quiz and so on. The live product is a web app at everl.com/app. This folder holds the redesign: working prototypes of the app and the website, plus the final logo kit.

Neither prototype is production code. Each is one self-contained `index.html` (vanilla JS, no build step) that shows exactly how the real app should look and behave.

## What's in this folder

| Folder | What it is | How to open |
|---|---|---|
| `app/` | Live at https://mockups94.xyz/app/. Tappable iPhone app prototype: splash, onboarding, Home, the go-available flow, match, meeting point, Rooms, You, Notifications | Double-click `app/index.html`, or serve the folder (see below) |
| `index.html`, `img/` (top level) | The redesigned everl.com landing page, live at https://mockups94.xyz | Double-click `index.html` |
| `logo/` | Live at https://mockups94.xyz/logo/. Final logo: SVG masters, PNGs, app icon, favicons, social avatar, and `build.py`, which regenerates every file | Open any SVG |
| `photos/` | Full-resolution Arcads photos (1536×2752 tall, 2752×1536 wide) | Images |

To view the app at iPhone size, use a local server from this folder:

```
python3 -m http.server 8798
```

Then open `http://localhost:8798/app/` in Safari on the iOS Simulator (iPhone 17).

Useful URL shortcuts:
- `?screen=home`, `?screen=rooms` or `?screen=you` jumps straight to a tab.
- `?photo=A` to `?photo=F` previews the other splash photos, if they're in `app/img`.

## Brand rules (agreed with the owner, don't break)

- **Logo:** an iOS switch turned on (green track, white knob on the right) next to lowercase "everl" in Outfit Bold, outlined, at −2.5% letter spacing.
  - Never put the lockup inside a box or tile. The tile is only for the app icon and avatar.
  - No dots, and nothing added to the switch.
- **Colours:**
  - Available green `#34C759`. It is used ONLY for the switch and for being available, never for buttons or ticks.
  - Midnight navy `#101A3C`, the brand colour, also used for selected states.
  - Paper `#F4F3EF` (background) and ink `#121212` (text and primary buttons).
- **App icon:** a full-bleed navy square with the switch filling 88% of the width (option B). Profile avatars use 70%.
- **Type:**
  - System font for everything (SF Pro, falling back to Inter Tight or Inter).
  - Outfit only inside the wordmark, because the owner felt Outfit headlines looked like thegen.app.
  - Scale: 34/28/22/17/15/13/11.
- **Spacing:** 4/8/12/16/20/24 only.
- **Tone:** professional and Apple-level, with no puns. Copy must be instantly clear ("Available", "Accept", "Continue").
- **Photos:**
  - AI photos are only for full-bleed moments (splash, website hero, ads). They must look like real 35mm film: candid, natural skin, mixed realistic clothing, framed so you can see the activity.
  - Never use AI photos on in-app cards. Cards use the fun flat-colour emoji pattern tiles.
- **Motion:** calm and quick. The splash opens with only the switch (off, centred). It flicks on, the logo glides left as "everl" fades in, then the tagline appears. The photo never animates.

## Screens: where the review got to

The owner is walking through the app screen by screen on the simulator. Done and approved, in order:

1. **Splash:** padel photo, switch-first logo animation.
2. **What are you looking for?** Social or Adult cards with line icons and a navy tick, and an age-check card above Continue.
3. **What are you into?** Search with add-your-own, 9 popular chips, and "Show all 28". The interest list matches the original everl.com app.
4. **How you like to meet (optional):** What you're after, the vibe you want, and must-haves behind a link. Skip sits in the top bar, and nothing is pre-selected. The wording comes from the original app.

**Next up:** the area screen (step 4 of 5), then codename, Home, go available, the request sheet, match, meeting point, Rooms, room detail, You and Notifications. These were all already polished in an earlier pass (nine fixes), but they haven't had the owner's one-by-one review yet.

**Open suggestion, not yet decided:** change the splash buttons to "Continue with Apple" (main), "Continue with email" (secondary) and "I already have an account" (text link). Ask the owner before doing it.

## How the owner likes to work

- Show the change on the iPhone simulator, then say plainly what changed. Use short lists, no jargon.
- Raise issues one screen at a time and wait for "fix" or "next".
- Fix exactly what was asked. Suggest extras, but don't add them unasked.
- Publish an updated version after each approved change, and keep the Desktop copy in sync.

## Still open

- Matching the brand colours for print, with a proofed print run.
- A trademark search on the name and logo.
- The real build: these prototypes are the spec. The production app's code lives in the owner's Everl repo, which wasn't available here.
