"""
產生 PNG 圖片：Favicon 多尺寸 + OG Image + PWA Icons
使用 Windows 中文字體 (微軟正黑體)
"""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.join(os.path.dirname(__file__), '..', 'images')

# ===== 字體 =====
FONT_BOLD = "C:/Windows/Fonts/msyhbd.ttc"
FONT_REG = "C:/Windows/Fonts/msjh.ttc"

def make_favicon(size=512):
    """產生三色漸層圓角方形 + 白色「作」字 + 上傳箭頭"""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 繪製漸層背景 (左上紅→中間青→右下黃)
    for y in range(size):
        for x in range(size):
            # 漸層計算
            t = (x + y) / (2 * size)
            if t < 0.5:
                t2 = t * 2
                r = int(255 * (1 - t2) + 78 * t2)
                g = int(107 * (1 - t2) + 205 * t2)
                b = int(107 * (1 - t2) + 196 * t2)
            else:
                t2 = (t - 0.5) * 2
                r = int(78 * (1 - t2) + 255 * t2)
                g = int(205 * (1 - t2) + 230 * t2)
                b = int(196 * (1 - t2) + 109 * t2)

            # 圓角遮罩
            radius = size * 0.195
            in_rect = True
            # 四角圓角判斷
            corners = [
                (radius, radius),
                (size - radius, radius),
                (radius, size - radius),
                (size - radius, size - radius)
            ]
            for cx, cy in corners:
                if (x < radius or x > size - radius) and (y < radius or y > size - radius):
                    dx = x - cx
                    dy = y - cy
                    if (dx * dx + dy * dy) > radius * radius:
                        in_rect = False
                        break
            if x < 0 or x >= size or y < 0 or y >= size:
                in_rect = False

            if in_rect:
                img.putpixel((x, y), (r, g, b, 255))

    # 「作」字
    try:
        font_size = int(size * 0.55)
        font = ImageFont.truetype(FONT_BOLD, font_size, index=0)
        text = "作"
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        tx = (size - tw) // 2 - bbox[0]
        ty = (size - th) // 2 - bbox[1] - int(size * 0.03)
        draw.text((tx, ty), text, fill=(255, 255, 255, 255), font=font)
    except Exception as e:
        print(f"Font error: {e}")

    # 上傳箭頭（底部）
    arrow_y = int(size * 0.82)
    arrow_cx = size // 2
    arrow_size = int(size * 0.04)
    points = [
        (arrow_cx, arrow_y - arrow_size * 2),
        (arrow_cx - arrow_size * 2, arrow_y),
        (arrow_cx - arrow_size * 0.8, arrow_y),
        (arrow_cx - arrow_size * 0.8, arrow_y + arrow_size * 1.5),
        (arrow_cx + arrow_size * 0.8, arrow_y + arrow_size * 1.5),
        (arrow_cx + arrow_size * 0.8, arrow_y),
        (arrow_cx + arrow_size * 2, arrow_y),
    ]
    draw.polygon(points, fill=(255, 255, 255, 230))

    return img


