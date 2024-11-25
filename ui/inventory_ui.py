
from dal.inventory_dal import CheckNewUser, CheckAddReveiver, CheckStock, CheckDeleteReveiver, CheckDeleteStock, CheckAddDepository, CheckDeleteDepository, CheckAddDepositoryExit, CheckDeleteDepositoryExit, CheckAddMoein, CheckDeleteMoein
from tkinter import Listbox, Text, Tk, Label, Frame,Entry, TOP, LEFT, RIGHT, BOTTOM, PhotoImage, X,NO, Y, BOTH, Button, W, Toplevel, READABLE, StringVar, END
from tkinter.ttk import Combobox, Scrollbar, Treeview
from tkinter.messagebox import showerror, showinfo
import tkinter.messagebox as msg
from tkinter import ttk
import sqlite3
import os
import jdatetime
import threading



def new_user_form():

    def save_user():
        new_user_val = new_user.get()
        new_pass_val = new_pass.get()
        rep_new_pass_val = rep_new_pass.get()

        CheckNewUser(user = new_user_val, password=new_pass_val, repassword=rep_new_pass_val)

        new_user.delete(0, END)
        new_pass.delete(0, END)
        rep_new_pass.delete(0, END)

    def back_btn_onclick():
        new_user_form.quit()
        new_user_form.destroy()

     
    new_user_form = Tk()
    new_user_form.title("SepidehS3")

    form_width = 400
    form_height = 300
    left_pad = (new_user_form.winfo_screenwidth()//2) - (form_width//2)
    top_pad = (new_user_form.winfo_screenheight()//2) - (form_height//2)
    new_user_form.geometry(f"{form_width}x{form_height}+{left_pad}+{top_pad}")
    new_user_form.configure(bg="#F1EFEF")
    new_user_form.overrideredirect(True)



    # region frame
    header = Frame(
        master=new_user_form,
        height=60,
        bg="#F1EFEF"
    )
    header.pack(side=TOP, fill=X)
    header.propagate(False)
    

    footer = Frame(
        master=new_user_form,
        height=100,
        bg="#F1EFEF"
    )
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)

    body = Frame(
        master=new_user_form,
        bg="#F1EFEF",
        height=200
    )
    body.pack(fill=BOTH, expand=True, padx=10, pady=10)
    body.propagate(False)

    user_entry = Frame(
        master = body, 
        height=30,
        bg='#F1EFEF'
    )
    user_entry.pack(fill=X, expand=True, padx=10, pady=(0,0), side=TOP)
    user_entry.propagate(False)

    pass_entry = Frame(
        master = body, 
        height=30,
        bg='#F1EFEF'
    )
    pass_entry.pack(fill=X, expand=True, padx=10, pady=(0,0), side=TOP)
    pass_entry.propagate(False)

    rep_pass_entry = Frame(
        master = body, 
        height=30,
        bg='#F1EFEF'
    )
    rep_pass_entry.pack(fill=X, expand=True, padx=10, pady=(0,0), side=TOP)
    rep_pass_entry.propagate(False)


    # endregion

    #region Label

    ttk.Label(
        master=header,
        text="ایجاد حساب کاربری",
        font=("Dubai", 15, 'bold'),
        compound=LEFT
    ).pack(side=TOP, pady=(20, 0))


    ttk.Label(
        master=user_entry,
        text="نام كاربری",
        font=("Dubai", 10),
        compound=LEFT
    ).pack(side=RIGHT, padx=(10,50))

    ttk.Label(
        master=pass_entry,
        text="رمز عبور",
        font=("Dubai", 10),
        compound=LEFT

    ).pack(side=RIGHT, padx=(10,50))

    ttk.Label(
        master=rep_pass_entry,
        text="تکرار رمز عبور",
        font=("Dubai", 10),
        compound=LEFT

    ).pack(side=RIGHT, padx=(15,50))

    # endregion

    new_user_var = StringVar()
    new_pass_var = StringVar()
    rep_new_pass_var = StringVar()

    #region Entry

    new_user = ttk.Entry(
        master=user_entry,
        width=100,
        justify=RIGHT,
        textvariable= new_user_var
    )
    new_user.pack(fill=BOTH, expand=True, padx=(60,22))

    new_pass = ttk.Entry(
        master=pass_entry,
        width=100,
        justify=RIGHT,
        textvariable= new_pass_var
    )
    new_pass.pack(fill=BOTH, expand=True, padx=(60,30) )


    rep_new_pass = ttk.Entry(
        master=rep_pass_entry,
        width=100,
        justify=RIGHT,
        textvariable= rep_new_pass_var
    )
    rep_new_pass.pack(fill=BOTH, expand=True, padx=(60,0) )



    #endregion

    #region enter

    ttk.Button(
        master=footer,
        text='ثبت',
        compound=LEFT,
        command=save_user
    ).pack(side=TOP, padx=6, pady=1)

    ttk.Button(
        master=footer,
        text='<',
        compound=LEFT,
        command=back_btn_onclick
    ).pack(side=BOTTOM, padx=(10,320), pady=10)

    #endregion

    new_user_form.mainloop()    

def enter_form():

    def change_color(event):
        event.widget.config(foreground="red")  

    def reset_color(event):
        event.widget.config(foreground="black") 

    def exit_btn_onclick():
        form.quit()
        form.destroy()

    def select_receiver(event):

        def get_number():

            DATABASE_DIR = 'database'
            DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')
            connection = sqlite3.connect(DATABASE_PATH)
            cursor = connection.cursor()
            cursor.execute('SELECT number FROM receiver')
            rows = cursor.fetchall()

            a = -1

            for row in rows:
                a+=1
            
            try:
                num = rows[a][0]+1
            
            except IndexError:
                num = 1

            connection.close()

            return num        

        def show_table():
            
            for item in tree.get_children():
                tree.delete(item)

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
            cursor.execute(f'SELECT * FROM receiver')
            rows = cursor.fetchall()

            data=[]


            for row in rows:

                data.append(row)  

            for item in data:  

                number = item[0] 
                code = item[1]
                title = item[2]

                tree.insert('', 'end', values=(title, code, number)) 
            
            num = get_number()
            num_var.set(num) 
            
            

            connection.close()

        def remove_btn():

            selected_item = tree.selection()

            if selected_item:  
                for item in selected_item:
                    values = tree.item(item, 'values')
                    name = values[0]
                    code= values[1]
                    number = values[2]

                CheckDeleteReveiver(number= number, code= code, title= name)  
                threading.Thread(target= show_table).start()
                  
                    
            else:
                msg.showerror("Error", "Please select a user to delete.")

        def add_btn():

            num_val = num_var.get()
            code_val = code_var.get()
            title_val = title_var.get()
            
            CheckAddReveiver(number = num_val, code= code_val, title= title_val)

            
            code_var.set('')
            title_var.set('')
            threading.Thread(target= show_table).start()
            
        for widgets in btn_frame.winfo_children():
             widgets.destroy()

        for widgets in add_frame.winfo_children():
             widgets.destroy()

        for item in tree.get_children():
            tree.delete(item) 

        tree['columns'] = ('3', '2', '1')

        tree.column('#0', width=0, stretch=NO)  
        tree.column('3', width=300, anchor='center')
        tree.column('2', width=100, anchor='center') 
        tree.column('1', width=10, anchor='center')

        tree.heading('#0', text='', anchor='center')  
        tree.heading('3', text='عنوان', anchor='center')
        tree.heading('2', text='کد', anchor='center')
        tree.heading('1', text='#', anchor='center')

        
        
        tree.pack(padx=(20,0), pady=(20,0), fill=X)


        first_add_frame = Frame(master=add_frame, bg="#F1EFEF")
        first_add_frame.pack(fill=BOTH)

        heading_in_add_frame= Frame(master=first_add_frame, width=800, height=35, bg='#F1EFEF')
        heading_in_add_frame.pack(side=TOP, fill=X, padx=10)

        entry_in_add_frame= Frame(master=first_add_frame, width=800, height=40, bg='#F1EFEF')
        entry_in_add_frame.pack(side=TOP, fill=X, padx=10)
        entry_in_add_frame.propagate(False)

        #region button
            
        add_button_receiver = ttk.Button(
            master=btn_frame,
            text='اضافه',
            compound=LEFT,
            command=add_btn
        ).pack(side=BOTTOM, padx=(0,0), pady=1)  

        delete = ttk.Button(
            master=btn_frame,
            text='حذف',
            compound=LEFT,
            command=remove_btn
        ).pack(side=BOTTOM, padx=(0,0), pady=1)  


        #endregion

        #region add Label
            
        label_num= ttk.Label(
            master=heading_in_add_frame,
            text='#',
            font=("Dubai", 12),
            compound=TOP,
            background='#F1EFEF'

        )
        label_num.pack(side=RIGHT, padx=(0,120), fill=Y)

        label_code= ttk.Label(
            master=heading_in_add_frame,
            text='کد',
            font=("Dubai", 12),
            compound=TOP,
            background='#F1EFEF'

        )
        label_code.pack(side=RIGHT, padx=(0,240), fill=Y)

        label_title= ttk.Label(
            master=heading_in_add_frame,
            text='عنوان',
            font=("Dubai", 10),
            compound=TOP,
            background='#F1EFEF'

        )
        label_title.pack(side=RIGHT, padx=(0,240), fill=Y)

        #endregion


        #region stringvar

        num_var = StringVar()
        code_var = StringVar()
        title_var = StringVar()


        #endregion



        #code_values = values_get('code')

        #region Entry

            
        entry_num=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            width=42,
            textvariable=num_var
            
        ).pack(fill=BOTH, expand=False, side=RIGHT)

        entry_code=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            width=42,
            textvariable=code_var,
        ).pack(fill=BOTH, expand=False, side=RIGHT)

        entry_title=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            width=43,
            textvariable= title_var
        ).pack(fill=BOTH, expand=False, side=RIGHT)

        show_table()

        


        #endregion

    def click_open_depository(event):

        def get_number():

            DATABASE_DIR = 'database'
            DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')
            connection = sqlite3.connect(DATABASE_PATH)
            cursor = connection.cursor()
            cursor.execute(f'SELECT number FROM {id_dep}')
            rows = cursor.fetchall()

            a = -1

            for row in rows:
                a+=1
            
            try:
                num = rows[a][0]+1
            
            except IndexError:
                num = 1

            connection.close()

            return num        

        def show_table():
            
            for item in tree.get_children():
                tree.delete(item)

            DATABASE_DIR = 'database'
            DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')
            connection = sqlite3.connect(DATABASE_PATH)
            cursor = connection.cursor()
            cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {id_dep} (
                number INTEGER ,
                kalacode INTEGER,
                kalaname TEXT NOT NULL,
                unit TEXT NOT NULL,
                moeincode INTEGER,
                moeinname TEXT NOT NULL
            )
            ''')
            cursor.execute(f'SELECT * FROM {id_dep}')
            rows = cursor.fetchall()
            data=[]


            for row in rows:

                data.append(row)  

            for item in data:  

                number = item[0] 
                kala_code = item[1]
                kala_name = item[2]
                unit = item[3]
                moein_code = item[4]
                moein_name = item[5]

                tree.insert('', 'end', values=(moein_name, moein_code, unit, kala_name, kala_code, number)) 
            
            num = get_number()
            number_entry.insert(0, num)

            connection.close()

        def select_back():
            for widgets in depository_title_frame.winfo_children():
                widgets.destroy()
            select_depository(event)

        def fetch_kala():
            DATABASE_DIR = 'database'
            DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')
            connection = sqlite3.connect(DATABASE_PATH)
            cursor = connection.cursor()
            
            
            cursor.execute("SELECT kala, code FROM stock")
            items = cursor.fetchall()
            return {item[0]: item[1] for item in items} 

        def update_kala_code_entry(event):

            selected_name = kala_entry.get() 
            code = data.get(selected_name) 
            kala_code_entry.delete(0, END)
            if code:
                kala_code_entry.insert(0, code)

        def update_combobox_kala(event):
            try:
                kala_name = int(kala_code_entry.get())  

            except ValueError:
                kala_name = kala_code_entry.get()  

            for item in data.keys():
                if data[item] == kala_name:  
                    kala_entry.set(item)  
                    break
            else:
                kala_entry.set('')

        def fetch_moein():
            DATABASE_DIR = 'database'
            DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')
            connection = sqlite3.connect(DATABASE_PATH)
            cursor = connection.cursor()
            
            
            cursor.execute("SELECT title, code FROM moein")
            items = cursor.fetchall()
            return {item[0]: item[1] for item in items} 
            
        def update_moein_code_entry(event):
            
            selected_name = moein_entry.get() 
            code = data_moein.get(selected_name) 
            moein_code_entry.delete(0, END)
            if code:
                moein_code_entry.insert(0, code)

        def update_combobox_moein(event):
            try:
                moein_name = int(moein_code_entry.get())  

            except ValueError:
                moein_name = moein_code_entry.get()  

            for item in data_moein.keys():
                if data_moein[item] == moein_name:  
                    moein_entry.set(item)  
                    break
            else:
                moein_entry.set('')
        
        def select_add_btn():
            num_val = number_entry.get()
            kalacode_val = kala_code_entry.get()
            kalaname_val = kala_entry.get()
            unit_val = unit_entry.get()
            moeincode_val = moein_code_entry.get()
            moeinname_val = moein_entry.get()
            
            
            CheckAddDepositoryExit(number=num_val , kalacode=kalacode_val , kalaname=kalaname_val ,
                                   unit=unit_val , moeincode=moeincode_val, moeinname=moeinname_val, id_= id_dep)
            kala_code_entry.delete(0, END)
            kala_entry.set('')
            unit_entry.delete(0, END)
            moein_code_entry.delete(0, END)
            moein_entry.set('')
            number_entry.delete(0, END)
            threading.Thread(target= show_table).start()  

        def remove_btn():

            selected_item = tree.selection()

            if selected_item:  
                for item in selected_item:
                    values = tree.item(item, 'values')
                    moeinname = values[0]
                    moeincode= values[1]
                    unit = values[2]
                    kalaname = values[3]
                    kalacode = values[4]
                    num = values[5]

                CheckDeleteDepositoryExit(number=num , kalacode=kalacode , kalaname=kalaname ,
                                   unit=unit , moeincode=moeincode, moeinname=moeinname, id_= id_dep)   
                
                threading.Thread(target= show_table).start() 
                    
            else:
                msg.showerror("Error", "Please select a user to delete.")
            
            kala_code_entry.delete(0, END)
            kala_entry.set('')
            unit_entry.delete(0, END)
            moein_code_entry.delete(0, END)
            moein_entry.set('')
            number_entry.delete(0, END)
            show_table()

        selected_item = tree.focus()

        item_values = tree.item(selected_item, 'values')

        id_dep = f'dep{item_values[4]}'
        date = item_values[3]
        name = item_values[1]

        

        for widgets in btn_frame.winfo_children():
            widgets.destroy()
        

        for widgets in add_frame.winfo_children():
            widgets.destroy()

        for item in tree.get_children():
            tree.delete(item)

        dep_title = ttk.Label(
        master=depository_title_frame,
        text=name,
        font=("Dubai", 10),
        compound=TOP,
        background='#F1EFEF'

        )
        dep_title.pack(side=TOP, pady=(25,5))

        dep_date = ttk.Label(
            master=depository_title_frame,
            text=date,
            font=("Dubai", 10),
            compound=TOP,
            background='#F1EFEF'
            

        )
        dep_date.pack(side=TOP,pady=(0,5))

        first_add_frame = Frame(master=add_frame, bg="#F1EFEF")
        first_add_frame.pack(fill=BOTH)

        heading_in_add_frame= Frame(master=first_add_frame, width=800, height=35, bg='#F1EFEF')
        heading_in_add_frame.pack(side=TOP, fill=X, padx=10)

        entry_in_add_frame= Frame(master=first_add_frame, width=800, height=40, bg='#F1EFEF')
        entry_in_add_frame.pack(side=TOP, fill=X, padx=10)
        entry_in_add_frame.propagate(False)

        tree['columns'] = ('6','5','4','3', '2', '1')

        tree.column('#0', width=0, stretch=NO)
        tree.column('6', width=130, anchor='center')
        tree.column('5', width=130, anchor='center')
        tree.column('4', width=130, anchor='center')
        tree.column('3', width=130, anchor='center')
        tree.column('2', width=130, anchor='center') 
        tree.column('1', width=50, anchor='center')

        tree.heading('#0', text='', anchor='center') 
        tree.heading('6', text='عنوان معین', anchor='center') 
        tree.heading('5', text='کد معین', anchor='center') 
        tree.heading('4', text='واحد', anchor='center') 
        tree.heading('3', text='عنوان کالا', anchor='center')
        tree.heading('2', text='کد کالا', anchor='center')
        tree.heading('1', text='ردیف', anchor='center')

    
        tree.pack(padx=(20,0), pady=(20,0), fill=X)

        add_button_depository = ttk.Button(
            master=btn_frame,
            text='اضافه',
            compound=LEFT,
            command=select_add_btn
        ).pack(side=BOTTOM, padx=(0,0), pady=1)  
        
        delete = ttk.Button(
            master=btn_frame,
            text='حذف',
            compound=LEFT,
            command=remove_btn
        ).pack(side=BOTTOM, padx=(0,0), pady=1)  

        back = ttk.Button(
        master=btn_frame,
        text='برگشت',
        compound=LEFT,
        command=select_back
        ).pack(side=BOTTOM, padx=(0,0), pady=1)  

        

        #region add Label
            
        number_label= ttk.Label(
            master=heading_in_add_frame,
            text='ردیف',
            font=("Dubai", 10),
            compound=TOP,
            background='#F1EFEF'

        )
        number_label.pack(side=RIGHT, padx=(0,20), fill=Y)

        kala_code_label= ttk.Label(
            master=heading_in_add_frame,
            text='کد کالا',
            font=("Dubai", 10),
            compound=TOP,
            background='#F1EFEF'

        )
        kala_code_label.pack(side=RIGHT, padx=(0,70), fill=Y)

        kala_label= ttk.Label(
            master=heading_in_add_frame,
            text='عنوان کالا',
            font=("Dubai", 10),
            compound=TOP,
            background='#F1EFEF'

        )
        kala_label.pack(side=RIGHT, padx=(0,100), fill=Y)

        unit_label= ttk.Label(
            master=heading_in_add_frame,
            text='تعداد',
            font=("Dubai", 10),
            compound=TOP,
            background='#F1EFEF'

        )
        unit_label.pack(side=RIGHT, padx=(0,110), fill=Y)

        moein_code_label= ttk.Label(
            master=heading_in_add_frame,
            text='کد معین',
            font=("Dubai", 10),
            compound=TOP,
            background='#F1EFEF'

        )
        moein_code_label.pack(side=RIGHT, padx=(0,100), fill=Y)

        moein_label= ttk.Label(
            master=heading_in_add_frame,
            text='عنوان معین',
            font=("Dubai", 10),
            compound=TOP,
            background='#F1EFEF'

        )
        moein_label.pack(side=RIGHT, padx=(0,100), fill=Y)

    
        #endregion

        kala_code_var = StringVar()
        kala_name_var = StringVar()
        unit_var = StringVar()
        moein_code_var = StringVar()
        moein_name_var = StringVar()

        #region Entry

            
        number_entry=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            width=10
        )
        number_entry.pack(fill=BOTH, expand=False, side=RIGHT)

        kala_code_entry=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            width=23
        )
        kala_code_entry.pack(fill=BOTH, expand=False, side=RIGHT)
        kala_code_entry.bind("<KeyRelease>", update_combobox_kala)

        data = fetch_kala()

        kala_entry=ttk.Combobox(
            master=entry_in_add_frame,
            justify='center',
            width=20,
            state="readonly"
        )
        kala_entry.pack(fill=BOTH, expand=False, side=RIGHT)
        kala_entry['values'] = list(data.keys())
        kala_entry.bind("<<ComboboxSelected>>", update_kala_code_entry)        

        unit_entry=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            width=23
        )
        unit_entry.pack(fill=BOTH, expand=False, side=RIGHT)

        moein_code_entry=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            width=20
        )
        moein_code_entry.pack(fill=BOTH, expand=False, side=RIGHT)
        moein_code_entry.bind("<KeyRelease>", update_combobox_moein)

        data_moein = fetch_moein()
        moein_entry=ttk.Combobox(
            master=entry_in_add_frame,
            justify='center',
            width=25,
            state="readonly"
        )
        moein_entry.pack(fill=BOTH, expand=False, side=RIGHT)
        moein_entry['values'] = list(data_moein.keys())
        moein_entry.bind("<<ComboboxSelected>>", update_moein_code_entry)    

        show_table()

    def select_depository(event):

        def get_number():

            DATABASE_DIR = 'database'
            DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')
            connection = sqlite3.connect(DATABASE_PATH)
            cursor = connection.cursor()
            cursor.execute('SELECT number FROM depository')
            rows = cursor.fetchall()

            a = -1

            for row in rows:
                a+=1
            
            try:
                num = rows[a][0]+1
            
            except IndexError:
                num = 1

            connection.close()

            return num        

        def show_table():
            
            for item in tree.get_children():
                tree.delete(item)

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
            cursor.execute(f'SELECT * FROM depository')
            rows = cursor.fetchall()

            data=[]


            for row in rows:

                data.append(row)  

            for item in data:  

                number = item[0] 
                date = item[1]
                receiv_code = item[2]
                receiv_name = item[3]
                desc = item[4]

                tree.insert('', 'end', values=(desc, receiv_name, receiv_code, date, number)) 
            
            num = get_number()
            current_date = jdatetime.datetime.now()

            number_entry.delete(0, END)
            day_entry.delete(0, END)
            month_entry.delete(0, END)
            year_entry.delete(0, END)

            number_entry.insert(0, num)
            day_entry.insert(0, current_date.strftime('%d'))
            month_entry.insert(0, current_date.strftime('%m'))
            year_entry.insert(0, current_date.strftime('%Y'))
            





            connection.close()

        def remove_btn():

            selected_item = tree.selection()

            if selected_item:  
                for item in selected_item:
                    values = tree.item(item, 'values')
                    
                    number = values[4]
                    date = values[3]
                    reciev_code = values[2]
                    reciev_name = values[1]
                    desc = values[0]

                CheckDeleteDepository(number = number, date = date , reciev_code = reciev_code, reciev_name = reciev_name, desc = desc)   
                threading.Thread(target= show_table).start()   
                    
            else:
                msg.showerror("Error", "Please select a user to delete.")

        def add_btn():

            number = number_entry.get()
            date = (f'{year_entry.get()}-{month_entry.get()}-{day_entry.get()}')
            reciev_code = reciev_code_entry.get()
            reciev_name = reciev_name_entry.get()
            desc = desc_entry.get()
            
            CheckAddDepository(number = number, date = date , reciev_code = reciev_code, reciev_name = reciev_name, desc = desc)

            
            reciev_code_entry.delete(0, END)
            reciev_name_entry.set('')
            desc_var.set('')
            threading.Thread(target= show_table).start()

        def fetch_reciev():
            DATABASE_DIR = 'database'
            DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')
            connection = sqlite3.connect(DATABASE_PATH)
            cursor = connection.cursor()
            
            
            cursor.execute("SELECT title, code FROM receiver")
            items = cursor.fetchall()
            return {item[0]: item[1] for item in items} 

        def update_reciev_code_entry(event):
            
            selected_name = reciev_name_entry.get() 
            code = data_reciev.get(selected_name) 
            reciev_code_entry.delete(0, END)
            if code:
                reciev_code_entry.insert(0, code)

        def update_combobox_reciev(event):
            try:
                moein_name = int(reciev_code_entry.get())  

            except ValueError:
                moein_name = reciev_code_entry.get()  

            for item in data_reciev.keys():
                if data_reciev[item] == moein_name:  
                    reciev_name_entry.set(item)  
                    break
            else:
                reciev_name_entry.set('')

        for widgets in depository_title_frame.winfo_children():
                widgets.destroy()

        for widgets in btn_frame.winfo_children():
            widgets.destroy()

        for widgets in add_frame.winfo_children():
            widgets.destroy()

        for item in tree.get_children():
            tree.delete(item)

        tree['columns'] = ('5','4','3', '2', '1')

        tree.column('#0', width=0, stretch=NO)
        tree.column('5', width=100, anchor='center')
        tree.column('4', width=100, anchor='center')
        tree.column('3', width=100, anchor='center')
        tree.column('2', width=100, anchor='center') 
        tree.column('1', width=50, anchor='center')

        tree.heading('#0', text='', anchor='center') 
        tree.heading('5', text='توضیحات', anchor='center') 
        tree.heading('4', text='عنوان تحویل گیرنده', anchor='center') 
        tree.heading('3', text='کد تحویل گیرنده', anchor='center')
        tree.heading('2', text='تاریخ', anchor='center')
        tree.heading('1', text='شماره', anchor='center')

        
        tree.pack(padx=(20,0), pady=(20,0), fill=X)

        tree.bind("<Double-1>", click_open_depository)

        
        second_add_frame = Frame(master=add_frame, bg="#F1EFEF")
        second_add_frame.pack(fill=BOTH)

        heading_in_add_frame= Frame(master=second_add_frame, width=800, height=35, bg='#F1EFEF')
        heading_in_add_frame.pack(side=TOP, fill=X, padx=10)

        entry_in_add_frame= Frame(master=second_add_frame, width=800, height=40, bg='#F1EFEF')
        entry_in_add_frame.pack(side=TOP, fill=X, padx=10)
        entry_in_add_frame.propagate(False)

        #region button

        
            
        add_button_depository = ttk.Button(
            master=btn_frame,
            text='اضافه',
            compound=LEFT,
            command=add_btn
        ).pack(side=BOTTOM, padx=(0,0), pady=1)  
        
        delete = ttk.Button(
            master=btn_frame,
            text='حذف',
            compound=LEFT,
            command=remove_btn
        ).pack(side=BOTTOM, padx=(0,0), pady=1)  
  

        #endregion

        #region add Label
            
        number_label= ttk.Label(
            master=heading_in_add_frame,
            text='شماره',
            font=("Dubai", 10),
            compound=TOP,
            background='#F1EFEF'

        )
        number_label.pack(side=RIGHT, padx=(0,60), fill=Y)

        date_label= ttk.Label(
            master=heading_in_add_frame,
            text='تاریخ',
            font=("Dubai", 10),
            compound=TOP,
            background='#F1EFEF'

        )
        date_label.pack(side=RIGHT, padx=(0,120), fill=Y)

        reciev_code_label= ttk.Label(
            master=heading_in_add_frame,
            text='کد تحویل گیرنده',
            font=("Dubai", 10),
            compound=TOP,
            background='#F1EFEF'

        )
        reciev_code_label.pack(side=RIGHT, padx=(0,80), fill=Y)

        reciev_name_label= ttk.Label(
            master=heading_in_add_frame,
            text='عنوان تحویل گیرنده',
            font=("Dubai", 10),
            compound=TOP,
            background='#F1EFEF'

        )
        reciev_name_label.pack(side=RIGHT, padx=(0,80), fill=Y)

        desc_label= ttk.Label(
            master=heading_in_add_frame,
            text='توضیحات',
            font=("Dubai", 10),
            compound=TOP,
            background='#F1EFEF'

        )
        desc_label.pack(side=RIGHT, padx=(0,90), fill=Y)

    
        #endregion

        number_var = StringVar()
        day_var = StringVar()
        month_var = StringVar()
        year_var = StringVar()
        receiv_code_var = StringVar()
        receiv_name_var = StringVar()
        desc_var = StringVar()

        #region Entry

            
        number_entry=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            width=25
        )
        number_entry.pack(fill=BOTH, expand=False, side=RIGHT)

        day_entry=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            width=6
        )
        day_entry.pack(fill=BOTH, expand=False, side=RIGHT)
        month_entry=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            width=6
        )
        month_entry.pack(fill=BOTH, expand=False, side=RIGHT)
        year_entry=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            width=7
        )
        year_entry.pack(fill=BOTH, expand=False, side=RIGHT)

        reciev_code_entry=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            width=27
        )
        reciev_code_entry.pack(fill=BOTH, expand=False, side=RIGHT)
        reciev_code_entry.bind("<KeyRelease>", update_combobox_reciev)

        #reciev_code_entry.bind("<FocusOut>", on_reciev_code_entry_leave)


        data_reciev = fetch_reciev()
        reciev_name_entry=ttk.Combobox(
            master=entry_in_add_frame,
            justify='center',
            width=27,
            state="readonly"
        )
        reciev_name_entry.pack(fill=BOTH, expand=False, side=RIGHT)
        reciev_name_entry['values'] = list(data_reciev.keys())
        reciev_name_entry.bind("<<ComboboxSelected>>", update_reciev_code_entry) 

        

        desc_entry=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            textvariable= desc_var ,
            width=28
        )
        desc_entry.pack(fill=BOTH, expand=False, side=RIGHT)

        number_entry.update_idletasks()

        show_table()

        



        #endregion

    def select_stock(event):
      

        def show_table():
            
            for item in tree.get_children():
                tree.delete(item)

            DATABASE_DIR = 'database'
            DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')
            connection = sqlite3.connect(DATABASE_PATH)
            cursor = connection.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS stock (
            code INTEGER ,
            kala TEXT ,
            number INTEGER,
            unit TEXT NOT NULL
            )
            ''')
            cursor.execute(f'SELECT * FROM stock')
            rows = cursor.fetchall()

            data=[]


            for row in rows:

                data.append(row)  

            for item in data:  

                code = item[0] 
                kala = item[1]
                number = item[2]
                unit = item[3]

                tree.insert('', 'end', values=(unit ,number , kala ,code)) 
            
            
            

            connection.close()

        def remove_btn():

            selected_item = tree.selection()

            if selected_item:  
                for item in selected_item:
                    values = tree.item(item, 'values')
                    code = values[3] 
                    kala = values[2]
                    number = values[1]
                    unit = values[0]

                CheckDeleteStock(code = code , kala_name = kala , number= number ,  unit = unit)   
                threading.Thread(target= show_table).start() 
                    
            else:
                msg.showerror("Error", "Please select a user to delete.")

        def add_btn():
            code_val = code_var.get()
            kala_name_val = kala_name_var.get()
            number_val = number_var.get()
            unit_val = unit_var.get()
            
            CheckStock(code =code_val , kala_name =kala_name_val , number=number_val ,  unit=unit_val )
            code_var.set('')
            kala_name_var.set('')
            number_var.set('')
            unit_var.set('')

            threading.Thread(target= show_table).start()

        def edit_btn():

            selected_item = tree.selection()

            if selected_item:  
                for item in selected_item:
                    values = tree.item(item, 'values')
                    code = values[3] 
                    kala = values[2]
                    number = values[1]
                    unit = values[0]

                CheckDeleteStock(code = code , kala_name = kala , number= number ,  unit = unit)   
                threading.Thread(target= show_table).start() 

            code_var.set(code)
            kala_name_var.set(kala)
            number_var.set(number)
            unit_var.set(unit)



            

        for widgets in btn_frame.winfo_children():
             widgets.destroy()

        for widgets in add_frame.winfo_children():
             widgets.destroy()

        for item in tree.get_children():
            tree.delete(item)

        for widgets in depository_title_frame.winfo_children():
            widgets.destroy()

        tree['columns'] = ('4','3', '2', '1')

        tree.column('#0', width=0, stretch=NO)
        tree.column('4', width=100, anchor='center')
        tree.column('3', width=100, anchor='center')
        tree.column('2', width=100, anchor='center') 
        tree.column('1', width=50, anchor='center')

        tree.heading('#0', text='', anchor='center') 
        tree.heading('4', text='واحد', anchor='center') 
        tree.heading('3', text='تعداد', anchor='center')
        tree.heading('2', text='نام کالا', anchor='center')
        tree.heading('1', text='کد', anchor='center')

        
        tree.pack(padx=(20,0), pady=(20,0), fill=X)

        
        third_add_frame = Frame(master=add_frame, bg="#F1EFEF")
        third_add_frame.pack(fill=BOTH)

        heading_in_add_frame= Frame(master=third_add_frame, width=800, height=35, bg='#F1EFEF')
        heading_in_add_frame.pack(side=TOP, fill=X, padx=10)

        entry_in_add_frame= Frame(master=third_add_frame, width=800, height=40, bg='#F1EFEF')
        entry_in_add_frame.pack(side=TOP, fill=X, padx=10)
        entry_in_add_frame.propagate(False)


        #region button
            
        add_button_stock = ttk.Button(
            master=btn_frame,
            text='اضافه',
            compound=LEFT,
            command=add_btn,
            
        ).pack(side=BOTTOM, padx=(0,0), pady=1)

        delete = ttk.Button(
            master=btn_frame,
            text='حذف',
            compound=LEFT,
            command=remove_btn
        ).pack(side=BOTTOM, padx=(0,0), pady=1)    

        edit = ttk.Button(
            master=btn_frame,
            text='ویرایش',
            compound=LEFT,
            command=edit_btn
        ).pack(side=BOTTOM, padx=(0,0), pady=1) 


        #endregion


        #region add Label
            
        code= ttk.Label(
            master=heading_in_add_frame,
            text='کد',
            font=("Dubai", 12),
            compound=TOP,
            background='#F1EFEF'

        )
        code.pack(side=RIGHT, padx=(0,90), fill=Y)

        kala_name= ttk.Label(
            master=heading_in_add_frame,
            text='عنوان کالا',
            font=("Dubai", 12),
            compound=TOP,
            background='#F1EFEF'

        )
        kala_name.pack(side=RIGHT, padx=(0,150), fill=Y)

        number= ttk.Label(
            master=heading_in_add_frame,
            text='تعداد',
            font=("Dubai", 10),
            compound=TOP,
            background='#F1EFEF'

        )
        number.pack(side=RIGHT, padx=(0,150), fill=Y)

        unit= ttk.Label(
            master=heading_in_add_frame,
            text='واحد',
            font=("Dubai", 10),
            compound=TOP,
            background='#F1EFEF'

        )
        unit.pack(side=RIGHT, padx=(0,160), fill=Y)

        #endregion


        #region stringvar


        code_var = StringVar()
        kala_name_var = StringVar()
        number_var = StringVar()
        unit_var = StringVar()


        #endregion


        #region Entry

            
        entry_code=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            width=31,
            textvariable=code_var
            
        ).pack(fill=BOTH, expand=False, side=RIGHT)

        entry_kala_name=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            width=31,
            textvariable=kala_name_var
        ).pack(fill=BOTH, expand=False, side=RIGHT)

        entry_number=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            width=31,
            textvariable=number_var
        ).pack(fill=BOTH, expand=False, side=RIGHT)


        entry_unit=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            width=31,
            textvariable=unit_var
        ).pack(fill=BOTH, expand=False, side=RIGHT)

        show_table()


        #endregion

    def select_moein(event):
        
        def get_number():

            DATABASE_DIR = 'database'
            DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')
            connection = sqlite3.connect(DATABASE_PATH)
            cursor = connection.cursor()
            cursor.execute('SELECT number FROM moein')
            rows = cursor.fetchall()

            a = -1

            for row in rows:
                a+=1
            
            try:
                num = rows[a][0]+1
            
            except IndexError:
                num = 1

            connection.close()

            return num        

        def show_table():
            
            for item in tree.get_children():
                tree.delete(item)

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
            cursor.execute(f'SELECT * FROM moein')
            rows = cursor.fetchall()

            data=[]


            for row in rows:

                data.append(row)  

            for item in data:  

                number = item[0] 
                code = item[1]
                title = item[2]

                tree.insert('', 'end', values=(title, code, number)) 
            
            num = get_number()
            num_var.set(num) 
            
            

            connection.close()

        def remove_btn():

            selected_item = tree.selection()

            if selected_item:  
                for item in selected_item:
                    values = tree.item(item, 'values')
                    name = values[0]
                    code= values[1]
                    number = values[2]

                CheckDeleteMoein(number= number, code= code, title= name)   
                show_table()    
                    
            else:
                msg.showerror("Error", "Please select a user to delete.")

        def add_btn():

            num_val = num_var.get()
            code_val = code_var.get()
            title_val = title_var.get()
            
            CheckAddMoein(number = num_val, code= code_val, title= title_val)

            
            code_var.set('')
            title_var.set('')
            show_table()
            
        for widgets in btn_frame.winfo_children():
             widgets.destroy()

        for widgets in add_frame.winfo_children():
             widgets.destroy()

        for item in tree.get_children():
            tree.delete(item) 

        for widgets in depository_title_frame.winfo_children():
            widgets.destroy()

        tree['columns'] = ('3', '2', '1')

        tree.column('#0', width=0, stretch=NO)  
        tree.column('3', width=300, anchor='center')
        tree.column('2', width=100, anchor='center') 
        tree.column('1', width=10, anchor='center')

        tree.heading('#0', text='', anchor='center')  
        tree.heading('3', text='عنوان', anchor='center')
        tree.heading('2', text='کد', anchor='center')
        tree.heading('1', text='#', anchor='center')

        
        
        tree.pack(padx=(20,0), pady=(20,0), fill=X)


        first_add_frame = Frame(master=add_frame, bg="#F1EFEF")
        first_add_frame.pack(fill=BOTH)

        heading_in_add_frame= Frame(master=first_add_frame, width=800, height=35, bg='#F1EFEF')
        heading_in_add_frame.pack(side=TOP, fill=X, padx=10)

        entry_in_add_frame= Frame(master=first_add_frame, width=800, height=40, bg='#F1EFEF')
        entry_in_add_frame.pack(side=TOP, fill=X, padx=10)
        entry_in_add_frame.propagate(False)

        #region button
            
        add_button_receiver = ttk.Button(
            master=btn_frame,
            text='اضافه',
            compound=LEFT,
            command=add_btn
        ).pack(side=BOTTOM, padx=(0,0), pady=1)  

        delete = ttk.Button(
            master=btn_frame,
            text='حذف',
            compound=LEFT,
            command=remove_btn
        ).pack(side=BOTTOM, padx=(0,0), pady=1)  


        #endregion

        #region add Label
            
        label_num= ttk.Label(
            master=heading_in_add_frame,
            text='#',
            font=("Dubai", 12),
            compound=TOP,
            background='#F1EFEF'

        )
        label_num.pack(side=RIGHT, padx=(0,120), fill=Y)

        label_code= ttk.Label(
            master=heading_in_add_frame,
            text='کد',
            font=("Dubai", 12),
            compound=TOP,
            background='#F1EFEF'

        )
        label_code.pack(side=RIGHT, padx=(0,240), fill=Y)

        label_title= ttk.Label(
            master=heading_in_add_frame,
            text='عنوان',
            font=("Dubai", 10),
            compound=TOP,
            background='#F1EFEF'

        )
        label_title.pack(side=RIGHT, padx=(0,240), fill=Y)

        #endregion


        #region stringvar

        num_var = StringVar()
        code_var = StringVar()
        title_var = StringVar()


        #endregion



        #code_values = values_get('code')

        #region Entry

            
        entry_num=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            width=42,
            textvariable=num_var
            
        ).pack(fill=BOTH, expand=False, side=RIGHT)

        entry_code=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            width=42,
            textvariable=code_var,
        ).pack(fill=BOTH, expand=False, side=RIGHT)

        entry_title=ttk.Entry(
            master=entry_in_add_frame,
            justify='center',
            width=43,
            textvariable= title_var
        ).pack(fill=BOTH, expand=False, side=RIGHT)

        show_table()

        


        #endregion


    form = Tk()
    form.title("SepidehS3")

    form_width = 1000
    form_height = 600
    left_pad = (form.winfo_screenwidth()//2) - (form_width//2)
    top_pad = (form.winfo_screenheight()//2) - (form_height//2)
    form.geometry(f"{form_width}x{form_height}+{left_pad}+{top_pad}")
    form.configure(bg="#F1EFEF")
    form.overrideredirect(False)
    style = ttk.Style()
    style.configure("Table.TFrame", background="#C7C8CC")


    #region Frame
    

    all_selection_frame = Frame(master=form, height=600, width=200, bg="#F1EFEF")
    all_selection_frame.pack(side=RIGHT, padx=(10, 25), pady=(25, 25))
    all_selection_frame.propagate(True)
    

    table_selection_frame = Frame(master=all_selection_frame, height=250, width=200, bg="#C7C8CC")
    table_selection_frame.pack(side=TOP, padx=(0, 0), pady=(0, 0))
    

    labels_frame = Frame(master=table_selection_frame, height=400, width=200, bg="#C7C8CC")
    labels_frame.pack(side=RIGHT, padx=(25, 25), pady=(0, 100))

    add_frame = Frame(master=form, width=799, height=50, bg="#F1EFEF")
    add_frame.pack(side=BOTTOM,  pady=(0,25), padx=(25,25), fill=BOTH)

    table_frame = Frame(master=form, width=750, height=500, bg="#C7C8CC")
    table_frame.pack(fill=BOTH, expand=True, padx=25, pady=(25, 0))


    btn_frame = Frame(master=all_selection_frame, height=150, width=100, bg='#F1EFEF')
    btn_frame.pack(side=BOTTOM, padx=0, pady=0, fill=X)
    btn_frame.propagate(False)

    depository_title_frame = Frame(master=all_selection_frame, height=100, width=100, bg='#F1EFEF')
    depository_title_frame.pack(side=BOTTOM, padx=0, pady=0, fill=X)
    depository_title_frame.propagate(False)

    exit_frame = Frame(master=all_selection_frame, height=200, width=100, bg='#F1EFEF')
    exit_frame.pack(side=BOTTOM, padx=0, pady=0, fill=BOTH)

    #endregion


    #region Label

    receiver = ttk.Label(
        master=labels_frame,
        text="تحویل گیرنده",
        font=("Dubai", 10),
        compound=TOP,
        background='#C7C8CC'

    )
    receiver.pack(side=TOP, pady=(25,5))
    receiver.bind("<Button-1>", select_receiver)
    receiver.bind("<Enter>", change_color) 
    receiver.bind("<Leave>", reset_color)

    depository = ttk.Label(
        master=labels_frame,
        text="خروج انبار",
        font=("Dubai", 10),
        compound=TOP,
        background='#C7C8CC'
        

    )
    depository.pack(side=TOP,pady=(0,5))
    depository.bind("<Button-1>", select_depository)
    depository.bind("<Enter>", change_color) 
    depository.bind("<Leave>", reset_color)

    stock = ttk.Label(
        master=labels_frame,
        text="موجودی",
        font=("Dubai", 10),
        compound=TOP,
        background='#C7C8CC'

    )
    stock.pack(side=TOP,pady=(0,5))
    stock.bind("<Button-1>", select_stock)
    stock.bind("<Enter>", change_color) 
    stock.bind("<Leave>", reset_color) 

    moein = ttk.Label(
        master=labels_frame,
        text="معین",
        font=("Dubai", 10),
        compound=TOP,
        background='#C7C8CC'

    )
    moein.pack(side=TOP,pady=(0,5))
    moein.bind("<Button-1>", select_moein)
    moein.bind("<Enter>", change_color) 
    moein.bind("<Leave>", reset_color) 

    #endregion


    #region grid

    scrollbar_x = Scrollbar(master=table_frame, orient="horizontal")
    scrollbar_x.pack(side=BOTTOM, fill=X, padx=(20,20), pady=(0,20))

    scrollbar_y = Scrollbar(master=table_frame, orient="vertical")
    scrollbar_y.pack(side=RIGHT, fill=Y, pady=(20,0), padx=(0,20))

    tree = ttk.Treeview(table_frame, height=100)

    tree.pack(padx=(20,0), pady=(20,0), fill=BOTH)

    scrollbar_y["command"] = tree.yview
    scrollbar_x["command"] = tree.xview

    #endregion



    # region button 

    ttk.Button(
        master=exit_frame,
        text='خروج',
        compound=LEFT,
        command=exit_btn_onclick

    ).pack(side=TOP,pady=5)

    #endregion
    
    form.mainloop() 

def main_window():

    def set_database():

        DATABASE_DIR = 'database'
        DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS users (
            user BLOB NOT NULL,
            password BLOB NOT NULL
        )
        ''')

    def change_color(event):
        new_user.config(foreground="red")  

    def reset_color(event):
        new_user.config(foreground="black") 

    def exit_btn_onclick():
        main_form.quit()
        main_form.destroy()

    def check_user(user, password):
      
        DATABASE_DIR = 'database'
        DATABASE_PATH = os.path.join(DATABASE_DIR, 'database.db')
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()

     
        cursor.execute("SELECT * FROM users WHERE user = ? AND password = ?", (user, password))
        
        results = cursor.fetchall()

        connection.close()

        return results

        

    def on_click(event):
        main_form.withdraw()
        new_user_form()
        main_form.deiconify()
    
    def on_click_enter():

        user_val = user_var.get()
        pass_val = pass_var.get()

        results = check_user(user_val, pass_val)

        if results:
            main_form.quit()
            main_form.destroy()
            enter_form()

        else:
            msg.showinfo("Error", "No User Found!")

        user_var.set('')
        pass_var.set('')

        
            

    main_form = Tk()

    # region config
    main_form.title("SepidehS3")

    form_width = 400
    form_height = 300
    left_pad = (main_form.winfo_screenwidth()//2) - (form_width//2)
    top_pad = (main_form.winfo_screenheight()//2) - (form_height//2)
    main_form.geometry(f"{form_width}x{form_height}+{left_pad}+{top_pad}")
    main_form.configure(bg="#F1EFEF")
    main_form.overrideredirect(True)
    #endregion

    set_database()

    user_var = StringVar()
    pass_var = StringVar()

    # region frame
    

    body = Frame(
        master=main_form,
        bg="#F1EFEF"
    )
    body.pack(fill=BOTH, expand=True, padx=10, pady=10)
    body.propagate(False)

    user_frame = Frame(
        master = body, 
        height=30,
        bg='#F1EFEF',
        
        
    )
    user_frame.pack(fill=X, expand=True, padx=10, pady=(40,0), side=TOP)
    user_frame.propagate(False)

    pass_frame = Frame(
        master = body, 
        height=30,
        bg='#F1EFEF'
    )
    pass_frame.pack(fill=X, expand=True, padx=10, pady=(0,10), side=TOP)
    pass_frame.propagate(False)


    # endregion

    #region Label



    ttk.Label(
        master=user_frame,
        text="نام كاربری",
        font=("Dubai", 10),
        compound=LEFT,
    ).pack(side=RIGHT, padx=(15,50))

    ttk.Label(
        master=pass_frame,
        text="رمز عبور",
        font=("Dubai", 10),
        compound=LEFT,

    ).pack(side=RIGHT, padx=(20,50))

    # endregion


    user_var = StringVar()
    pass_var = StringVar()

    #region Entry

    user_entry =ttk.Entry(
        master=user_frame,
        width=100,
        justify=RIGHT,
        textvariable=user_var
    )
    user_entry.pack(fill=BOTH, expand=True, padx=(60,0))

    pass_entry= ttk.Entry(
        master=pass_frame,
        width=100,
        justify=RIGHT,
        textvariable=pass_var
    )
    pass_entry.pack(fill=BOTH, expand=True, padx=(60,0) )



    #endregion

    #region enter

    ttk.Button(
        master=body,
        text='ورود',
        compound=LEFT,
        command=on_click_enter
    ).pack(side=TOP, padx=6, pady=(0,10))

    new_user= ttk.Label(
        master=body,
        text="ایجاد حساب کاربری",
        font=("Dubai", 10),
        compound="center",
        underline=0,
        cursor="hand2"
    )
    new_user.pack(side=TOP, pady=(10, 30))
    new_user.bind("<Button-1>", on_click)
    new_user.bind("<Enter>", change_color) 
    new_user.bind("<Leave>", reset_color) 

    #endregion


    ttk.Button(
        master=body,
        command=exit_btn_onclick,
        text='خروج',
        compound=LEFT,
    ).pack(side=BOTTOM, padx=(0,320), pady=1)

    main_form.mainloop()
