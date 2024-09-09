import sqlite3
from tkinter import Tk, Label, Entry, Button, messagebox
from bl.inventory_bl import AddReceiver, AddStock, DeleteReceiver
from tkinter.messagebox import showerror, showinfo
import tkinter.messagebox as msg



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

