
from tkinter import *
from tkinter import ttk

def imt():
    try:
        weight = float(mass.get())
        high = float(rost.get())
        put = int(weight/(high)**2)
        Imt.set(put)
        if put<16:
            a.set("Выраженный дефицит массы тела")
        if 16<=put<18.5:
            a.set("Недостаточная масса тела")
        if 18.5<=put<25:
            a.set("Норма")
        if 25<=put<30:
            a.set("Избыточная масса тела")
        if 30<=put<35:
            a.set("Ожирение степени 1")
        if 35<=put<40:
            a.set("Ожирение степени 2")
        if 40<=put:
            a.set("Ожирение степени 3")
        
    except ValueError:
        pass

root = Tk()
root.title('IMT')
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mass = StringVar()
mass_entry = ttk.Entry(mainframe, width=7, textvariable=mass)
mass_entry.grid(column=2, row=1, sticky=(W, E))

rost = StringVar()
rost_entry = ttk.Entry(mainframe, width=8, textvariable=rost)
rost_entry.grid(column=2, row=2, sticky=(W, E))

Imt = StringVar()
ttk.Label(mainframe, textvariable=Imt).grid(column=2, row=4, sticky=(W, E))

ttk.Button(mainframe, text="Вычислить", command=imt).grid(column=2, row=3, sticky=W)


a = StringVar()
ttk.Label(mainframe, textvariable=a).grid(column=2, row=5, sticky=W)

ttk.Label(mainframe, text="Ваш вес в кг").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Ваш рост в м").grid(column=3, row=2, sticky=E)
ttk.Label(mainframe, text="ИМТ").grid(column=3, row=4, sticky=W)

root.mainloop()