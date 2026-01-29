import os
from PIL import Image, ImageDraw

# Kreiraj mapu assets
if not os.path.exists("assets"):
    os.makedirs("assets")


def create_icon(filename, color, shape="circle", symbol=""):
    """Crta jednostavne moderne ikonice."""
    size = (64, 64)
    # Transparentna pozadina
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Crtanje oblika
    padding = 4
    if shape == "circle":
        draw.ellipse(
            [padding, padding, size[0]-padding, size[1]-padding],
            fill=color
        )
    elif shape == "rect":
        draw.rounded_rectangle(
            [padding, padding, size[0]-padding, size[1]-padding],
            radius=15,
            fill=color
        )
    
    # Crtanje simbola (jednostavne linije)
    center = size[0] // 2
    
    # Bijela boja za simbole
    sym_color = "white"
    
    if symbol == "bell":
        # Zvono
        draw.polygon([(center, 15), (20, 45), (44, 45)], fill=sym_color)
        draw.ellipse([center-4, 42, center+4, 50], fill=sym_color)
    
    elif symbol == "lock":
        # Lokot
        draw.rectangle([22, 28, 42, 48], fill=sym_color)
        draw.arc([24, 15, 40, 35], 180, 0, fill=sym_color, width=3)
        
    elif symbol == "unlock":
        # Otključano
        draw.rectangle([22, 28, 42, 48], fill=sym_color)
        draw.arc([24, 15, 40, 35], 180, 270, fill=sym_color, width=3)
        
    elif symbol == "user":
        # Korisnik (glava i tijelo)
        draw.ellipse([center-8, 15, center+8, 31], fill=sym_color)
        draw.arc([18, 35, 46, 60], 180, 0, fill=sym_color, width=15)
        
    elif symbol == "admin":
        # Admin (kruna/zvijezda)
        draw.polygon(
            [(center, 15), (20, 45), (44, 45)],
            fill=sym_color
        )  # Trokut
        draw.ellipse([center-8, 15, center+8, 31], fill=sym_color)  # Glava
        
    elif symbol == "delete":
        # X
        draw.line([20, 20, 44, 44], fill=sym_color, width=5)
        draw.line([20, 44, 44, 20], fill=sym_color, width=5)

    img.save(f"assets/{filename}.png")
    print(f"Generated: assets/{filename}.png")


# Generiraj set ikona
create_icon("bell", "#E67E22", "circle", "bell")       # Narančasta
create_icon("lock", "#27AE60", "rect", "lock")         # Zelena
create_icon("lock_closed", "#C0392B", "rect", "lock")  # Crvena (zaključano)
create_icon("user", "#3498DB", "circle", "user")       # Plava
create_icon("admin", "#8E44AD", "circle", "admin")     # Ljubičasta
create_icon("delete", "#C0392B", "circle", "delete")   # Crvena X

print("✅ Sve ikonice su spremne!")