def make_og_image():
    """產生 1200x630 OG 社群預覽圖"""
    W, H = 1200, 630
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)

    # 漸層背景 (紫色系)
    for y in range(H):
        for x in range(W):
            t = (x / W * 0.6 + y / H * 0.4)
            if t < 0.5:
                t2 = t * 2
                r = int(102 * (1 - t2) + 118 * t2)
                g = int(126 * (1 - t2) + 75 * t2)
                b = int(234 * (1 - t2) + 162 * t2)
            else:
                t2 = (t - 0.5) * 2
                r = int(118 * (1 - t2) + 240 * t2)
                g = int(75 * (1 - t2) + 147 * t2)
                b = int(162 * (1 - t2) + 251 * t2)
            img.putpixel((x, y), (r, g, b))

    # 裝飾圓圈（半透明效果）
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    circles = [(100, 100, 70), (1100, 530, 90), (1050, 120, 50), (150, 480, 55), (600, 50, 40)]
    for cx, cy, cr in circles:
        odraw.ellipse([cx-cr, cy-cr, cx+cr, cy+cr], fill=(255, 255, 255, 15))
    img.paste(Image.alpha_composite(Image.new("RGBA", (W, H), (0,0,0,0)), overlay).convert("RGB"), (0, 0))

    # 小 Logo 方塊
    logo_size = 80
    logo_x, logo_y = (W - logo_size) // 2, 85
    # 漸層 logo 背景
    for ly in range(logo_size):
        for lx in range(logo_size):
            lt = (lx + ly) / (2 * logo_size)
            r = int(255 * (1 - lt) + 255 * lt)
            g = int(107 * (1 - lt) + 230 * lt)
            b = int(107 * (1 - lt) + 109 * lt)
            # 圓角
            rad = 18
            in_r = True
            for ccx, ccy in [(rad, rad), (logo_size-rad, rad), (rad, logo_size-rad), (logo_size-rad, logo_size-rad)]:
                if (lx < rad or lx > logo_size-rad) and (ly < rad or ly > logo_size-rad):
                    if ((lx-ccx)**2 + (ly-ccy)**2) > rad**2:
                        in_r = False
                        break
            if in_r:
                img.putpixel((logo_x + lx, logo_y + ly), (r, g, b))

    # Logo 上的「作」字
    try:
        logo_font = ImageFont.truetype(FONT_BOLD, 42, index=0)
        bbox = draw.textbbox((0, 0), "作", font=logo_font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((logo_x + (logo_size - tw)//2 - bbox[0], logo_y + (logo_size - th)//2 - bbox[1]),
                  "作", fill=(255, 255, 255), font=logo_font)
    except:
        pass

    draw = ImageDraw.Draw(img)

    # 主標題 "手作課"
    try:
        title_font = ImageFont.truetype(FONT_BOLD, 72, index=0)
        text = "手作課"
        bbox = draw.textbbox((0, 0), text, font=title_font)
        tw = bbox[2] - bbox[0]
        draw.text(((W - tw) // 2 - bbox[0], 195), text, fill=(255, 255, 255), font=title_font)
    except:
        pass

    # 副標題 "作品上傳平台" (漸層效果用黃橘色)
    try:
        sub_font = ImageFont.truetype(FONT_BOLD, 66, index=0)
        text = "作品上傳平台"
        bbox = draw.textbbox((0, 0), text, font=sub_font)
        tw = bbox[2] - bbox[0]
        # 用偏暖色
        draw.text(((W - tw) // 2 - bbox[0], 285), text, fill=(255, 217, 61), font=sub_font)
    except:
        pass

    # 描述文字
    try:
        desc_font = ImageFont.truetype(FONT_REG, 24, index=0)
        text = "記錄每一份用心創作的美好時刻"
        bbox = draw.textbbox((0, 0), text, font=desc_font)
        tw = bbox[2] - bbox[0]
        draw.text(((W - tw) // 2 - bbox[0], 385), text, fill=(255, 255, 255, 220), font=desc_font)
    except:
        pass

    # Badge
    try:
        badge_font = ImageFont.truetype(FONT_BOLD, 20, index=0)
        text = "六年級專屬 ・ Google 雲端上傳"
        bbox = draw.textbbox((0, 0), text, font=badge_font)
        tw = bbox[2] - bbox[0]
        bx = (W - tw) // 2 - bbox[0]
        # 半透明背景
        draw.rounded_rectangle([bx - 20, 440, bx + tw + 20, 486], radius=23, fill=(255, 255, 255, 38))
        draw.text((bx, 448), text, fill=(255, 255, 255), font=badge_font)
    except:
        pass

    # 班級彩色圓點
    colors = [(99, 102, 241), (239, 68, 68), (16, 185, 129), (245, 158, 11), (59, 130, 246), (139, 92, 246)]
    labels = ["1", "2", "3", "4", "5", "6"]
    start_x = 400
    try:
        dot_font = ImageFont.truetype(FONT_BOLD, 14, index=0)
        suffix_font = ImageFont.truetype(FONT_REG, 18, index=0)
        for i, (color, label) in enumerate(zip(colors, labels)):
            cx = start_x + i * 42
            cy = 535
            draw.ellipse([cx-14, cy-14, cx+14, cy+14], fill=color)
            bbox = draw.textbbox((0, 0), label, font=dot_font)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
            draw.text((cx - tw//2 - bbox[0], cy - th//2 - bbox[1]), label, fill=(255,255,255), font=dot_font)

        # "601~606 班級專區"
        draw.text((start_x + 6*42 + 10, 525), "601~606 班級專區", fill=(255,255,255,180), font=suffix_font)
    except:
        pass

    return img


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)

    print("generating favicon 512x512...")
    fav = make_favicon(512)
    fav.save(os.path.join(OUT, "favicon-512.png"), "PNG")

    print("generating icon-192.png...")
    fav.resize((192, 192), Image.LANCZOS).save(os.path.join(OUT, "icon-192.png"), "PNG")

    print("generating icon-512.png...")
    fav.resize((512, 512), Image.LANCZOS).save(os.path.join(OUT, "icon-512.png"), "PNG")

    print("generating favicon-32.png...")
    fav.resize((32, 32), Image.LANCZOS).save(os.path.join(OUT, "favicon-32.png"), "PNG")

    print("generating favicon-16.png...")
    fav.resize((16, 16), Image.LANCZOS).save(os.path.join(OUT, "favicon-16.png"), "PNG")

    print("generating apple-touch-icon.png...")
    fav.resize((180, 180), Image.LANCZOS).save(os.path.join(OUT, "apple-touch-icon.png"), "PNG")

    print("generating og-image.png...")
    og = make_og_image()
    og.save(os.path.join(OUT, "og-image.png"), "PNG", quality=95)

    print("All images generated!")
    for f in sorted(os.listdir(OUT)):
        if f.endswith('.png'):
            size = os.path.getsize(os.path.join(OUT, f))
            print(f"  {f}: {size:,} bytes")
