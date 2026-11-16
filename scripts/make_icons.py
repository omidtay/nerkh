"""Draw the app icon (two overlapping coins) and write the PNG sizes the web app needs.

Run from the repo root:  python3 scripts/make_icons.py
"""
from pathlib import Path

from PIL import Image, ImageDraw

S = 1024
OUT = Path(__file__).resolve().parent.parent / "icons"


def lerp(a, b, t):
    return tuple(round(x + (y - x) * t) for x, y in zip(a, b))


def draw() -> Image.Image:
    img = Image.new("RGB", (S, S))
    px = ImageDraw.Draw(img)
    top, bottom = (22, 26, 36), (10, 12, 17)
    for y in range(S):
        px.line([(0, y), (S, y)], fill=lerp(top, bottom, y / (S - 1)))

    # Work at 4x and downsample for smooth edges.
    big = S * 4
    layer = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    r = int(big * 0.235)
    back = (int(big * 0.40), int(big * 0.42))
    front = (int(big * 0.60), int(big * 0.58))
    ring = int(big * 0.012)

    d.ellipse([back[0] - r, back[1] - r, back[0] + r, back[1] + r], fill=(38, 43, 58, 255))
    # Gap between the coins, in the background colour.
    g = r + int(big * 0.022)
    d.ellipse([front[0] - g, front[1] - g, front[0] + g, front[1] + g], fill=(15, 18, 25, 255))
    d.ellipse([front[0] - r, front[1] - r, front[0] + r, front[1] + r], fill=(61, 213, 152, 255))
    inner = int(r * 0.72)
    d.ellipse([front[0] - inner, front[1] - inner, front[0] + inner, front[1] + inner],
              outline=(24, 120, 84, 255), width=ring)

    layer = layer.resize((S, S), Image.LANCZOS)
    img.paste(layer, (0, 0), layer)
    return img


def main() -> None:
    OUT.mkdir(exist_ok=True)
    icon = draw()
    for name, size in [("icon-512.png", 512), ("icon-192.png", 192), ("apple-touch-icon.png", 180)]:
        icon.resize((size, size), Image.LANCZOS).save(OUT / name, optimize=True)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
