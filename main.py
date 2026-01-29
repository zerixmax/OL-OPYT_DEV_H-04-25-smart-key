import customtkinter as ctk
from tkinter import messagebox
from database import DatabaseManager
from PIL import Image
import os

# --- POKUŠAJ IMPORTA ZA BRENDING ---
try:
    from pyfiglet import figlet_format
    from colorama import Fore, Style, init
    HAS_BRANDING = True
except ImportError:
    HAS_BRANDING = False

# --- KONFIGURACIJA ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class SmartKeyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Setup Prozora
        self.title("Smart Key - PyZ3R Security v2.0")
        self.geometry("450x700")
        self.resizable(False, False)
        
        # Inicijalizacija Baze
        self.db = DatabaseManager()
        
        # Ispis potpisa
        self.print_startup_signature()

        # --- UČITAVANJE IKONA ---
        self.icons = self.load_icons()

        # Varijable
        self.current_pin = ""
        self.current_frame = None

        # Pokreni prvi ekran
        self.show_welcome_screen()

    def load_icons(self):
        """Učitava slike iz assets foldera u CTkImage objekte."""
        icons = {}
        
        def get_img(name, size=(30, 30)):
            """Pomoćna funkcija za sigurno učitavanje."""
            path = f"assets/{name}.png"
            if os.path.exists(path):
                return ctk.CTkImage(
                    light_image=Image.open(path),
                    dark_image=Image.open(path),
                    size=size
                )
            return None  # Vraća None ako slika ne postoji

        icons['bell'] = get_img('bell', (40, 40))
        icons['unlock'] = get_img('lock', (40, 40))
        icons['locked'] = get_img('lock_closed', (80, 80))
        icons['user'] = get_img('user', (24, 24))
        icons['admin'] = get_img('admin', (24, 24))
        icons['delete'] = get_img('delete', (20, 20))
        return icons

    def print_startup_signature(self):
        """Ispisuje PyZ3R potpis u konzolu."""
        if HAS_BRANDING:
            try:
                init(autoreset=True)
                GREEN = Fore.GREEN
                RESET = Style.RESET_ALL
                print("=" * 50)
                print(GREEN + figlet_format("SmartKey", font="slant") + RESET)
                print(f"{GREEN}PyZ3R Security System v2.0 with Icons{RESET}")
                print("=" * 50)
            except Exception:
                print("--- SmartKey v2.0 Started ---")
        else:
            print("=" * 50)
            print("SmartKey - PyZ3R Security v2.0 with Icons")
            print("=" * 50)

    def clear_screen(self):
        """Briše trenutni frame kako bi se prikazao novi."""
        if self.current_frame:
            self.current_frame.pack_forget()
            self.current_frame.destroy()
        self.current_frame = None

    # ==========================================
    # 1. WELCOME SCREEN (Pozvoni / Otključaj)
    # ==========================================
    def show_welcome_screen(self):
        self.clear_screen()
        
        self.current_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Logo / Header
        if self.icons['locked']:
            ctk.CTkLabel(
                self.current_frame,
                text="",
                image=self.icons['locked']
            ).pack(pady=(40, 10))
        
        title_label = ctk.CTkLabel(
            self.current_frame,
            text="SMART LOCK",
            font=("Roboto", 30, "bold"),
            text_color="#3B8ED0"
        )
        title_label.pack()
        
        subtitle_label = ctk.CTkLabel(
            self.current_frame,
            text="Hacijenda PyZ3R",
            font=("Roboto", 16),
            text_color="gray"
        )
        subtitle_label.pack(pady=(0, 50))

        # Gumbi s ikonama
        btn_ring = ctk.CTkButton(
            self.current_frame,
            text=" POZVONI",
            image=self.icons['bell'],
            compound="left",
            height=60,
            width=280,
            font=("Roboto", 20, "bold"),
            fg_color="#E67E22",
            hover_color="#D35400",
            command=self.action_ring
        )
        btn_ring.pack(pady=15)

        btn_unlock = ctk.CTkButton(
            self.current_frame,
            text=" OTKLJUČAJ",
            image=self.icons['unlock'],
            compound="left",
            height=60,
            width=280,
            font=("Roboto", 20, "bold"),
            fg_color="#27AE60",
            hover_color="#2ECC71",
            command=self.show_pinpad_screen
        )
        btn_unlock.pack(pady=15)

        # Status Poruka
        self.lbl_status = ctk.CTkLabel(
            self.current_frame,
            text="Sustav spreman.",
            font=("Consolas", 12),
            text_color="gray"
        )
        self.lbl_status.pack(side="bottom", pady=5)
        
        # Dark/Light Mode Selektor
        mode_frame = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        mode_frame.pack(side="bottom", pady=10)
        
        ctk.CTkLabel(
            mode_frame,
            text="Tema:",
            font=("Roboto", 10),
            text_color="gray"
        ).pack(side="left", padx=5)
        
        self.mode_switch = ctk.CTkSegmentedButton(
            mode_frame,
            values=["🌙 Dark", "☀️ Light"],
            command=self.change_theme,
            selected_color="#3B8ED0",
            selected_hover_color="#2E7CBF",
            font=("Roboto", 10)
        )
        self.mode_switch.set("🌙 Dark")
        self.mode_switch.pack(side="left", padx=5)
        
        # Footer Potpis
        footer_label = ctk.CTkLabel(
            self.current_frame,
            text="Dev: PyZ3R © 2026",
            font=("Roboto", 10),
            text_color="#333"
        )
        footer_label.pack(side="bottom")

    def change_theme(self, value):
        """Mijenja temu aplikacije."""
        if value == "🌙 Dark":
            ctk.set_appearance_mode("Dark")
            self.lbl_status.configure(text="Tema: Dark Mode 🌙")
        else:
            ctk.set_appearance_mode("Light")
            self.lbl_status.configure(text="Tema: Light Mode ☀️")
        
        # Resetuj status nakon 2 sekunde
        self.after(2000, lambda: self.lbl_status.configure(
            text="Sustav spreman."
        ))

    def action_ring(self):
        self.lbl_status.configure(
            text="📞 Pozivam vlasnika...",
            text_color="#3498DB"
        )
        # Simulacija čekanja
        self.after(3000, lambda: self.lbl_status.configure(
            text="⚠️ Nitko se ne javlja.",
            text_color="#E74C3C"
        ))

    # ==========================================
    # 2. PIN PAD SCREEN (Unos Šifre)
    # ==========================================
    def show_pinpad_screen(self):
        self.clear_screen()
        self.current_pin = ""  # Reset

        self.current_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Display
        pin_title = ctk.CTkLabel(
            self.current_frame,
            text="UNESITE PIN",
            font=("Roboto", 24, "bold")
        )
        pin_title.pack(pady=(30, 20))
        
        self.lbl_pin_display = ctk.CTkLabel(
            self.current_frame,
            text="____",
            font=("Consolas", 42),
            text_color="#3B8ED0"
        )
        self.lbl_pin_display.pack(pady=(0, 30))

        # Tipkovnica (Grid)
        keypad_frame = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        keypad_frame.pack()

        buttons = [
            ('1', '2', '3'),
            ('4', '5', '6'),
            ('7', '8', '9'),
            ('C', '0', '<')
        ]

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                text_col = "white"
                border_col = "#444"
                
                if char == 'C':
                    text_col = "#E74C3C"  # Crveno
                if char == '<':
                    text_col = "#F1C40F"  # Žuto

                cmd = lambda x=char: self.process_key(x)
                
                # Malo veći gumbi i zaobljeni
                btn = ctk.CTkButton(
                    keypad_frame,
                    text=char,
                    width=75,
                    height=75,
                    corner_radius=20,
                    font=("Roboto", 26, "bold"),
                    fg_color="#2B2B2B" if char not in ['C', '<'] else "transparent",
                    border_width=2,
                    border_color=border_col,
                    text_color=text_col,
                    command=cmd
                )
                btn.grid(row=r, column=c, padx=8, pady=8)

        # Back gumb
        back_btn = ctk.CTkButton(
            self.current_frame,
            text="Natrag",
            fg_color="transparent",
            text_color="gray",
            hover_color="#333",
            command=self.show_welcome_screen
        )
        back_btn.pack(side="bottom", pady=20)

    def process_key(self, key):
        if key == 'C':
            self.current_pin = ""
        elif key == '<':
            self.current_pin = self.current_pin[:-1]
        else:
            if len(self.current_pin) < 6:
                self.current_pin += key
        
        self.update_pin_ui()

        # Automatska provjera ako je duljina 4 ili više
        if len(self.current_pin) >= 4:
            self.check_pin_db()

    def update_pin_ui(self):
        # Prikazuj zvjezdice ili crtice
        masked = "•" * len(self.current_pin)
        placeholder = "_" * (4 - len(self.current_pin)) if len(
            self.current_pin
        ) < 4 else ""
        self.lbl_pin_display.configure(text=f"{masked}{placeholder}")

    def check_pin_db(self):
        user = self.db.check_pin(self.current_pin)
        
        if user:
            if user['role'] == 'admin':
                self.show_admin_screen(user['name'])
            else:
                self.show_unlocked_screen(user['name'])
        else:
            # Ako je duljina 4, a nije točno -> Greška
            if len(self.current_pin) == 4:
                self.lbl_pin_display.configure(text="ERR", text_color="red")
                self.after(500, lambda: self.lbl_pin_display.configure(
                    text_color="#3B8ED0"
                ))
                self.after(800, lambda: self.process_key('C'))

    # ==========================================
    # 3. UNLOCKED SCREEN (Zeleno)
    # ==========================================
    def show_unlocked_screen(self, name):
        self.clear_screen()
        
        self.current_frame = ctk.CTkFrame(
            self,
            fg_color="#27AE60"
        )  # Zelena pozadina
        self.current_frame.pack(fill="both", expand=True)

        lock_icon = ctk.CTkLabel(
            self.current_frame,
            text="🔓",
            font=("Roboto", 80)
        )
        lock_icon.pack(pady=(150, 20))
        
        welcome_label = ctk.CTkLabel(
            self.current_frame,
            text="DOBRODOŠLI",
            font=("Roboto", 30, "bold"),
            text_color="white"
        )
        welcome_label.pack()
        
        name_label = ctk.CTkLabel(
            self.current_frame,
            text=name,
            font=("Roboto", 20),
            text_color="#DAF7A6"
        )
        name_label.pack(pady=10)

        # Auto povratak
        self.after(4000, self.show_welcome_screen)

    # ==========================================
    # 4. ADMIN PANEL (CRUD)
    # ==========================================
    def show_admin_screen(self, admin_name):
        self.clear_screen()
        
        self.current_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.current_frame.pack(fill="both", expand=True, padx=15, pady=15)

        # Header
        top = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        top.pack(fill="x", pady=10)
        
        # Prikaz Admin ikone
        ctk.CTkLabel(
            top,
            text="",
            image=self.icons['admin']
        ).pack(side="left", padx=5)
        
        admin_title = ctk.CTkLabel(
            top,
            text="ADMIN PANEL",
            font=("Roboto", 24, "bold")
        )
        admin_title.pack(side="left")
        
        logout_btn = ctk.CTkButton(
            top,
            text="Odjava",
            width=80,
            fg_color="#C0392B",
            command=self.show_welcome_screen
        )
        logout_btn.pack(side="right")
        
        admin_info = ctk.CTkLabel(
            self.current_frame,
            text=f"Prijavljen: {admin_name}",
            font=("Roboto", 12),
            text_color="gray"
        )
        admin_info.pack(anchor="w", pady=(0, 20))

        # Add User Form
        form_frame = ctk.CTkFrame(self.current_frame)
        form_frame.pack(fill="x", pady=10, padx=5)
        
        self.entry_name = ctk.CTkEntry(
            form_frame,
            placeholder_text="Ime korisnika",
            height=40
        )
        self.entry_name.pack(side="left", fill="x", expand=True, padx=5, pady=10)
        
        self.entry_pin = ctk.CTkEntry(
            form_frame,
            placeholder_text="PIN",
            width=80,
            height=40
        )
        self.entry_pin.pack(side="left", padx=5, pady=10)
        
        add_btn = ctk.CTkButton(
            form_frame,
            text="+ DODAJ",
            width=80,
            height=40,
            fg_color="#2980B9",
            command=self.add_new_user
        )
        add_btn.pack(side="right", padx=5, pady=10)

        # Lista (Scrollable)
        list_title = ctk.CTkLabel(
            self.current_frame,
            text="Korisnici u bazi:",
            anchor="w"
        )
        list_title.pack(fill="x", pady=(10, 5))
        
        self.scroll_frame = ctk.CTkScrollableFrame(self.current_frame)
        self.scroll_frame.pack(fill="both", expand=True)

        self.refresh_user_list()

    def refresh_user_list(self):
        for w in self.scroll_frame.winfo_children():
            w.destroy()
            
        users = self.db.get_all_users()
        
        for u in users:
            uid, name, pin, role = u
            row = ctk.CTkFrame(
                self.scroll_frame,
                fg_color=("gray85", "gray25")
            )
            row.pack(fill="x", pady=3)
            
            # Ikona ovisno o roli
            role_icon = self.icons['admin'] if role == 'admin' else self.icons['user']
            
            # Lijevi dio s ikonom i imenom
            left_cont = ctk.CTkFrame(row, fg_color="transparent")
            left_cont.pack(side="left", padx=5)
            
            ctk.CTkLabel(
                left_cont,
                text="",
                image=role_icon
            ).pack(side="left", padx=5)
            
            ctk.CTkLabel(
                left_cont,
                text=name,
                font=("Roboto", 14, "bold")
            ).pack(side="left")

            # Desni dio PIN i Delete
            delete_btn = ctk.CTkButton(
                row,
                text="",
                image=self.icons['delete'],
                width=40,
                height=30,
                fg_color="transparent",
                hover_color="#555",
                command=lambda x=uid: self.delete_user(x)
            )
            delete_btn.pack(side="right", padx=10, pady=5)
            
            pin_label = ctk.CTkLabel(
                row,
                text=f"PIN: {pin}",
                font=("Consolas", 12),
                text_color="gray"
            )
            pin_label.pack(side="right", padx=10)

    def add_new_user(self):
        name = self.entry_name.get()
        pin = self.entry_pin.get()
        
        if not name or not pin:
            messagebox.showerror("Greška", "Unesi ime i PIN!")
            return
            
        ok, msg = self.db.add_user(name, pin)
        if ok:
            self.entry_name.delete(0, 'end')
            self.entry_pin.delete(0, 'end')
            self.refresh_user_list()
        else:
            messagebox.showerror("Greška", msg)

    def delete_user(self, uid):
        if messagebox.askyesno("Potvrdi", "Obrisati ovog korisnika?"):
            ok, msg = self.db.delete_user(uid)
            if ok:
                self.refresh_user_list()
            else:
                messagebox.showerror("Greška", msg)


if __name__ == "__main__":
    app = SmartKeyApp()
    app.mainloop()
