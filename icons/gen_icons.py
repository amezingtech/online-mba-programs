"""Generate Store-ready PNG icons matching the app's SVG icon design."""
from PIL import Image, ImageDraw

NAVY1, NAVY2 = (22, 38, 79), (15, 27, 61)
GOLD, RED = (244, 180, 0), (229, 50, 79)

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def gradient(size, c1, c2):
    img = Image.new("RGB", (size, size))
    px = img.load()
    for y in range(size):
        for x in range(size):
            px[x, y] = lerp(c1, c2, (x + y) / (2 * size))
    return img

def draw_logo(size, pad=0.0):
    """pad = fraction of empty margin (for maskable icons)."""
    s = size
    bg = gradient(s, NAVY1, NAVY2)

    mask = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(mask)
    radius = int(s * 0.215)
    if pad == 0.0:
        d.rounded_rectangle([0, 0, s - 1, s - 1], radius=radius, fill=255)
    else:
        m = int(s * pad)
        d.rounded_rectangle([m, m, s - 1 - m, s - 1 - m], radius=int(radius * (1 - 2 * pad)), fill=255)

    out = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    out.paste(bg, (0, 0), mask)
    dr = ImageDraw.Draw(out)
    u = s / 512.0  # unit scale (design grid = 512)
    off = s * pad
    u_pad = u * (1 - 2 * pad) if pad else u

    def P(x, y):
        return (off + x * u_pad, off + y * u_pad)

    # mortar board (gold -> red gradient polygon)
    cap_poly = [P(40, 212), P(256, 118), P(472, 212), P(256, 306)]
    cap_grad = gradient(s, GOLD, RED)
    cap_mask = Image.new("L", (s, s), 0)
    ImageDraw.Draw(cap_mask).polygon(cap_poly, fill=255)
    board = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    board.paste(cap_grad, (0, 0), cap_mask)
    out = Image.alpha_composite(out, board)

    # right tassel arm of the board
    dr = ImageDraw.Draw(out)
    dr.polygon([P(424, 212), P(472, 212), P(472, 312), P(424, 312)], fill=RED)
    # tassel knob
    dr.ellipse([P(424 - 26, 128 - 26), P(424 + 26, 128 + 26)], fill=GOLD)
    # book / body (white)
    dr.polygon([P(136, 268), P(376, 268), P(376, 354), P(256, 406), P(136, 354)],
               fill=(255, 255, 255, 235))
    # book fold line
    dr.line([P(256, 320), P(256, 406)], fill=(210, 216, 232, 255), width=max(2, int(4 * u_pad)))
    return out

draw_logo(512).save("icon-512.png")
draw_logo(192).save("icon-192.png")
draw_logo(512, pad=0.12).save("icon-maskable-512.png")
print("icons generated")
