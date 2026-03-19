"""修正版 OG Image 產生器 - 正確漸層 + 半透明圓圈"""
from PIL import Image, ImageDraw, ImageFont
import math, os

OUT = os.path.join(os.path.dirname(__file__), '..', 'images')
FONT_BOLD = "C:/Windows/Fonts/msyhbd.ttc"
FONT_REG = "C:/Windows/Fonts/msjh.ttc"

W, H = 1200, 630
img = Image.new("RGB", (W, H))

# 1) 漸層背景 (紫藍→紫紅→粉紫)
for y in range(H):
    for x in range(W):
        t = x / W * 0.7 + y / H * 0.3
        # 三段漸層: #667eea → #764ba2 → #f093fb
        if t < 0.5:
            t2 = t * 2
            r = int(102 + (118 - 102) * t2)
            g = int(126 + (75 - 126) * t2)
            b = int(234 + (162 - 234) * t2)
        else:
            t2 = (t - 0.5) * 2
            r = int(118 + (240 - 118) * t2)
            g = int(75 + (147 - 75) * t2)
            b = int(162 + (251 - 162) * t2)
        img.putpixel((x, y), (r, g, b))

draw = ImageDraw.Draw(img)

# 2) 半透明裝飾圓圈 (直接用略淺的混合色)
circles = [(100, 100, 70), (1100, 530, 90), (1050, 120, 50), (150, 480, 55), (600, 50, 40)]
for cx, cy, cr in circles:
    # 模擬 6% 白色透明度覆蓋
    for dy in range(-cr, cr + 1):
        for dx in range(-cr, cr + 1):
            if dx * dx + dy * dy <= cr * cr:
                px, py = cx + dx, cy + dy
                if 0 <= px < W and 0 <= py < H:
                    orig = img.getpixel((px, py))
                    # 混合 6% 白色
                    nr = min(255, int(orig[0] + (255 - orig[0]) * 0.08))
                    ng = min(255, int(orig[1] + (255 - orig[1]) * 0.08))
                    nb = min(255, int(orig[2] + (255 - orig[2]) * 0.08))
                    img.putpixel((px, py), (nr, ng, nb))

# 3) 小 Logo 方塊 (漸層: 紅→青→黃)
logo_s = 80
lx0, ly0 = (W - logo_s) // 2, 90
rad = 18
for ly in range(logo_s):
    for lx in range(logo_s):
        t = (lx + ly) / (2 * logo_s)
        if t < 0.5:
            t2 = t * 2
            r = int(255 * (1-t2) + 78 * t2)
            g = int(107 * (1-t2) + 205 * t2)
            b = int(107 * (1-t2) + 196 * t2)
        else:
            t2 = (t - 0.5) * 2
            r = int(78 * (1-t2) + 255 * t2)
            g = int(205 * (1-t2) + 230 * t2)
            b = int(196 * (1-t2) + 109 * t2)
        # 圓角檢查
        in_r = True
        for ccx, ccy in [(rad, rad), (logo_s-rad-1, rad), (rad, logo_s-rad-1), (logo_s-rad-1, logo_s-rad-1)]:
            if (lx < rad or lx >= logo_s - rad) and (ly < rad or ly >= logo_s - rad):
                if ((lx - ccx)**2 + (ly - ccy)**2) > rad**2:
                    in_r = False
                    break
        if in_r:
            img.putpixel((lx0 + lx, ly0 + ly), (r, g, b))

# Logo「作」
draw = ImageDraw.Draw(img)
try:
    f = ImageFont.truetype(FONT_BOLD, 42, index=0)
    bb = draw.textbbox((0,0), "作", font=f)
    tw, th = bb[2]-bb[0], bb[3]-bb[1]
    draw.text((lx0 + (logo_s-tw)//2 - bb[0], ly0 + (logo_s-th)//2 - bb[1]), "作", fill="white", font=f)
except: pass

# 4) 主標題
try:
    f = ImageFont.truetype(FONT_BOLD, 72, index=0)
    bb = draw.textbbox((0,0), "手作課", font=f)
    tw = bb[2]-bb[0]
    draw.text(((W-tw)//2 - bb[0], 200), "手作課", fill="white", font=f)
except: pass

# 5) 副標題 (金黃色)
try:
    f = ImageFont.truetype(FONT_BOLD, 66, index=0)
    bb = draw.textbbox((0,0), "作品上傳平台", font=f)
    tw = bb[2]-bb[0]
    draw.text(((W-tw)//2 - bb[0], 290), "作品上傳平台", fill=(255, 217, 61), font=f)
except: pass

# 6) 描述
try:
    f = ImageFont.truetype(FONT_REG, 24, index=0)
    t = "記錄每一份用心創作的美好時刻"
    bb = draw.textbbox((0,0), t, font=f)
    tw = bb[2]-bb[0]
    draw.text(((W-tw)//2 - bb[0], 390), t, fill=(255, 255, 255), font=f)
except: pass

# 7) Badge 圓角矩形
try:
    f = ImageFont.truetype(FONT_BOLD, 20, index=0)
    t = "六年級專屬 ・ Google 雲端上傳"
    bb = draw.textbbox((0,0), t, font=f)
    tw = bb[2]-bb[0]
    bx = (W - tw) // 2 - bb[0]
    # 半透明 badge 背景 (模擬)
    for by in range(445, 490):
        for bxx in range(bx - 25, bx + tw + 25):
            if 0 <= bxx < W:
                # 圓角
                in_b = True
                r_b = 22
                for ccx, ccy in [(bx-25+r_b, 445+r_b), (bx+tw+25-r_b, 445+r_b), (bx-25+r_b, 490-r_b), (bx+tw+25-r_b, 490-r_b)]:
                    if (bxx < bx-25+r_b or bxx > bx+tw+25-r_b) and (by < 445+r_b or by > 490-r_b):
                        if ((bxx-ccx)**2 + (by-ccy)**2) > r_b**2:
                            in_b = False
                            break
                if in_b:
                    orig = img.getpixel((bxx, by))
                    nr = min(255, int(orig[0] + (255 - orig[0]) * 0.15))
                    ng = min(255, int(orig[1] + (255 - orig[1]) * 0.15))
                    nb = min(255, int(orig[2] + (255 - orig[2]) * 0.15))
                    img.putpixel((bxx, by), (nr, ng, nb))
    draw.text((bx, 455), t, fill="white", font=f)
except: pass

# 8) 班級彩色圓點
colors = [(99,102,241), (239,68,68), (16,185,129), (245,158,11), (59,130,246), (139,92,246)]
try:
    dot_f = ImageFont.truetype(FONT_BOLD, 14, index=0)
    suf_f = ImageFont.truetype(FONT_REG, 18, index=0)
    sx = 390
    for i, c in enumerate(colors):
        cx = sx + i * 44
        cy = 545
        draw.ellipse([cx-14, cy-14, cx+14, cy+14], fill=c)
        label = str(i + 1)
        bb = draw.textbbox((0,0), label, font=dot_f)
        tw, th = bb[2]-bb[0], bb[3]-bb[1]
        draw.text((cx - tw//2 - bb[0], cy - th//2 - bb[1]), label, fill="white", font=dot_f)
    draw.text((sx + 6*44 + 15, 535), "601~606 班級專區", fill=(220,220,255), font=suf_f)
except: pass

img.save(os.path.join(OUT, "og-image.png"), "PNG", quality=95)
print("OG image saved!")
sz = os.path.getsize(os.path.join(OUT, "og-image.png"))
print(f"  og-image.png: {sz:,} bytes")
