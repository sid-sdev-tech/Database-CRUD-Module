from tkinter import *
from tkinter import ttk
import sqlite3
import mysql.connector
from prettytable import prettytable
base = Tk()

base.title("DataBaseModule")
base.geometry("800x755")
base.configure(bg = "#DCDCDC")
fontstyle = ("Comic Sans MS BOLD",13)

def Save():
    pass
def Run():
    pass
def Insert():
    def Save():
        t1=str(inputBox.get())
        t2=str(inputBox1.get())
        t3=str(inputBox2.get())
        t4=str(inputBox3.get())
        t5=str(inputBox4.get())
        #con = sqlite3.connect("BasicDataTable.db")
        conn = mysql.connector.connect(user='root',password='',host='localhost',database='STUDENT_INFO1')
        q1 = "Insert into "+t1+"(Enrollment_Number,Student_Name,Student_Mob_No,Student_City) values (" + t2 + ",'" + t3 + "'," + t4 + ",'" + t5 + "')";
        print(q1)
        cur = conn.cursor()
        cur.execute(q1)
        conn.commit()
        conn.close()
    def Reset():
        inputBox.delete(0, END)
        inputBox1.delete(0, END)
        inputBox2.delete(0, END)
        inputBox3.delete(0, END)
        inputBox4.delete(0,END)

    base1 = Tk()
    base1.title("Insert Operation ")
    base1.geometry("800x800")
    header = Label(base1, text="Insert Query ", font=50, height=4)
    header.pack()

    text1 = Label(base1, text=" Table Name :")
    text1.place(x=150, y=110)

    inputBox = Entry(base1, font=10, width=30)
    inputBox.place(x=310, y=110)

    text2 = Label(base1, text="Enrollment Number: ")
    text2.place(x=150, y=150)

    inputBox1 = Entry(base1, font=10, width=30)
    inputBox1.place(x=310, y=150)

    text3 = Label(base1, text="Student Name :")
    text3.place(x=150, y=190)

    inputBox2 = Entry(base1, font=10, width=30)
    inputBox2.place(x=310, y=190)

    text4 = Label(base1, text="Student Mob. No.: ")
    text4.place(x=150, y=240)

    inputBox3 = Entry(base1, font=10, width=30)
    inputBox3.place(x=310, y=240)

    text5 = Label(base1, text="Student City: ")
    text5.place(x=150, y=280)

    inputBox4 = Entry(base1,font = 10,width =30)
    inputBox4.place(x=310,y=280)

    btn = Button(base1, text="Insert", bg='#0d6efd', fg='white', command=Save)
    btn.place(x=200, y=330, height=50, width=150)

    btn = Button(base1, text="Reset", bg='#198754', fg='white', command=Reset)
    btn.place(x=480, y=330, height=50, width=150)

    base1.mainloop()

