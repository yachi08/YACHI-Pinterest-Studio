# 額縁入りのアートポスターの商品写真（1254×1254px）からピン画像を作る。
# 使い方: python3 make_pins_poster.py 元写真 出力先 "見出し" "ピン3の文字"
import sys
from PIL import Image, ImageDraw, ImageFont
src, out, heading, label = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
im = Image.open(src).convert("RGB")
W, H = 1000, 1500
FONT = "/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf"
bg = (28, 28, 28)

def font(size): return ImageFont.truetype(FONT, size)

def ctext(d, y, text, size, fill):
    f = font(size); w = d.textlength(text, font=f)
    d.text(((W - w) / 2, y), text, font=f, fill=fill)

def fit(img, w):
    return img.resize((w, round(img.height * w / img.width)), Image.LANCZOS)

# 1: whole photo, no text
c = Image.new("RGB", (W, H), bg); p = fit(im, W); c.paste(p, (0, (H - p.height) // 2)); c.save(f"{out}/pin1.jpg", quality=92)
# 2: photo + black band with heading
c = Image.new("RGB", (W, H), (0, 0, 0)); p = fit(im, W); c.paste(p, (0, 120)); d = ImageDraw.Draw(c)
ctext(d, 1190, heading, 72, (255, 255, 255)); ctext(d, 1300, "NECLEFX ART POSTER", 36, (200, 200, 200)); c.save(f"{out}/pin2.jpg", quality=92)
# 3: decoration close-up
c = im.crop((420, 230, 900, 950)).resize((W, 1400), Image.LANCZOS); cc = Image.new("RGB", (W, H), (0, 0, 0)); cc.paste(c, (0, 0)); d = ImageDraw.Draw(cc)
ctext(d, 1425, label, 40, (255, 255, 255)); cc.save(f"{out}/pin3.jpg", quality=92)
# 4: size
c = Image.new("RGB", (W, H), (255, 255, 255)); p = fit(im, W); c.paste(p, (0, 0)); d = ImageDraw.Draw(c)
ctext(d, 1110, "A2サイズ", 110, (20, 20, 20)); ctext(d, 1270, "420×594mm・フレームなし", 52, (60, 60, 60)); c.save(f"{out}/pin4.jpg", quality=92)
# 5: crop including the words in the artwork
im.crop((350, 228, 930, 1098)).resize((W, H), Image.LANCZOS).save(f"{out}/pin5.jpg", quality=92)

# contact sheet for review
sheet = Image.new("RGB", (5 * 400 + 6 * 20, 600 + 80), (240, 240, 240)); d = ImageDraw.Draw(sheet)
for i in range(5):
    t = Image.open(f"{out}/pin{i+1}.jpg").resize((400, 600), Image.LANCZOS); x = 20 + i * 420
    sheet.paste(t, (x, 20)); d.text((x + 170, 630), f"ピン{i+1}", font=font(32), fill=(0, 0, 0))
sheet.save(f"{out}/一覧.jpg", quality=90)
