from tkinter import *
import random
import datetime

root = Tk()
root.geometry("1600x8000")
root.title("Restaurant Management System")

# Top frame
Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

# Bottom frame
f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

# add restaurant name
restro_name = Label(Tops, font=('arial', 50, 'bold'), text="RESTAURANT", fg="Steel Blue", anchor='center')
restro_name.grid(row=0, column=2)

# add time to top frame
time = datetime.datetime.now()
time_display = Label(Tops, font=('arial', 50, 'bold'), text=time, fg="Steel Blue", anchor='center')
time_display.grid(row=1, column=2)


def cal_total():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Reference.set(randomRef)
    # get number of items enter
    if Idly.get() == '':
        idly_total = 0
    else:
        idly_total = float(Idly.get())

    if Dosa.get() == '':
        dosa_total = 0
    else:
        dosa_total = float(Dosa.get())

    if Drink.get() == '':
        drink_total = 0
    else:
        drink_total = float(Drink.get())

    if Rice.get() == '':
        rice_total = 0
    else:
        rice_total = float(Rice.get())

    if Pulav.get() == '':
        pulav_total = 0
    else:
        pulav_total = float(Pulav.get())

    if Pav_bhaji.get() == '':
        pav_total = 0
    else:
        pav_total = float(Pav_bhaji.get())

    idly_cal = idly_total * 50
    dosa_cal = dosa_total * 100
    rice_cal = rice_total * 80
    drink_cal = drink_total * 20
    pulav_cal = pulav_total * 70
    pav_cal = pav_total * 90

    cost_meal_total = str('%.2f' % (idly_cal + dosa_cal + rice_cal + drink_cal + pulav_cal + pav_cal))
    service_cal = str('%.2f' % (float(cost_meal_total) * 0.08))
    state_cal = str('%.2f' % (float(cost_meal_total) * 0.07))
    sub_cal = str('%.2f' % (float(cost_meal_total) * 0.05))
    total_cal = str('%.2f' % (float(cost_meal_total) + float(service_cal) + float(state_cal) + float(sub_cal)))
    total_tax.set(total_cal)
    sub_tax.set(sub_cal)
    State_tax.set(state_cal)
    Service_cost.set(service_cal)
    Cost_of_meal.set(cost_meal_total)


# function to reset all the values
def reset():
    Reference.set('')
    Idly.set('')
    Drink.set('')
    Cost_of_meal.set('')
    Service_cost.set('')
    Dosa.set('')
    Pav_bhaji.set('')
    Pulav.set('')
    Rice.set('')
    State_tax.set('')
    sub_tax.set('')
    total_tax.set('')


Reference = StringVar()
Idly = StringVar()
Drink = StringVar()
Cost_of_meal = StringVar()
Service_cost = StringVar()
Dosa = StringVar()
Pav_bhaji = StringVar()
Pulav = StringVar()
Rice = StringVar()
State_tax = StringVar()
sub_tax = StringVar()
total_tax = StringVar()
# reference label
reference = Label(f1, font=('arial', 20, 'bold'), text="REFERENCE", fg="black", anchor='w')
reference.grid(row=0, column=0)
reference = Entry(f1, font=('arial', 20, 'bold'), textvariable=Reference, bd=10, insertwidth=4, bg="#3992a0",
                  justify='right')
reference.grid(row=0, column=1)

# drinks label
drink = Label(f1, font=('arial', 20, 'bold'), text="DRINK", fg="black", anchor='w')
drink.grid(row=0, column=3)
drink = Entry(f1, font=('arial', 20, 'bold'), textvariable=Drink, bd=10, insertwidth=4, bg="#3992a0",
              justify='right')
drink.grid(row=0, column=4)

# idly label
idly = Label(f1, font=('arial', 20, 'bold'), text="IDLY", fg="black", anchor='w')
idly.grid(row=1, column=0)
idly = Entry(f1, font=('arial', 20, 'bold'), textvariable=Idly, bd=10, insertwidth=4, bg="#3992a0", justify='right')
idly.grid(row=1, column=1)

