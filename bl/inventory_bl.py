import sqlite3
from tkinter import Tk, Label, Entry, Button, messagebox
import os

DATABASE_DIR = 'database'

class AddReceiver:
    def __init__ (self, number, code, title):
        self.number = number
        self.code = code
        self.title = title
        
        self.setup_database() 
        self.save_to_database()


    def setup_database(self):

        DATABASE_DIR = 'database'
        DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')
        connection = sqlite3.connect(DATABASE_PATH)

        cursor = connection.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS receiver (
            number INTEGER ,
            code INTEGER,
            title TEXT NOT NULL
        )
        ''')

        cursor.close()

    def save_to_database(self):

        DATABASE_DIR = 'database'
        DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
     
        cursor.execute('''
        INSERT INTO receiver (number, code, title) VALUES (?, ?, ?)
        ''', (self.number, self.code, self.title))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data saved successfully!")

class DeleteReceiver:
    def __init__ (self, number, code, title):
        self.number = number
        self.code = code
        self.title = title
        
        self.delete_row_database()


    def delete_row_database(self):

        DATABASE_DIR = 'database'
        DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
     
        cursor.execute('''
        DELETE FROM receiver WHERE number = ? AND code = ? AND title = ?
        ''', (self.number, self.code, self.title))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data deleted successfully!")

class AddStock:
    def __init__ (self, code, kala_name, number, unit):
        self.code = code
        self.kala_name = kala_name
        self.number = number
        self.unit = unit
        
        self.setup_database() 
        self.save_to_database()


    def setup_database(self):

        DATABASE_DIR = 'database'
        DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')
        connection = sqlite3.connect(DATABASE_PATH)

        cursor = connection.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock (
            code INTEGER ,
            kala TEXT NOT NULL,
            number INTEGER,
            unit TEXT NOT NULL
        )
        ''')

        cursor.close()

    def save_to_database(self):

        DATABASE_DIR = 'database'
        DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
    
        cursor.execute('''
        INSERT INTO stock (code, kala, number, unit) VALUES (?, ?, ?, ?)
        ''', ( self.code, self.kala_name, self.number, self.unit))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data saved successfully!")

class DeleteStock:
    def __init__ (self, code, kala_name, number, unit):
        self.code = code
        self.kala_name = kala_name
        self.number = number
        self.unit = unit
        
        self.delete_row_database()


    def delete_row_database(self):

        DATABASE_DIR = 'database'
        DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
     
        cursor.execute('''
        DELETE FROM stock WHERE code = ? AND kala = ? AND number = ? AND unit = ?
        ''', (self.code, self.kala_name, self.number, self.unit))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data deleted successfully!")