def Update():
    def Save1():
        t1 = str(inputBox.get())
        t2 = str(inputBox1.get())
        t3 = str(inputBox2.get())
        t4 = str(inputBox3.get())
        t5 = str(inputBox4.get())
        #con = sqlite3.connect("BasicDataTable.db")
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='STUDENT_INFO1')
        q2 = "Update " + t1 + " set Student_Name = '" + t3 + "',Student_City = '" + t5 + "' where Enrollment_Number = " + t2 + " and Student_Mob_No = " + t4 + ";";
        print(q2)
        cur = conn.cursor()
        cur.execute(q2)
        conn.commit()
        conn.close()

    def Reset1():
        inputBox.delete(0, END)
        inputBox1.delete(0, END)
        inputBox2.delete(0, END)
        inputBox3.delete(0, END)
        inputBox4.delete(0,END)

    base2 = Tk()
    base2.title("Update Operation ")
    base2.geometry("800x800")
    header = Label(base2, text="Update Query ", font=50, height=4)
    header.pack()

    text1 = Label(base2, text=" Table Name :")
    text1.place(x=150, y=110)

    inputBox = Entry(base2, font=10, width=30)
    inputBox.place(x=310, y=110)

    text2 = Label(base2, text="Enrollment Number: ")
    text2.place(x=150, y=150)

    inputBox1 = Entry(base2, font=10, width=30)
    inputBox1.place(x=310, y=150)

    text3 = Label(base2, text="Student Name :")
    text3.place(x=150, y=190)

    inputBox2 = Entry(base2, font=10, width=30)
    inputBox2.place(x=310, y=190)

    text4 = Label(base2, text="Student Mob. No.: ")
    text4.place(x=150, y=240)

    inputBox3 = Entry(base2, font=10, width=30)
    inputBox3.place(x=310, y=240)

    text5 = Label(base2, text="Student City: ")
    text5.place(x=150, y=280)

    inputBox4 = Entry(base2,font = 10,width =30)
    inputBox4.place(x=310,y=280)

    btn = Button(base2, text="Update", bg='#0d6efd', fg='white', command=Save1)
    btn.place(x=200, y=330, height=50, width=150)

    btn = Button(base2, text="Reset", bg='#198754', fg='white', command=Reset1)
    btn.place(x=480, y=330, height=50, width=150)

    base2.mainloop()

def Delete():
    def Save():
        t1 = str(inputBox.get())
        t2 = str(inputBox1.get())
        t3 = str(inputBox2.get())
        t4 = str(inputBox3.get())
        t5 = str(inputBox4.get())
        #con = sqlite3.connect("BasicDataTable.db")
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='STUDENT_INFO1')
        q3 = "Delete from " + t1 + " where Enrollment_Number = " + t2 + " and Student_Mob_No = " + t4
        print(q3)
        cur = conn.cursor()
        cur.execute(q3)
        conn.commit()
        conn.close()


    def Reset():
        inputBox.delete(0, END)
        inputBox1.delete(0, END)
        inputBox2.delete(0, END)
        inputBox3.delete(0, END)
        inputBox4.delete(0,END)

    base3 = Tk()
    base3.title("Delete Operation ")
    base3.geometry("800x800")
    header = Label(base3, text="Delete Query ", font=50, height=4)
    header.pack()

    text1 = Label(base3, text=" Table Name :")
    text1.place(x=150, y=110)

    inputBox = Entry(base3, font=10, width=30)
    inputBox.place(x=310, y=110)

    text2 = Label(base3, text="Enrollment Number: ")
    text2.place(x=150, y=150)

    inputBox1 = Entry(base3, font=10, width=30)
    inputBox1.place(x=310, y=150)

    text3 = Label(base3, text="Student Name :")
    text3.place(x=150, y=190)

    inputBox2 = Entry(base3, font=10, width=30)
    inputBox2.place(x=310, y=190)

    text4 = Label(base3, text="Student Mob. No.: ")
    text4.place(x=150, y=240)

    inputBox3 = Entry(base3, font=10, width=30)
    inputBox3.place(x=310, y=240)

    text5 = Label(base3, text="Student City: ")
    text5.place(x=150, y=280)

    inputBox4 = Entry(base3,font = 10,width =30)
    inputBox4.place(x=310,y=280)

    btn = Button(base3, text="Delete", bg='#0d6efd', fg='white', command=Save)
    btn.place(x=200, y=330, height=50, width=150)

    btn = Button(base3, text="Reset", bg='#198754', fg='white', command=Reset)
    btn.place(x=480, y=330, height=50, width=150)

    base3.mainloop()
def reset():
    txt.delete('1.0', 'end')
def Search():

    var = StringVar()
