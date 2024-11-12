import sqlite3
from tkinter import Tk, Label, Entry, Button, messagebox
from bl.inventory_bl import AddReceiver, AddStock, DeleteReceiver, DeleteStock, AddDepository, DeleteDepository, AddDepositoryExit, DeleteDepositoryExit, AddMoein, DeleteMoein
from tkinter.messagebox import showerror, showinfo
import tkinter.messagebox as msg
import os


class CheckAddReveiver:
    def __init__(self, number, code, title):
        self.number = number
        self.code = code
        self.title = title

        self.check()

    def check(self):

        error = False
         
        if not self.number or not self.code or not self.title:
            messagebox.showerror("Error", "All fields are required!")
            error = True

            return
        try:
            self.code = int(self.code)  # تبدیل سن به عدد صحیح
        except ValueError:
            messagebox.showerror("Error", "code must be a number!")
            error = True
            return
        
        try:
            self.number = int(self.number)  # تبدیل سن به عدد صحیح
        except ValueError:
            messagebox.showerror("Error", "just number!")
            error = True
            return
        
        if not error:
            AddReceiver(number = self.number, code= self.code, title= self.title)
            
class CheckDeleteReveiver:
    def __init__(self, number, code, title):
        self.number = number
        self.code = code
        self.title = title

        self.check()

    def check(self):

        message = (f'number: {self.number} \ncode: {self.code} \ntitle: {self.title}\nAre you sure you want to delete this row?')
        confirm = msg.askyesno(title='Confirmation', message=message)
        if confirm:
            DeleteReceiver(number = self.number, code= self.code, title= self.title)
            
class CheckStock:
    def __init__(self, code, kala_name, number, unit):
        self.code = code
        self.kala_name = kala_name
        self.number = number
        self.unit = unit

        self.check()

    def check(self):

        error = False
         
        if not self.code or not self.kala_name or not self.number or not self.unit:
            messagebox.showerror("Error", "All fields are required!")
            error = True

            return
       
        
        try:
            self.number = int(self.number)  # تبدیل سن به عدد صحیح
        except ValueError:
            messagebox.showerror("Error", "just number!")
            error = True
            return
        
        if not error:
            AddStock(code =self.code , kala_name =self.kala_name , number=self.number ,  unit=self.unit)

class CheckDeleteStock:
    def __init__(self, code, kala_name, number, unit):
        self.code = code
        self.kala_name = kala_name
        self.number = number
        self.unit = unit

        self.check()

    def check(self):

        message = (f'code: {self.code} \nkala: {self.kala_name} \nnumber: {self.number}\nunit: {self.unit}\nAre you sure you want to delete this row?')
        confirm = msg.askyesno(title='Confirmation', message=message)
        if confirm:
            DeleteStock(code =self.code , kala_name =self.kala_name , number=self.number ,  unit=self.unit)

class CheckAddDepository:
    def __init__(self, number, date , reciev_code , reciev_name , desc):
        self.number = number
        self.date = date
        self.reciev_code = reciev_code
        self.reciev_name = reciev_name
        self.desc = desc

        self.check()

    def check(self):

        error = False
         
        if not self.number or not self.date or not self.reciev_code or not self.reciev_name or not self.desc:
            messagebox.showerror("Error", "All fields are required!")
            error = True

            return
        try:
            self.number = int(self.number)  # تبدیل سن به عدد صحیح
        except ValueError:
            messagebox.showerror("Error", "code must be a number!")
            error = True
            return
        
        try:
            self.number = int(self.number)  # تبدیل سن به عدد صحیح
        except ValueError:
            messagebox.showerror("Error", "just number!")
            error = True
            return
        
        if not error:
            AddDepository(number = self.number, date = self.date , reciev_code = self.reciev_code, reciev_name = self.reciev_name, desc = self.desc)

