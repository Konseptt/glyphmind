"""Render the 12 Egyptian-hieroglyph stimuli used by GLYPHMIND as PNGs.

Each PNG is named after its Gardiner-style id (D010.png, D021.png, ...) so the
filenames match the `Stimulus` column in the .xlsx export. Drop the resulting
`stim/` folder next to your E-Prime experiment file and reference
`stim/[Stim].png` from your ImageDisplay object.

Run with the project venv:
    .venv/bin/python glyph.py
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
FONT_PATH = HERE / "fonts" / "NotoSansEgyptianHieroglyphs-Regular.ttf"
OUT_DIR = HERE / "stim"
OUT_DIR.mkdir(exist_ok=True)

SIZE = 400
BG = (32, 22, 12)        # dark warm corridor tone
FG = (245, 192, 82)      # gold ink
FONT_SIZE = 256

GLYPHS = [
    ("D010", 0x13080),  # Eye
    ("D021", 0x1308B),  # Mouth
    ("D036", 0x1309D),  # Hand
    ("G017", 0x13153),  # Owl
    ("H006", 0x13184),  # Feather
    ("I009", 0x13191),  # Horned viper
    ("I010", 0x13193),  # Cobra
    ("N035", 0x13216),  # Water
    ("N014", 0x131FC),  # Star
    ("X001", 0x133CF),  # Loaf
    ("N005", 0x131F3),  # Sun
    ("R011", 0x132BD),  # Djed pillar
]

if not FONT_PATH.exists():
    raise SystemExit(
        f"Missing font: {FONT_PATH}\n"
        "Download Noto Sans Egyptian Hieroglyphs TTF from\n"
        "  https://fonts.google.com/noto/specimen/Noto+Sans+Egyptian+Hieroglyphs\n"
        f"and place it at the path above."
    )

font = ImageFont.truetype(str(FONT_PATH), FONT_SIZE)

for sid, cp in GLYPHS:
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img)
    ch = chr(cp)
    left, top, right, bottom = draw.textbbox((0, 0), ch, font=font)
    w, h = right - left, bottom - top
    draw.text(
        ((SIZE - w) / 2 - left, (SIZE - h) / 2 - top),
        ch,
        fill=FG,
        font=font,
    )
    out = OUT_DIR / f"{sid}.png"
    img.save(out)
    print(f"wrote {out.relative_to(HERE)}")

print(f"\nDone. {len(GLYPHS)} PNGs in {OUT_DIR.relative_to(HERE)}/")
