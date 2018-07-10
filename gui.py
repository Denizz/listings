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

    #поле ввода адреса сайта
    webaddress = Entry(win, width=30)
    webaddress.focus()
    webaddress.grid(row=1, column=0)
    lbl_address = Label(win, text="Название сайта начиная с http:// ")
    lbl_address.grid(row=1, column=1)

    #поле ввода количества ссылок
    ent_amount = Entry(win, width=2)
    ent_amount.grid(row=2, column=0)
    lbl_ent = Label(win, text="Количество ссылок")
    lbl_ent.grid(row=2, column=1)

    #чек-бокс производить ли поиск через поисковик
    is_search = IntVar()
    check1 = Checkbutton(win, text=u'Через поисковик', variable=is_search,
    onvalue=1, offvalue=0)
    check1.grid(row=3, column=0)

    #select список
    searcher = StringVar()
    searcher_chosen = ttk.Combobox(win, textvariable=searcher)
    searcher_chosen['values'] = ("Yandex", "Google")
    searcher_chosen.current(0)
    searcher_chosen.grid(row=3, column=1)

    #фраза для поиска
    phrase = Entry(win, width=30)
    phrase.grid(row=4, column=0)
    lbl_phrase = Label(win, text="Фраза для поиска")
    lbl_phrase.grid(row=4, column=1)

    #шаблон адреса для поиска
    tmp_address = Entry(win, width=30)
    tmp_address.grid(row=5, column=0)
    lbl_tmp_address = Label(win, text="Шаблон названия сайта")
    lbl_tmp_address.grid(row=5, column=1)

    #клики по рекламе
    is_ads = IntVar()
    check1 = Checkbutton(win, text=u'Кликнуть по рекламе', variable=is_ads,
    onvalue=1, offvalue=0)
    check1.grid(row=6, column=0)

    #количество переходов по рекламе
    ads_amount = Entry(win, width=2)
    ads_amount.grid(row=6, column=1)
    lbl_ads = Label(win, text="Количество переходов по рекламе")
    lbl_ads.grid(row=6, column=2)

    #кнопка выполнить
    start_button = Button(win, text='Выполнить', width=10, height=2,
    command=start_walk)
    start_button.grid(row=7, column=2)

    win.mainloop()

if __name__ == '__main__':
    main()