# cost of meal label
cost_meal = Label(f1, font=('arial', 20, 'bold'), text="COST OF MEAL", fg="black", anchor='w')
cost_meal.grid(row=1, column=3)
cost_meal = Entry(f1, font=('arial', 20, 'bold'), textvariable=Cost_of_meal, bd=10, insertwidth=4, bg="#3992a0",
                  justify='right')
cost_meal.grid(row=1, column=4)

# dosa label
dosa = Label(f1, font=('arial', 20, 'bold'), text="DOSA", fg="black", anchor='w')
dosa.grid(row=2, column=0)
dosa = Entry(f1, font=('arial', 20, 'bold'), textvariable=Dosa, bd=10, insertwidth=4, bg="#3992a0", justify='right')
dosa.grid(row=2, column=1)

# Service charge label
service = Label(f1, font=('arial', 20, 'bold'), text="SERVICE CHARGE", fg="black", anchor='w')
service.grid(row=2, column=3)
service = Entry(f1, font=('arial', 20, 'bold'), textvariable=Service_cost, bd=10, insertwidth=4, bg="#3992a0",
                justify='right')
service.grid(row=2, column=4)

# Rice label
rice = Label(f1, font=('arial', 20, 'bold'), text="RICE", fg="black", anchor='w')
rice.grid(row=3, column=0)
rice = Entry(f1, font=('arial', 20, 'bold'), textvariable=Rice, bd=10, insertwidth=4, bg="#3992a0", justify='right')
rice.grid(row=3, column=1)

# State Tax label
state = Label(f1, font=('arial', 20, 'bold'), text="STATE TAX", fg="black", anchor='w')
state.grid(row=3, column=3)
state = Entry(f1, font=('arial', 20, 'bold'), textvariable=State_tax, bd=10, insertwidth=4, bg="#3992a0",
              justify='right')
state.grid(row=3, column=4)

# Pulav label
pulav = Label(f1, font=('arial', 20, 'bold'), text="PULAV", fg="black", anchor='w')
pulav.grid(row=4, column=0)
pulav = Entry(f1, font=('arial', 20, 'bold'), textvariable=Pulav, bd=10, insertwidth=4, bg="#3992a0",
              justify='right')
pulav.grid(row=4, column=1)

# SUB TAX label
sub = Label(f1, font=('arial', 20, 'bold'), text="SUB TAX", fg="black", anchor='w')
sub.grid(row=4, column=3)
sub = Entry(f1, font=('arial', 20, 'bold'), textvariable=sub_tax, bd=10, insertwidth=4, bg="#3992a0",
            justify='right')
sub.grid(row=4, column=4)

# Pav Bhaji label
pav = Label(f1, font=('arial', 20, 'bold'), text="PAV BHAJI", fg="black", anchor='w')
pav.grid(row=5, column=0)
pav = Entry(f1, font=('arial', 20, 'bold'), textvariable=Pav_bhaji, bd=10, insertwidth=4, bg="#3992a0",
            justify='right')
pav.grid(row=5, column=1)

# Total Cost label
total = Label(f1, font=('arial', 20, 'bold'), text="TOTAL COST", fg="black", anchor='w')
total.grid(row=5, column=3)
total = Entry(f1, font=('arial', 20, 'bold'), textvariable=total_tax, bd=10, insertwidth=4, bg="#3992a0",
              justify='right')
total.grid(row=5, column=4)

# Total Button
total_button = Button(f1, font=('arial', 20, 'bold'), text="TOTAL", bg="#3992a0", anchor='w', command=cal_total)
total_button.grid(row=7, column=1)

# Reset Button
total = Button(f1, font=('arial', 20, 'bold'), text="RESET", bg="#3992a0", anchor='w', command=reset)
total.grid(row=7, column=2)

# EXIT Button
total = Button(f1, font=('arial', 20, 'bold'), text="EXIT", bg="#3992a0", anchor='w', command=quit)
total.grid(row=7, column=3)


root.mainloop()
