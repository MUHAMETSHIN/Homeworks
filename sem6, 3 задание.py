import pandas as pd
import random
from tkinter import *
from tkinter import ttk
films = pd.read_csv('imdb_top_250.csv')

fims_spisok = list(films['Title'])
gen = list(films['Genre'])

def finder():
    want = youwant.get()
    podhod = []
    for i in range(len(gen)):
        if want in gen[i]:
            podhod.append(fims_spisok[i])
    random_film = random.choice(podhod)
    a.set(random_film)
    ttk.Label(mainframe, text="Советуем посмотреть").grid(column=1, row=3, sticky=W)

root = Tk()
root.title('Фильмотека')
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

youwant = StringVar()
youwant_entry = ttk.Entry(mainframe, width=7, textvariable=youwant)
youwant_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Поиск", command=finder).grid(column=2, row=2, sticky=W)

ttk.Label(mainframe, text="Какой жанр вас интересует?").grid(column=1, row=1, sticky=W)


a = StringVar()
ttk.Label(mainframe, textvariable=a).grid(column=2, row=3, sticky=W)
root.mainloop()