class CheckDeleteDepository:
    def __init__(self, number, date , reciev_code , reciev_name , desc):
        self.number = number
        self.date = date
        self.reciev_code = reciev_code
        self.reciev_name = reciev_name
        self.desc = desc

        self.check()

    def check(self):

        message = (f'number: {self.number} \ndate: {self.date} \nreceiver code: {self.reciev_code}\nreceiver name: {self.reciev_name}\ndescription: {self.desc}\nAre you sure you want to delete this row?')
        confirm = msg.askyesno(title='Confirmation', message=message)
        if confirm:
            DeleteDepository(number = self.number, date = self.date , reciev_code = self.reciev_code, reciev_name = self.reciev_name, desc = self.desc)

class CheckAddDepositoryExit:
    def __init__(self, number, kalacode , kalaname , unit , moeincode, moeinname, id_):
        self.number = number
        self.kalacode = kalacode
        self.kalaname = kalaname
        self.unit = unit
        self.moeincode = moeincode
        self.moeinname = moeinname
        self.id_dep = id_

        self.check()

    def check(self):

        error = False
         
        if not self.number or not self.kalacode or not self.kalaname or not self.unit or not self.moeincode or not self.moeinname:
            messagebox.showerror("Error", "All fields are required!")
            error = True

            return
        try:
            self.number = int(self.number)  # تبدیل سن به عدد صحیح
        except ValueError:
            messagebox.showerror("Error", "code must be a number!")
            error = True
            return
        
        try:
            self.unit = int(self.unit)  # تبدیل سن به عدد صحیح
        except ValueError:
            messagebox.showerror("Error", "just number!")
            error = True
            return
        
        try:
            self.moeincode = int(self.moeincode)  # تبدیل سن به عدد صحیح
        except ValueError:
            messagebox.showerror("Error", "just number!")
            error = True
            return
        
        try:
            self.kalacode = int(self.kalacode)  # تبدیل سن به عدد صحیح
        except ValueError:
            messagebox.showerror("Error", "just number!")
            error = True
            return
        
        if not error:
            AddDepositoryExit(number=self.number , kalacode=self.kalacode , kalaname=self.kalaname ,
                          unit=self.unit , moeincode=self.moeincode, moeinname=self.moeinname, id_=self.id_dep )

class CheckDeleteDepositoryExit:
    def __init__(self, number, kalacode , kalaname , unit , moeincode, moeinname, id_):
        self.number = number
        self.kalacode = kalacode
        self.kalaname = kalaname
        self.unit = unit
        self.moeincode = moeincode
        self.moeinname = moeinname
        self.id_dep = id_


        self.check()

    def check(self):

        message = ('Are you sure you want to delete this row?')
        confirm = msg.askyesno(title='Confirmation', message=message)
        if confirm:
            DeleteDepositoryExit(number=self.number , kalacode=self.kalacode , kalaname=self.kalaname ,
                          unit=self.unit , moeincode=self.moeincode, moeinname=self.moeinname, id_=self.id_dep )
            
class CheckAddMoein:
    def __init__(self, number, code, title):
        self.number = number
        self.code = code
        self.title = title

        self.check()

    def check(self):

        error = False
         
        if not self.number or not self.code or not self.title:
            messagebox.showerror("Error", "All fields are required!")
            error = True

            return
        try:
            self.code = int(self.code)  # تبدیل سن به عدد صحیح
        except ValueError:
            messagebox.showerror("Error", "code must be a number!")
            error = True
            return
        
        try:
            self.number = int(self.number)  # تبدیل سن به عدد صحیح
        except ValueError:
            messagebox.showerror("Error", "just number!")
            error = True
            return
        
        if not error:
            AddMoein(number = self.number, code= self.code, title= self.title)
            
class CheckDeleteMoein:
    def __init__(self, number, code, title):
        self.number = number
        self.code = code
        self.title = title

        self.check()

    def check(self):

        message = (f'number: {self.number} \ncode: {self.code} \ntitle: {self.title}\nAre you sure you want to delete this row?')
        confirm = msg.askyesno(title='Confirmation', message=message)
        if confirm:
            DeleteMoein(number = self.number, code= self.code, title= self.title)
            