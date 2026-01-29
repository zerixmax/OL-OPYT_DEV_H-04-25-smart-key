# Changelog

Sve značajne promjene u projektu će biti dokumentirane u ovom fajlu.

Format se zasniva na [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [2.0.0] - 2026-01-29

### ✨ Added
- **Profesionalne HQ ikone** sa 4x anti-aliasingom (256x256 → 64x64)
- **assets_generator_pro.py** - Napredni generator ikona
- Ikona zaključane brave (80x80) na Welcome ekranu
- Admin ikona (🛡️ štit sa zvijezdom) u headeru Admin Panela
- Role ikone (admin/user) u listi korisnika
- Delete ikona umjesto teksta "X"
- Compound layout za gumbe (ikona + tekst)
- **CHANGELOG.md** i kompletan **README.md**

### 🎨 Changed
- Povećan prozor sa 400x650 na **450x700px**
- "Rezidencija PyZ3R" → **"Hacijenda PyZ3R"**
- Gumbi na PIN padu: 70x70 → **75x75px**
- Dodani zaobljeni gumbi: **corner_radius=20**
- PIN display font: 40pt → **42pt**
- PIN title font: 20pt → **24pt**
- Admin title font: 20pt → **24pt**
- Input height: default → **40px**
- Gumb width u Welcome: 250px → **280px**
- Status poruka u potpisu: "System Active" → **"PyZ3R Security System v2.0 with Icons"**
- Verzija aplikacije: 1.0 → **2.0**

### 🔧 Improved
- Bolji spacing u PIN padu (padx/pady: 5 → **8**)
- Veći border na keypad gumbima (border_width=2)
- Bolji layout admin liste (left_cont container)
- Profesionalniji izgled svih ekrana
- Glatke ikone sa anti-aliasingom
- Veće ikone na file sistemu (2-3KB umjesto 400B)

### 📝 Documentation
- Kompletan README.md sa instalacijom i svim detaljima
- CHANGELOG.md verzioniranje
- Detaljna dokumentacija u docs/README.md
- PEP-8 compliance napomene

---

## [1.0.0] - 2026-01-29 (Initial Release)

### ✨ Added
- **Početna implementacija** Smart Key aplikacije
- CustomTkinter GUI framework (Dark Mode)
- SQLite baza podataka za korisnike
- 4 ekrana:
  - Welcome Screen (Pozvoni / Otključaj)
  - PIN Pad (Numerička tipkovnica)
  - Unlock Screen (Zeleni uspješan login)
  - Admin Panel (CRUD za korisnike)
- Defaultni admin korisnik: **pyZ3R** (PIN: **0953**)
- PIN validacija i maskiranje (••••)
- Role-based access (admin/user)
- Zaštita od brisanja zadnjeg admina
- PyZ3R ASCII art branding (pyfiglet + colorama)
- Emoji ikone u GUI-ju (🔔🔐👤🛡️)
- Automatsko kreiranje baze pri prvom pokretanju
- Virtual environment setup
- requirements.txt sa dependencies
- .gitignore za Python/SQLite

### 🔒 Security
- Jedinstveni PIN kodovi (UNIQUE constraint)
- Zaštita zadnjeg admina
- PIN maskiranje u GUI-ju
- Role-based pristup kontroli

### 🛠️ Technical
- Python 3.10+ kompatibilnost
- PEP-8 coding style
- MVC-like arhitektura
- Modularni kod (main.py + database.py)
- Virtual environment izolacija
- Cross-platform support (Windows/Linux/Mac)

---

## Oznake Verzija

- **[2.0.0]** - Current Release (HQ Icons Update)
- **[1.0.0]** - Initial Release (Basic Functionality)

---

**PyZ3R @ Algebra 2026**
