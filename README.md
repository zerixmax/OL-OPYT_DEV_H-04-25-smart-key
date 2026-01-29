# 🔐 Smart Key - PyZ3R Edition v2.0

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-green.svg)
![SQLite](https://img.shields.io/badge/Database-SQLite-orange.svg)
![Version](https://img.shields.io/badge/Version-2.0-red.svg)
![License](https://img.shields.io/badge/License-Educational-yellow.svg)

Napredna simulacija pametne brave (Smart Lock) razvijena u Pythonu koristeći **CustomTkinter** i **SQLite**.

---

## 📌 O Projektu

**Smart Key** je desktop aplikacija koja simulira moderan pametni portafon s kontrolom pristupa. Aplikacija omogućava:

- 🔔 **Pozivanje** vlasnika/stanara
- 🔐 **PIN autentifikaciju** za otključavanje
- 👤 **Upravljanje korisnicima** (CRUD operacije)
- 🛡️ **Admin panel** za administratore
- 🎨 **Profesionalne HQ ikone** sa anti-aliasingom

---

## 🎯 Funkcionalnosti

### 1️⃣ Welcome Screen
- Vizualno atraktivan početni ekran
- Ikona zaključane brave
- Gumbi za pozivanje i otključavanje
- Real-time status poruke

### 2️⃣ PIN Unos
- Numerička tipkovnica (0-9)
- **C** - čišćenje cijelog unosa
- **<** - brisanje zadnje brojke
- Vizualno maskiranje (••••)
- Automatska validacija nakon 4 znaka

### 3️⃣ Unlock Screen
- Zeleni ekran potvrde
- Prikazuje ime korisnika
- Automatski povratak nakon 4 sekunde

### 4️⃣ Admin Panel
- Lista svih korisnika (scrollable)
- Dodavanje novih korisnika
- Brisanje korisnika (sa zaštitom zadnjeg admina)
- Razlikovanje admin/user uloga
- Profesionalne ikone za svaku ulogu

---

## 🛠️ Tehnologije

- **Python 3.10+** - Programski jezik
- **CustomTkinter** - Moderni GUI framework (Dark Mode)
- **SQLite3** - Lokalna baza podataka
- **Pillow (PIL)** - Procesiranje slika i ikona
- **pyfiglet** - ASCII art branding
- **colorama** - Obojeni terminal output

---

## 📂 Struktura Projekta

```
OL-OPYT_DEV_H-04-25-smart-key/
├── main.py                   # Glavna GUI aplikacija
├── database.py               # SQLite database manager
├── assets_generator_pro.py   # HQ ikona generator
├── requirements.txt          # Python dependencies
├── smart_lock.db            # SQLite baza (auto-generated)
│
├── assets/                   # Profesionalne PNG ikone
│   ├── admin.png            # 🛡️ Admin ikona (štit sa zvijezdom)
│   ├── bell.png             # 🔔 Zvono
│   ├── delete.png           # ❌ Delete (X)
│   ├── lock.png             # 🔐 Otključano
│   ├── lock_closed.png      # 🔒 Zaključano (veliki logo)
│   └── user.png             # 👤 Korisnik
│
├── docs/                     # Dokumentacija
│   └── README.md            # Detaljna dokumentacija
│
├── opis_zadatka/            # Zadatak specifikacija
│   └── opis_zadatka.md
│
└── venv/                     # Python virtual environment
```

---

## 🚀 Instalacija i Pokretanje

### Preduvjeti
- **Python 3.10** ili novija verzija
- **pip** package manager

### 1. Kloniraj Repozitorij

```bash
git clone https://github.com/yourusername/OL-OPYT_DEV_H-04-25-smart-key.git
cd OL-OPYT_DEV_H-04-25-smart-key
```

### 2. Kreiraj Virtualno Okruženje

```bash
python -m venv venv
```

### 3. Aktiviraj Virtualno Okruženje

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instaliraj Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. (Opcionalno) Regeneriraj Ikone

```bash
python assets_generator_pro.py
```

### 6. Pokreni Aplikaciju

**Windows:**
```powershell
$env:TCL_LIBRARY="$PWD\venv\tcl\tcl8.6"
$env:TK_LIBRARY="$PWD\venv\tcl\tk8.6"
python main.py
```

**Linux/Mac:**
```bash
python main.py
```

---

## 👤 Defaultni Korisnici

| Korisnik | PIN | Uloga | Pristup |
|----------|-----|-------|---------|
| **pyZ3R** | 0953 | Admin | Admin Panel + Unlock |

> **Napomena:** Admin korisnik se automatski kreira pri prvom pokretanju.

---

## 📖 Korištenje Aplikacije

### Pozivanje Vlasnika
1. Na Welcome ekranu klikni **🔔 POZVONI**
2. Status poruka prikazat će "📞 Pozivam vlasnika..."
3. Nakon 3 sekunde: "⚠️ Nitko se ne javlja."

### Otključavanje Vrata
1. Klikni **🔐 OTKLJUČAJ**
2. Unesi PIN kod (npr. **0953**)
3. Ako je PIN točan:
   - **Admin** → Otvara Admin Panel
   - **User** → Prikazuje Unlock ekran

### Admin Panel
1. Unesi admin PIN (**0953**)
2. U Admin Panelu možeš:
   - **Dodati** novog korisnika (ime + PIN)
   - **Vidjeti** sve korisnike sa njihovim PINovima
   - **Obrisati** korisnika (osim zadnjeg admina)
3. Klikni **Odjava** za povratak

---

## 🔒 Sigurnosne Značajke

✅ **Jedinstveni PIN kodovi** - Constraint u bazi sprječava duplikate  
✅ **Zaštita zadnjeg admina** - Ne može se obrisati jedini admin  
✅ **PIN maskiranje** - Prikazuje se kao •••• u GUI-ju  
✅ **Automatsko čišćenje** - Pogrešan unos se briše nakon 0.8s  
✅ **Role-based access** - Admini imaju dodatne privilegije  

---

## 🎨 Ikone (Anti-Aliasing)

Ikone se generiraju na **256x256px** rezoluciji i smanjuju na **64x64px** koristeći **LANCZOS anti-aliasing** za glatke rubove:

- **bell.png** - Narančasto zvono
- **lock.png** - Zeleni otključani lokot
- **lock_closed.png** - Crveni zaključani lokot
- **user.png** - Plavi korisnik
- **admin.png** - Ljubičasti štit sa zvijezdom
- **delete.png** - Crveni X

---

## 📝 PEP-8 Compliance

Projekt prati **PEP-8** Python style guide:
- ✅ 4 spaces indentacija
- ✅ Max 79 znakova po liniji (gdje moguće)
- ✅ Snake_case za funkcije i varijable
- ✅ PascalCase za klase
- ✅ Docstrings za sve funkcije

---

## 🐛 Poznati Issues

- **Tcl/Tk Warning** - "Could not find platform independent libraries" se pojavljuje na nekim Python 3.13 instalacijama, ali ne utječe na funkcionalnost

---

## 📦 Dependencies

| Package | Verzija | Svrha |
|---------|---------|-------|
| customtkinter | latest | Moderni GUI framework |
| Pillow | latest | Image processing |
| pyfiglet | latest | ASCII art |
| colorama | latest | Terminal colors |

---

## 🤝 Doprinos

Ovaj projekt je razvijen za edukacijske svrhe. Prijedlozi i poboljšanja su dobrodošli!

---

## 📄 Licenca

Ovaj projekt je razvijen u edukacijske svrhe kao dio Python developer trening programa.

---

## 👨‍💻 Autor

**PyZ3R @ Algebra 2026**

Developed with 💜 for learning purposes.

---

## 🔄 Changelog

### v2.0 (2026-01-29)
- ✨ Dodane profesionalne HQ ikone sa anti-aliasingom
- 🎨 Poboljšan dizajn svih ekrana
- 🔧 Veći prozor (450x700px)
- 🛡️ Admin ikona u headeru
- 🎯 Role ikone u user listi
- 🗑️ Delete ikona umjesto teksta
- 📝 Promijenjen naziv u "Hacijenda PyZ3R"
- 🔄 Zaobljeni gumbi (corner_radius=20)
- 📏 Veći gumbi na PIN padu (75x75px)

### v1.0 (Initial Release)
- 🎉 Početna verzija sa osnovnim funkcionalnostima
- 🔐 PIN autentifikacija
- 👥 CRUD operacije za korisnike
- 📱 CustomTkinter GUI
- 💾 SQLite baza

---

**🔐 Hacijenda PyZ3R - Smart Security System v2.0**
