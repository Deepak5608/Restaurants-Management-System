from tkinter import *
import random
from datetime import datetime
from PIL import Image, ImageTk
from csv import DictWriter
import os

root = Tk()
root.geometry("1000x850+350+50")
root.title("Restaurant Management System")

text_Input = StringVar()
operator = ""

Tops = Frame(root, width=1600, height=50, bg="turquoise", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

#==============================TIME & DATE====================================
now = datetime.now()
localtime = now.strftime("%d/%m/%Y \t %H:%M:%S")

# ============================INFO======================================
image = Image.open('images.jpg')
tk_image = ImageTk.PhotoImage(image.resize((450, 150)))

lblInfo = Label(Tops, font=('arial', 30, 'bold'), image=tk_image, bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
lblInfo = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="firebrick", bd=10, anchor='w')
lblInfo.grid(row=1, column=0)

# ========================================List 1===============================================
Bill_No = StringVar()
Chicken_Biryani = StringVar()
Mutton_Biryani = StringVar()
Mutton_Kheema = StringVar()
Cold_Drink = StringVar()
Butter_Chicken = StringVar()
Chicken_Tikka_Masala = StringVar()
Tandoori_Chicken = StringVar()
Chilli_Chicken = StringVar()
Chicken_Handi = StringVar()
Roti = StringVar()
Butter_Naan = StringVar()
Cost_of_Meal = StringVar()
GST = StringVar()
Total_cost = StringVar()

def ref():
    x = random.randint(189873, 988778)
    randomRef = str(x)
    Bill_No.set(randomRef)

    try : CoCB = float(Chicken_Biryani.get())
    except : CoCB = 0
    try : CoMB = float(Mutton_Biryani.get())
    except : CoMB = 0
    try : CoMK = float(Mutton_Kheema.get())
    except : CoMK = 0
    try : CoCD = float(Cold_Drink.get())
    except : CoCD = 0
    try : CoBC = float(Butter_Chicken.get())
    except : CoBC = 0
    try : CoCTM = float(Chicken_Tikka_Masala.get())
    except : CoCTM = 0
    try : CoTC = float(Tandoori_Chicken.get())
    except : CoTC = 0
    try : CoCC = float(Chilli_Chicken.get())
    except : CoCC = 0
    try : CoR = float(Roti.get())
    except : CoR = 0
    try : CoCH = float(Chicken_Handi.get())
    except : CoCH = 0
    try : CoBN = float(Butter_Naan.get())
    except : CoBN = 0

    CostofChicken_Biryani = CoCB * 180
    CostofCold_Drink = CoCD * 20
    CostofButter_Chicken = CoBC * 220
    CostofChicken_Tikka_Masala = CoCTM * 160
    CostofTandoori_Chicken = CoTC * 200
    CostofChilli_Chicken = CoCC * 140
    CostofChicken_Handi = CoCH * 350
    CostofMutton_Biryani = CoMB * 220
    CostofMutton_Kheema = CoMK * 180
    CostofButter_Naan = CoBN * 25
    CostofRoti = CoR * 10

    CostofMeal = "Rs", str(
        '%.2f' % (CostofChicken_Biryani + CostofCold_Drink + CostofButter_Chicken + CostofChicken_Tikka_Masala +
                  CostofTandoori_Chicken + CostofChilli_Chicken + CostofChicken_Handi + CostofMutton_Biryani +
                  CostofMutton_Kheema + CostofButter_Naan + CostofRoti))

    PayTax = ((CostofChicken_Biryani + CostofCold_Drink + CostofButter_Chicken + CostofChicken_Tikka_Masala +
               CostofTandoori_Chicken + CostofChilli_Chicken + CostofChicken_Handi + CostofMutton_Biryani +
               CostofMutton_Kheema + CostofButter_Naan + CostofRoti) * .18)

    TotalCost = (CostofChicken_Biryani + CostofCold_Drink + CostofButter_Chicken + CostofChicken_Tikka_Masala +
                 CostofTandoori_Chicken + CostofChilli_Chicken + CostofChicken_Handi + CostofMutton_Biryani +
                 CostofMutton_Kheema + CostofButter_Naan + CostofRoti)

    OverAllCost = "Rs", str('%.2f' % (PayTax + TotalCost))
    PaidTax = "Rs", str('%.2f' % PayTax)
    Cost_of_Meal.set(CostofMeal)
    GST.set(PaidTax)
    Total_cost.set(OverAllCost)


def exit():
    root.destroy()


def reset():
    Bill_No.set("")
    Chicken_Biryani.set("")
    Mutton_Biryani.set("")
    Mutton_Kheema.set("")
    Cold_Drink.set("")
    Butter_Chicken.set("")
    Chicken_Tikka_Masala.set("")
    Tandoori_Chicken.set("")
    Chilli_Chicken.set("")
    Chicken_Handi.set("")
    Roti.set("")
    Butter_Naan.set("")
    Cost_of_Meal.set("")
    GST.set("")
    Total_cost.set("")

lblChicken_Biryani = Label(f1, font=('arial', 16, 'bold'), text='Chicken Biryani', bd=10, anchor='w')
lblChicken_Biryani.grid(row=0, column=0)
txtChicken_Biryani = Entry(f1, font=('arial', 16, 'bold'), textvariable=Chicken_Biryani, bd=6, insertwidth=4,
                           bg='plum', justify='center')
txtChicken_Biryani.grid(row=0, column=1)

lblButter_Chicken = Label(f1, font=('arial', 16, 'bold'), text='Butter Chicken', bd=10, anchor='w')
lblButter_Chicken.grid(row=1, column=0)
txtButter_Chicken = Entry(f1, font=('arial', 16, 'bold'), textvariable=Butter_Chicken, bd=6, insertwidth=4,
                          bg='plum', justify='center')
txtButter_Chicken.grid(row=1, column=1)

lblChicken_Tikka_Masala = Label(f1, font=('arial', 16, 'bold'), text='Chicken Tikka Masala', bd=10, anchor='w')
lblChicken_Tikka_Masala.grid(row=2, column=0)
txtChicken_Tikka_Masala = Entry(f1, font=('arial', 16, 'bold'), textvariable=Chicken_Tikka_Masala, bd=6, insertwidth=4,
                                bg='plum', justify='center')
txtChicken_Tikka_Masala.grid(row=2, column=1)

lblTandoori_Chicken = Label(f1, font=('arial', 16, 'bold'), text='Tandoori Chicken', bd=10, anchor='w')
lblTandoori_Chicken.grid(row=3, column=0)
txtTandoori_Chicken = Entry(f1, font=('arial', 16, 'bold'), textvariable=Tandoori_Chicken, bd=6, insertwidth=4,
                            bg='plum', justify='center')
txtTandoori_Chicken.grid(row=3, column=1)

lblChilli_Chicken = Label(f1, font=('arial', 16, 'bold'), text='Chilli Chicken', bd=10, anchor='w')
lblChilli_Chicken.grid(row=4, column=0)
txtChilli_Chicken = Entry(f1, font=('arial', 16, 'bold'), textvariable=Chilli_Chicken, bd=6, insertwidth=4,
                          bg='plum', justify='center')
txtChilli_Chicken.grid(row=4, column=1)

lblChicken_Handi = Label(f1, font=('arial', 16, 'bold'), text='Chicken Handi', bd=10, anchor='w')
lblChicken_Handi.grid(row=5, column=0)
txtChicken_Handi = Entry(f1, font=('arial', 16, 'bold'), textvariable=Chicken_Handi, bd=6, insertwidth=4,
                          bg='plum', justify='center')
txtChicken_Handi.grid(row=5, column=1)

lblMutton_Kheema = Label(f1, font=('arial', 16, 'bold'), text='Mutton Kheema', bd=10, anchor='w')
lblMutton_Kheema.grid(row=6, column=0)
txtMutton_Kheema = Entry(f1, font=('arial', 16, 'bold'), textvariable=Mutton_Kheema, bd=6, insertwidth=4,
                          bg='plum', justify='center')
txtMutton_Kheema.grid(row=6, column=1)

lblMutton_Biryani = Label(f1, font=('arial', 16, 'bold'), text='Mutton Biryani', bd=10, anchor='w')
lblMutton_Biryani.grid(row=7, column=0)
txtMutton_Biryani = Entry(f1, font=('arial', 16, 'bold'), textvariable=Mutton_Biryani, bd=6, insertwidth=4,
                           bg='plum', justify='center')
txtMutton_Biryani.grid(row=7, column=1)

# ==========================================List 2========================================================

lblButter_Naan = Label(f1, font=('arial', 16, 'bold'), text='Butter Naan', bd=10, anchor='w')
lblButter_Naan.grid(row=0, column=2)
txtButter_Naan = Entry(f1, font=('arial', 16, 'bold'), textvariable=Butter_Naan, bd=6, insertwidth=4,
                           bg='plum', justify='center')
txtButter_Naan.grid(row=0, column=3)

lblRoti = Label(f1, font=('arial', 16, 'bold'), text='Tandoor Roti', bd=10, anchor='w')
lblRoti.grid(row=1, column=2)
txtRoti = Entry(f1, font=('arial', 16, 'bold'), textvariable=Roti, bd=6, insertwidth=4,
                bg='plum', justify='center')
txtRoti.grid(row=1, column=3)

lblCold_Drink = Label(f1, font=('arial', 16, 'bold'), text='Cold Drink', bd=10, anchor='w')
lblCold_Drink.grid(row=2, column=2)
txtCold_Drink = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cold_Drink, bd=6, insertwidth=4,
                      bg='plum', justify='center')
