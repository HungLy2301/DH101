from PIL import Image, ImageDraw
import os

ROOT = os.path.dirname(os.path.dirname(__file__))
OUT_DIR = os.path.join(ROOT, 'assets', 'images')
os.makedirs(OUT_DIR, exist_ok=True)
OUT_PATH = os.path.join(OUT_DIR, 'dot.gif')

# Image size similar to attachment proportions
W, H = 1200, 800
BG = (255, 255, 255)
DOT_COLOR = (0, 0, 0)

img = Image.new('RGB', (W, H), BG)
draw = ImageDraw.Draw(img)

# draw a solid circle near left edge
cx, cy = 80, H // 2
r = 70
bbox = [cx - r, cy - r, cx + r, cy + r]
draw.ellipse(bbox, fill=DOT_COLOR)

img.save(OUT_PATH, format='GIF')
print(f'Wrote GIF to {OUT_PATH}')
