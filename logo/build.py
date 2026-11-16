"""Everl logo kit generator. One unit H = switch height; everything else derives from it."""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

GREEN, NAVY, WHITE, PAPER = "#34C759", "#101A3C", "#FFFFFF", "#F4F3EF"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "final")
FONT = TTFont(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../everl-logo/v3/outfit-700.woff2"))
GS, CM = FONT.getGlyphSet(), FONT.getBestCmap()

# Switch proportions (iOS switch: 51x31 track, 27 knob, 2 inset)
W_RATIO = 51 / 31          # track width / height
KNOB_R = 0.4194            # knob radius / height  (inset ~0.081H)
XH_RATIO = 0.70            # wordmark x-height / switch height
GAP = 0.36                 # space between switch and wordmark / H
TRACK = -0.025             # letter spacing, em


def f(n):
    return f"{n:.2f}".rstrip("0").rstrip(".")


def switch(x, y, h, track=GREEN, knob=WHITE, mono=None):
    w = h * W_RATIO
    r, cx, cy = h * KNOB_R, x + w - h / 2, y + h / 2
    if mono:  # one colour: knob punched out of the track
        k = (f"M{f(cx - r)} {f(cy)}a{f(r)} {f(r)} 0 1 0 {f(2*r)} 0a{f(r)} {f(r)} 0 1 0 {f(-2*r)} 0Z")
        t = (f"M{f(x + h/2)} {f(y)}H{f(x + w - h/2)}a{f(h/2)} {f(h/2)} 0 0 1 0 {f(h)}"
             f"H{f(x + h/2)}a{f(h/2)} {f(h/2)} 0 0 1 0 {f(-h)}Z")
        return f'<path fill="{mono}" fill-rule="evenodd" d="{t}{k}"/>'
    return (f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" rx="{f(h/2)}" fill="{track}"/>'
            f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{knob}"/>')


def word(x0, base, h):
    """'everl' outlined, x-height = XH_RATIO*h. Returns (path d, width, top)."""
    size = XH_RATIO * h / (FONT["OS/2"].sxHeight / 1000)
    s, x, parts, bp = size / 1000, x0, [], BoundsPen(GS)
    first_lsb = None
    for ch in "everl":
        g = GS[CM[ord(ch)]]
        b = BoundsPen(GS); g.draw(b)
        if first_lsb is None:
            first_lsb = b.bounds[0] * s
            x -= first_lsb          # start ink exactly at x0
        pen = SVGPathPen(GS)
        g.draw(TransformPen(pen, (s, 0, 0, -s, x, base)))
        parts.append(pen.getCommands())
        last_right = x + b.bounds[2] * s
        x += g.width * s + TRACK * size
    top = base - 726 * s
    return " ".join(parts), last_right - x0, top, base + 11 * s


def svg(vb, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}"><title>{title}</title>{body}</svg>\n')


def save(name, content):
    p = os.path.join(OUT, name)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(content)


H = 100
# ---------- Horizontal lockup: switch bottom sits on the baseline ----------
d, ww, top, desc = word(0, 0, H)
sw_w = H * W_RATIO
wx = sw_w + GAP * H
d, ww, top, desc = word(wx, 0, H)
y0, y1 = min(top, -H), max(desc, 0)
vb_h = f"0 {f(y0)} {f(wx + ww)} {f(y1 - y0)}"
for suf, wc, sw in [("", NAVY, dict()), ("-reversed", WHITE, dict()),
                    ("-mono-navy", NAVY, dict(mono=NAVY)), ("-mono-white", WHITE, dict(mono=WHITE)),
                    ("-black", "#141414", dict(mono="#141414"))]:
    save(f"lockup/everl-horizontal{suf}.svg",
         svg(vb_h, switch(0, -H, H, **sw) + f'<path fill="{wc}" d="{d}"/>', f"Everl{suf.replace('-', ' ')}"))

# ---------- Stacked lockup: switch centred above the wordmark ----------
H2 = 100
d2, ww2, top2, desc2 = word(0, 0, H2)
sw2 = H2 * W_RATIO
total_w = max(ww2, sw2)
gap_v = 0.5 * H2
sy = top2 - gap_v - H2
for suf, wc, sw in [("", NAVY, dict()), ("-reversed", WHITE, dict()),
                    ("-mono-navy", NAVY, dict(mono=NAVY)), ("-mono-white", WHITE, dict(mono=WHITE))]:
    body = switch((total_w - sw2) / 2, sy, H2, **sw) + \
        f'<g transform="translate({f((total_w - ww2) / 2)} 0)"><path fill="{wc}" d="{d2}"/></g>'
    save(f"lockup/everl-stacked{suf}.svg",
         svg(f"0 {f(sy)} {f(total_w)} {f(desc2 - sy)}", body, f"Everl stacked{suf.replace('-', ' ')}"))

# ---------- Wordmark only ----------
d3, ww3, top3, desc3 = word(0, 0, H)
for suf, c in [("-navy", NAVY), ("-white", WHITE)]:
    save(f"wordmark/everl-wordmark{suf}.svg",
         svg(f"0 {f(top3)} {f(ww3)} {f(desc3 - top3)}", f'<path fill="{c}" d="{d3}"/>', "Everl wordmark"))

# ---------- Symbol (256 canvas, optically centred) ----------
SH = 256 * 0.78 / W_RATIO          # switch fills 78% of the width
sx, sy_ = (256 - SH * W_RATIO) / 2, (256 - SH) / 2
save("symbol/everl-symbol.svg", svg("0 0 256 256", switch(sx, sy_, SH), "Everl symbol"))
save("symbol/everl-symbol-mono-navy.svg", svg("0 0 256 256", switch(sx, sy_, SH, mono=NAVY), "Everl symbol navy"))
save("symbol/everl-symbol-mono-white.svg", svg("0 0 256 256", switch(sx, sy_, SH, mono=WHITE), "Everl symbol white"))
save("symbol/everl-symbol-tile.svg",
     svg("0 0 256 256", f'<rect width="256" height="256" rx="57" fill="{NAVY}"/>' + switch(sx, sy_, SH), "Everl symbol tile"))

# ---------- App icon 1024 (full bleed square; iOS applies the mask) ----------
AH = 1024 * 0.88 / W_RATIO         # option B: switch = 88% of icon width
ax, ay = (1024 - AH * W_RATIO) / 2, (1024 - AH) / 2 - 1024 * 0.008   # tiny lift for optical centre
save("app-icon/everl-app-icon-1024.svg",
     svg("0 0 1024 1024", f'<rect width="1024" height="1024" fill="{NAVY}"/>' + switch(ax, ay, AH), "Everl app icon"))

# ---------- Profile picture: circle-safe, switch 70% so it clears the crop ----------
PH = 1024 * 0.70 / W_RATIO
px, py = (1024 - PH * W_RATIO) / 2, (1024 - PH) / 2
save("social/everl-avatar-source.svg",
     svg("0 0 1024 1024", f'<rect width="1024" height="1024" fill="{NAVY}"/>' + switch(px, py, PH), "Everl avatar"))

# ---------- Small-size cut for favicons (16-32 px): bigger switch, thicker inset ----------
FH = 256 * 0.86 / W_RATIO
fx, fy = (256 - FH * W_RATIO) / 2, (256 - FH) / 2
w, h = FH * W_RATIO, FH
r, cx, cy = h * 0.37, fx + w - h / 2, fy + h / 2   # smaller knob = wider green ring, reads at 16 px
save("symbol/everl-symbol-small.svg", svg(
    "0 0 256 256",
    f'<rect width="256" height="256" rx="48" fill="{NAVY}"/>'
    f'<rect x="{f(fx)}" y="{f(fy)}" width="{f(w)}" height="{f(h)}" rx="{f(h/2)}" fill="{GREEN}"/>'
    f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{WHITE}"/>', "Everl favicon"))
print("built", sum(len(fs) for _, _, fs in os.walk(OUT)), "files")
