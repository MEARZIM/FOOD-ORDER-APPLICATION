#Admin Login
#Username: ayan     Password: ayan123
from tkinter import *
from tkinter import messagebox   
import sqlite3
from datetime import date
from datetime import time 
from datetime import datetime
from PIL import ImageTk, Image
import db_operations as db
import Admin_db_operations as adb
w = Tk()
w.geometry("1366x768")
w.state('normal')
# w.resizable(0,0)
canvas = Canvas(w, width = 1920, height = 1273, bg = 'black')
canvas.pack(expand = YES, fill = BOTH)
image1 = ImageTk.PhotoImage(file = r"shake.jpg")
canvas.create_image(0, 0, image = image1, anchor = NW)
val1=val2=val3=val4=val5=val6=val7=val8=val9=val10=val11=val12=val13=val14=val15=0
val16=val17=val18=val19=val20=val21=val22=val23=val24=val25=val26=val27=0
tab1=tab2=tab3=tab4=tab5=tab6=tab7=tab8=tab9=tab10=0
total1=total2=total3=total3=total4=total5=total5=total6=total7=total8=total9=total10=total11=total12=total13=total14=0
total15=total16=total17=total18=total19=total20=total21=total22=total23=total24=total25=total26=total27=0
USERNAME = StringVar()
PASSWORD = StringVar()
date1 = StringVar()
date2 = StringVar()
now=datetime.now()
def Database():
    global conn, cursor
    conn = sqlite3.connect("usernpass.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")       
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'ayan' AND `password` = 'ayan123'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('ayan', 'ayan123')")
        conn.commit() 
def table1():
    global tab1
    tab1=1
    menu()
def table2():
    global tab2
    tab2=1
    menu()
def table3():
    global tab3
    tab3=1
    menu()
def table4():
    global tab4
    tab4=1
    menu()
def table5():
    global tab5
    tab5=1
    menu()
def table6():
    global tab6
    tab6=1
    menu()
def table7():
    global tab7
    tab7=1
    menu()
def table8():
    global tab8
    tab8=1
    menu()
def table9():
    global tab9
    tab9=1
    menu()
def table10():
    global tab10
    tab10=1
    menu()
def bac1():
    global tab1
    global tab2
    global tab3
    global tab4
    global tab5
    global tab6
    global tab7
    global tab8
    global tab9
    global tab10
    tab1=tab2=tab3=tab4=tab5=tab6=tab7=tab8=tab9=tab10=0
    t.withdraw()
def Shackburger():
    z1=Toplevel(w)
    z1.geometry("550x550+350+100")
    z1.focus_set()
    canvas = Canvas(z1, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z1, image=photox, compound = TOP, command=z1.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"Shack burger.png")
    b1=Button(z1, text = 'Shack Burger', image = photo1, compound = TOP, font='LITHOGRAPH',bd=0)
    b1.image=photo1
    b1.place(x=70,y=100)    
    def add():
        global val1 
        val1=val1+1
        if val1>=10 :
            val1=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val1)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val1)
    def sub():
        global val1
        val1=val1-1
        if val1<0 :
            val1=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val1)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val1)
    def cnf():
        global total1
        global val1
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        total1=price1*val1
        if(tab1==1):
            db.insert1('Shack burger',val1,price1,total1)
        elif(tab2==1):
            db.insert2('Shack burger',val1,price1,total1)
        elif(tab3==1):
            db.insert3('Shack burger',val1,price1,total1)
        elif(tab4==1):
            db.insert4('Shack burger',val1,price1,total1)
        elif(tab5==1):           
            db.insert5('Shack burger',val1,price1,total1)
        elif(tab6==1):            
            db.insert6('Shack burger',val1,price1,total1)
        elif(tab7==1):           
            db.insert7('Shack burger',val1,price1,total1)
        elif(tab8==1):            
            db.insert8('Shack burger',val1,price1,total1)
        elif(tab9==1):            
            db.insert9('Shack burger',val1,price1,total1)
        elif(tab10==1):
            db.insert10('Shack burger',val1,price1,total1)
        val1=0
        total1=0
        z1.destroy()
    txtbox=Text(z1,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)    
    plus=Button(z1,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)    
    minus=Button(z1,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)    
    b2=Button(z1, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)    
    var = StringVar()
    label1 = Label( z1, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white')
    var.set("Cheese Burger topped with lettuce, tomato\nand ShackSauce")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z1, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹5")
    price1=5
    label2.place(x=70,y=420)
    z1.title("Shack Burger")
def Shroomburger():
    z2=Toplevel(w)
    z2.geometry("550x550+350+100")
    z2.focus_set()
    canvas = Canvas(z2, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z2, image=photox, compound = TOP, command=z2.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"Shroom burger.png")
    b1=Button(z2, text = 'Shroom Burger', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val2 
        val2=val2+1
        if val2>=10 :
            val2=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val2)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val2)
    def sub():
        global val2
        val2=val2-1
        if val2<0 :
            val2=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val2)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val2)
    def cnf():
        global total2
        global val2
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        total2=price2*val2
        if(tab1==1):
            db.insert1('Shroom Burger',val2,price2,total2)
        elif(tab2==1):
            db.insert2('Shroom Burger',val2,price2,total2)
        elif(tab3==1):
            db.insert3('Shroom Burger',val2,price2,total2)
        elif(tab4==1):
            db.insert4('Shroom Burger',val2,price2,total2)
        elif(tab5==1):           
            db.insert5('Shroom Burger',val2,price2,total2)
        elif(tab7==1):           
            db.insert7('Shroom Burger',val2,price2,total2)
        elif(tab8==1):            
            db.insert8('Shroom Burger',val2,price2,total2)
        elif(tab9==1):            
            db.insert9('Shroom Burger',val2,price2,total2)
        elif(tab10==1):
            db.insert10('Shroom Burger',val2,price2,total2)
        val2=0
        total2=0
        z2.destroy()
    txtbox=Text(z2,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z2,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z2,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z2, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z2, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Crisp fried portobello mushroom filled with\nmelted muenster and cheddar cheeses,\ntopped with lettuce, tomato and ShackSauce")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z2, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹4")
    price2=4
    label2.place(x=70,y=420)
    z2.title("Shroom Burger")
def Smokeshack():
    z3=Toplevel(w)
    z3.geometry("550x550+350+100")
    z3.focus_set()
    canvas = Canvas(z3, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z3, image=photox, compound = TOP, command=z3.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"Smoke shack.png")
    b1=Button(z3, text = 'Smoke Shack', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val3 
        val3=val3+1
        if val3>=10 :
            val3=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val3)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val3)
    def sub():
        global val3
        val3=val3-1
        if val3<0 :
            val3=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val3)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val3)
    def cnf():
        global total3
        global val3
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        total3=price3*val3
        if(tab1==1):
            db.insert1('Smoke Shack',val3,price3,total3)
        elif(tab2==1):
            db.insert2('Smoke Shack',val3,price3,total3)
        elif(tab3==1):
            db.insert3('Smoke Shack',val3,price3,total3)
        elif(tab4==1):
            db.insert4('Smoke Shack',val3,price3,total3)
        elif(tab5==1):           
            db.insert5('Smoke Shack',val3,price3,total3)
        elif(tab6==1):            
            db.insert6('Smoke Shack',val3,price3,total3)
        elif(tab7==1):           
            db.insert7('Smoke Shack',val3,price3,total3)
        elif(tab8==1):            
            db.insert8('Smoke Shack',val3,price3,total3)
        elif(tab9==1):            
            db.insert9('Smoke Shack',val3,price3,total3)
        elif(tab10==1):
            db.insert10('Smoke Shack',val3,price3,total3)
        val3=0
        total3=0
        z3.destroy()
    txtbox=Text(z3,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z3,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z3,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z3, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z3, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Cheeseburger with veal bacon, spicy chopped\ncherry peppers and ShackSauce")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z3, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹5")
    price3=5
    label2.place(x=70,y=420)
    z3.title("Smoke Shack")
def Stackshack():
    z4=Toplevel(w)
    z4.geometry("550x550+350+100")
    z4.focus_set()
    canvas = Canvas(z4, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z4, image=photox, compound = TOP, command=z4.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"Stack shack.png")
    b1=Button(z4, text = 'Stack Shack', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val4 
        val4=val4+1
        if val4>=10 :
            val4=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val4)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val4)
    def sub():
        global val4
        val4=val4-1
        if val4<0 :
            val4=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val4)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val4)
    def cnf():
        global total4
        global val4
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        total4=price4*val4
        if(tab1==1):
            db.insert1('Stack Shack',val4,price4,total4)
        elif(tab2==1):
            db.insert2('Stack Shack',val4,price4,total4)
        elif(tab3==1):
            db.insert3('Stack Shack',val4,price4,total4)
        elif(tab4==1):
            db.insert4('Stack Shack',val4,price4,total4)
        elif(tab5==1):           
            db.insert5('Stack Shack',val4,price4,total4)
        elif(tab6==1):            
            db.insert6('Stack Shack',val4,price4,total4)
        elif(tab7==1):           
            db.insert7('Stack Shack',val4,price4,total4)            
        elif(tab8==1):       
            db.insert8('Stack Shack',val4,price4,total4)
        elif(tab9==1):            
            db.insert9('Stack Shack',val4,price4,total4)
        elif(tab10==1):
            db.insert10('Stack Shack',val4,price4,total4)
        val4=0
        total4=0
        z4.destroy()
    txtbox=Text(z4,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z4,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z4,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z4, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z4, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Cheeseburger and a 'Shroom Burger with lettuce,\ntomato and ShackSauce")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z4, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹5")
    price4=5
    label2.place(x=70,y=420)
    z4.title("Stack shack")
def Cheeseburger():
    z5=Toplevel(w)
    z5.geometry("550x550+350+100")
    z5.focus_set()
    canvas = Canvas(z5, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z5, image=photox, compound = TOP, command=z5.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"Cheese burger.png")
    b1=Button(z5, text = 'Cheese Burger', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val5 
        val5=val5+1
        if val5>=10 :
            val5=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val5)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val5)
    def sub():
        global val5
        val5=val5-1
        if val5<0 :
            val5=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val5)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val5)
    def cnf():
        global total5
        global val5
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        total5=price5*val5
        if(tab1==1):
            db.insert1('Cheese Burger',val5,price5,total5)
        elif(tab2==1):
            db.insert2('Cheese Burger',val5,price5,total5)
        elif(tab3==1):
            db.insert3('Cheese Burger',val5,price5,total5)
        elif(tab4==1):
            db.insert4('Cheese Burger',val5,price5,total5)
        elif(tab5==1):           
            db.insert5('Cheese Burger',val5,price5,total5)
        elif(tab6==1):            
            db.insert6('Cheese Burger',val5,price5,total5)
        elif(tab7==1):           
            db.insert7('Cheese Burger',val5,price5,total5)
        elif(tab8==1):            
            db.insert8('Cheese Burger',val5,price5,total5)
        elif(tab9==1):            
            db.insert9('Cheese Burger',val5,price5,total5)
        elif(tab10==1):
            db.insert10('Cheese Burger',val5,price5,total5)
        val5=0
        total5=0
        z5.destroy()
    txtbox=Text(z5,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z5,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z5,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z5, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z5, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Let us know if you would like lettuce, tomato,\npickle or onion")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z5, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹5")
    price5=5
    label2.place(x=70,y=420)
    z5.title("Cheese Burger")
