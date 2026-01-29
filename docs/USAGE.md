# 📖 Uputstvo za Korištenje - Smart Key v2.0

Dobrodošli u Smart Key aplikaciju! Ovaj vodič će vas provesti kroz sve funkcionalnosti sistema.

---

## 🚀 Pokretanje Aplikacije

### Windows - Jednostavno Pokretanje

**Dvostruki klik na:**
- `run.bat` (CMD verzija)
- `run.ps1` (PowerShell verzija)

Aplikacija će se automatski pokrenuti sa svim potrebnim postavkama.

### Manualno Pokretanje

```powershell
# Aktiviraj virtual environment
.\venv\Scripts\Activate.ps1

# Postavi Tcl/Tk environment
$env:TCL_LIBRARY="$PWD\venv\tcl\tcl8.6"
$env:TK_LIBRARY="$PWD\venv\tcl\tk8.6"

# Pokreni aplikaciju
python main.py
```

---

## 🏠 Welcome Screen (Početni Ekran)

Kada pokrenete aplikaciju, vidjet ćete:

### Elementi Ekrana

**🔒 Logo**
- Velika ikona zaključane brave na vrhu
- Označava da je sistem aktivan i siguran

**Naslov**
- "SMART LOCK"
- "Hacijenda PyZ3R"

**Gumbi:**

#### 🔔 POZVONI
- Simulira pozivanje vlasnika/stanara
- Nakon klika prikazuje se status: "📞 Pozivam vlasnika..."
- Nakon 3 sekunde: "⚠️ Nitko se ne javlja."

**Kako koristiti:**
1. Klikni na narančasti "🔔 POZVONI" gumb
2. Pričekaj odgovor (simulacija)
3. Sistem će prikazati rezultat poziva

#### 🔐 OTKLJUČAJ
- Otvara ekran za unos PIN koda
- Vodi do autentifikacije

**Kako koristiti:**
1. Klikni na zeleni "🔐 OTKLJUČAJ" gumb
2. Otvara se numerička tipkovnica

### Status Poruka
- Prikazuje trenutno stanje sistema
- Najčešće poruke:
  - "Sustav spreman." - sve OK
  - "Pozivam vlasnika..." - poziv u tijeku
  - "Tema: Dark Mode 🌙" - promijenjena tema

### 🌙☀️ Dark/Light Mode Selektor

**Lokacija:** Footer ekrana (dolje)

**Opcije:**
- **🌙 Dark** - Tamna tema (default)
- **☀️ Light** - Svijetla tema

**Kako promijeniti temu:**
1. Klikni na željenu opciju (Dark/Light)
2. Aplikacija odmah primijeni novu temu
3. Status poruka potvrđuje promjenu

---

## 🔢 PIN Pad Screen (Unos Šifre)

Nakon klika na "OTKLJUČAJ", otvara se ekran za unos PIN-a.

### Elementi Ekrana

**Naslov:** "UNESITE PIN"

**PIN Display:** 
- Prikazuje uneseni PIN kao točke (••••)
- Crtice (_) označavaju preostala polja
- Primjer: "•••_" znači 3 znaka unesena, 1 preostao

### Numerička Tipkovnica

**Layout:**
```
1   2   3
4   5   6
7   8   9
C   0   <
```

**Gumbi:**

- **0-9** - Unos brojeva
- **C** (crveno) - Čisti cijeli unos
- **<** (žuto) - Briše zadnju unesenu brojku

### Proces Unosa

1. **Klikni brojeve** za unos PIN-a
2. **Vidi feedback** - svaki klik prikazuje točku (•)
3. **Automatska provjera** - nakon 4 znaka sistem automatski provjerava PIN

### Greška pri Unosu

Ako unesete **pogrešan PIN**:
- Display će prikazati "ERR" u crvenoj boji
- Nakon 0.5 sekundi display se vraća u normalu
- Nakon 0.8 sekundi unos se automatski briše
- Možete pokušati ponovo

### Ispravno Uneseni PIN

**Ako je PIN točan:**

**Admin PIN (0953):**
- Otvara se Admin Panel
- Pristup upravljanju korisnicima

