from seo_walker import SeoWalker
from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        value = link.get()
        sw = SeoWalker()
        sw.walk(value, 2)
        answers.set("Result will be soon!")
    except ValueError:
        pass


root = Tk()
root.title("Робот-бродилка!")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

link = StringVar()
answers = StringVar()

link_entry = ttk.Entry(mainframe, width=7, textvariable=link)
link_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=answers).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Вперед!", command=calculate).grid(column=3, row=3, sticky=W)


ttk.Label(mainframe, text="Найдено линков:").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

link_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