def Hamburger():
    z6=Toplevel(w)
    z6.geometry("550x550+350+100")
    z6.focus_set()
    canvas = Canvas(z6, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z6, image=photox, compound = TOP, command=z6.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"Hamburger.png")
    b1=Button(z6, text = 'Hamburger', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val6 
        val6=val6+1
        if val6>=10 :
            val6=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val6)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val6)

    def sub():
        global val6
        val6=val6-1
        if val6<0 :
            val6=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val6)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val6)
    def cnf():
        global total6
        global val6
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        total6=price6*val6
        if(tab1==1):
            db.insert1('Hamburger',val6,price6,total6)
        elif(tab2==1):
            db.insert2('Hamburger',val6,price6,total6)
        elif(tab3==1):
            db.insert3('Hamburger',val6,price6,total6)
        elif(tab5==1):           
            db.insert5('Hamburger',val6,price6,total6)
        elif(tab6==1):            
            db.insert6('Hamburger',val6,price6,total6)
        elif(tab7==1):           
            db.insert7('Hamburger',val6,price6,total6)
        elif(tab8==1):            
            db.insert8('Hamburger',val6,price6,total6)
        elif(tab9==1):            
            db.insert9('Hamburger',val6,price6,total6)
        elif(tab10==1):
            db.insert10('Hamburger',val6,price6,total6)
        val6=0
        total6=0
        z6.destroy()
    txtbox=Text(z6,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z6,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z6,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z6, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z6, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Let us know if you would like lettuce, tomato,\npickle or onion")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z6, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹6")
    price6=6
    label2.place(x=70,y=420)
    z6.title("Hamburger")
def Chicknshack():
    z7=Toplevel(w)
    z7.geometry("550x550+350+100")
    z7.focus_set()
    canvas = Canvas(z7, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z7, image=photox, compound = TOP, command=z7.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"Chick n shack.png")
    b1=Button(z7, text = 'Chick N Shack', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val7 
        val7=val7+1
        if val7>=10 :
            val7=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val7)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val7)

    def sub():
        global val7
        val7=val7-1
        if val7<0 :
            val7=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val7)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val7)
    def cnf():
        global total7
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        global val7
        total7=price7*val7
        if(tab1==1):
            db.insert1('Chick N Shack',val7,price7,total7)
        elif(tab2==1):
            db.insert2('Chick N Shack',val7,price7,total7)
        elif(tab3==1):
            db.insert3('Chick N Shack',val7,price7,total7)
        elif(tab4==1):
            db.insert4('Chick N Shack',val7,price7,total7)
        elif(tab5==1):           
            db.insert5('Chick N Shack',val7,price7,total7)
        elif(tab6==1):            
            db.insert6('Chick N Shack',val7,price7,total7)
        elif(tab7==1):           
            db.insert7('Chick N Shack',val7,price7,total7)
        elif(tab8==1):            
            db.insert8('Chick N Shack',val7,price7,total7)
        elif(tab9==1):            
            db.insert9('Chick N Shack',val7,price7,total7)
        elif(tab10==1):
            db.insert10('Chick N Shack',val7,price7,total7)
        val7=0
        total7=0
        z7.destroy()
    txtbox=Text(z7,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z7,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z7,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z7, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z7, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Crispy chicken breast with lettuce, pickles\nand herb mayo")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z7, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹4")
    price7=4
    label2.place(x=70,y=420)
    z7.title("Chick N Shack")
    
def Chipotlecheddarchicken():
    z8=Toplevel(w)
    z8.geometry("550x550+350+100")
    z8.focus_set()
    canvas = Canvas(z8, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z8, image=photox, compound = TOP, command=z8.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"Chipotle cheddar chicken.png")
    b1=Button(z8, text = 'Chipotle Chicken', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val8 
        val8=val8+1
        if val8>=10 :
            val8=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val8)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val8)

    def sub():
        global val8
        val8=val8-1
        if val8<0 :
            val8=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val8)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val8)
    def cnf():
        global total8
        global val8
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        total8=price8*val8
        if(tab1==1):
            db.insert1('Chipotle Chicken',val8,price8,total8)
        elif(tab2==1):
            db.insert2('Chipotle Chicken',val8,price8,total8)
        elif(tab3==1):
            db.insert3('Chipotle Chicken',val8,price8,total8)
        elif(tab4==1):
            db.insert4('Chipotle Chicken',val8,price8,total8)
        elif(tab5==1):           
            db.insert5('Chipotle Chicken',val8,price8,total8)
        elif(tab6==1):            
            db.insert6('Chipotle Chicken',val8,price8,total8)
        elif(tab7==1):           
            db.insert7('Chipotle Chicken',val8,price8,total8)
        elif(tab8==1):            
            db.insert8('Chipotle Chicken',val8,price8,total8)
        elif(tab9==1):            
            db.insert9('Chipotle Chicken',val8,price8,total8)
        elif(tab10==1):
            db.insert10('Chipotle Chicken',val8,price8,total8)
        val8=0
        total8=0
        z8.destroy()
    txtbox=Text(z8,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z8,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z8,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z8, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z8, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Crispy chicken breast topped with chipotle cheddar\ncheese sauce, pickled white onion, shwhiteded lettuce\nand chipotle ShackSauce")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z8, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹5")
    price8=5
    label2.place(x=70,y=420)
    z8.title("Chipotle Chicken")
def shackcagohotdog():
    z9=Toplevel(w)
    z9.geometry("550x550+350+100")
    z9.focus_set()
    canvas = Canvas(z9, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z9, image=photox, compound = TOP, command=z9.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"shack-cago hot dog.png")
    b1=Button(z9, text = 'Shack-Cago HD', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val9 
        val9=val9+1
        if val9>=10 :
            val9=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val9)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val9)
    def sub():
        global val9
        val9=val9-1
        if val9<0 :
            val9=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val9)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val9)
    def cnf():
        global total9
        global val9
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        total9=price9*val9
        if(tab1==1):
            db.insert1('Shack-Cago HD',val9,price9,total9)
        elif(tab2==1):
            db.insert2('Shack-Cago HD',val9,price9,total9)
        elif(tab3==1):
            db.insert3('Shack-Cago HD',val9,price9,total9)
        elif(tab4==1):
            db.insert4('Shack-Cago HD',val9,price9,total9)
        elif(tab5==1):           
            db.insert5('Shack-Cago HD',val9,price9,total9)
        elif(tab6==1):            
            db.insert6('Shack-Cago HD',val9,price9,total9)
        elif(tab7==1):           
            db.insert7('Shack-Cago HD',val9,price9,total9)
        elif(tab8==1):            
            db.insert8('Shack-Cago HD',val9,price9,total9)
        elif(tab9==1):            
            db.insert9('Shack-Cago HD',val9,price9,total9)
        elif(tab10==1):
            db.insert10('Shack-Cago HD',val9,price9,total9)
        val9=0
        total9=0
        z9.destroy()
    txtbox=Text(z9,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z9,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z9,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z9, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z9, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Vienna all-beef hot dog dragged through\nthe garden with Rick's Picks Shack relish,\nonion, cucumber, pickle, tomato, sport\npepper, celery salt and mustard")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z9, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹8")
    price9=8
    label2.place(x=70,y=450)
    z9.title("Shack-Cago HD")
def newyorkstylehotdog():
    z10=Toplevel(w)
    z10.geometry("550x550+350+100")
    z10.focus_set()
    canvas = Canvas(z10, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z10, image=photox, compound = TOP, command=z10.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"new york style hotdog.png")
    b1=Button(z10, text = 'NY Style Hotdog', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val10 
        val10=val10+1
        if val10>=10 :
            val10=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val10)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val10)

    def sub():
        global val10
        val10=val10-1
        if val10<0 :
            val10=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val10)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val10)
    def cnf():
        global total10
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        global val10
        total10=price10*val10
        if(tab1==1):
            db.insert1('NY Style Hotdog',val10,price10,total10)
        elif(tab2==1):
            db.insert2('NY Style Hotdog',val10,price10,total10)
        elif(tab3==1):
            db.insert3('NY Style Hotdog',val10,price10,total10)
        elif(tab4==1):
            db.insert4('NY Style Hotdog',val10,price10,total10)
        elif(tab5==1):           
            db.insert5('NY Style Hotdog',val10,price10,total10)
        elif(tab6==1):            
            db.insert6('NY Style Hotdog',val10,price10,total10)
        elif(tab7==1):           
            db.insert7('NY Style Hotdog',val10,price10,total10)
        elif(tab8==1):            
            db.insert8('NY Style Hotdog',val10,price10,total10)
        elif(tab9==1):            
            db.insert9('NY Style Hotdog',val10,price10,total10)
        elif(tab10==1):
            db.insert10('NY Style Hotdog',val10,price10,total10)
        val10=0
        total10=0
        z10.destroy()
    txtbox=Text(z10,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z10,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z10,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z10, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z10, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Vienna all-beef hot dog")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z10, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹7")
    price10=7
    label2.place(x=70,y=420)
    z10.title("NY Style Hotdog")