class AddDepository:
    def __init__ (self, number, date , reciev_code , reciev_name , desc):
        self.number = number
        self.date = date
        self.reciev_code = reciev_code
        self.reciev_name = reciev_name
        self.desc = desc
        
        self.setup_database() 
        self.save_to_database()


    def setup_database(self):

        DATABASE_DIR = 'database'
        DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')
        connection = sqlite3.connect(DATABASE_PATH)

        cursor = connection.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS depository (
            number INTEGER ,
            date text,
            recievercode TEXT NOT NULL,
            recievername TEXT NOT NULL,
            desc TEXT NOT NULL
        
        )
        ''')

        cursor.close()

    def save_to_database(self):

        DATABASE_DIR = 'database'
        DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
     
        cursor.execute('''
        INSERT INTO depository (number, date, recievercode, recievername, desc) VALUES (?, ?, ?, ?, ?)
        ''', (self.number, self.date, self.reciev_code, self.reciev_name, self.desc))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data saved successfully!")

class DeleteDepository:
    def __init__ (self, number, date , reciev_code , reciev_name , desc):
        self.number = number
        self.date = date
        self.reciev_code = reciev_code
        self.reciev_name = reciev_name
        self.desc = desc
        
        self.delete_row_database()


    def delete_row_database(self):

        DATABASE_DIR = 'database'
        DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
     
        cursor.execute('''
        DELETE FROM depository WHERE number = ? AND date = ? AND recievercode = ? AND recievername = ? AND desc = ?
        ''', ( self.number, self.date, self.reciev_code, self.reciev_name, self.desc))

        table_name = f'dep{self.number}'
        print(table_name)

        cursor.execute(f"SELECT kalacode, unit FROM {table_name}")
        items = cursor.fetchall()
        

        for item in items:

            cursor.execute(f"""
            SELECT number
            FROM stock
            WHERE code = ?;
            """, (item[0],))

            result = cursor.fetchone()

            new_value = result[0] + int(item[1])
            condition_value = item[0]

            
            cursor.execute(f"""
                UPDATE stock
                SET number = ?
                WHERE code = ?;
            """, (new_value, condition_value))




        try:
            cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
        except sqlite3.Error as e:
            print(f"خطا در حذف جدول: {e}")
    
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data deleted successfully!")

class AddDepositoryExit:
    def __init__ (self, number, kalacode , kalaname , unit , moeincode, moeinname, id_):
        self.number = number
        self.kalacode = kalacode
        self.kalaname = kalaname
        self.unit = unit
        self.moeincode = moeincode
        self.moeinname = moeinname
        self.id_dep = id_
        
        self.setup_database() 
        self.save_to_database()


    def setup_database(self):

        DATABASE_DIR = 'database'
        DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {self.id_dep} (
            number INTEGER ,
            kalacode INTEGER,
            kalaname TEXT NOT NULL,
            unit TEXT NOT NULL,
            moeincode INTEGER,
            moeinname TEXT NOT NULL
        )
        ''')

        cursor.close()

    def save_to_database(self):

        DATABASE_DIR = 'database'
        DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
     
        cursor.execute(f'''
        INSERT INTO {self.id_dep} (number , kalacode , kalaname , unit, moeincode , moeinname) VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.number , self.kalacode , self.kalaname , self.unit , self.moeincode , self.moeinname))

        cursor.execute(f"""
            SELECT number
            FROM stock
            WHERE code = ?;
        """, (self.kalacode,))

        result = cursor.fetchone()

        new_value = result[0] - self.unit
        condition_value = self.kalacode

        
        cursor.execute(f"""
            UPDATE stock
            SET number = ?
            WHERE code = ?;
        """, (new_value, condition_value))



        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data saved successfully!")

class DeleteDepositoryExit:
    def __init__ (self, number, kalacode , kalaname , unit , moeincode, moeinname, id_):
        self.number = number
        self.kalacode = kalacode
        self.kalaname = kalaname
        self.unit = unit
        self.moeincode = moeincode
        self.moeinname = moeinname
        self.id_dep = id_
        
        self.delete_row_database()


    def delete_row_database(self):

        DATABASE_DIR = 'database'
        DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
     
        cursor.execute(f'''
        DELETE FROM {self.id_dep} WHERE number = ? AND kalacode = ? AND kalaname = ? AND unit = ? AND moeincode = ? AND moeinname = ?
        ''', (self.number , self.kalacode , self.kalaname , self.unit , self.moeincode , self.moeinname))

        cursor.execute(f"""
            SELECT number
            FROM stock
            WHERE code = ?;
        """, (self.kalacode,))

        result = cursor.fetchone()

        new_value = result[0] + int(self.unit)
        condition_value = self.kalacode

        
        cursor.execute(f"""
            UPDATE stock
            SET number = ?
            WHERE code = ?;
        """, (new_value, condition_value))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data deleted successfully!")

class AddMoein:
    def __init__ (self, number, code, title):
        self.number = number
        self.code = code
        self.title = title
        
        self.setup_database() 
        self.save_to_database()


    def setup_database(self):

        DATABASE_DIR = 'database'
        DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')
        connection = sqlite3.connect(DATABASE_PATH)

        cursor = connection.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS moein (
            number INTEGER ,
            code INTEGER,
            title TEXT NOT NULL
        )
        ''')

        cursor.close()

    def save_to_database(self):

        DATABASE_DIR = 'database'
        DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
     
        cursor.execute('''
        INSERT INTO moein (number, code, title) VALUES (?, ?, ?)
        ''', (self.number, self.code, self.title))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data saved successfully!")

class DeleteMoein:
    def __init__ (self, number, code, title):
        self.number = number
        self.code = code
        self.title = title
        
        self.delete_row_database()


    def delete_row_database(self):

        DATABASE_DIR = 'database'
        DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
     
        cursor.execute('''
        DELETE FROM moein WHERE number = ? AND code = ? AND title = ?
        ''', (self.number, self.code, self.title))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data deleted successfully!")
