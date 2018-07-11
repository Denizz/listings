from tkinter import *
from tkinter import ttk


def start_walk():
    print("Here we go!")
    return


def main():
    win = Tk()
    win.geometry('800x500+180+100')
    win.title('SEO Walker V.1.0.0')
    win.resizable(False, False)

    #tabs-menu
    tabControl = ttk.Notebook(win)

    simple_walk = ttk.Frame(tabControl)
    tabControl.add(simple_walk, text=u'Простое посещение')
    search_walk = ttk.Frame(tabControl)
    tabControl.add(search_walk, text=u'Через поисковик')
    tabControl.pack(expand=1, fill="both")

    #поле ввода адреса сайта
    webaddress = Entry(simple_walk, width=30, font="Courier 20")
    webaddress.focus()
    webaddress.pack()
    lbl_address = Label(simple_walk, text="Название сайта начиная с http:// ",
    font="Courier 20")
    lbl_address.pack()

    #поле ввода количества ссылок
    ent_amount = Entry(simple_walk, width=2, font="Courier 20")
    ent_amount.pack()
    lbl_ent = Label(simple_walk, text="Количество ссылок", font="Courier 20")
    lbl_ent.pack()

    #select список
    searcher = StringVar()
    searcher_chosen = ttk.Combobox(search_walk, textvariable=searcher,
    font="Courier 20")
    searcher_chosen['values'] = ("Yandex", "Google")
    searcher_chosen.current(0)
    searcher_chosen.pack()

    #фраза для поиска
    phrase = Entry(search_walk, width=30, font="Courier 20")
    phrase.pack()
    lbl_phrase = Label(search_walk, text="Фраза для поиска", font="Courier 20")
    lbl_phrase.pack()

    #шаблон адреса для поиска
    tmp_address = Entry(search_walk, width=30, font="Courier 20")
    tmp_address.pack()
    lbl_tmp_address = Label(search_walk, text="Шаблон названия сайта",
    font="Courier 20")
    lbl_tmp_address.pack()

    #клики по рекламе1
    is_ads1 = IntVar()
    check1 = Checkbutton(search_walk, text=u'Кликнуть по рекламе',
    variable=is_ads1, onvalue=1, offvalue=0, font="Courier 20")
    check1.pack()

    #клики по рекламе2
    is_ads2 = IntVar()
    check2 = Checkbutton(simple_walk, text=u'Кликнуть по рекламе',
    variable=is_ads2, onvalue=1, offvalue=0, font="Courier 20")
    check2.pack()

    #количество переходов по рекламе
    ads_amount = Entry(search_walk, width=2)
    ads_amount.pack()
    lbl_ads = Label(search_walk, text="Количество переходов по рекламе")
    lbl_ads.pack()

    #кнопка выполнить
    start_button = Button(simple_walk, text='Выполнить', width=10, height=2,
    command=start_walk)
    start_button.pack()

    win.mainloop()

if __name__ == '__main__':
    main()
