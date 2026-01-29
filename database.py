import sqlite3
import os

DB_NAME = "smart_lock.db"


class DatabaseManager:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.init_db()

    def connect(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def init_db(self):
        """Kreira tablicu i defaultnog admina (0953) ako ne postoji."""
        self.connect()
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    pin TEXT UNIQUE NOT NULL,
                    role TEXT NOT NULL CHECK(role IN ('admin', 'user'))
                )
            """)
            
            # Provjeri postoji li Admin, ako ne, kreiraj ga
            self.cursor.execute("SELECT * FROM users WHERE role='admin'")
            if not self.cursor.fetchone():
                self.cursor.execute(
                    "INSERT INTO users (name, pin, role) VALUES (?, ?, ?)",
                    ("pyZ3R", "0953", "admin")
                )
                print("[DB] Kreiran default admin (PIN: 0953)")
            
            self.conn.commit()
        except Exception as e:
            print(f"[DB Error] {e}")
        finally:
            self.disconnect()

    def check_pin(self, pin):
        """Provjerava PIN i vraća podatke o korisniku ili None."""
        self.connect()
        try:
            self.cursor.execute(
                "SELECT id, name, role FROM users WHERE pin = ?",
                (pin,)
            )
            data = self.cursor.fetchone()
            if data:
                return {"id": data[0], "name": data[1], "role": data[2]}
            return None
        finally:
            self.disconnect()

    def get_all_users(self):
        self.connect()
        try:
            self.cursor.execute(
                "SELECT id, name, pin, role FROM users"
            )
            return self.cursor.fetchall()
        finally:
            self.disconnect()

    def add_user(self, name, pin, role="user"):
        self.connect()
        try:
            self.cursor.execute(
                "INSERT INTO users (name, pin, role) VALUES (?, ?, ?)",
                (name, pin, role)
            )
            self.conn.commit()
            return True, "Korisnik uspješno dodan."
        except sqlite3.IntegrityError:
            return False, "Taj PIN već postoji!"
        except Exception as e:
            return False, str(e)
        finally:
            self.disconnect()

    def delete_user(self, user_id):
        self.connect()
        try:
            # Sigurnost: Ne briši zadnjeg admina
            self.cursor.execute(
                "SELECT role FROM users WHERE id=?",
                (user_id,)
            )
            role_data = self.cursor.fetchone()
            
            if role_data and role_data[0] == 'admin':
                self.cursor.execute(
                    "SELECT count(*) FROM users WHERE role='admin'"
                )
                if self.cursor.fetchone()[0] <= 1:
                    return False, "Ne možeš obrisati zadnjeg admina!"

            self.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            self.conn.commit()
            return True, "Korisnik obrisan."
        finally:
            self.disconnect()
