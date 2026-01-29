# Smart Key

Simulacija pametne brave u Pythonu.

## Opis rada

Aplikacija je pisana u Tkinter ili Custom Tkinter okviru. Kada se pokrene otvori se pozdravna poruka koja omogućava krajnjem korisniku da pozvoni, odnosno pozove nekoga u kući. Kada klikne na poyvoni gumb, onda se pokaže poruka o statusu. Na primjer poyivam korisnika ili može poyvati i na telefon pa će se vlasnik javiti i razgovarati s onim ispred njegovog stana.

Drugi gumb je za otključavanje vrata i klik na njega otvara srednji frame u kojem se nalazi numberička tipkovnica s brojevima od 0 do 9 i C gumbom za poništavanje cijelog unosa te još jednim < gumbom koji briše zadnje unesenu brojku pina.

Ako se unese pin običnog korisnika, onda se otključaju vrata, a ako se unese admin pin onda se otvori zadnji frame u kojem se nalzi lista svih osoba koje imaju pravo ulaska i forma koja omogućava creiranje, editiranje i brisanje tih podataka.

Svi podaci se nalaze u bazi i prilikom pokretanja aplikacije se učitaju iz baze.