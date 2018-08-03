from tkinter import *
from tkinter import ttk


class Gui():

    def start_walk(self, tab, links_amount):

        if (tab == 1):
            self.result_text.delete(1.0, END)

            s = str("seowalker run... with " + links_amount + " links")
        elif (tab == 2):
            self.result_text.delete(1.0, END)
            s = str("seosearcher starts... " + links_amount + " links")

        self.result_text.insert(END, s)
        return

    def change(self, event, widget, widget_gui, widget_lbl, is_ads):

        x = is_ads.get()
        if x == 1:
            widget_gui.configure(state=NORMAL)
            widget_lbl.configure(state=NORMAL)
        else:
            widget_gui.configure(state=DISABLED)
            widget_lbl.configure(state=DISABLED)

    def __init__(self):
        self.win = Tk()
        self.win.geometry('800x600+180+100')
        self.win.title('SEO Walker V.1.0.0')
        self.win.resizable(False, False)

    #tabs-menu
        tabControl = ttk.Notebook(self.win)

        simple_walk = ttk.Frame(tabControl)
        tabControl.add(simple_walk, text=u'Простое посещение')
        search_walk = ttk.Frame(tabControl)
        tabControl.add(search_walk, text=u'Через поисковик')
        tabControl.pack(side="top")

    #фреймы для simple_walk
        tab1_frame1 = Frame(simple_walk)
        tab1_frame1.pack(side='top')
        tab1_frame2 = Frame(simple_walk)
        tab1_frame2.pack(side='top')
        tab1_frame3 = Frame(simple_walk)
        tab1_frame3.pack(side='top')

    #фреймы для search_walk
        tab2_frame1 = Frame(search_walk)
        tab2_frame1.pack(side='top')
        tab2_frame2 = Frame(search_walk)
        tab2_frame2.pack(side='top')
        tab2_frame3 = Frame(search_walk)
        tab2_frame3.pack(side='top')
        tab2_frame4 = Frame(search_walk)
        tab2_frame4.pack(side='top')

#__________________TAB1______________________________________________#

    #поле ввода адреса сайта
        webaddress = Entry(tab1_frame1, width=30, font="Courier 16")
        webaddress.focus()
        webaddress.pack(side='left', pady=10)
        lbl_address = Label(tab1_frame1, text="Название сайта с http:// ",
        font="Courier 16")
        lbl_address.pack(side='left', padx=10, pady=10)

    #поле ввода количества ссылок 1
        links_amount = StringVar()
        ent_amount1 = Entry(tab1_frame2, width=2, font="Courier 16",
        textvariable=links_amount)
        ent_amount1.pack(side='left')
        lbl_ent1 = Label(tab1_frame2, text="Количество переходов по сайту",
        font="Courier 14")
        lbl_ent1.pack(side='left')

    #клики по рекламе1
        is_ads1 = IntVar()
        self.check1 = Checkbutton(tab1_frame3, text=u'Кликнуть по рекламе',
        variable=is_ads1, font="Courier 14", command=lambda:
        self.change(self, self.check1, ads_amount1, lbl_ads1, is_ads1))
        self.check1.pack(side="left")

    #количество переходов по рекламе 1
        ads_amount1 = Entry(tab1_frame3, width=2, font="Courier 14",
        state=DISABLED)
        ads_amount1.pack(side='left')
        lbl_ads1 = Label(tab1_frame3, text="Количество переходов по рекламе",
        font="Courier 12", state=DISABLED)
        lbl_ads1.pack(side='left')

    #кнопка выполнить 1
        start_button1 = Button(simple_walk, text='Выполнить', width=10,
        height=2, command=lambda: self.start_walk(1, links_amount.get()),
        font="Courier 16")
        start_button1.pack(side='bottom', padx=10, pady=10, fill=X)

#__________________TAB2______________________________________________#

    #поле ввода количества ссылок 2
        links_amount2 = StringVar()
        ent_amount2 = Entry(tab2_frame3, width=2, font="Courier 16",
        textvariable=links_amount2)
        ent_amount2.pack(side='left')
        lbl_ent2 = Label(tab2_frame3, text="Количество переходов по сайту",
        font="Courier 16")
        lbl_ent2.pack(side='left')

    #select список
        searcher = StringVar()
        searcher_chosen = ttk.Combobox(tab2_frame1, textvariable=searcher,
        font="Courier 16", state='readonly')
        searcher_chosen['values'] = ("Yandex", "Google")
        searcher_chosen.current(0)
        searcher_chosen.pack(side="left")

    #фраза для поиска
        phrase = Entry(tab2_frame1, width=30, font="Courier 14")
        phrase.pack(side="left")
        lbl_phrase = Label(tab2_frame1, text="Фраза для поиска",
        font="Courier 14")
        lbl_phrase.pack(side="left")

    #шаблон адреса для поиска
        tmp_address = Entry(tab2_frame2, width=30, font="Courier 14")
        tmp_address.pack(side="left")
        lbl_tmp_address = Label(tab2_frame2, text="Шаблон названия сайта",
        font="Courier 14")
        lbl_tmp_address.pack(side="left")

    #клики по рекламе2
        is_ads2 = IntVar()
        self.check2 = Checkbutton(tab2_frame4, text=u'Кликнуть по рекламе',
        onvalue=1, offvalue=0, font="Courier 14", variable=is_ads2,
        command=lambda: self.change(self, self.check2, ads_amount2, lbl_ads2,
        is_ads2))
        self.check2.pack(side='left', padx=10, pady=10, fill=X)

    #количество переходов по рекламе 2
        ads_amount2 = Entry(tab2_frame4, width=2, font="Courier 16",
        state=DISABLED)
        ads_amount2.pack(side="left")
        lbl_ads2 = Label(tab2_frame4, text="Количество переходов по рекламе",
        font="Courier 14", state=DISABLED)
        lbl_ads2.pack(side="left")

    #кнопка выполнить 2
        start_button2 = Button(search_walk, text='Выполнить', width=10,
        height=2, command=lambda: self.start_walk(2, links_amount2.get()),
        font="Courier 16")
        start_button2.pack(side='bottom', padx=10, pady=10, fill=X)

#_________________________TABS END_______________________________#

    #textarea для результата
        self.result_text = Text(self.win, height=20, width=100)
        self.result_text.pack(side="top")


if __name__ == "__main__":
    gui = Gui()
    gui.win.mainloop()