def cheesehotdog():
    z11=Toplevel(w)
    z11.geometry("550x550+350+100")
    z11.focus_set()
    canvas = Canvas(z11, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z11, image=photox, compound = TOP, command=z11.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"cheese hotdog.png")
    b1=Button(z11, text = 'Cheese Hotdog', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val11 
        val11=val11+1
        if val11>=10 :
            val11=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val11)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val11)

    def sub():
        global val11
        val11=val11-1
        if val11<0 :
            val11=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val11)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val11)
    def cnf():
        global total11
        global val11
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        total11=price11*val11
        if(tab1==1):
            db.insert1('Cheese Hotdog',val11,price11,total11)
        elif(tab2==1):
            db.insert2('Cheese Hotdog',val11,price11,total11)
        elif(tab3==1):
            db.insert3('Cheese Hotdog',val11,price11,total11)
        elif(tab4==1):
            db.insert4('Cheese Hotdog',val11,price11,total11)
        elif(tab5==1):           
            db.insert5('Cheese Hotdog',val11,price11,total11)
        elif(tab6==1):            
            db.insert6('Cheese Hotdog',val11,price11,total11)
        elif(tab7==1):           
            db.insert7('Cheese Hotdog',val11,price11,total11)
        elif(tab8==1):            
            db.insert8('Cheese Hotdog',val11,price11,total11)
        elif(tab9==1):            
            db.insert9('Cheese Hotdog',val11,price11,total11)
        elif(tab10==1):
            db.insert10('Cheese Hotdog',val11,price11,total11)
        val11=0
        total11=0
        z11.destroy()
    txtbox=Text(z11,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z11,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z11,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z11, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z11, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Vienna all-beef hot dog topped with our\nShack cheddar and American cheese sauce")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z11, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹5")
    price11=5
    label2.place(x=70,y=420)
    z11.title("Cheese Hotdog")
def normalfries():
    z12=Toplevel(w)
    z12.geometry("550x550+350+100")
    z12.focus_set()
    canvas = Canvas(z12, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z12, image=photox, compound = TOP, command=z12.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"normal fries.png")
    b1=Button(z12, text = 'Normal Fries', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val12 
        val12=val12+1
        if val12>=10 :
            val12=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val12)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val12)

    def sub():
        global val12
        val12=val12-1
        if val12<0 :
            val12=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val12)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val12)
    def cnf():
        global total12
        global val12
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        total12=price12*val12
        if(tab1==1):
            db.insert1('Normal Fries',val12,price12,total12)
        elif(tab2==1):
            db.insert2('Normal Fries',val12,price12,total12)
        elif(tab3==1):
            db.insert3('Normal Fries',val12,price12,total12)
        elif(tab4==1):
            db.insert4('Normal Fries',val12,price12,total12)
        elif(tab5==1):           
            db.insert5('Normal Fries',val12,price12,total12)
        elif(tab6==1):            
            db.insert6('Normal Fries',val12,price12,total12)
        elif(tab7==1):           
            db.insert7('Normal Fries',val12,price12,total12)
        elif(tab8==1):            
            db.insert8('Normal Fries',val12,price12,total12)
        elif(tab9==1):            
            db.insert9('Normal Fries',val12,price12,total12)
        elif(tab10==1):
            db.insert10('Normal Fries',val12,price12,total12)
        val12=0
        total12=0
        z12.destroy()
    txtbox=Text(z12,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z12,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z12,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z12, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z12, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Crinkle cut Yukon potatoes, 100% free of\nartificial trans fats and 25% less fat than\naverage fries.")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z12, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹2")
    price12=2
    label2.place(x=70,y=420)
    z12.title("Normal Fries")
def cheesefries():
    z13=Toplevel(w)
    z13.geometry("550x550+350+100")
    z13.focus_set()
    canvas = Canvas(z13, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z13, image=photox, compound = TOP, command=z13.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"cheese fries.png")
    b1=Button(z13, text = 'Cheese Fries', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val13 
        val13=val13+1
        if val13>=10 :
            val13=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val13)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val13)

    def sub():
        global val13
        val13=val13-1
        if val13<0 :
            val13=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val13)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val13)
    def cnf():
        global total13
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        global val13
        total13=price13*val13
        if(tab1==1):
            db.insert1('Cheese Fries',val13,price13,total13)
        elif(tab2==1):
            db.insert2('Cheese Fries',val13,price13,total13)
        elif(tab3==1):
            db.insert3('Cheese Fries',val13,price13,total13)
        elif(tab4==1):
            db.insert4('Cheese Fries',val13,price13,total13)
        elif(tab5==1):           
            db.insert5('Cheese Fries',val13,price13,total13)
        elif(tab6==1):            
            db.insert6('Cheese Fries',val13,price13,total13)
        elif(tab7==1):           
            db.insert7('Cheese Fries',val13,price13,total13)
        elif(tab8==1):            
            db.insert8('Cheese Fries',val13,price13,total13)
        elif(tab9==1):            
            db.insert9('Cheese Fries',val13,price13,total13)
        elif(tab10==1):
            db.insert10('Cheese Fries',val13,price13,total13)
        val13=0
        total13=0
        z13.destroy()
    txtbox=Text(z13,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z13,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z13,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z13, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z13, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Topped with out Shack cheddar and\nAmerican cheese sauce")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z13, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹5")
    price13=5
    label2.place(x=70,y=420)
    z13.title("Cheese Fries")
def vealbaconandcheesefries():
    z14=Toplevel(w)
    z14.geometry("550x550+350+100")
    z14.focus_set()
    canvas = Canvas(z14, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z14, image=photox, compound = TOP, command=z14.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"veal bacon and cheese fries.png")
    b1=Button(z14, text = 'Bacon & Cheese', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val14 
        val14=val14+1
        if val14>=10 :
            val14=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val14)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val14)

    def sub():
        global val14
        val14=val14-1
        if val14<0 :
            val14=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val14)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val14)
    def cnf():
        global total14
        global val14
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        total14=price14*val14
        if(tab1==1):
            db.insert1('Bacon & Cheese',val14,price14,total14)
        elif(tab2==1):
            db.insert2('Bacon & Cheese',val14,price14,total14)
        elif(tab3==1):
            db.insert3('Bacon & Cheese',val14,price14,total14)
        elif(tab4==1):
            db.insert4('Bacon & Cheese',val14,price14,total14)
        elif(tab5==1):           
            db.insert5('Bacon & Cheese',val14,price14,total14)
        elif(tab6==1):            
            db.insert6('Bacon & Cheese',val14,price14,total14)
        elif(tab7==1):           
            db.insert7('Bacon & Cheese',val14,price14,total14)
        elif(tab8==1):            
            db.insert8('Bacon & Cheese',val14,price14,total14)
        elif(tab9==1):            
            db.insert9('Bacon & Cheese',val14,price14,total14)
        elif(tab10==1):
            db.insert10('Bacon & Cheese',val14,price14,total14)
        val14=0
        total14=0
        z14.destroy()
    txtbox=Text(z14,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z14,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z14,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z14, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z14, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Topped with out Shack cheddar and\nAmerican cheese sauce with veal bacon")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z14, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹7")
    price14=7
    label2.place(x=70,y=420)
    z14.title("Bacon & Cheese")
def cinnamonsoul():
    z15=Toplevel(w)
    z15.geometry("550x550+350+100")
    z15.focus_set()
    canvas = Canvas(z15, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z15, image=photox, compound = TOP, command=z15.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"cinnamon soul.png")
    b1=Button(z15, text = 'Cinnamon Soul', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val15 
        val15=val15+1
        if val15>=10 :
            val15=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val15)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val15)

    def sub():
        global val15
        val15=val15-1
        if val15<0 :
            val15=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val15)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val15)
    def cnf():
        global total15
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        global val15
        total15=price15*val15
        if(tab1==1):
            db.insert1('Cinnamon Soul',val15,price15,total15)
        elif(tab2==1):
            db.insert2('Cinnamon Soul',val15,price15,total15)
        elif(tab3==1):
            db.insert3('Cinnamon Soul',val15,price15,total15)
        elif(tab4==1):
            db.insert4('Cinnamon Soul',val15,price15,total15)
        elif(tab5==1):           
            db.insert5('Cinnamon Soul',val15,price15,total15)
        elif(tab6==1):            
            db.insert6('Cinnamon Soul',val15,price15,total15)
        elif(tab7==1):           
            db.insert7('Cinnamon Soul',val15,price15,total15)
        elif(tab8==1):
            db.insert8('Cinnamon Soul',val15,price15,total15)
        elif(tab9==1):            
            db.insert9('Cinnamon Soul',val15,price15,total15)
        elif(tab10==1):
            db.insert10('Cinnamon Soul',val15,price15,total15)
        val15=0
        total15=0
        z15.destroy()
    txtbox=Text(z15,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z15,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z15,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z15, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z15, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Vanilla custard, cinnamon marshmallow\nsauce, strawberry purée and\ncinnamon dusted fried waffles")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z15, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹8")
    price15=8
    label2.place(x=70,y=420)
    z15.title("Cinnamon Soul")
def blackandwhite():
    z16=Toplevel(w)
    z16.geometry("550x550+350+100")
    z16.focus_set()
    canvas = Canvas(z16, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z16, image=photox, compound = TOP, command=z16.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"black and white.png")
    b1=Button(z16, text = 'black and White', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val16 
        val16=val16+1
        if val16>=10 :
            val16=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val16)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val16)

    def sub():
        global val16
        val16=val16-1
        if val16<0 :
            val16=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val16)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val16)
    def cnf():
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        global total16
        global val16
        total16=price16*val16
        if(tab1==1):
            db.insert1('green and White',val16,price16,total16)
        elif(tab2==1):
            db.insert2('green and White',val16,price16,total16)
        elif(tab3==1):
            db.insert3('green and White',val16,price16,total16)
        elif(tab4==1):
            db.insert4('green and White',val16,price16,total16)
        elif(tab5==1):           
            db.insert5('green and White',val16,price16,total16)
        elif(tab6==1):            
            db.insert6('green and White',val16,price16,total16)
        elif(tab7==1):           
            db.insert7('green and White',val16,price16,total16)
        elif(tab8==1):            
            db.insert8('green and White',val16,price16,total16)
        elif(tab9==1):            
            db.insert9('green and White',val16,price16,total16)
        elif(tab10==1):
            db.insert10('green and White',val16,price16,total16)
        val16=0
        total16=0
        z16.destroy()
    txtbox=Text(z16,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z16,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z16,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z16, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z16, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Vanilla frozen custard hand spun with Shack\nfudge sauce")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z16, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹5")
    price16=5
    label2.place(x=70,y=420)
    z16.title("green and White")