txtCold_Drink.grid(row=2, column=3)

lblBill_No = Label(f1, font=('arial', 16, 'bold'), text='Bill No', bd=10, anchor='w')
lblBill_No.grid(row=4, column=2)
txtBill_No = Entry(f1, font=('arial', 16, 'bold'), textvariable=Bill_No, bd=6, insertwidth=4,
                     bg='peachpuff', justify='center')
txtBill_No.grid(row=4, column=3)

lblCost_of_Meal = Label(f1, font=('arial', 16, 'bold'), text='Cost of Meal', bd=10, anchor='w')
lblCost_of_Meal.grid(row=5, column=2)
txtCost_of_Meal = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost_of_Meal, bd=6, insertwidth=4,
                        bg='peachpuff', justify='center')
txtCost_of_Meal.grid(row=5, column=3)

lblGST = Label(f1, font=("arial", 16, "bold"), text="GST", bd=10, anchor='w')
lblGST.grid(row=6, column=2)
txtGST = Entry(f1, font=('arial', 16, 'bold'), textvariable=GST, bd=6, insertwidth=4,
               bg='peachpuff', justify='center')
txtGST.grid(row=6, column=3)

lblTotal_Cost = Label(f1, font=('arial', 16, 'bold'), bd=10, anchor='w', text='Total cost')
lblTotal_Cost.grid(row=7, column=2)
txtTotal_cost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total_cost, bd=6, insertwidth=4,
                      bg='peachpuff', justify='center')
