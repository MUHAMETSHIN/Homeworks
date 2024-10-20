from tkinter import *

def calc(*argc):
    try:
        result.set('= '+ str(eval(command.get())))
    except:
        pass

root = Tk()
root.title("Калькулятор")
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, S, W, E))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

command = StringVar()
result = StringVar()
entry = Entry(mainframe, width=10, textvariable=command)
entry.grid(column=1, row=1, sticky=(W))

Label(mainframe, textvariable=result).grid(column=2, row=1, sticky=W)
Button(mainframe, text = "Вычислить", command=calc).grid(column=1, row=2)
root.bind('<Return>', calc)
entry.focus()

root.mainloop()