def freshhbrewedicetea():
    z17=Toplevel(w)
    z17.geometry("550x550+350+100")
    z17.focus_set()
    canvas = Canvas(z17, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z17, image=photox, compound = TOP, command=z17.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"fresh brewed ice tea.png")
    b1=Button(z17, text = 'Ice Tea', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val17 
        val17=val17+1
        if val17>=10 :
            val17=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val17)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val17)

    def sub():
        global val17
        val17=val17-1
        if val17<0 :
            val17=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val17)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val17)
    def cnf():
        global total17
        global val17
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        total17=price17*val17
        if(tab1==1):
            db.insert1('Ice Tea',val17,price17,total17)
        elif(tab2==1):
            db.insert2('Ice Tea',val17,price17,total17)
        elif(tab3==1):
            db.insert3('Ice Tea',val17,price17,total17)
        elif(tab4==1):
            db.insert4('Ice Tea',val17,price17,total17)
        elif(tab5==1):           
            db.insert5('Ice Tea',val17,price17,total17)
        elif(tab6==1):            
            db.insert6('Ice Tea',val17,price17,total17)
        elif(tab7==1):           
            db.insert7('Ice Tea',val17,price17,total17)
        elif(tab8==1):            
            db.insert8('Ice Tea',val17,price17,total17)
        elif(tab9==1):            
            db.insert9('Ice Tea',val17,price17,total17)
        elif(tab10==1):
            db.insert10('Ice Tea',val17,price17,total17)
        val17=0
        total17=0
        z17.destroy()
    txtbox=Text(z17,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z17,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z17,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z17, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z17, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Iced tea flavours:\n->Iced Peach Green Tea.\n->Iced Peach Green Tea Lemonade.\n->Iced Matcha Green Tea Latte.\n->Iced Green Tea.\n->Iced Green Tea Lemonade.")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z17, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹6")
    price17=6
    label2.place(x=70,y=490)
    z17.title("Ice Tea")
def floatbottledwater():
    z18=Toplevel(w)
    z18.geometry("550x550+350+100")
    z18.focus_set()
    canvas = Canvas(z18, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z18, image=photox, compound = TOP, command=z18.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"float bottled water.png")
    b1=Button(z18, text = 'Float Water', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val18 
        val18=val18+1
        if val18>=10 :
            val18=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val18)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val18)

    def sub():
        global val18
        val18=val18-1
        if val18<0 :
            val18=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val18)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val18)
    def cnf():
        global total18
        global val18
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        total18=price18*val18
        if(tab1==1):
            db.insert1('Float Water',val18,price18,total18)
        elif(tab2==1):
            db.insert2('Float Water',val18,price18,total18)
        elif(tab3==1):
            db.insert3('Float Water',val18,price18,total18)
        elif(tab4==1):
            db.insert4('Float Water',val18,price18,total18)
        elif(tab5==1):           
            db.insert5('Float Water',val18,price18,total18)
        elif(tab6==1):            
            db.insert6('Float Water',val18,price18,total18)
        elif(tab7==1):           
            db.insert7('Float Water',val18,price18,total18)
        elif(tab8==1):            
            db.insert8('Float Water',val18,price18,total18)
        elif(tab9==1):            
            db.insert9('Float Water',val18,price18,total18)
        elif(tab10==1):
            db.insert10('Float Water',val18,price18,total18)
        val18=0
        total18=0
        z18.destroy()
    txtbox=Text(z18,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z18,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z18,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z18, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z18, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Shake Shack's exclusive packaged water bottle\nfrom Alpes")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z18, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹3")
    price18=3
    label2.place(x=70,y=420)
    z18.title("Float Water")
def fiftyfifty():
    z19=Toplevel(w)
    z19.geometry("550x550+350+100")
    z19.focus_set()
    canvas = Canvas(z19, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z19, image=photox, compound = TOP, command=z19.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"fiftyfifty.png")
    b1=Button(z19, text = 'Fifty-Fifty', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val19 
        val19=val19+1
        if val19>=10 :
            val19=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val19)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val19)

    def sub():
        global val19
        val19=val19-1
        if val19<0 :
            val19=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val19)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val19)
    def cnf():
        global total19
        global val19
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        total19=price19*val19
        if(tab1==1):
            db.insert1('Fifty-Fifty',val19,price19,total19)
        elif(tab2==1):
            db.insert2('Fifty-Fifty',val19,price19,total19)
        elif(tab3==1):
            db.insert3('Fifty-Fifty',val19,price19,total19)
        elif(tab4==1):
            db.insert4('Fifty-Fifty',val19,price19,total19)
        elif(tab5==1):           
            db.insert5('Fifty-Fifty',val19,price19,total19)
        elif(tab6==1):            
            db.insert6('Fifty-Fifty',val19,price19,total19)
        elif(tab7==1):           
            db.insert7('Fifty-Fifty',val19,price19,total19)
        elif(tab8==1):            
            db.insert8('Fifty-Fifty',val19,price19,total19)
        elif(tab9==1):            
            db.insert9('Fifty-Fifty',val19,price19,total19)
        elif(tab10==1):
            db.insert10('Fifty-Fifty',val19,price19,total19)
        val19=0
        total19=0
        z19.destroy()
    txtbox=Text(z19,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z19,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z19,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z19, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z19, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Half lemonade, half iced tea")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z19, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹5")
    price19=5
    label2.place(x=70,y=420)
    z19.title("Fifty-Fifty")
def shackmadelemonade():
    z20=Toplevel(w)
    z20.geometry("550x550+350+100")
    z20.focus_set()
    canvas = Canvas(z20, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z20, image=photox, compound = TOP, command=z20.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"shack-made lemonade.png")
    b1=Button(z20, text = 'Shack Lemonade', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val20 
        val20=val20+1
        if val20>=10 :
            val20=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val20)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val20)

    def sub():
        global val20
        val20=val20-1
        if val20<0 :
            val20=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val20)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val20)
    def cnf():
        global total20
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        global val20
        total20=price20*val20
        if(tab1==1):
            db.insert1('Shack Lemonade',val20,price20,total20)
        elif(tab2==1):
            db.insert2('Shack Lemonade',val20,price20,total20)
        elif(tab3==1):
            db.insert3('Shack Lemonade',val20,price20,total20)
        elif(tab4==1):
            db.insert4('Shack Lemonade',val20,price20,total20)
        elif(tab5==1):           
            db.insert5('Shack Lemonade',val20,price20,total20)
        elif(tab6==1):            
            db.insert6('Shack Lemonade',val20,price20,total20)
        elif(tab7==1):       
            db.insert7('Shack Lemonade',val20,price20,total20)
        elif(tab8==1):            
            db.insert8('Shack Lemonade',val20,price20,total20)
        elif(tab9==1):            
            db.insert9('Shack Lemonade',val20,price20,total20)
        elif(tab10==1):
            db.insert10('Shack Lemonade',val20,price20,total20)
        val20=0
        total20=0
        z20.destroy()
    txtbox=Text(z20,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z20,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z20,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z20, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z20, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Your choice: Original / Featuwhite <3")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z20, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹4")
    price20=4
    label2.place(x=70,y=420)
    z20.title("Shack Lemonade")
def shackattack():
    z21=Toplevel(w)
    z21.geometry("550x550+350+100")
    z21.focus_set()
    canvas = Canvas(z21, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z21, image=photox, compound = TOP, command=z21.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"shack attack.png")
    b1=Button(z21, text = 'Shack Attack', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val21 
        val21=val21+1
        if val21>=10 :
            val21=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val21)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val21)

    def sub():
        global val21
        val21=val21-1
        if val21<0 :
            val21=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val21)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val21)
    def cnf():
        global total21
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        global val21
        total21=price21*val21
        if(tab1==1):
            db.insert1('Shack Attack',val21,price21,total21)
        elif(tab2==1):
            db.insert2('Shack Attack',val21,price21,total21)
        elif(tab3==1):
            db.insert3('Shack Attack',val21,price21,total21)
        elif(tab4==1):
            db.insert4('Shack Attack',val21,price21,total21)
        elif(tab5==1):           
            db.insert5('Shack Attack',val21,price21,total21)
        elif(tab6==1):            
            db.insert6('Shack Attack',val21,price21,total21)
        elif(tab7==1):           
            db.insert7('Shack Attack',val21,price21,total21)
        elif(tab8==1):            
            db.insert8('Shack Attack',val21,price21,total21)
        elif(tab9==1):            
            db.insert9('Shack Attack',val21,price21,total21)
        elif(tab10==1):
            db.insert10('Shack Attack',val21,price21,total21)
        val21=0
        total21=0
        z21.destroy()
    txtbox=Text(z21,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z21,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z21,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z21, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z21, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Chocolate custard,fudge sauce,chocolate\ntruffle cookie dough,Valrhona 55% solid\nchocolate pearls and chocolate sprinkles")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z21, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹6")
    price21=6
    label2.place(x=70,y=420)
    z21.title("Shack Attack")