txtTotal_cost.grid(row=7, column=3)

# ====================================BUTTONS======================================

btnTotal = Button(f1, padx=16, pady=8, bd=8, fg='black', font=("arial", 16, "bold"), width=10,
                  text="TOTAL", bg="turquoise", command=ref).grid(row=10, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=8, fg='black', font=('arial', 16, 'bold'), width=10,
                  text="RESET", bg='turquoise', command=reset).grid(row=10, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=8, fg='black', font=('arial', 16, 'bold'), width=10,
                 text="EXIT", bg='turquoise', command=exit).grid(row=10, column=3)


def price():
    roo = Tk()
    roo.geometry("500x500+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('arial', 18, 'bold'), text="ITEM", fg="black", bd=5).grid(row=0, column=0)
    lblinfo = Label(roo, font=('arial', 18, 'bold'), text=" "*20, fg='white', anchor='w').grid(row=0, column=2)
    lblinfo = Label(roo, font=('arial', 18, 'bold'), text='PRICE', fg='black', bd=5).grid(row=0, column=3)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text='', fg='forestgreen', bd=5).grid(row=1, column=0)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text="", fg='forestgreen', anchor='w').grid(row=1, column=3)

    lblinfo = Label(roo, font=('arial', 15, 'bold'), text='Chicken Biryani', fg='forestgreen', bd=5).grid(row=2, column=0)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text="180", fg='forestgreen', anchor='w').grid(row=2, column=3)

    lblinfo = Label(roo, font=('arial', 15, 'bold'), text='Butter Chicken', fg='forestgreen', bd=5).grid(row=3, column=0)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text='220', fg='forestgreen', bd=5).grid(row=3, column=3)

    lblinfo = Label(roo, font=('arial', 15, 'bold'), text='Chicken Tikka Masala', fg='forestgreen', bd=5).grid(row=4, column=0)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text="160", fg='forestgreen', anchor='w').grid(row=4, column=3)

    lblinfo = Label(roo, font=('arial', 15, 'bold'), text='Tandoori Chicken', fg='forestgreen', bd=5).grid(row=5, column=0)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text='200', fg='forestgreen', bd=5).grid(row=5, column=3)

    lblinfo = Label(roo, font=('arial', 15, 'bold'), text='Chilli Chicken', fg='forestgreen', bd=5).grid(row=6, column=0)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text="140", fg='forestgreen', anchor='w').grid(row=6, column=3)

    lblinfo = Label(roo, font=('arial', 15, 'bold'), text='Chicken Handi', fg='forestgreen', bd=5).grid(row=7, column=0)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text='350', fg='forestgreen', bd=5).grid(row=7, column=3)

    lblinfo = Label(roo, font=('arial', 15, 'bold'), text='Mutton Kheema', fg='forestgreen', bd=5).grid(row=8, column=0)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text='180', fg='forestgreen', bd=5).grid(row=8, column=3)

    lblinfo = Label(roo, font=('arial', 15, 'bold'), text='Mutton Biryani', fg='forestgreen', bd=5).grid(row=9, column=0)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text='220', fg='forestgreen', bd=5).grid(row=9, column=3)

    lblinfo = Label(roo, font=('arial', 15, 'bold'), text='Butter Naan', fg='forestgreen', bd=5).grid(row=10, column=0)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text='25', fg='forestgreen', bd=5).grid(row=10, column=3)

    lblinfo = Label(roo, font=('arial', 15, 'bold'), text='Tandoor Roti', fg='forestgreen', bd=5).grid(row=11, column=0)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text="10", fg='forestgreen', anchor='w').grid(row=11, column=3)

    lblinfo = Label(roo, font=('arial', 15, 'bold'), text='Cold Drink', fg='forestgreen', bd=5).grid(row=12, column=0)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text='20', fg='forestgreen', bd=5).grid(row=12, column=3)

    roo.mainloop()

btnPrice = Button(f1, padx=16, pady=8, bd=8, fg="black", font=("arial", 16, "bold"), width=10,
                  text="PRICE", bg="turquoise", command=price)
btnPrice.grid(row=10, column=0)

root.mainloop()

