"""Render the 15s vertical "Make the Turn" ad for Caddie Social.

Usage: python3 render.py <assets_dir> <fonts_dir> <out.mp4>
Frames are drawn with Pillow and piped to ffmpeg (H.264, 1080x1920, 30fps).
"""
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ASSETS, FONTS, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
W, H, FPS, DUR = 1080, 1920, 30, 15.0

GREEN = (30, 74, 50)
GOLD = (212, 175, 55)
WHITE = (247, 248, 244)

front = Image.open(f"{ASSETS}/hat-front.jpg").convert("RGB")
side = Image.open(f"{ASSETS}/hat-three-quarter.jpg").convert("RGB")


def font(name, size):
    return ImageFont.truetype(f"{FONTS}/{name}", size)


F_BIG = font("BarlowCondensed-Bold.ttf", 230)
F_MED = font("BarlowCondensed-Bold.ttf", 120)
F_LINE = font("BarlowCondensed-SemiBold.ttf", 96)
F_MONO = font("PlexMono.ttf", 38)
F_CTA = font("BarlowCondensed-Bold.ttf", 64)


def ease(x):
    x = max(0.0, min(1.0, x))
    return 1 - (1 - x) ** 3


def prog(t, start, length):
    return ease((t - start) / length)


def cover(img, zoom, cx, cy):
    """Crop img to a W:H window scaled by zoom, centered near (cx, cy) in source pixels."""
    sw, sh = img.size
    base = max(W / sw, H / sh)
    scale = base * zoom
    cw, ch = W / scale, H / scale
    x0 = min(max(cx - cw / 2, 0), sw - cw)
    y0 = min(max(cy - ch / 2, 0), sh - ch)
    return img.resize((W, H), Image.LANCZOS, box=(x0, y0, x0 + cw, y0 + ch))


def shade(img, top=0.0, bottom=0.0):
    """Darken top and/or bottom with a vertical gradient so text stays readable."""
    overlay = Image.new("L", (1, H))
    for y in range(H):
        a = 0.0
        if top:
            a = max(a, top * max(0.0, 1 - y / (H * 0.42)))
        if bottom:
            a = max(a, bottom * max(0.0, (y - H * 0.5) / (H * 0.5)))
        overlay.putpixel((0, y), int(255 * a))
    mask = overlay.resize((W, H))
    return Image.composite(Image.new("RGB", (W, H), (8, 18, 12)), img, mask)


def text(draw, xy, s, f, fill, alpha=1.0, anchor="la"):
    if alpha <= 0:
        return
    r, g, b = fill
    draw.text(xy, s, font=f, fill=(r, g, b, int(255 * alpha)), anchor=anchor)


def layer(base, fn):
    over = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    fn(ImageDraw.Draw(over))
    return Image.alpha_composite(base.convert("RGBA"), over).convert("RGB")


# Precompute shading masks per scene (gradients are static).
def scene1(t):
    z = 1.0 + 0.12 * (t / 4.0)
    img = shade(cover(front, z, 620, 620), top=0.55, bottom=0.85)

    def draw(d):
        a = prog(t, 0.3, 0.6)
        text(d, (80, 170), "HOLE 9  →  HOLE 10", F_MONO, GOLD, a)
        for i, line in enumerate(["MAKE THE", "TURN."]):
            p = prog(t, 0.7 + i * 0.35, 0.7)
            y = 1360 + i * 215 + int(60 * (1 - p))
            text(d, (80, y), line, F_BIG, WHITE if i == 0 else GOLD, p)
    return layer(img, draw)


def scene2(t):
    p = t / 4.0
    img = shade(cover(side, 1.08, 520 + 220 * p, 700), bottom=0.9)
    lines = ["PERFORATED CROWN.", "ROPE FRONT.", "3D PUFF LOGO."]

    def draw(d):
        for i, line in enumerate(lines):
            a = prog(t, 0.35 + i * 0.7, 0.5)
            y = 1420 + i * 125 + int(40 * (1 - a))
            if a > 0:
                d.rectangle((80, y + 30, 104, y + 54), fill=GOLD + (int(255 * a),))
            text(d, (130, y), line, F_LINE, WHITE, a)
    return layer(img, draw)


def scene3(t):
    z = 1.3 + 0.12 * (t / 3.5)
    img = shade(cover(front, z, 625, 600), top=0.8)

    def draw(d):
        for i, line in enumerate(["EVERY ROUND", "NEEDS A SOCIAL."]):
            a = prog(t, 0.3 + i * 0.4, 0.6)
            text(d, (W // 2, 170 + i * 135 + int(30 * (1 - a))), line, F_MED,
                 WHITE if i == 0 else GOLD, a, anchor="ma")
    return layer(img, draw)


# End card: green field, framed product photo, wordmark, CTA.
END_PHOTO = cover(front, 1.0, 640, 700).crop((90, 330, 990, 1230)).resize((760, 760), Image.LANCZOS)
END_MASK = Image.new("L", (760, 760), 0)
ImageDraw.Draw(END_MASK).rounded_rectangle((0, 0, 759, 759), radius=40, fill=255)


def scene4(t):
    img = Image.new("RGB", (W, H), GREEN)
    p = prog(t, 0.0, 0.8)
    py = 190 + int(50 * (1 - p))
    photo = END_PHOTO.copy()
    if p < 1:
        photo = Image.blend(Image.new("RGB", photo.size, GREEN), photo, p)
    img.paste(photo, ((W - 760) // 2, py), END_MASK)

    def draw(d):
        a = prog(t, 0.5, 0.7)
        text(d, (W // 2, 1030), "CADDIE SOCIAL", F_MED, WHITE, a, anchor="ma")
        b = prog(t, 0.8, 0.6)
        text(d, (W // 2, 1185), "EVERY ROUND NEEDS A SOCIAL", F_MONO, GOLD, b, anchor="ma")
        c = prog(t, 1.2, 0.6)
        text(d, (W // 2, 1440), "MAKE THE TURN.", F_MED, WHITE, c, anchor="ma")
        e = prog(t, 1.7, 0.5)
        if e > 0:
            bw, bh = 640, 120
            x0, y0 = (W - bw) // 2, 1640 + int(30 * (1 - e))
            d.rounded_rectangle((x0, y0, x0 + bw, y0 + bh), radius=60, fill=GOLD + (int(255 * e),))
            text(d, (W // 2, y0 + 26), "SHOP THE ROPE HAT", F_CTA, GREEN, e, anchor="ma")
    return layer(img, draw)


SCENES = [(0.0, 4.0, scene1), (4.0, 8.0, scene2), (8.0, 11.5, scene3), (11.5, 15.0, scene4)]
XF = 0.45  # crossfade seconds


def frame(t):
    for i, (s, e, fn) in enumerate(SCENES):
        if s <= t < e or (i == len(SCENES) - 1 and t >= s):
            cur = fn(t - s)
            if i > 0 and t - s < XF:
                ps, pe, pfn = SCENES[i - 1]
                prev = pfn(t - ps)
                return Image.blend(prev, cur, (t - s) / XF)
            return cur


ff = subprocess.Popen([
    "ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
    "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
    "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
    "-movflags", "+faststart", OUT,
], stdin=subprocess.PIPE)
n = int(DUR * FPS)
for k in range(n):
    ff.stdin.write(frame(k / FPS).tobytes())
ff.stdin.close()
ff.wait()
print("wrote", OUT, n, "frames")