def vanilla():
    z22=Toplevel(w)
    z22.geometry("550x550+350+100")
    z22.focus_set()
    canvas = Canvas(z22, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z22, image=photox, compound = TOP, command=z22.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"vanilla.png")
    b1=Button(z22, text = 'Vanilla', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val22 
        val22=val22+1
        if val22>=10 :
            val22=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val22)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val22)

    def sub():
        global val22
        val22=val22-1
        if val22<0 :
            val22=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val22)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val22)
    def cnf():
        global total22
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        global val22
        total22=price22*val22
        if(tab1==1):
            db.insert1('Vanilla',val22,price22,total22)
        elif(tab2==1):
            db.insert2('Vanilla',val22,price22,total22)
        elif(tab3==1):
            db.insert3('Vanilla',val22,price22,total22)
        elif(tab4==1):
            db.insert4('Vanilla',val22,price22,total22)
        elif(tab5==1):           
            db.insert5('Vanilla',val22,price22,total22)
        elif(tab6==1):            
            db.insert6('Vanilla',val22,price22,total22)
        elif(tab7==1):           
            db.insert7('Vanilla',val22,price22,total22)
        elif(tab8==1):            
            db.insert8('Vanilla',val22,price22,total22)
        elif(tab9==1):            
            db.insert9('Vanilla',val22,price22,total22)
        elif(tab10==1):
            db.insert10('Vanilla',val22,price22,total22)
        val22=0
        total22=0
        z22.destroy()
    txtbox=Text(z22,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z22,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z22,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z22, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z22, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("The classic, spun with premium real Vanilla")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z22, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹2")
    price22=2
    label2.place(x=70,y=420)
    z22.title("Vanilla")
def vanillatoffeetwirl():
    z23=Toplevel(w)
    z23.geometry("550x550+350+100")
    z23.focus_set()
    canvas = Canvas(z23, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z23, image=photox, compound = TOP, command=z23.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"vanilla toffee twirl.png")
    b1=Button(z23, text = 'Vnilla Tfee Twirl', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val23 
        val23=val23+1
        if val23>=10 :
            val23=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val23)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val23)

    def sub():
        global val23
        val23=val23-1
        if val23<0 :
            val23=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val23)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val23)
    def cnf():
        global total23
        global val23
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        total23=price23*val23
        if(tab1==1):
            db.insert1('Vnilla Tfee Twirl',val23,price23,total23)
        elif(tab2==1):
            db.insert2('Vnilla Tfee Twirl',val23,price23,total23)
        elif(tab3==1):
            db.insert3('Vnilla Tfee Twirl',val23,price23,total23)
        elif(tab4==1):
            db.insert4('Vnilla Tfee Twirl',val23,price23,total23)
        elif(tab5==1):           
            db.insert5('Vnilla Tfee Twirl',val23,price23,total23)
        elif(tab6==1):            
            db.insert6('Vnilla Tfee Twirl',val23,price23,total23)
        elif(tab7==1):           
            db.insert7('Vnilla Tfee Twirl',val23,price23,total23)
        elif(tab8==1):            
            db.insert8('Vnilla Tfee Twirl',val23,price23,total23)
        elif(tab9==1):            
            db.insert9('Vnilla Tfee Twirl',val23,price23,total23)
        elif(tab10==1):
            db.insert10('Vnilla Tfee Twirl',val23,price23,total23)
        val23=0
        total23=0
        z23.destroy()
    txtbox=Text(z23,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z23,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z23,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z23, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z23, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Vanilla custard, caramel sauce, chocolate\ntoffee and Valrhona chocolate pearls")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z23, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹4")
    price23=4
    label2.place(x=70,y=420)
    z23.title("Vnilla Tfee Twirl")
def strawberrybannanatrifle():
    z24=Toplevel(w)
    z24.geometry("550x550+350+100")
    z24.focus_set()
    canvas = Canvas(z24, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z24, image=photox, compound = TOP, command=z24.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"strawberry bannana trifle.png")
    b1=Button(z24, text = 'B N B Trifle', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val24 
        val24=val24+1
        if val24>=10 :
            val24=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val24)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val24)

    def sub():
        global val24
        val24=val24-1
        if val24<0 :
            val24=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val24)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val24)
    def cnf():
        global total24
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        global val24
        total24=price24*val24
        if(tab1==1):
            db.insert1('B N B Trifle',val24,price24,total24)
        elif(tab2==1):
            db.insert2('B N B Trifle',val24,price24,total24)
        elif(tab3==1):
            db.insert3('B N B Trifle',val24,price24,total24)
        elif(tab4==1):
            db.insert4('B N B Trifle',val24,price24,total24)
        elif(tab5==1):           
            db.insert5('B N B Trifle',val24,price24,total24)
        elif(tab6==1):            
            db.insert6('B N B Trifle',val24,price24,total24)
        elif(tab7==1):           
            db.insert7('B N B Trifle',val24,price24,total24)
        elif(tab8==1):            
            db.insert8('B N B Trifle',val24,price24,total24)
        elif(tab9==1):            
            db.insert9('B N B Trifle',val24,price24,total24)
        elif(tab10==1):
            db.insert10('B N B Trifle',val24,price24,total24)
        val24=0
        total24=0
        z24.destroy()
    txtbox=Text(z24,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z24,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z24,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z24, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z24, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Vanilla custard, strawberry purée, fresh\nbanana and shortbread cookie")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z24, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹6")
    price24=6
    label2.place(x=70,y=420)
    z24.title("B N B Trifle")
def peanutbutter():
    z25=Toplevel(w)
    z25.geometry("550x550+350+100")
    z25.focus_set()
    canvas = Canvas(z25, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z25, image=photox, compound = TOP, command=z25.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"peanut butter.png")
    b1=Button(z25, text = 'Peanut Butter', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val25 
        val25=val25+1
        if val25>=10 :
            val25=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val25)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val25)

    def sub():
        global val25
        val25=val25-1
        if val25<0 :
            val25=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val25)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val25)
    def cnf():
        global total25
        global val25
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        total25=price25*val25
        if(tab1==1):
            db.insert1('Peanut Butter',val25,price25,total25)
        elif(tab2==1):
            db.insert2('Peanut Butter',val25,price25,total25)
        elif(tab3==1):
            db.insert3('Peanut Butter',val25,price25,total25)
        elif(tab4==1):
            db.insert4('Peanut Butter',val25,price25,total25)
        elif(tab5==1):           
            db.insert5('Peanut Butter',val25,price25,total25)
        elif(tab6==1):            
            db.insert6('Peanut Butter',val25,price25,total25)
        elif(tab7==1):           
            db.insert7('Peanut Butter',val25,price25,total25)
        elif(tab8==1):            
            db.insert8('Peanut Butter',val25,price25,total25)
        elif(tab9==1):            
            db.insert9('Peanut Butter',val25,price25,total25)
        elif(tab10==1):
            db.insert10('Peanut Butter',val25,price25,total25)
        val25=0
        total25=0
        z25.destroy()
    txtbox=Text(z25,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z25,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z25,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z25, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z25, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Our Vanilla shake with creamy peanut butter sauce")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z25, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹3")
    price25=3
    label2.place(x=70,y=420)
    z25.title("Peanut Butter")