**Korisnički PIN:**
- Prikazuje se zeleni "Unlock" ekran
- Potvrđuje uspješan pristup

### Natrag Gumb

- Lokacija: Dolje lijevo
- Vraća vas na Welcome ekran
- Ne sprema uneseni PIN

---

## ✅ Unlock Screen (Uspješan Pristup)

Kada unesete **korisnički PIN** (ne admin), vidite:

### Elementi Ekrana

**Pozadina:** Zelena (#27AE60)

**Ikona:** 🔓 Velika ikona otključane brave

**Poruka:** "DOBRODOŠLI"

**Ime korisnika:** Prikazuje se ime prijavljenog korisnika

### Automatski Povratak

- **Vrijeme:** 4 sekunde
- **Akcija:** Vraća se na Welcome ekran
- **Razlog:** Sigurnost - ne ostavljaj otvorenim

**Primjer toka:**
```
1. Uneseš PIN: 5678
2. Vidiš: "DOBRODOŠLI - Marko"
3. Nakon 4s: Povratak na Welcome
```

---

## 🛡️ Admin Panel

Najmoćniji dio aplikacije - dostupan samo administratorima!

### Pristup Admin Panelu

**PIN:** `0953` (defaultni admin)

### Elementi Ekrana

#### Header (Vrh Ekrana)

**Lijevo:**
- 🛡️ Admin ikona
- "ADMIN PANEL" naslov

**Desno:**
- "Odjava" gumb (crveni)
- Vraća te na Welcome ekran

**Ispod headera:**
- "Prijavljen: pyZ3R" (tvoje admin ime)

#### Forma za Dodavanje Korisnika

**Polja:**
1. **Ime korisnika** - Unesite ime (npr. "Marko Marić")
2. **PIN** - Unesite 4-znamenkasti PIN (npr. "1234")

**Gumb:** "+ DODAJ" (plavi)

**Kako dodati novog korisnika:**
1. Upiši ime u prvo polje
2. Upiši PIN (4 broja) u drugo polje
3. Klikni "+ DODAJ"
4. Korisnik se pojavljuje u listi dolje

**Validacije:**
- ✅ Ime ne smije biti prazno
- ✅ PIN ne smije biti prazan
- ✅ PIN mora biti jedinstven (neće dopustiti duplikat)

**Primjer:**
```
Ime: Marko Marić
PIN: 5678
[+ DODAJ]
```

#### Lista Korisnika (Scrollable)

**Prikaz svakog korisnika:**

```
🛡️ pyZ3R          PIN: 0953     [X]
👤 Marko Marić    PIN: 5678     [X]
```

**Ikone:**
- 🛡️ - Admin korisnik (ljubičasta ikona)
- 👤 - Obični korisnik (plava ikona)

**Informacije:**
- Ime korisnika
- PIN kod
- Delete gumb ([X])

**Delete Gumb:**
- Crveni X
- Klik otvara potvrdu: "Obrisati ovog korisnika?"
- Potvrdi sa "Da" ili odustani sa "Ne"

### Sigurnosne Mjere

#### ⚠️ Zaštita Zadnjeg Admina

**Scenario:**
- Imaš samo 1 admin korisnika u bazi
- Pokušavaš obrisati tog admina

**Što se dogodi:**
- Sistem pokazuje grešku: "Ne možeš obrisati zadnjeg admina!"
- Admin ostaje u bazi
- **Razlog:** Sustav mora imati barem 1 admina

#### Jedinstveni PIN-ovi

**Scenario:**
- Pokušavaš dodati korisnika sa PIN-om koji već postoji

**Što se dogodi:**
- Greška: "Taj PIN već postoji!"
- Korisnik se NE dodaje
- **Razlog:** Svaki korisnik mora imati jedinstven PIN

### Odjava

**Kako se odjaviti:**
1. Klikni "Odjava" gumb (gore desno, crveni)
2. Vraćaš se na Welcome ekran
3. PIN se ne pamti

---

## 💡 Savjeti i Trikovi

### 1. Brzi Pristup Admin Panelu

Zapamti zadani admin PIN: **0953**

### 2. Testiranje Sistema

**Koraci:**
1. Dodaj test korisnika (npr. "Test User", PIN: "1111")
2. Odjavi se iz Admin Panela
3. Na Welcome ekranu klikni "OTKLJUČAJ"
4. Unesi PIN "1111"
5. Vidi zeleni Unlock ekran sa imenom "Test User"

### 3. Upravljanje Korisnicima

**Best Practice:**
- Koristi памtljive PIN-ove za obične korisnike (1234, 5678, itd.)
- Admin PIN drži tajnim (0953)
- Redovno brišiinaktivne korisnike

### 4. Prebacivanje Tema

**Za testiranje:**
- Probaj Dark i Light mode
- Vidi kako se ikone ponašaju na različitim temama
- Light mode može biti bolji pri jakom svjetlu

---

## ❓ Česta Pitanja (FAQ)

### Q1: Zaboravio sam admin PIN?

**A:** Defaultni admin PIN je uvijek **0953**. Ako si ga promijenio i zaboravio:
1. Obriši `smart_lock.db` fajl
2. Pokreni aplikaciju ponovno
3. Sistem će kreirati novog admina sa PIN-om 0953

### Q2: Kako promijeniti svoj PIN?

**A:** Trenutno nema "promijeni PIN" opcije. Workaround:
1. Ulogiraj se kao admin (PIN: 0953)
2. Obriši starog korisnika
3. Dodaj novog sa istim imenom ali novim PIN-om

### Q3: Mogu li imati više admina?

**A:** Da! Admin može dodati nove korisnike. Da bi bio admin:
1. Moraš ručno promijeniti role u bazi (napredno)
2. Ili modificirati `database.py` da doda admin opciju

### Q4: Koliko korisnika mogu imati?

**A:** Nema teoretskog limita. Lista je scrollable, tako da može imati stotine korisnika.

### Q5: Aplikacija ne reagira na klikove?

**A:** 
1. Zatvori aplikaciju
2. Pokreni ponovo sa `run.bat` ili `run.ps1`
3. Ako problem persista, restart računala

### Q6: Tipkovnica na PIN padu ne radi?

**A:**
- Moraš koristiti miš
- Lambda funkcije možda ne rade - restartuj app

### Q7: Kako resetirati sve podatke?

**A:**
1. Zatvori aplikaciju
2. Obriši `smart_lock.db`
3. Pokreni aplikaciju
4. Sistem kreira novu bazu sa default adminom

---

## 🎯 Napredne Funkcionalnosti

### PIN Format

**Dopušteno:**
- Bilo koji broj dužine 4 ili više znakova
- Samo numerički znakovi (0-9)

**Preporuke:**
- Koristi 4-znamenkaste PIN-ove za jednostavnost
- Izbjegavaj očite kombinacije (1111, 0000)
- Ne koristi datume rođenja

### Baza Podataka

**Lokacija:** `smart_lock.db`

**Struktura:**
```sql
TABLE users:
  - id (INTEGER PRIMARY KEY)
  - name (TEXT)
  - pin (TEXT UNIQUE)
  - role ('admin' ili 'user')
```

**Backup:**
1. Zatvori aplikaciju
2. Kopiraj `smart_lock.db` na sigurno mjesto
3. Restore: Vrati kopirani fajl u root folder

---

## 🔐 Sigurnost

### Best Practices

**DO:**
✅ Drži admin PIN tajnim
✅ Redovno mijenjaj PIN-ove
✅ Backup bazu redovno
✅ Brišiinaktivne korisnike
✅ Koristi jake PIN-ove (ne 1234)

**DON'T:**
❌ Ne dijeli admin pristup
❌ Ne koristi iste PIN-ove
❌ Ne ostavljaj app otvorenim bez nadzora
❌ Ne koristi očite PIN-ove

---

## 📞 Podrška

Za dodatnu pomoć:
- Provjeri GitHub Issues
- Kontaktiraj PyZ3R tim
- Pročitaj CHANGELOG.md za najnovije izmjene

---

**Smart Key v2.0 - Hacijenda PyZ3R**  
*Developed by PyZ3R @ Algebra 2026*