mb = Menu(base,bg = "brown",font = fontstyle)
m1 = Menu(mb,tearoff = False)
m1.add_command(label = "Insert        ctrl+I",font = fontstyle,command = Insert)
m1.add_command(label = "Update      ctrl+U",font = fontstyle)
m1.add_command(label = "Delete       ctrl+D",font = fontstyle)
m1.add_separator()
m1.add_command(label = "Quit            Alt+X",font = fontstyle)
mb.add_cascade(menu = m1,label = "Operation",font=fontstyle)
base.configure(menu = mb)
txt = Text(base,font = fontstyle,width = '75',height = '5')
txt.place(x=25,y=58)
btn1 = Button(base,text = "Save",bg = "brown",font = fontstyle,command=Save,width = '5',height = '1')
btn1.place(x =645, y =12)
btn2 = Button(base,text = 'Run',bg = 'brown',font = fontstyle,command=Run,width = '5',height = '1')
btn2.place(x = 713,y = 12)
btn3 = Button(base,text = "INSERT Query",bg = "#BFBFBF",font = fontstyle,command=Insert,width = '13',height = '1')
btn3.place(x =30, y =205)
btn4 = Button(base,text = 'UPDATE Query',bg = '#BFBFBF',font = fontstyle,command=Update,width = '13',height = '1')
btn4.place(x = 175,y = 205)
btn5 = Button(base,text = "DELETE Query",bg = "#BFBFBF",font = fontstyle,command=Delete,width = '13',height = '1')
btn5.place(x =323, y =205)
btn6 = Button(base,text = 'Reset',bg = '#BFBFBF',font = fontstyle,command=reset,width = '7',height = '1')
btn6.place(x = 470,y = 205)
CB = Checkbutton(base, text="Auto-Commit", bg = "brown",font = fontstyle,width='10',onvalue = 1)
CB.select()
CB.place( x=28,y= 18)
l4 = Label(base,width = 50,height = 18,font = fontstyle,bg = '#FCFCFC')
l4.place(x=30,y=310)
l1 = Label(base,text = "Column Name",width = 13,height = 1,font = fontstyle,bg = '#DCDCDC')
l1.place(x=45,y=265)
l2 = Label(base,text = "Datatype",width = 13,height = 1,font = fontstyle,bg = '#DCDCDC')
l2.place(x=215,y=265)
l3 = Label(base,text = "Length",width = 13,height = 1,font = fontstyle,bg = '#DCDCDC')
l3.place(x=380,y=265)
btn7 = Button(base,text='Create Table',bg = 'silver',font = fontstyle,width = 11,height = 1)
btn7.place(x=540,y=270)


my_entries = []
def something():
    entry_list = " "
    for entries in my_entries:
        entry_list = entry_list + str(entries) + "\n"
        print(entry_list)
y = 0
ls = [0]
def add_record():
    if len(ls)!=0:
        y = ls[0]
        ls.remove(ls[0])
        col_nm = Entry(l4, bg="white", font=fontstyle, width='13')
        col_nm.grid(row=y, column=0, sticky='w', pady=10,padx=10)
        col_nm.insert(0,'5')
        #col_nm.place(x=70, y=313)
        datatypes = (
        'BIGINT', 'BLOB', 'BOOLEAN', 'CHAR', 'DATE', 'DATETIME', 'DOUBLE', 'DECIMAL', 'INTEGER', 'INT', 'NONE',
        'NUMERIC', 'REAL', 'TEXT', 'STRING', 'TIME', 'VARCHAR')
        dt = ttk.Combobox(l4, values=datatypes, state='read', width=11)
        dt.set('NUMERIC')
        dt.grid(row=y,column=1,sticky='w',pady=10,padx=10)
        #dt.place(x=255, y=315)
        length = Entry(l4, bg="white", font=fontstyle, width='13')
        length.grid(row=y, column=2, sticky='w', pady=10, padx=10)
        length.insert(0,"10")
        #length.place(x=390, y=310)
        my_entries.append(col_nm)
        ls.append(y+1)
        col_nm.delete(0,END)
        dt.delete(0,END)
        length.delete(0,END)
        print(ls,y)
btn8 = Button(base,text='Add Column',bg = 'blue',font = fontstyle,command = add_record,width = 11,height = 1)
btn8.place(x=670,y=270)

base.mainloop()