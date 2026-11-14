from PIL import Image, ImageSequence
from collections import deque
import glob, os, io, base64, json

D = '/tmp/claude-0/-home-user-teste/d76167c4-7d3d-5872-a48b-bfac51b722e2/images'
SP = '/tmp/claude-0/-home-user-teste/d76167c4-7d3d-5872-a48b-bfac51b722e2/scratchpad'
ART = '/home/user/teste/NASA-SAC-2026/art'
os.makedirs(ART, exist_ok=True)

# visor colour -> crew slot
COLORS = {
    '8':  ('gold',  (254, 242, 25)),
    '9':  ('green', (38, 166, 75)),
    '10': ('cyan',  (20, 183, 232)),
    '11': ('red',   (215, 28, 35)),
}
ORDER = ['10', '9', '8', '11']   # cyan, green, gold, red  = players 1-4

W = H = 30
NEAR_WHITE = 230


def key_outside(fr):
    """Transparent only where white is reachable from the border.
    Interior white (the suit) is preserved."""
    im = fr.convert('RGBA')
    px = im.load()
    seen = [[False] * H for _ in range(W)]
    q = deque()
    for x in range(W):
        for y in (0, H - 1):
            q.append((x, y))
    for y in range(H):
        for x in (0, W - 1):
            q.append((x, y))
    while q:
        x, y = q.popleft()
        if x < 0 or y < 0 or x >= W or y >= H or seen[x][y]:
            continue
        r, g, b, a = px[x, y]
        if not (r >= NEAR_WHITE and g >= NEAR_WHITE and b >= NEAR_WHITE):
            continue          # hit the black outline - stop
        seen[x][y] = True
        px[x, y] = (0, 0, 0, 0)
        q.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])
    return im


manifest = {}
for key in ORDER:
    name, rgb = COLORS[key]
    src = Image.open(f'{D}/{key}.gif')
    frames = [key_outside(fr) for fr in ImageSequence.Iterator(src)]
    strip = Image.new('RGBA', (W * len(frames), H), (0, 0, 0, 0))
    for i, fr in enumerate(frames):
        strip.paste(fr, (i * W, 0))
    strip.save(f'{ART}/astro_{name}.png')
    b = io.BytesIO(); strip.save(b, 'PNG', optimize=True)
    raw = b.getvalue()
    manifest[name] = {
        'frames': len(frames),
        'w': W, 'h': H,
        'rgb': '#%02x%02x%02x' % rgb,
        'data': 'data:image/png;base64,' + base64.b64encode(raw).decode(),
    }
    # how much got cleared?
    clear = sum(1 for p in frames[0].getdata() if p[3] == 0)
    print(f'{name:6s} {len(frames)} frames  strip {strip.size}  {len(raw)} bytes  '
          f'frame0 transparent {clear*100//900}%')

json.dump(manifest, open(f'{SP}/sprite_manifest.json', 'w'))
total = sum(len(v['data']) for v in manifest.values())
print(f'\ntotal base64 payload: {total//1024} KB')

# preview on a dark background to prove transparency
prev = Image.new('RGBA', (W * 8 * 4, H * 4), (10, 14, 26, 255))
for r, key in enumerate(ORDER):
    name, _ = COLORS[key]
    s = Image.open(f'{ART}/astro_{name}.png')
    prev.alpha_composite(s.resize((W * 8 * 4, H * 4), Image.NEAREST).crop((0, 0, W * 8 * 4, H * 4)), (0, r * H * 4))
prev.save(f'{SP}/show/sprite-alpha-check.png')

# tidy side-by-side: each colour's 8 frames at 4x on dark
grid = Image.new('RGBA', (W * 4 * 8, H * 4 * 4), (10, 14, 26, 255))
for r, key in enumerate(ORDER):
    name, _ = COLORS[key]
    s = Image.open(f'{ART}/astro_{name}.png')
    for i in range(8):
        f = s.crop((i * W, 0, (i + 1) * W, H)).resize((W * 4, H * 4), Image.NEAREST)
        grid.alpha_composite(f, (i * W * 4, r * H * 4))
grid.convert('RGB').save(f'{SP}/show/sprite-alpha-check.png')
print('alpha check ->', f'{SP}/show/sprite-alpha-check.png')
