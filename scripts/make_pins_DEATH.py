import sys
from PIL import Image, ImageDraw, ImageFont
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
W, H = 1000, 1500
FONT = "/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf"

def font(size): return ImageFont.truetype(FONT, size)

def ctext(d, y, text, size, fill):
    f = font(size); w = d.textlength(text, font=f)
    d.text(((W - w) / 2, y), text, font=f, fill=fill)

def fit_h(img, h):
    return img.resize((round(img.width * h / img.height), h), Image.LANCZOS)

# 1: whole card, no text
c = Image.new("RGB", (W, H), (0, 0, 0)); p = fit_h(im, 1440); c.paste(p, ((W - p.width) // 2, 30)); c.save(f"{out}/pin1.jpg", quality=92)
# 2: card + band with heading
c = Image.new("RGB", (W, H), (0, 0, 0)); p = fit_h(im, 1180); c.paste(p, ((W - p.width) // 2, 30)); d = ImageDraw.Draw(c)
ctext(d, 1270, "タロットカード風ステッカー", 64, (255, 255, 255)); ctext(d, 1370, "NECLEFX STICKER", 36, (200, 200, 200)); c.save(f"{out}/pin2.jpg", quality=92)
# 3: skull close-up
c = im.crop((0, 120, 512, 888)).resize((W, H), Image.LANCZOS); c.save(f"{out}/pin3.jpg", quality=92)
# 4: card + words on the card
c = Image.new("RGB", (W, H), (0, 0, 0)); p = fit_h(im, 1180); c.paste(p, ((W - p.width) // 2, 30)); d = ImageDraw.Draw(c)
ctext(d, 1260, "XIII  DEATH", 72, (255, 255, 255)); ctext(d, 1370, "END・TRANSFORMATION・REBIRTH", 38, (230, 80, 140)); c.save(f"{out}/pin4.jpg", quality=92)

sheet = Image.new("RGB", (4 * 400 + 5 * 20, 600 + 80), (240, 240, 240)); d = ImageDraw.Draw(sheet)
for i in range(4):
    t = Image.open(f"{out}/pin{i+1}.jpg").resize((400, 600), Image.LANCZOS); x = 20 + i * 420
    sheet.paste(t, (x, 20)); d.text((x + 170, 630), f"ピン{i+1}", font=font(32), fill=(0, 0, 0))
sheet.save(f"{out}/一覧.jpg", quality=90)
