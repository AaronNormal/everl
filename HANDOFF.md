# Everl: design handoff

**For:** the next Claude (or designer) picking up the Everl app and everl.com redesign.
**Last updated:** 16 Nov 2026

Everl is a social app for meeting people nearby, in person. You flip a switch to "available", and people nearby with the same interests can see you. From there you meet up for a pint, padel, karaoke, a pub quiz and so on. The live product is a web app at everl.com/app. This folder holds the redesign: working prototypes of the app and the website, plus the final logo kit.

Neither prototype is production code. Each is one self-contained `index.html` (vanilla JS, no build step) that shows exactly how the real app should look and behave.

## What's in this folder

| Folder | What it is | How to open |
|---|---|---|
| `app/` | Live at https://mockups94.xyz/everl/app/. Tappable iPhone app prototype: splash, onboarding, Home, the go-available flow, match, meeting point, Rooms, You, Notifications | Double-click `app/index.html`, or serve the folder (see below) |
| `index.html`, `img/` (top level) | The redesigned everl.com landing page, live at https://mockups94.xyz/everl/ | Double-click `index.html` |
| `logo/` | Live at https://mockups94.xyz/everl/logo/. Final logo: SVG masters, PNGs, app icon, favicons, social avatar, and `build.py`, which regenerates every file | Open any SVG |
| `photos/` | Full-resolution Arcads photos (1536×2752 tall, 2752×1536 wide) | Images |

To view the app at iPhone size, use a local server from this folder:

```
python3 -m http.server 8798
```

Then open `http://localhost:8798/app/` in Safari on the iOS Simulator (iPhone 17).

Useful URL shortcuts:
- `?screen=splash` restarts from the welcome screen. `?mode=adult` opens Up for more (`&ready=1` skips its setup), `?screen=aq&mode=adult&aq=0` jumps to a setup question, `?verified=1` skips the age check.
- `?screen=home`, `?screen=rooms` or `?screen=you` jumps straight to a tab. Any other screen name works too, e.g. `?screen=area` or `?screen=codename`.
- `?photo=A` to `?photo=F` previews the other splash photos, if they're in `app/img`.

## Brand rules (agreed with the owner, don't break)

- **Logo:** an iOS switch turned on (green track, white knob on the right) next to lowercase "everl" in Outfit Bold, outlined, at −2.5% letter spacing.
  - Never put the lockup inside a box or tile. The tile is only for the app icon and avatar.
  - No dots, and nothing added to the switch.
- **Colours:**
  - Available green `#34C759`. It is used ONLY for the switch and for being available, never for buttons or ticks.
  - Midnight navy `#101A3C`, the brand colour, also used for selected states.
  - App: white `#FFFFFF` screens with Apple's cool grey `#F2F2F7` for controls, and ink `#121212` for text and primary buttons (changed 16 Nov 2026 after the UI audit; warm cream read as AI). The website keeps Paper `#F4F3EF`.
  - No uppercase labels, no ` · ` separators, no divider lines between rows. Use plain wording or a second line.
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

## Where things are (16 Nov 2026)

- **Live:** https://mockups94.xyz/everl/app/ (app), https://mockups94.xyz/everl/ (website), https://mockups94.xyz/everl/logo/ (logo kit). Hosted by GitHub Pages from the public repo `AaronNormal/everl` (branch `main`, root). A small home repo `AaronNormal/AaronNormal.github.io` owns the domain mockups94.xyz; DNS is at Porkbun.
- **Add to Home Screen:** the app has a web manifest, so on an iPhone it opens full screen from the home screen.
- **Two modes:** Social and Up for more (18+). The switch lives in **You → Mode**, never on Home (discretion).

### Approved screens, in flow order

1. **Splash:** padel photo, switch-first logo animation, Continue with Apple, Continue with email, "Already on Everl? Log in", tappable Terms and Privacy.
2. **How do you want to meet?** Apple Invites style: a bright blue Social card and a purple Up for more card, each with a tidy emoji pattern in the top half and a big white title. Copy is option C ("Real people near you, up for the same thing as you. Meet in person, not on a screen."). Line under Continue: "Everyone on Everl is a verified adult."
3. **Social setup:** interests, how you like to meet, where you live (Manchester live; Leeds and elsewhere get a waiting list), area, codename. Picks, ticks and progress use Social blue `#1E7BF2`.
4. **Up for more setup:** night-mode intro ("Meet someone nearby tonight", photo `app/img/upformore.jpg`, "Safety comes first" list, white button), the one-time age check, then one question per screen in a night look: gender, age, who you're looking for, ages, how far, how you like to start, what you want, role (single choice, only shown when relevant, never to straight pairings), boundaries. Then an optional "Want sharper matches?" step for ethnicity and orientation preferences, your orientation, vibe and kinks. Everything is editable later under Showing as → Your details.
5. **Codename:** a big avatar in the codename's colour with its animal emoji (Ochre Wren is an ochre circle with a bird), and a 🎲 Shuffle button. The same colour-and-animal avatars are used everywhere in the app.
6. **Home (Social):** "Going out in Northern Quarter ⌄" opens an area picker; Go available card; Tonight tiles; This week rows. Going available plays the "Light up" moment on a mint card.
7. **Up for more Home:** stays WHITE (the owner hated a dark version). Open to meeting card, Showing as, nudge setting, Everl+ list.
8. **Tab bar:** full-width frosted floating bar; Home, Rooms, You (Up for more has Home and You only).

### Not reviewed one by one yet

The meet request sheet, match screen, meeting point, Rooms, room detail, Notifications. The last audit (board: https://claude.ai/artifact/6dVj7uAFSbW4Ftd6iz5q1R) still has open medium and low items: room tiles too big, room detail About text cut off by the Join button, safety contact hidden on Meeting point, vague options on "How you like to meet", map pin colours, splash buttons over the players.

### Owner's taste (learned the hard way)

- Hates anything that looks AI-made: ` · ` separators, uppercase labels, divider lines, warm cream, card soup, frosted caption boxes, random emoji scatter, vague copy like "One match" or "Tonight" on its own, single words left on their own line.
- Hates orange. Hates dark backgrounds on everyday screens; night mode is only for the 18+ intro and questions.
- Choice screens use colour and icons or emoji, not photos. Photos only for single full-screen moments, and they must look real and candid, never corny (no candles).
- Wants it fun and colourful but Apple-clean. When stuck, ask "what would Apple do?" and look at Mobbin.
- Copy must say plainly what things are. Balance line breaks (`text-wrap: balance`).

## How the owner likes to work

- Show the change on the iPhone simulator, then say plainly what changed. Use short lists, no jargon.
- Raise issues one screen at a time and wait for "fix" or "next".
- Fix exactly what was asked. Suggest extras, but don't add them unasked.
- Show options side by side on a board (a claude.ai artifact with simulator screenshots) when there's a choice to make.
- Nothing goes live until the owner's message says exactly "ship it". After "ship it": commit with a clear message, publish to GitHub, and check the live page has the change.

## Still open

- Matching the brand colours for print, with a proofed print run.
- A trademark search on the name and logo.
- The real build: these prototypes are the spec. The production app's code lives in the owner's Everl repo, which wasn't available here.
