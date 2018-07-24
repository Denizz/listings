from tkinter import *
from tkinter import ttk

class Gui():
    def start_walk(self, tab):

        self.result_text.insert(END, str(tab)+'\n')
        return

    def __init__(self):
        win = Tk()
        win.geometry('800x600+180+100')
        win.title('SEO Walker V.1.0.0')
        win.resizable(False, False)

    #tabs-menu
        tabControl = ttk.Notebook(win)

        simple_walk = ttk.Frame(tabControl)
        tabControl.add(simple_walk, text=u'Простое посещение')
        search_walk = ttk.Frame(tabControl)
        tabControl.add(search_walk, text=u'Через поисковик')
        tabControl.pack(side="top")

    #фреймы для simple_walk
        tab1_frame1 = Frame(simple_walk, bg='green', bd=5)
        tab1_frame1.pack(side='top')
        tab1_frame2 = Frame(simple_walk, bg='lightgreen', bd=5)
        tab1_frame2.pack(side='top')
        tab1_frame3 = Frame(simple_walk, bg='lightgreen', bd=5)
        tab1_frame3.pack(side='top')

    #фреймы для search_walk
        tab2_frame1 = Frame(search_walk, bg='green', bd=5)
        tab2_frame1.pack(side='top')
        tab2_frame2 = Frame(search_walk, bg='lightgreen', bd=5)
        tab2_frame2.pack(side='top')
        tab2_frame3 = Frame(search_walk, bg='lightgreen', bd=5)
        tab2_frame3.pack(side='top')
        tab2_frame4 = Frame(search_walk, bg='lightgreen', bd=5)
        tab2_frame4.pack(side='top')

    #поле ввода адреса сайта
        webaddress = Entry(tab1_frame1, width=30, font="Courier 16")
        webaddress.focus()
        webaddress.pack(side='left', pady=10)
        lbl_address = Label(tab1_frame1, text="Название сайта с http:// ",
        font="Courier 16")
        lbl_address.pack(side='left', padx=10, pady=10)

    #поле ввода количества ссылок 1
        ent_amount1 = Entry(tab1_frame2, width=2, font="Courier 16")
        ent_amount1.pack(side='left')
        lbl_ent1 = Label(tab1_frame2, text="Количество переходов по сайту",
        font="Courier 16")
        lbl_ent1.pack(side='left')

    #поле ввода количества ссылок 2
        ent_amount2 = Entry(tab2_frame3, width=2, font="Courier 16")
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

    #клики по рекламе1
        is_ads1 = IntVar()
        check1 = Checkbutton(tab2_frame4, text=u'Кликнуть по рекламе',
        variable=is_ads1, onvalue=1, offvalue=0, font="Courier 14")
        check1.pack(side="left")

    #кнопка выполнить 1
        start_button1 = Button(simple_walk, text='Выполнить', width=10,
        height=2, command=lambda: self.start_walk(1), font="Courier 16")
        start_button1.pack(side='bottom', padx=10, pady=10, fill=X)

    #клики по рекламе2
        is_ads2 = IntVar()
        check2 = Checkbutton(tab1_frame3, text=u'Кликнуть по рекламе',
        variable=is_ads2, onvalue=1, offvalue=0, font="Courier 14")
        check2.pack(side='left', padx=10, pady=10, fill=X)

    #количество переходов по рекламе 1
        ads_amount1 = Entry(tab1_frame3, width=2, font="Courier 14")
        ads_amount1.pack(side='left')
        lbl_ads1 = Label(tab1_frame3, text="Количество переходов по рекламе",
        font="Courier 12")
        lbl_ads1.pack(side='left')

        #количество переходов по рекламе 2
        ads_amount2 = Entry(tab2_frame4, width=2, font="Courier 16")
        ads_amount2.pack(side="left")
        lbl_ads2 = Label(tab2_frame4, text="Количество переходов по рекламе",
        font="Courier 16")
        lbl_ads2.pack(side="left")

    #кнопка выполнить 2
        start_button2 = Button(search_walk, text='Выполнить', width=10,
        height=2, command=lambda: self.start_walk(2), font="Courier 16")
        start_button2.pack(side='bottom', padx=10, pady=10, fill=X)

    #textarea для результата
        self.result_text = Text(win, height=20, width=100)
        self.result_text.pack(side="top")

        win.mainloop()

s = Gui()
