import os
from PIL import Image, ImageDraw, ImageFont

# Kreiraj mapu assets ako ne postoji
if not os.path.exists("assets"):
    os.makedirs("assets")


def draw_smooth_icon(filename, color, icon_type):
    """
    Crta ikonicu u visokoj rezoluciji (256x256) i smanjuje je na (64x64)
    kako bi dobili savršeno glatke rubove (Anti-aliasing).
    """
    # Crtamo na 4x većoj površini
    size = 256
    target_size = 64
    
    # Transparentna pozadina
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    center = size // 2
    
    # --- LOGIKA CRTANJA ---
    
    if icon_type == "bell":
        # Zvono (Narančasto)
        # Tijelo zvona
        draw.chord(
            [size*0.2, size*0.2, size*0.8, size*0.8],
            180, 0,
            fill=color
        )
        draw.rectangle(
            [size*0.2, size*0.5, size*0.8, size*0.75],
            fill=color
        )
        # Dno zvona (zakrivljeno)
        draw.chord(
            [size*0.15, size*0.65, size*0.85, size*0.85],
            0, 180,
            fill=color
        )
        # Kuglica dolje
        draw.ellipse(
            [size*0.42, size*0.80, size*0.58, size*0.96],
            fill=color
        )
        
    elif icon_type == "lock":
        # Lokot Otključan (Zeleni)
        # Tijelo
        draw.rounded_rectangle(
            [size*0.2, size*0.4, size*0.8, size*0.9],
            radius=40,
            fill=color
        )
        # Karika (Otvorena)
        draw.arc(
            [size*0.3, size*0.1, size*0.7, size*0.6],
            180, 0,
            fill=color,
            width=35
        )
        # Ključanica
        draw.ellipse(
            [center-20, size*0.6-20, center+20, size*0.6+20],
            fill="white"
        )
        draw.rectangle(
            [center-8, size*0.6, center+8, size*0.75],
            fill="white"
        )

    elif icon_type == "lock_closed":
        # Lokot Zaključan (Crveni) - Veliki
        # Tijelo
        draw.rounded_rectangle(
            [size*0.15, size*0.4, size*0.85, size*0.95],
            radius=40,
            fill=color
        )
        # Karika (Zatvorena)
        draw.arc(
            [size*0.25, size*0.05, size*0.75, size*0.55],
            180, 0,
            fill=color,
            width=40
        )
        # Ključanica
        draw.ellipse(
            [center-25, size*0.6-25, center+25, size*0.6+25],
            fill="white"
        )
        draw.rectangle(
            [center-10, size*0.6, center+10, size*0.78],
            fill="white"
        )

    elif icon_type == "user":
        # Korisnik (Plavi)
        # Glava
        draw.ellipse([center-50, 20, center+50, 120], fill=color)
        # Tijelo (Luk)
        draw.chord([40, 130, size-40, size+80], 0, 180, fill=color)

    elif icon_type == "admin":
        # Admin (Ljubičasti) - S krunom/štitom
        # Štit oblik
        draw.polygon([
            (center, 20), (size-40, 60), (size-40, 160),
            (center, size-20), (40, 160), (40, 60)
        ], fill=color)
        
        # Zvijezda unutar štita
        star_center_x = center
        star_center_y = 110
        star_size = 50
        
        # 5-kraka zvijezda
        points = []
        for i in range(10):
            angle = i * 36 - 90  # -90 da počne od vrha
            radius = star_size if i % 2 == 0 else star_size * 0.4
            import math
            x = star_center_x + radius * math.cos(math.radians(angle))
            y = star_center_y + radius * math.sin(math.radians(angle))
            points.append((x, y))
        
        draw.polygon(points, fill="white")

    elif icon_type == "delete":
        # X za brisanje (Crveni)
        # Krug pozadina
        draw.ellipse([20, 20, size-20, size-20], fill=color)
        
        # Bijeli X (debele linije)
        line_width = 30
        offset = size * 0.25
        
        draw.line(
            [offset, offset, size-offset, size-offset],
            fill="white",
            width=line_width
        )
        draw.line(
            [size-offset, offset, offset, size-offset],
            fill="white",
            width=line_width
        )
    
    # Smanjivanje slike na target size sa anti-aliasingom
    img_small = img.resize((target_size, target_size), Image.LANCZOS)
    
    # Spremanje
    img_small.save(f"assets/{filename}.png")
    print(f"✓ Generated HQ: assets/{filename}.png")


# === GENERIRANJE IKONA ===
print("🎨 Generiram profesionalne ikonice...\n")

draw_smooth_icon("bell", "#E67E22", "bell")             # Narančasta
draw_smooth_icon("lock", "#27AE60", "lock")             # Zelena
draw_smooth_icon("lock_closed", "#C0392B", "lock_closed")  # Crvena
draw_smooth_icon("user", "#3498DB", "user")             # Plava
draw_smooth_icon("admin", "#8E44AD", "admin")           # Ljubičasta
draw_smooth_icon("delete", "#C0392B", "delete")         # Crvena

print("\n✅ Sve HQ ikonice su spremne!")
print("📁 Provjerite folder: assets/")
