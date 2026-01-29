# 🔐 Smart Key - PyZ3R Edition

Napredna simulacija pametne brave (Smart Lock) razvijena u Pythonu koristeći **CustomTkinter** i **SQLite**.

![Status](https://img.shields.io/badge/Status-Development-blue)
![Python](https://img.shields.io/badge/Python-3.10%2B-yellow)

---

## 📌 Opis Rada

Aplikacija simulira rad pametnog portafona s kontrolom pristupa. Sadrži četiri glavna modula:

1. **Welcome Screen:** Početni zaslon koji omogućuje posjetitelju da pozvoni ili pokrene proces otključavanja.
2. **Pin Pad:** Sigurnosna tipkovnica za unos PIN-a. Podržava maskiranje unosa (zvjezdice/crtice).
3. **Unlock Logic:**
   - Unos **Korisničkog PIN-a** → Otvara vrata (Zeleni ekran).
   - Unos **Admin PIN-a** → Otvara Admin Panel.
4. **Admin Panel:** CRUD (Create, Read, Update, Delete) sučelje za upravljanje korisnicima u bazi.

---

## 🛠️ Tehnička Specifikacija

- **GUI Okvir:** CustomTkinter (Moderni Dark Mode)
- **Baza Podataka:** SQLite3 (`smart_lock.db`)
- **Sigurnost:** Sprječavanje brisanja jedinog preostalog administratora
- **Branding:** PyZ3R ASCII art potpis u konzoli (pyfiglet + colorama)

---

## 🚀 Upute za Pokretanje

### 1. Preduvjeti

Potrebno je instalirati zavisnosti iz `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 2. Pokretanje Aplikacije

Pozicionirajte se u root direktorij projekta i pokrenite:

```bash
python main.py
```

### 3. Prvi Pristup (Admin)

Baza podataka automatski kreira prvog administratora ako ne postoji:

- **Ime:** pyZ3R
- **PIN:** 0953

Koristite ovaj PIN za ulazak u Admin Panel i dodavanje novih korisnika.

---

## 📂 Struktura Direktorija

```
OL-OPYT_DEV_H-04-25-smart-key/
├── main.py              # Glavna logika aplikacije (CustomTkinter GUI)
├── database.py          # SQL upiti i konekcija na bazu
├── requirements.txt     # Popis potrebnih biblioteka
├── smart_lock.db        # SQLite baza (generira se automatski)
├── docs/                # Dokumentacija projekta
│   └── README.md        # Ovaj fajl
└── opis_zadatka/        # Originalna specifikacija
    └── opis_zadatka.md
```

---

## 🎨 Funkcionalnosti

### 🔔 Welcome Screen
- **Pozvoni gumb:** Simulira poziv vlasnika (status poruke)
- **Otključaj gumb:** Otvara PIN pad za unos šifre
- Dark mode dizajn sa PyZ3R brendingom

### 🔢 PIN Pad
- Numerička tipkovnica (0-9)
- **C gumb:** Briše cijeli unos
- **< gumb:** Briše zadnju brojku
- Vizualno maskiranje (••••)
- Automatska validacija nakon 4 znaka

### ✅ Unlock Screen
- Zeleni ekran potvrde
- Prikazuje ime korisnika
- Automatski povratak na Welcome nakon 4 sekunde

### 🛡️ Admin Panel
- Lista svih korisnika (scrollable)
- Dodavanje novih korisnika (ime + PIN)
- Brisanje korisnika (sa sigurnosnom provjerom)
- Razlikovanje admin (🛡️) i običnih (👤) korisnika
- Odjava gumb

---

## 🔒 Sigurnost

- ✅ Jedinstveni PIN kodovi (constraint u bazi)
- ✅ Zaštita od brisanja zadnjeg admina
- ✅ Maskiranje PIN-a u GUI-ju
- ✅ Automatsko brisanje pogrešnog unosa

---

## 📦 Dependencies

| Biblioteka | Verzija | Funkcija |
|-----------|---------|----------|
| customtkinter | latest | Moderni GUI framework |
| Pillow | latest | Podrška za slike |
| pyfiglet | latest | ASCII art potpis |
| colorama | latest | Obojeni konzolni output |

---

## 👨‍💻 Autor

**PyZ3R @ Algebra 2026**  
Razvijeno kao dio Python developer trening programa.

---

## 📝 Licenca

Ovaj projekt je razvijen u edukacijske svrhe.

---

*Verzija: 1.0.0*  
*Zadnje ažurirano: 29.01.2026*
