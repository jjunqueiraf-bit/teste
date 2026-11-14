from PIL import Image, ImageSequence
from collections import Counter
import glob, os

D = '/tmp/claude-0/-home-user-teste/d76167c4-7d3d-5872-a48b-bfac51b722e2/images'
OUT = '/tmp/claude-0/-home-user-teste/d76167c4-7d3d-5872-a48b-bfac51b722e2/scratchpad/show'
os.makedirs(OUT, exist_ok=True)

files = sorted(glob.glob(f'{D}/*.gif'),
               key=lambda x: int(''.join(c for c in os.path.basename(x) if c.isdigit())))

SCALE = 6
sheet = Image.new('RGB', (30 * SCALE * 8, 30 * SCALE * len(files)), (255, 0, 255))

for r, f in enumerate(files):
    im = Image.open(f)
    frames = [fr.convert('RGB') for fr in ImageSequence.Iterator(im)]
    # corner pixels tell us the background
    corners = []
    for fr in frames:
        for xy in [(0, 0), (29, 0), (0, 29), (29, 29)]:
            corners.append(fr.getpixel(xy))
    bg = Counter(corners).most_common(3)
    print(f'{os.path.basename(f):8s} frames={len(frames)} corner colors={bg}')
    for c, fr in enumerate(frames):
        sheet.paste(fr.resize((30 * SCALE, 30 * SCALE), Image.NEAREST), (c * 30 * SCALE, r * 30 * SCALE))

sheet.save(f'{OUT}/sprite-frames.png')
print('\nframe sheet ->', f'{OUT}/sprite-frames.png')

# how much of each frame is the background colour?
for f in files:
    im = Image.open(f)
    fr = next(ImageSequence.Iterator(im)).convert('RGB')
    px = list(fr.getdata())
    top = Counter(px).most_common(4)
    print(f'{os.path.basename(f):8s} dominant pixels:', [(c, f'{n*100//900}%') for c, n in top])
