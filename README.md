# Everl mockups

Working prototypes for the Everl redesign. Everl is a social app for meeting people nearby, in person: flip a switch to "available" and people nearby with the same interests can see you.

Live at **https://mockups94.xyz/everl/**

| Path | What it is |
|---|---|
| `/` (`index.html`, `img/`) | The redesigned everl.com landing page |
| `/app/` | Tappable iPhone app prototype |
| `/logo/` | Final logo kit: SVG masters, PNGs, app icon, favicons, avatar, and `build.py` |
| `photos/` | Full-resolution photos for full-bleed use |

These are not production code. Each page is one self-contained `index.html` (vanilla JS, no build step). See [HANDOFF.md](HANDOFF.md) for the brand rules, what's approved and how the review works.

To run locally: `python3 -m http.server 8798` in this folder, then open `http://localhost:8798`.