def chocolate():
    z26=Toplevel(w)
    z26.geometry("550x550+350+100")
    z26.focus_set()
    canvas = Canvas(z26, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z26, image=photox, compound = TOP, command=z26.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"chocolate.png")
    b1=Button(z26, text = 'Chocolate', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val26 
        val26=val26+1
        if val26>=10 :
            val26=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val26)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val26)

    def sub():
        global val26
        val26=val26-1
        if val26<0 :
            val26=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val26)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val26)
    def cnf():
        global total26
        global val26
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        total26=price26*val26
        if(tab1==1):
            db.insert1('Chocolate',val26,price26,total26)
        elif(tab2==1):
            db.insert2('Chocolate',val26,price26,total26)
        elif(tab3==1):
            db.insert3('Chocolate',val26,price26,total26)
        elif(tab4==1):
            db.insert4('Chocolate',val26,price26,total26)
        elif(tab5==1):           
            db.insert5('Chocolate',val26,price26,total26)
        elif(tab6==1):            
            db.insert6('Chocolate',val26,price26,total26)
        elif(tab7==1):           
            db.insert7('Chocolate',val26,price26,total26)
        elif(tab8==1):            
            db.insert8('Chocolate',val26,price26,total26)
        elif(tab9==1):            
            db.insert9('Chocolate',val26,price26,total26)
        elif(tab10==1):
            db.insert10('Chocolate',val26,price26,total26)
        val26=0
        total26=0
        z26.destroy()
    txtbox=Text(z26,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z26,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z26,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z26, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z26, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Shake Shack's own blend of distinct fine chocolates")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z26, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹4")
    price26=4
    label2.place(x=70,y=420)
    z26.title("Chocolate")
def dubaimalt():
    z27=Toplevel(w)
    z27.geometry("550x550+350+100")
    z27.focus_set()
    canvas = Canvas(z27, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(z27, image=photox, compound = TOP, command=z27.withdraw)
    back.image=photox
    back.place(x=410,y=10)
    photo1 = PhotoImage(file = r"dubai malt.png")
    b1=Button(z27, text = 'Dubai Malt', image = photo1, compound = TOP, font='LITHOGRAPH')
    b1.image=photo1
    b1.place(x=70,y=100)
    def add():
        global val27 
        val27=val27+1
        if val27>=10 :
            val27=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,val27)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,val27)

    def sub():
        global val27
        val27=val27-1
        if val27<0 :
            val27=0
            txtbox.delete("1.0",END)
            txtbox.insert(END,val27)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END) #val
    def cnf():
        global total27
        global val27
        global tab1
        global tab2
        global tab3
        global tab4
        global tab5
        global tab6
        global tab7
        global tab8
        global tab9
        global tab10
        total27=price27*val27
        if(tab1==1):
            db.insert1('Dubai Malt',val27,price27,total27)
        elif(tab2==1):
            db.insert2('Dubai Malt',val27,price27,total27)
        elif(tab3==1):
            db.insert3('Dubai Malt',val27,price27,total27)
        elif(tab4==1):
            db.insert4('Dubai Malt',val27,price27,total27)
        elif(tab5==1):           
            db.insert5('Dubai Malt',val27,price27,total27)
        elif(tab6==1):            
            db.insert6('Dubai Malt',val27,price27,total27)
        elif(tab7==1):           
            db.insert7('Dubai Malt',val27,price27,total27)
        elif(tab8==1):            
            db.insert8('Dubai Malt',val27,price27,total27)
        elif(tab9==1):            
            db.insert9('Dubai Malt',val27,price27,total27)
        elif(tab10==1):
            db.insert10('Dubai Malt',val27,price27,total27)
        val27=0
        total27=0
        z27.destroy()
    txtbox=Text(z27,height=0.5,width=5,bd=0,font='LITHOGRAPH',fg="white",bg="green")
    txtbox.place(x=368,y=165)
    plus=Button(z27,text='+',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=add)
    plus.place(x=340,y=100)
    minus=Button(z27,text='-',font=('arial',16,'bold'),width=5,fg="white",bg="green",command=sub)
    minus.place(x=340,y=220)
    b2=Button(z27, text = 'Confirm Order', compound = TOP, font='LITHOGRAPH',bd=0,fg="green",bg="white",command=cnf)
    b2.place(x=325,y=300)
    var = StringVar()
    label1 = Label( z27, textvariable=var, relief=RAISED, justify=LEFT, font='LITHOGRAPH', bg = 'green', bd=0, fg = 'white'  )
    var.set("Vanilla and Chocolate custard, malt,\nmarshmallow sauce and chocolte truffle\ncookie dough")
    label1.place(x=70,y=350)
    var1 = StringVar()
    label2 = Label( z27, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',25), bg = 'green', bd=0, fg = 'white')
    var1.set("₹10")
    price27=10
    label2.place(x=70,y=420)
    z27.title("Dubai Malt")
def burger():
    b=Toplevel(w)
    b.geometry("1366x768+0+0")
    b.state('zoomed')
    b.resizable(0,0)
    canvas = Canvas(b, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(b, image=photox, compound = TOP, command=b.withdraw)
    back.image=photox
    back.place(x=1300,y=15)
    photo1 = PhotoImage(file = r"Shack burger.png")
    b1=Button(b, text = 'Shack Burger', image = photo1, font='LITHOGRAPH', compound = TOP,command=Shackburger)
    b1.image=photo1
    b1.place(x=27,y=120)
    photo2 = PhotoImage(file = r"Shroom burger.png")
    b2=Button(b, text = 'Shroom burger', image = photo2, font='LITHOGRAPH', compound = TOP,command=Shroomburger)
    b2.image=photo2
    b2.place(x=307,y=120)
    photo3 = PhotoImage(file = r"Smoke shack.png")
    b3=Button(b, text = 'Smoke Shack', image = photo3, font='LITHOGRAPH', compound = TOP,command=Smokeshack)
    b3.image=photo3
    b3.place(x=587,y=120)
    photo4 = PhotoImage(file = r"Stack shack.png")
    b4=Button(b, text = 'Stack Shack', image = photo4, font='LITHOGRAPH', compound = TOP, command=Stackshack)
    b4.image=photo4
    b4.place(x=867,y=120)
    photo5 = PhotoImage(file = r"Cheese burger.png")
    b5=Button(b, text = 'Cheese Burger', image = photo5, font='LITHOGRAPH', compound = TOP, command=Cheeseburger)
    b5.image=photo5
    b5.place(x=1147,y=120)
    photo6 = PhotoImage(file = r"Hamburger.png")
    b6=Button(b, text = 'Hamburger', image = photo6, font='LITHOGRAPH', compound = TOP, command=Hamburger)
    b6.image=photo6
    b6.place(x=27,y=450)
    photo7 = PhotoImage(file = r"Chick n shack.png")
    b7=Button(b, text = 'Chick N Shack', image = photo7, font='LITHOGRAPH', compound = TOP, command=Chicknshack)
    b7.image=photo7
    b7.place(x=307,y=450)
    photo8 = PhotoImage(file = r"Chipotle cheddar chicken.png")
    b8=Button(b, text = 'Chipotle Chicken', image = photo8, font='LITHOGRAPH', compound = TOP, command=Chipotlecheddarchicken)
    b8.image=photo8
    b8.place(x=587,y=450)
    b.title("Burger")
def Fries():
    c=Toplevel(w)
    c.geometry("1366x768+0+0")
    c.state('zoomed')
    c.resizable(0,0)
    canvas = Canvas(c, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(c, image=photox, compound = TOP, command=c.withdraw)
    back.image=photox
    back.place(x=1300,y=15)
    photo1 = PhotoImage(file = r"normal fries.png")
    b1=Button(c, text = 'Normal Fries', image = photo1, font='LITHOGRAPH', compound = TOP, command=normalfries)
    b1.image=photo1
    b1.place(x=27,y=120)
    photo2 = PhotoImage(file = r"cheese fries.png")
    b2=Button(c, text = 'cheese fries', image = photo2, font='LITHOGRAPH', compound = TOP, command=cheesefries)
    b2.image=photo2
    b2.place(x=307,y=120)
    photo3 = PhotoImage(file = r"veal bacon and cheese fries.png")
    b3=Button(c, text = 'Bacon & Cheese', image = photo3, font='LITHOGRAPH', compound = TOP, command=vealbaconandcheesefries)
    b3.image=photo3
    b3.place(x=587,y=120)
    c.title("Fries")
def Shakes():
    d=Toplevel(w)
    d.geometry("1366x768+0+0")
    d.state('zoomed')
    d.resizable(0,0)
    canvas = Canvas(d, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(d, image=photox, compound = TOP, command=d.withdraw)
    back.image=photox
    back.place(x=1300,y=15)
    photo1 = PhotoImage(file = r"cinnamon soul.png")
    b1=Button(d, text = 'Cinnamon Soul', image = photo1, font='LITHOGRAPH', compound = TOP, command=cinnamonsoul)
    b1.image=photo1
    b1.place(x=27,y=120)
    photo2 = PhotoImage(file = r"black and white.png")
    b2=Button(d, text = 'green and white', image = photo2, font='LITHOGRAPH', compound = TOP, command=blackandwhite)
    b2.image=photo2
    b2.place(x=307,y=120)
    d.title("Shakes")
def Hotdog():
    e=Toplevel(w)
    e.geometry("1366x768+0+0")
    e.state('zoomed')
    e.resizable(0,0)
    canvas = Canvas(e, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(e, image=photox, compound = TOP, command=e.withdraw)
    back.image=photox
    back.place(x=1300,y=15)
    photo1 = PhotoImage(file = r"cheese hotdog.png")
    b1=Button(e, text = 'Cheese Hotdog', image = photo1, font='LITHOGRAPH', compound = TOP, command=cheesehotdog)
    b1.image=photo1
    b1.place(x=27,y=120)
    photo2 = PhotoImage(file = r"new york style hotdog.png")
    b2=Button(e, text = 'NY Style Hotdog', image = photo2, font='LITHOGRAPH', compound = TOP, command=newyorkstylehotdog)
    b2.image=photo2
    b2.place(x=307,y=120)
    photo3 = PhotoImage(file = r"shack-cago hot dog.png")
    b3=Button(e, text = 'Shack-Cago HD', image = photo3, font='LITHOGRAPH', compound = TOP, command=shackcagohotdog)
    b3.image=photo3
    b3.place(x=587,y=120)
    e.title("Hotdog")
def Drinks():
    f=Toplevel(w)
    f.geometry("1366x768+0+0")
    f.state('zoomed')
    f.resizable(0,0)
    canvas = Canvas(f, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(f, image=photox, compound = TOP, command=f.withdraw)
    back.image=photox
    back.place(x=1300,y=15)
    photo1 = PhotoImage(file = r"fresh brewed ice tea.png")
    b1=Button(f, text = 'Ice Tea', image = photo1, font='LITHOGRAPH', compound = TOP, command=freshhbrewedicetea)
    b1.image=photo1
    b1.place(x=27,y=120)
    photo2 = PhotoImage(file = r"float bottled water.png")
    b2=Button(f, text = 'Float Water', image = photo2, font='LITHOGRAPH', compound = TOP, command=floatbottledwater)
    b2.image=photo2
    b2.place(x=307,y=120)
    photo3 = PhotoImage(file = r"fiftyfifty.png")
    b3=Button(f, text = 'Fifty-Fifty', image = photo3, font='LITHOGRAPH', compound = TOP, command=fiftyfifty)
    b3.image=photo3
    b3.place(x=587,y=120)
    photo4 = PhotoImage(file = r"shack-made lemonade.png")
    b4=Button(f, text = 'Shack Lemonade', image = photo4, font='LITHOGRAPH', compound = TOP, command=shackmadelemonade)
    b4.image=photo4
    b4.place(x=867,y=120)
    f.title("Drinks")
def IceCream():
    g=Toplevel(w)
    g.geometry("1366x768+0+0")
    g.state('zoomed')
    g.resizable(0,0)
    canvas = Canvas(g, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(g, image=photox, compound = TOP, command=g.withdraw)
    back.image=photox
    back.place(x=1300,y=15)
    photo1 = PhotoImage(file = r"shack attack.png")
    b1=Button(g, text = 'Shack Attack', image = photo1, font='LITHOGRAPH', compound = TOP, command=shackattack)
    b1.image=photo1
    b1.place(x=27,y=120)
    photo2 = PhotoImage(file = r"vanilla.png")
    b2=Button(g, text = 'Vanilla', image = photo2, font='LITHOGRAPH', compound = TOP, command=vanilla)
    b2.image=photo2
    b2.place(x=307,y=120)
    photo3 = PhotoImage(file = r"vanilla toffee twirl.png")
    b3=Button(g, text = 'Vnilla Tfee Twirl', image = photo3, font='LITHOGRAPH', compound = TOP, command=vanillatoffeetwirl)
    b3.image=photo3
    b3.place(x=587,y=120)
    photo4 = PhotoImage(file = r"strawberry bannana trifle.png")
    b4=Button(g, text = 'B N B Trifle', image = photo4, font='LITHOGRAPH', compound = TOP, command=strawberrybannanatrifle)
    b4.image=photo4
    b4.place(x=867,y=120)
    photo5 = PhotoImage(file = r"peanut butter.png")
    b5=Button(g, text = 'Peanut Butter', image = photo5, font='LITHOGRAPH', compound = TOP, command=peanutbutter)
    b5.image=photo5
    b5.place(x=1147,y=120)
    photo6 = PhotoImage(file = r"chocolate.png")
    b6=Button(g, text = 'Chocolate', image = photo6, font='LITHOGRAPH', compound = TOP, command=chocolate)
    b6.image=photo6
    b6.place(x=27,y=450)
    photo7 = PhotoImage(file = r"dubai malt.png")
    b7=Button(g, text = 'Dubai Malt', image = photo7, font='LITHOGRAPH', compound = TOP, command=dubaimalt)
    b7.image=photo7
    b7.place(x=307,y=450)
    g.title("IceCream")
def menu():
    global t
    t=Toplevel(w)
    t.geometry("1366x768+0+0")
    t.state('zoomed')
    # t.resizable(0,0)
    canvas = Canvas(t, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    menu = Menu(t) 
    t.config(menu=menu)
    filemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Menu', menu=filemenu) 
    filemenu.add_command(label='Burger',command=burger) 
    filemenu.add_command(label='Fries',command=Fries) 
    filemenu.add_command(label='Shakes',command=Shakes)
    filemenu.add_command(label='Hotdog',command=Hotdog)
    filemenu.add_command(label='Drinks',command=Drinks)
    filemenu.add_command(label='Ice-Cream',command=IceCream)
    helpmenu = Menu(menu, tearoff=0) 
    menu.add_cascade(label='Help', menu=helpmenu) 
    helpmenu.add_command(label='About', command=about)
    photox=PhotoImage(file = r"backbutton.png")
    back=Button(t, image=photox, compound = TOP, command=bac1)
    back.image=photox
    back.place(x=1300,y=15)
    photoy=PhotoImage(file = r"printbill.png")
    back=Button(t, image=photoy, compound = TOP, command=bill)
    back.image=photoy
    back.place(x=15,y=15)
    photo1 = PhotoImage(file = r"Shack burger.png")
    b1=Button(t, text = 'Shack Burger', image = photo1, font='LITHOGRAPH', compound = TOP, command=Shackburger)
    b1.image=photo1
    b1.place(x=27,y=120)
    photo2 = PhotoImage(file = r"Shroom burger.png")
    b2=Button(t, text = 'Shroom Burger', image = photo2, font='LITHOGRAPH', compound = TOP, command=Shroomburger)
    b2.image=photo2
    b2.place(x=307,y=120)
    photo3 = PhotoImage(file = r"Smoke shack.png")
    b3=Button(t, text = 'Smoke Shack', image = photo3, font='LITHOGRAPH', compound = TOP,command=Smokeshack)
    b3.image=photo3
    b3.place(x=587,y=120)
    photo4 = PhotoImage(file = r"Stack shack.png")
    b4=Button(t, text = 'Stack Shack', image = photo4, font='LITHOGRAPH', compound = TOP,command=Stackshack)
    b4.image=photo4
    b4.place(x=867,y=120)
    photo5 = PhotoImage(file = r"Cheese burger.png")
    b5=Button(t, text = 'Cheese Burger', image = photo5, font='LITHOGRAPH', compound = TOP, command=Cheeseburger)
    b5.image=photo5
    b5.place(x=1147,y=120)
    photo6 = PhotoImage(file = r"Hamburger.png")
    b6=Button(t, text = 'Hamburger', image = photo6, font='LITHOGRAPH', compound = TOP, command=Hamburger)
    b6.image=photo6
    b6.place(x=27,y=450)
    photo7 = PhotoImage(file = r"Chick n shack.png")
    b7=Button(t, text = 'Chick N Shack', image = photo7, font='LITHOGRAPH', compound = TOP, command=Chicknshack)
    b7.image=photo7
    b7.place(x=307,y=450)
    photo8 = PhotoImage(file = r"Chipotle cheddar chicken.png")
    b8=Button(t, text = 'Chipotle Chicken', image = photo8, font='LITHOGRAPH', compound = TOP, command=Chipotlecheddarchicken)
    b8.image=photo8
    b8.place(x=587,y=450)
    photo9 = PhotoImage(file = r"shack-cago hot dog.png")
    b9=Button(t, text = 'Shack-Cago HD', image = photo9, font='LITHOGRAPH', compound = TOP, command=shackcagohotdog)
    b9.image=photo9
    b9.place(x=867,y=450)
    photo10 = PhotoImage(file = r"new york style hotdog.png")
    b10=Button(t, text = 'NY style hotdog', image = photo10, font='LITHOGRAPH', compound = TOP, command=newyorkstylehotdog)
    b10.image=photo10
    b10.place(x=1147,y=450)
    if(tab1==1):
        t.title("TABLE 1 MENU")
    elif(tab2==1):
        t.title("TABLE 2 MENU")
    elif(tab3==1):
        t.title("TABLE 3 MENU")
    elif(tab4==1):
        t.title("TABLE 4 MENU")
    elif(tab5==1):           
        t.title("TABLE 5 MENU")
    elif(tab6==1):            
        t.title("TABLE 6 MENU")
    elif(tab7==1):           
        t.title("TABLE 7 MENU")
    elif(tab8==1):            
        t.title("TABLE 8 MENU")
    elif(tab9==1):            
        t.title("TABLE 9 MENU")
    else:
        t.title("TABLE 10 MENU")
def clear():
    adb.del1()
    messagebox.showinfo("Information","Database Cleawhite Successfully")
def about():
    ts=Toplevel(w)
    ts.geometry("1080x720")
    ts.resizable(0,0)
    logo = ImageTk.PhotoImage(file= r"final.jpg")
    lab1 = Label(ts, image=logo, font=('LITHOGRAPH', 14),bg='white',fg='green')
    lab1.image=logo
    var = StringVar()
    label1 = Label( ts, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',35,'bold'), bg = 'green', bd=0, fg = 'white'  )
    label1.place(x=300,y=530)
    var.set("Project Created By:")
    var1 = StringVar()
    label2 = Label( ts, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH',20), bg = 'green', bd=0, fg = 'white'  )
    var1.set("Ayan Saha")
    label2.place(x=450,y=600)
    lab1.pack()
    ts.title("END")
def bdata():
    def brow():
        a=date1.get()
        b=date2.get()
        lb1.delete(0,'end')
        lb2.delete(0,'end')
        receipt.delete("1.0",END)
        conn = sqlite3.connect('ADMIN.sqlite')
        cursor = conn.cursor()
        if a == "" or b == "":
            messagebox.showerror("Error","Please Enter the Date")
            bdata()
        else:
            try:
                for row in cursor.execute("SELECT * from `ADMIN` where `DATE` = ?", (a,)):
                    id1=row[0]
                    break
                for row in cursor.execute("SELECT * FROM `ADMIN` WHERE `DATE` = ?", (b,)):
                    id2=row[0]
                if(id1>id2):
                    messagebox.showerror("Error","Date Entewhite Incorrectly")
                    bdata()
                else:
                    ##CORRECT DATE
                    receipt.delete("1.0",END)
                    receipt.insert(END,"ID\tBILL\tTABLE\t\tITEM\t\tQTY\tPRICE\tDATE\t   TIME\n")
                    receipt.insert(END,"==================================================================================\n\n")
                    for row in cursor.execute("SELECT * FROM `ADMIN` WHERE ID >= ? AND ID <= ?", (id1,id2,)):
                        a=row[0]
                        a=str(a)
                        b=row[1]
                        b=str(b)
                        c=row[2]
                        c=str(c)
                        d=row[3]
                        d=str(d)
                        e=row[4]
                        e=str(e)
                        f=row[5]
                        f=str(f)
                        g=row[6]
                        g=str(g)
                        h=row[7]
                        h=str(h)
                        receipt.insert(END,a+"\t"+b+"\t"+c+"\t\t"+d+"\t\t"+e+"\t"+f+"\t"+g+"\t   "+h+"\n")
            except UnboundLocalError:
                try:
                      try:
                          #LAST DATE OUT OF DB
                        for row in cursor.execute("SELECT * FROM 'ADMIN' "):
                            idx=row[0]
                        receipt.delete("1.0",END)
                        receipt.insert(END,"ID\tBILL\tTABLE\t\tITEM\t\tQTY\tPRICE\tDATE\t   TIME\n")
                        receipt.insert(END,"==================================================================================\n\n")
                        for row in cursor.execute("SELECT * FROM `ADMIN` WHERE ID >= ? AND ID <= ?", (id1,idx,)):
                            a=row[0]
                            a=str(a)
                            b=row[1]
                            b=str(b)
                            c=row[2]
                            c=str(c)
                            d=row[3]
                            d=str(d)
                            e=row[4]
                            e=str(e)
                            f=row[5]
                            f=str(f)
                            g=row[6]
                            g=str(g)
                            h=row[7]
                            h=str(h)
                            receipt.insert(END,a+"\t"+b+"\t"+c+"\t\t"+d+"\t\t"+e+"\t"+f+"\t"+g+"\t   "+h+"\n")
                      except UnboundLocalError:
                          #FIRST DATE OUT OF DB
                            for row in cursor.execute("SELECT * FROM 'ADMIN' "):
                                idy=row[0]
                                break
                            receipt.delete("1.0",END)
                            receipt.insert(END,"ID\tBILL\tTABLE\t\tITEM\t\tQTY\tPRICE\tDATE\t   TIME\n")
                            receipt.insert(END,"==================================================================================\n\n")
                            for row in cursor.execute("SELECT * FROM `ADMIN` WHERE ID >= ? AND ID <= ?", (idy,id2,)):
                                a=row[0]
                                a=str(a)
                                b=row[1]
                                b=str(b)
                                c=row[2]
                                c=str(c)
                                d=row[3]
                                d=str(d)
                                e=row[4]
                                e=str(e)
                                f=row[5]
                                f=str(f)
                                g=row[6]
                                g=str(g)
                                h=row[7]
                                h=str(h)
                                receipt.insert(END,a+"\t"+b+"\t"+c+"\t\t"+d+"\t\t"+e+"\t"+f+"\t"+g+"\t   "+h+"\n")
                except:
                    messagebox.showerror("Error","Date Format is Incorrect")
                    bdata()
        conn.commit()
        conn.close()
    r1=Toplevel(w)
    r1.geometry("1366x768+0+0")
    r1.resizable(0,0)
    r1.state('zoomed')
    r1.focus_set()
    canvas = Canvas(r1, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    receipt=Text(r1,height=19,width=88,bd=1,font=('LITHOGRAPH',20,'bold'),fg="white",bg="green")
    receipt.place(x=20,y=100)
    lab1 = Label(r1, text = "From:", font=('LITHOGRAPH', 14),bg='white',fg='green')
    lab1.place(x=380,y=10)
    lb1=Entry(r1, textvariable=date1, font=(14))
    lb1.place(x=460,y=10)
    lab2 = Label(r1, text = "To:", font=('LITHOGRAPH', 14),bg='white',fg='green')
    lab2.place(x=380,y=45)
    lb2=Entry(r1, textvariable=date2, font=(14))
    lb2.place(x=460,y=45)
    b1=Button(r1, width=10, text = 'Search', font=('LITHOGRAPH',14,'bold'),bg='white',fg='green', command=brow)
    b1.place(x=700,y=25)
    menubar = Menu(r1)
    filemenu = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Exit", command=r1.withdraw)
    helpmenu.add_command(label="About...", command=about)
    menubar.add_cascade(label="Help", menu=helpmenu)
    r1.config(menu=menubar)
    r1.title("Database")
    conn = sqlite3.connect('ADMIN.sqlite')
    cursor = conn.cursor()
    receipt.insert(END,"ID\tBILL\tTABLE\t\tITEM\t\tQTY\tPRICE\tDATE\t   TIME\n")
    receipt.insert(END,"==================================================================================\n\n")
    for row in cursor.execute("SELECT * from ADMIN"):       
        a=row[0]
        a=str(a)
        b=row[1]
        b=str(b)
        c=row[2]
        c=str(c)
        d=row[3]
        d=str(d)
        e=row[4]
        e=str(e)
        f=row[5]
        f=str(f)
        g=row[6]
        g=str(g)
        h=row[7]
        h=str(h)
        receipt.insert(END,a+"\t"+b+"\t"+c+"\t\t"+d+"\t\t"+e+"\t"+f+"\t"+g+"\t   "+h+"\n")                   
    conn.commit()
    conn.close()
def browse():
    r=Toplevel(w)
    r.geometry("400x400+450+200")
    r.resizable(0,0)
    r.focus_set()
    canvas = Canvas(r, width = 400, height = 400, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    b1=Button(r,width=15,text = 'Browse Data', font=('LITHOGRAPH',20,'bold'),bg='white',fg='green',command=bdata)
    b1.place(x=70,y=100)
    b2=Button(r,width=15, text = 'Clear Data', font=('LITHOGRAPH',20,'bold'),bg='white',fg='green',command=clear)
    b2.place(x=70,y=225)
    menu = Menu(r) 
    r.config(menu=menu) 
    filemenu = Menu(menu, tearoff=0) 
    menu.add_cascade(label='File', menu=filemenu) 
    filemenu.add_command(label='Exit', command=r.withdraw) 
    helpmenu = Menu(menu, tearoff=0) 
    menu.add_cascade(label='Help', menu=helpmenu) 
    helpmenu.add_command(label='About...', command=about)
    r.title("Browse")   
def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        USERNAME.set("")
        PASSWORD.set("")
        messagebox.showerror("Error","Please Enter Username and Password")  
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            USERNAME.set("")
            PASSWORD.set("")
            l1.withdraw()
            browse()
        else:
            USERNAME.set("")
            PASSWORD.set("")
            messagebox.showerror("Error","Invalid Username or Password")
            l1.withdraw()
    cursor.close()
    conn.close()
def admin():
    global l1
    l1=Toplevel(w)
    l1.geometry("375x160+500+300")
    l1.resizable(0,0)
    l1.focus_set()
    lbl_username = Label(l1, text = "Username:", font=('LITHOGRAPH', 14), bd=15)
    lbl_username.grid(row=0, sticky="e")
    lbl_password = Label(l1, text = "Password:", font=('LITHOGRAPH', 14), bd=15)
    lbl_password.grid(row=1, sticky="e")
    lbl_text = Label(l1)
    lbl_text.grid(row=2, columnspan=2)
    lbl_text = Label(l1)
    lbl_text.grid(row=2, columnspan=2)
    username = Entry(l1, textvariable=USERNAME, font=(14))
    username.grid(row=0, column=1)
    password = Entry(l1, textvariable=PASSWORD, show="*", font=(14))
    password.grid(row=1, column=1)
    btn_login = Button(l1, text="Login", width=45, command=Login)
    btn_login.place(x=25,y=120)
    btn_login.bind('<Return>', Login)
    l1.title("Login")
def fun():
    global f
    f=Toplevel(w)
    f.geometry("1366x768+0+0")
    f.state('zoomed')
    f.resizable(0,0)
    f.focus_set()
    canvas = Canvas(f, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    image1 = ImageTk.PhotoImage(file = r"logo.jpg")
    canvas.create_image(0, 0, image = image1, anchor = NW)
    menubar = Menu(f)
    filemenu = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Admin", command=admin)
    filemenu.add_separator()
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Exit", command=f.withdraw)
    helpmenu.add_command(label="About...", command=about)
    menubar.add_cascade(label="Help", menu=helpmenu)
    f.config(menu=menubar)
    photo1 = PhotoImage(file = r"1.png")
    b1=Button(f, text = 'TABLE 1', image = photo1, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table1)
    b1.image=photo1
    b1.place(x=27,y=80)
    photo2 = PhotoImage(file = r"4.png")
    b2=Button(f, text = 'TABLE 2', image = photo2, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table2)
    b2.image=photo2
    b2.place(x=307,y=80)
    photo3 = PhotoImage(file = r"2.png")
    b3=Button(f, text = 'TABLE 3', image = photo3, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table3)
    b3.image=photo3
    b3.place(x=587,y=80)
    photo4 = PhotoImage(file = r"4.png")
    b4=Button(f, text = 'TABLE 4', image = photo4, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table4)
    b4.image=photo4
    b4.place(x=867,y=80)
    photo5 = PhotoImage(file = r"2.png")
    b5=Button(f, text = 'TABLE 5', image = photo5, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table5)
    b5.image=photo5
    b5.place(x=1147,y=80)
    photo6 = PhotoImage(file = r"1.png")
    b6=Button(f, text = 'TABLE 6', image = photo6, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table6)
    b6.image=photo6
    b6.place(x=27,y=450)
    photo7 = PhotoImage(file = r"2.png")
    b7=Button(f, text = 'TABLE 7', image = photo7, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table7)
    b7.image=photo7
    b7.place(x=307,y=450)
    photo8 = PhotoImage(file = r"4.png")
    b8=Button(f, text = 'TABLE 8', image = photo8, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table8)
    b8.image=photo8
    b8.place(x=587,y=450)
    photo9 = PhotoImage(file = r"1.png")
    b9=Button(f, text = 'TABLE 9', image = photo9, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table9)
    b9.image=photo9
    b9.place(x=867,y=450)
    photo10 = PhotoImage(file = r"4.png")
    b10=Button(f, text = 'TABLE 10', image = photo10, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=table10)
    b10.image=photo10
    b10.place(x=1147,y=450)
    f.title("Table")    
def bill():
    global bil
    bil=Toplevel(w)
    bil.geometry("1366x768")
    bil.state('zoomed')
    bil.resizable(0,0)
    bil.focus_set()
    canvas = Canvas(bil, width = 1366, height = 768, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)
    tot=Text(bil,height=1,width=14,bd=0,font=('LITHOGRAPH',20,'bold'),fg="white",bg="green")
    tot.place(x=1358,y=800)
    receipt=Text(bil,height=20,width=88,bd=0,font=('LITHOGRAPH',20,'bold'),fg="white",bg="green")
    receipt.place(x=20,y=70)
    receipt.delete("1.0",END)
    tot.delete("1.0",END)
    TimeOfOrder=StringVar()
    DateOfOrder=StringVar()
    TimeOfOrder.set(now.strftime("%I:%M:%S %p"))
    DateOfOrder.set(now.strftime("%x"))
    receipt.insert(END,"\t\t\t\t   SHAKE SHACK,\n")
    receipt.insert(END,"\t\t\t           691 8th Ave, New York,\n")
    receipt.insert(END,"\t\t\t\t        NY, 10036\n")
    receipt.insert(END,"\t\t\t            TEL: +1 646-435-0135\n\n")
    receipt.insert(END," Date :\t\t"+DateOfOrder.get()+"\n")
    receipt.insert(END," Time :\t\t"+TimeOfOrder.get()+"\n\n")
    receipt.insert(END,"==================================================================================\n")
    receipt.insert(END,"\t\t\t\tORDER SUMMARY\n")
    receipt.insert(END,"==================================================================================\n\n")
    receipt.insert(END,"      ITEM			                     QUANTITY			                                                 PRICE\n")
    if(tab1==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE1"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 1",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek1())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             total:    ₹"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(tab2==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE2"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 2",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek2())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             total:    ₹"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(tab3==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE3"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 3",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek3())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             total:    ₹"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(tab4==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE4"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 4",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek4())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             total:    ₹"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(tab5==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE5"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 5",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek5())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             total:    ₹"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(tab6==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE6"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 6",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek6())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             total:    ₹"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(tab7==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE7"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 7",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek7())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             total:    ₹"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(tab8==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE8"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 8",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek8())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             total:    ₹"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(tab9==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE9"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 9",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek9())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             total:    ₹"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(tab10==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE10"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 10",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek10())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             total:    ₹"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    photo10 = PhotoImage(file = r"exit.png")
    b10=Button(bil, image = photo10, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=ex)
    b10.image=photo10
    b10.place(x=1250,y=10)
    if(tab1==1):
        bil.title("TABLE 1 BILL")
    elif(tab2==1):
        bil.title("TABLE 2 BILL")
    elif(tab3==1):
        bil.title("TABLE 3 BILL")
    elif(tab4==1):
        bil.title("TABLE 4 BILL")
    elif(tab5==1):           
        bil.title("TABLE 5 BILL")
    elif(tab6==1):            
        bil.title("TABLE 6 BILL")
    elif(tab7==1):           
        bil.title("TABLE 7 BILL")
    elif(tab8==1):            
        bil.title("TABLE 8 BILL")
    elif(tab9==1):            
        bil.title("TABLE 9 BILL")
    else:
        bil.title("TABLE 10 BILL")
def ex():
    global tab1
    global tab2
    global tab3
    global tab4
    global tab5
    global tab6
    global tab7
    global tab8
    global tab9
    global tab10
    global bil
    if(tab1==1):
        db.del1()
        tab1=0
        bil.withdraw()
        t.withdraw()
    elif(tab2==1):
        db.del2()
        tab2=0
        bil.withdraw()
        t.withdraw()
    elif(tab3==1):
        db.del3()
        tab3=0
        bil.withdraw()
        t.withdraw()
    elif(tab4==1):
        db.del4()
        tab4=0
        bil.withdraw()
        t.withdraw()
    elif(tab5==1):
        db.del5()
        tab5=0
        bil.withdraw()
        t.withdraw()
    elif(tab6==1):
        db.del6()
        tab6=0
        bil.withdraw()
        t.withdraw()
    elif(tab7==1):
        db.del7()
        tab7=0
        bil.withdraw()
        t.withdraw()
    elif(tab8==1):
        db.del8()
        tab8=0
        bil.withdraw()
        t.withdraw()
    elif(tab9==1):
        db.del9()
        tab9=0
        bil.withdraw()
        t.withdraw()
    elif(tab10==1):
        db.del10()
        tab10=0
        bil.withdraw()
        t.withdraw()
def mp():
    w.focus_set()
    menu1 = Menu(w) 
    w.config(menu=menu1) 
    filemenu = Menu(menu1, tearoff=0) 
    menu1.add_cascade(label='File', menu=filemenu) 
    filemenu.add_command(label='Admin',command=admin)
    filemenu.add_command(label='Order',command=fun)
    filemenu.add_separator() 
    filemenu.add_command(label='Exit',command=w.destroy) 
    helpmenu = Menu(menu1, tearoff=0) 
    menu1.add_cascade(label='Help', menu=helpmenu) 
    helpmenu.add_command(label='About...',command=about)
    w.title("Main Frame")
Billno=StringVar()
Cost=StringVar()
Items=StringVar()
Quantity=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()
TimeOfOrder.set(now.strftime("%I:%M:%S %p"))
DateOfOrder.set(now.strftime("%x"))
mp()
mainloop()

