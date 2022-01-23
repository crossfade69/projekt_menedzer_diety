import tkinter as tk
from tkinter import *
from biblioteki import pliki as p
from biblioteki import sortuj as s
from biblioteki import watki as w
from biblioteki import menu as m
from biblioteki import zapotrzebowanie as z
from datetime import datetime
import threading
import os


def Okno_dane(dzienne_zapotrzebowanie, lista_preferencji, dane, liczba_wszystkich):


    plec = IntVar()
    dieta = IntVar()
    aktywnosc = IntVar()

    frame1 = LabelFrame(frame_gl, text='Dane uzytkownika')
    frame1.grid(rowspan=5, row=0, column=1, padx=5, pady=5)

    # FRAME 1 METRYKA
    label1 = tk.Label(frame1, text='Waga')
    label1.grid(row=1, column=0, padx=2, pady=2)
    entry1 = tk.Entry(frame1)
    entry1.grid(row=2, column=0)

    label2 = tk.Label(frame1, text='Wzrost')
    label2.grid(row=3, column=0, padx=5, pady=5)
    entry2 = tk.Entry(frame1)
    entry2.grid(row=4, column=0)

    label3 = tk.Label(frame1, text='Wiek')
    label3.grid(row=5, column=0, padx=5, pady=5)
    entry3 = tk.Entry(frame1)
    entry3.grid(row=6, column=0)

    # WYBÓR PŁCI
    plec.set(0)
    label4 = tk.Label(frame1, text='Płeć')
    label4.grid(row=7, column=0, padx=5, pady=5)
    check1 = tk.Radiobutton(frame1, text='Mężczyzna', variable=plec, value=0)
    check1.grid(row=8, column=0)
    check2 = tk.Radiobutton(frame1, text='Kobieta', variable=plec, value=1)
    check2.grid(row=9, column=0)

    # WYBÓR TYPU DIETY
    dieta.set(0)
    label5 = tk.Label(frame1, text='Typ diety')
    label5.grid(row=10, column=0, padx=5, pady=5)
    check3 = tk.Radiobutton(frame1, text='Standardowa', variable=dieta, value=0)
    check3.grid(row=11, column=0)
    check4 = tk.Radiobutton(frame1, text='Wegańska', variable=dieta, value=1)
    check4.grid(row=12, column=0)
    check5 = tk.Radiobutton(frame1, text='Wegetariańska', variable=dieta, value=2)
    check5.grid(row=13, column=0)

    # WYBÓR DOTYCZĄCY AKTYWNOŚCI
    aktywnosc.set(1)
    label1_0 = Label(frame1, text="Jak zazwyczaj wygląda twoja aktywność fizyczna w ciągu tygodnia?")
    label1_0.grid(row=0, column=1, padx=25, sticky="NW")
    check_aktywnosc_1 = Radiobutton(frame1, text='Siedzący', variable=aktywnosc, value=1)
    check_aktywnosc_1.grid(row=2, column=1, padx=10, sticky="NW")
    label1_1 = Label(frame1, text="Jeśli wykonujesz minimalne ćwiczenia lub nie wykonujesz żadnych ćwiczeń.")
    label1_1.grid(row=3, column=1, padx=25, sticky="NW")
    check_aktywnosc_2 = Radiobutton(frame1, text='Lekko aktywny', variable=aktywnosc, value=2)
    check_aktywnosc_2.grid(row=5, column=1, padx=10, sticky="NW")
    label1_2 = Label(frame1, text="Jeśli ćwiczysz lekko od jednego do trzech dni w tygodniu.")
    label1_2.grid(row=6, column=1, padx=25, sticky="NW")
    check_aktywnosc_3 = Radiobutton(frame1, text='Umiarkowanie aktywny.', variable=aktywnosc, value=3)
    check_aktywnosc_3.grid(row=8, column=1, padx=10, sticky="NW")
    label1_3 = Label(frame1, text="Jeśli ćwiczysz umiarkowanie od trzech do pięciu dni w tygodniu.")
    label1_3.grid(row=9, column=1, padx=25, sticky="NW")
    check_aktywnosc_4 = Radiobutton(frame1, text='Bardzo aktywny', variable=aktywnosc, value=4)
    check_aktywnosc_4.grid(row=11, column=1, padx=10, sticky="NW")
    label1_4 = Label(frame1, text="Jeśli intensywnie ćwiczysz przez sześć do siedmiu dni w tygodniu.")
    label1_4.grid(row=12, column=1, padx=25, sticky="NW")
    check_aktywnosc_5 = Radiobutton(frame1, text='Ekstra aktywny', variable=aktywnosc, value=5)
    check_aktywnosc_5.grid(row=14, column=1, padx=15, sticky="NW")
    label1_5 = Label(frame1,
                     text="Jeśli wykonujesz bardzo ciężkie ćwiczenia przez sześć do siedmiu dni w tygodniu lub wykonujesz pracę fizyczną.")
    label1_5.grid(row=15, column=1, padx=25, sticky="NW")

    ostrzezenie = tk.Label(frame1, text='Wpisz prawidłowe wartości', fg='red', borderwidth='10')

    submitButton = Button(frame1, height=3, width=7, text='Zatwierdź',
                              command=lambda: dane == zatwierdz(dzienne_zapotrzebowanie, entry1.get(),
                                                                entry2.get(), entry3.get(),
                                                                plec.get(), aktywnosc.get(), dieta.get(), dane,
                                                                lista_preferencji, liczba_wszystkich, ostrzezenie))
    submitButton.grid(row=16, column=8, padx=5, pady=5)



def zatwierdz(dzienne_zapotrzebowanie, waga, wzrost, wiek, plec, aktywnosc, dieta, dane, lista_preferencji,
              liczba_wszystkich, ostrzezenie):
    try:

        waga = float(waga)
        wzrost = float(wzrost)
        wiek = float(wiek)
        plec = float(plec)

        dzienne_zapotrzebowanie.modyfikacja(waga, wzrost, wiek, plec, aktywnosc)
        if dieta == 0:
            lista_preferencji[0] = False
            lista_preferencji[1] = False
        elif dieta == 1:
            lista_preferencji[0] = False
            lista_preferencji[1] = True
        elif dieta == 2:
            lista_preferencji[0] = True
            lista_preferencji[1] = False
        m.modyfikuj_dane(dane, "dane.csv", liczba_wszystkich, isWegetarian=lista_preferencji[0],
                         isVegan=lista_preferencji[1])
        s.quickSort(dane, 0, len(dane) - 1, 0, s.digits_greater, s.digits_less)
    except ValueError:
        ostrzezenie.grid(row=16, column=0, pady=10, columnspan=3)



def Okno_spozycie(dzienne_zapotrzebowanie, dzienna_suma):
    # Dzienne_spozycie_okno = tk.Toplevel(root)
    # Dzienne_spozycie_okno.title('Spożycie')
    frame2 = LabelFrame(frame_gl, text="Monitoring spożycia")
    frame2.grid(rowspan=5, row=0, column=1, padx=5, pady=5)

    # PODPISY FRAME 2
    label6 = tk.Label(frame2, text="Dzienne zapotrzebowanie: ")
    label6.grid(row=0, column=0, padx=5, pady=5)

    label6_1 = tk.Label(frame2, text="Kalorie: " + str(round(dzienne_zapotrzebowanie.get_kalorie(),2)) + " kcal")
    label6_1.grid(row=1, column=0, padx=5, pady=5, sticky="NW")

    label6_2 = tk.Label(frame2, text="Białka: " + str(round(dzienne_zapotrzebowanie.get_bialka(),2)) + " g")
    label6_2.grid(row=2, column=0, padx=5, pady=5, sticky="NW")

    label6_3 = tk.Label(frame2, text="Tłuszcze: " + str(round(dzienne_zapotrzebowanie.get_tluszcze(),2)) + " g")
    label6_3.grid(row=3, column=0, padx=5, pady=5, sticky="NW")

    label6_4 = tk.Label(frame2, text="Węglowodany: " + str(round(dzienne_zapotrzebowanie.get_weglowodany(),2)) + " g")
    label6_4.grid(row=4, column=0, padx=5, pady=5, sticky="NW")

    label7 = tk.Label(frame2, text="Spożyto dzisiaj: ")
    label7.grid(row=5, column=0, padx=5, pady=5)

    label8 = tk.Label(frame2, text="Kalorie: " + str(round(dzienna_suma.get_kalorie(),2)) + " kcal")
    label8.grid(row=6, column=0, padx=5, pady=5, sticky="NW")

    label9 = tk.Label(frame2, text="Białka: " + str(round(dzienna_suma.get_bialka(),2)) + " g")
    label9.grid(row=7, column=0, padx=5, pady=5, sticky="NW")

    label10 = tk.Label(frame2, text="Tłuszcze: " + str(round(dzienna_suma.get_tluszcze(),2)) + " g")
    label10.grid(row=8, column=0, padx=5, pady=5, sticky="NW")

    label11 = tk.Label(frame2, text="Węglowodany: " + str(round(dzienna_suma.get_weglowodany(),2)) + " g")
    label11.grid(row=9, column=0, padx=5, pady=5, sticky="NW")

def zatwierdz_ilosc(ostrzezenie, dzienna_suma,wybor,dane,Okno_ilosc, ile):

    try:
        if not str.isdigit(ile) and not (bool(ostrzezenie.winfo_exists())):
            ostrzezenie = tk.Label(Okno_ilosc, text='Wpisz prawidłową wartość', fg='red', borderwidth='10')
        elif str.isdigit(ile) and (bool(ostrzezenie.winfo_exists())):
            ostrzezenie.destroy()

        ile = float(ile)
        kalorie = round((dane[wybor][1]/100)*ile, 2)
        bialka = round((dane[wybor][2]/100)*ile, 2)
        tluszcze = round((dane[wybor][3]/100)*ile, 2)
        weglowodany = round((dane[wybor][4]/100)*ile, 2)


        label_wyliczone = tk.Label(Okno_ilosc, text="Wartość odżywcza dla " + str(ile) + " g potrawy")
        label_wyliczone.grid(row=6, column=0, padx=40,pady=10, columnspan=5)

        label_nazwa3 = tk.Label(Okno_ilosc, text="Nazwa")
        label_nazwa3.grid(row=7, column=0,pady=10, padx=40)

        label_kcal3 = tk.Label(Okno_ilosc, text="Kalorie [Kcal]")
        label_kcal3.grid(row=7, column=1,pady=10, padx=10)

        label_bialko3 = tk.Label(Okno_ilosc, text="Białka [g]")
        label_bialko3.grid(row=7, column=2,pady=10, padx=10)

        label_tluszcz3 = tk.Label(Okno_ilosc, text="Tłuszcze [g]")
        label_tluszcz3.grid(row=7, column=3,pady=10, padx=10)

        label_wegle3 = tk.Label(Okno_ilosc, text="Węglowodany [g]")
        label_wegle3.grid(row=7, column=4,pady=10, padx=10)

        label_nazwa4 = tk.Label(Okno_ilosc, text=str(dane[wybor][0]))
        label_nazwa4.grid(row=8, column=0, pady=10, padx=30)

        label_kcal4 = tk.Label(Okno_ilosc, text=str(kalorie), borderwidth = 1, width = 10, relief="flat")
        label_kcal4.grid(row=8, column=1,pady=10, padx=30)

        label_bialko4 = tk.Label(Okno_ilosc, text=str(bialka), borderwidth = 1, width = 10, relief="flat")
        label_bialko4.grid(row=8, column=2,pady=10, padx=30)

        label_tluszcz4 = tk.Label(Okno_ilosc, text=str(tluszcze), borderwidth = 1, width = 10, relief="flat")
        label_tluszcz4.grid(row=8, column=3,pady=10, padx=30)

        label_wegle4 = tk.Label(Okno_ilosc, text=str(weglowodany), borderwidth = 1, width = 10, relief="flat")
        label_wegle4.grid(row=8, column=4,pady=10, padx=30)

        button_potwierdz = tk.Button(Okno_ilosc, text='Zjedz', width=20, command = lambda: m.dodaj_do_dziennej_sumy(dzienna_suma, kalorie, bialka, tluszcze, weglowodany))
        button_potwierdz.grid(row=9, column=3,pady=10, columnspan=2)

    except:
        ostrzezenie.grid(row=9, column=0, pady=10, columnspan=3)


def dodaj_do_sumy(ostrzezenie, dzienna_suma, kalorie, bialka, tluszcze, weglowodany):
    #if ostrzezenie.winfo_exists():
    ostrzezenie.destroy()
    m.dodaj_do_dziennej_sumy(dzienna_suma, kalorie, bialka, tluszcze, weglowodany)
# def Okno_wpisz(dzienna_suma, zaznaczony_index): to właściwa funkcja na później


def Okno_wpisz(dzienna_suma,dane, wybor):

    clear()

    Okno_ilosc = LabelFrame(frame_gl, text='Szczegolowe')
    Okno_ilosc.grid(row=0, column=3, padx=5, pady=5, columnspan=5)



    label_przywitanie = tk.Label(Okno_ilosc, text="Wartość odżywcza dla 1 grama potrawy")
    label_przywitanie.grid(row=1, column=0, padx=40, pady=10, columnspan=5)

    label_nazwa1 = tk.Label(Okno_ilosc, text="Nazwa")
    label_nazwa1.grid(row=2, column=0,pady=10, padx=40)

    label_kcal1 = tk.Label(Okno_ilosc, text="Kalorie [Kcal]")
    label_kcal1.grid(row=2, column=1,pady=10, padx=10)

    label_bialko1 = tk.Label(Okno_ilosc, text="Białka [g]")
    label_bialko1.grid(row=2, column=2,pady=10, padx=10)

    label_tluszcz1 = tk.Label(Okno_ilosc, text="Tłuszcze [g]")
    label_tluszcz1.grid(row=2, column=3,pady=10, padx=10)

    label_wegle1 = tk.Label(Okno_ilosc, text="Węglowodany [g]")
    label_wegle1.grid(row=2, column=4,pady=10, padx=10)

    label_wybor = tk.Label(Okno_ilosc, text=str(dane[wybor][0]))
    label_wybor.grid(row=3, column=0)

    label_kcal2 = tk.Label(Okno_ilosc, text=str(round(dane[wybor][1]/100,2)))
    label_kcal2.grid(row=3, column=1, pady=10, padx=10)

    label_bialko2 = tk.Label(Okno_ilosc, text=str(round(dane[wybor][2]/100,2)))
    label_bialko2.grid(row=3, column=2,pady=10, padx=10)

    label_tluszcz2 = tk.Label(Okno_ilosc, text=str(round(dane[wybor][3]/100,2)))
    label_tluszcz2.grid(row=3, column=3,pady=10, padx=10)

    label_wegle2 = tk.Label(Okno_ilosc, text=str(round(dane[wybor][4]/100,2)))
    label_wegle2.grid(row=3, column=4,pady=10, padx=10)

    label_ilosc2 = tk.Label(Okno_ilosc, text='Wpisz ilość spożytego posiłku w gramach')
    label_ilosc2.grid(row=4, column=0,pady=10, columnspan=3)
    entry_ilosc = tk.Entry(Okno_ilosc, width=40)
    entry_ilosc.grid(row=5, column=0,pady=10, columnspan=3)

    ostrzezenie = tk.Label(Okno_ilosc, text='Wpisz prawidłową wartość', fg='red', borderwidth='10')

    button_ilosc = tk.Button(Okno_ilosc, text='Zatwierdź', width=20,command=lambda: zatwierdz_ilosc(ostrzezenie, dzienna_suma,wybor,dane, Okno_ilosc, entry_ilosc.get()))
    button_ilosc.grid(row=5, column=3,pady=10, columnspan=2)

def Okno_lista(dane, lista_preferencji, liczba_wszystkich, dzienna_suma):
    # FRAME 3

    # dane = m.modyfikuj_dane(dane,'dane.csv',liczba_wszystkich,isVegan=lista_preferencji[0],isWegetarian=lista_preferencji[1])
    # print(dane)
    frame3 = LabelFrame(frame_gl, text="Lista przepisów")
    frame3.grid(row=0, column=3, padx=5, pady=5, columnspan=5)

    label_nazwa = tk.Label(frame3, text="Nazwa")
    label_nazwa.grid(row=2, column=0, padx=40)

    label_kcal = tk.Label(frame3, text="Kalorie [Kcal]")
    label_kcal.grid(row=2, column=1, padx=10)

    label_wegle = tk.Label(frame3, text="Białka [g]")
    label_wegle.grid(row=2, column=2, padx=10)

    label_bialko = tk.Label(frame3, text="Tłuszcze [g]")
    label_bialko.grid(row=2, column=3, padx=10)

    label_tluszcz = tk.Label(frame3, text="Węglowodany [g]")
    label_tluszcz.grid(row=2, column=4, padx=10)

    scrollbar = tk.Scrollbar(frame3, orient=VERTICAL)
    scrollbar.grid(row=3, column=5, sticky=NS)

    # LISTA PRZEPISOW(LISTBOX)
    przepisy_lista = Listbox(frame3, height=15, width=100, border=0)
    przepisy_lista.grid(row=0, column=0, columnspan=5, pady=20, padx=20)

    przepisy_lista.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=przepisy_lista.yview)

    # przepisy_lista.pack()

    for i in range(0, len(dane)):
        przepisy_lista.insert(i, str(dane[i][0]) + " | " + str(dane[i][1]) + " | " + str(dane[i][2]) + " | " + str(
            dane[i][3]) + " | " + str(dane[i][4]))
        # = tk.Label(przepisy_lista, text="Węglowodany [g]")
        # label_tluszcz.grid(row=2, column=4, padx=10)

    przepisy_lista.grid(row=3, column=0)

    Button_select = Button(frame3, text='wybierz',
                           command=lambda: Okno_wpisz_clear(dzienna_suma, przepisy_lista, dane, frame3))
    Button_select.grid(row=9, column=4)

    ##########################################################################################################
    # SORT MENU

    var = tk.StringVar(value="Sortuj listę")
    menubutton = tk.Menubutton(frame3, textvariable=var, indicatoron=True,
                               borderwidth=1, relief="raised", width=20)
    main_menu = tk.Menu(menubutton, tearoff=False)
    menubutton.configure(menu=main_menu)

    rozwijane = (("Rosnąco wg", "Nazwy", "Kalorii", "Białek", "Tłuszczy", "Węglowodanów"),
                 ("Malejąco wg", "Nazwy", "Kalorii", "Białek", "Tłuszczy", "Węglowodanów"))

    menu = tk.Menu(main_menu, tearoff=False)
    main_menu.add_cascade(label=rozwijane[0][0], menu=menu)
    menu.add_radiobutton(value=rozwijane[0][1], label=rozwijane[0][1], variable=var,
                         command=lambda: Sort_okno_lista(dane, 0, s.letter_greater, s.letter_less, False,
                                                         lista_preferencji, liczba_wszystkich, dzienna_suma))
    menu.add_radiobutton(value=rozwijane[0][2], label=rozwijane[0][2], variable=var,
                         command=lambda: Sort_okno_lista(dane, 1, s.digits_greater, s.digits_less, False,
                                                         lista_preferencji, liczba_wszystkich, dzienna_suma))
    menu.add_radiobutton(value=rozwijane[0][3], label=rozwijane[0][3], variable=var,
                         command=lambda: Sort_okno_lista(dane, 2, s.digits_greater, s.digits_less, False,
                                                         lista_preferencji, liczba_wszystkich, dzienna_suma))
    menu.add_radiobutton(value=rozwijane[0][4], label=rozwijane[0][4], variable=var,
                         command=lambda: Sort_okno_lista(dane, 3, s.digits_greater, s.digits_less, False,
                                                         lista_preferencji, liczba_wszystkich, dzienna_suma))
    menu.add_radiobutton(value=rozwijane[0][5], label=rozwijane[0][5], variable=var,
                         command=lambda: Sort_okno_lista(dane, 4, s.digits_greater, s.digits_less, False,
                                                         lista_preferencji, liczba_wszystkich, dzienna_suma))
    menu = tk.Menu(main_menu, tearoff=False)
    main_menu.add_cascade(label=rozwijane[1][0], menu=menu)
    menu.add_radiobutton(value=rozwijane[1][1], label=rozwijane[1][1], variable=var,
                         command=lambda: Sort_okno_lista(dane, 0, s.letter_greater, s.letter_less, True,
                                                         lista_preferencji, liczba_wszystkich, dzienna_suma))
    menu.add_radiobutton(value=rozwijane[1][2], label=rozwijane[1][2], variable=var,
                         command=lambda: Sort_okno_lista(dane, 1, s.digits_greater, s.digits_less, True,
                                                         lista_preferencji, liczba_wszystkich, dzienna_suma))
    menu.add_radiobutton(value=rozwijane[1][3], label=rozwijane[1][3], variable=var,
                         command=lambda: Sort_okno_lista(dane, 2, s.digits_greater, s.digits_less, True,
                                                         lista_preferencji, liczba_wszystkich, dzienna_suma))
    menu.add_radiobutton(value=rozwijane[1][4], label=rozwijane[1][4], variable=var,
                         command=lambda: Sort_okno_lista(dane, 3, s.digits_greater, s.digits_less, True,
                                                         lista_preferencji, liczba_wszystkich, dzienna_suma))
    menu.add_radiobutton(value=rozwijane[1][5], label=rozwijane[1][5], variable=var,
                         command=lambda: Sort_okno_lista(dane, 4, s.digits_greater, s.digits_less, True,
                                                         lista_preferencji, liczba_wszystkich, dzienna_suma))

    menubutton.grid(row=0, padx=20, pady=20)

def Okno_podsumowanie(dzienne_zapotrzebowanie, dzienna_suma):
    # Podsumowanie_okno = tk.Toplevel(root)
    # Podsumowanie_okno.title('Podsumowanie dnia')

    lista = m.podsumowanie(dzienne_zapotrzebowanie, dzienna_suma)
    frame4 = LabelFrame(frame_gl, text="Podsumowanie dnia")
    frame4.grid(row=0, column=0, padx=5, pady=5)

    label_p1 = Label(frame4, text="Kalorie: " + lista[0])
    label_p1.grid(row=0, column=0, padx=5, pady=5)
    label_p2 = Label(frame4, text="Białka: " + lista[1])
    label_p2.grid(row=1, column=0, padx=5, pady=5)
    label_p3 = Label(frame4, text="Tłuszcze: " + lista[2])
    label_p3.grid(row=2, column=0, padx=5, pady=5)
    label_p4 = Label(frame4, text="Węglowodany: " + lista[3])
    label_p4.grid(row=3, column=0, padx=5, pady=5)





def Okno_spozycie_clear(dzienne_zapotrzebowanie, dzienna_suma):
    clear()
    Okno_spozycie(dzienne_zapotrzebowanie, dzienna_suma)


def Okno_dane_clear(dzienne_zapotrzebowanie, lista_preferencji, dane, liczba_wszystkich):
    clear()
    Okno_dane(dzienne_zapotrzebowanie, lista_preferencji, dane, liczba_wszystkich)



def Okno_lista_clear(dane, lista_preferencji, liczba_wszystkich, dzienna_suma):
    clear()
    Okno_lista(dane, lista_preferencji, liczba_wszystkich, dzienna_suma)


def Sort_okno_lista(dane, po_czym, fun_greater, fun_less, reverse, lista_preferencji, liczba_wszystkich, dzienna_suma):
    s.quickSort(dane, 0, len(dane) - 1, po_czym, fun_greater, fun_less, reverse)
    Okno_lista_clear(dane, lista_preferencji, liczba_wszystkich, dzienna_suma)


def Okno_wpisz_clear(dzienna_suma,przepisy_lista,dane, frame3):
    try:
        for item in przepisy_lista.curselection():
            wybor = int(item)
        Okno_wpisz(dzienna_suma,dane, wybor)
    except:
        Ostrzezenie = tk.Label(frame3, text="Zaznacz potrawę", fg='red')
        Ostrzezenie.grid(row=4, column=0)
    # Okno_wpisz(dzienna_suma, zaznaczony_index) to właściwa funkcja na później

def zatwierdz_ilosc_clear(dzienna_suma,wybor,dane, Okno_ilosc):
    clear()
    zatwierdz_ilosc(dzienna_suma, wybor, dane, Okno_ilosc)


def Okno_podsumowanie_clear(dzienne_zapotrzebowanie, dzienna_suma):
    clear()
    Okno_podsumowanie(dzienne_zapotrzebowanie, dzienna_suma)


def clear():
    for widgets in frame_gl.winfo_children():
        widgets.destroy()


def wyjscie(lista, dzienne_zapotrzebowanie, aktualna_suma, lista_preferencji, plik_zapotrzebowanie, plik_daty,
            plik_preferencji):
    w.stop(lista)
    p.zapisz_dane(dzienne_zapotrzebowanie, aktualna_suma, plik_zapotrzebowanie)
    p.zapisz_date(plik_daty, lista[0])
    p.zapisz_preferencje(plik_preferencji, lista_preferencji[0], lista_preferencji[1])
    exit()


# GŁÓWNE OKNO
root = tk.Tk()
root.geometry('1230x600')
root.title('Menadżer diety')

frame_gl = LabelFrame(root, bg='#D7D7D7')
frame_gl.grid(row=0, column=1, rowspan=5, columnspan=20, padx=5, pady=5)

# ZMIENNE

dane = p.zczytaj_dane('dane.csv')
liczba_wszystkich = len(dane)
s.quickSort(dane, 0, liczba_wszystkich - 1, 0, s.letter_greater, s.letter_less, reverse=False)

# odczyt zapisanych danych
if not os.path.isfile('zapotrzebowanie.csv') or not os.path.isfile('data.txt') or not os.path.isfile('preferencje.csv'):
    dzienne_zapotrzebowanie = z.Zapotrzebowanie()
    lista_preferencji = [False, False]
    Okno_dane_clear(dzienne_zapotrzebowanie, lista_preferencji, dane, liczba_wszystkich)
    dzienna_suma = z.Zapotrzebowanie()
    aktualna_data = datetime.now().strftime("%d:%m:%Y")
else:
    dzienne_zapotrzebowanie, dzienna_suma, aktualna_data = p.odczyt_zapisanych_danych('data.txt', 'zapotrzebowanie.csv')
    lista_preferencji = p.odczyt_preferencji('preferencje.csv')

dane = m.modyfikuj_dane(dane, 'preferencje.csv', liczba_wszystkich, lista_preferencji[0], lista_preferencji[1])
lista_watku = [aktualna_data, True]
T = threading.Thread(target=w.run, args=(lista_watku, dzienna_suma))
T.start()

Button_spozycie = Button(root, text='Wprowadź dane', height=7, width=40,
                         command=lambda: Okno_dane_clear(dzienne_zapotrzebowanie, lista_preferencji, dane,
                                                         liczba_wszystkich))
Button_spozycie.grid(row=0, column=0)

# Okno_dane(dzienne_zapotrzebowanie)

Button_spozycie = Button(root, text='Aktualny stan spożycia', height=7, width=40,
                         command=lambda: Okno_spozycie_clear(dzienne_zapotrzebowanie, dzienna_suma))
Button_spozycie.grid(row=1, column=0)

Button_lista_przepisow = Button(root, text='Sprawdź listę przepisów oraz zaktualizuj spożycie', height=7, width=40,
                                command=lambda: Okno_lista_clear(dane, lista_preferencji, liczba_wszystkich,
                                                                 dzienna_suma))
Button_lista_przepisow.grid(row=2, column=0)

Button_podsumowanie = Button(root, text='Podsumowanie dnia', height=7, width=40,
                             command=lambda: Okno_podsumowanie_clear(dzienne_zapotrzebowanie, dzienna_suma))
Button_podsumowanie.grid(row=3, column=0)

# WYJŚCIE Z APLIKACJI
Button_exit = Button(root, text='Zapisz i wyjdź', height=7, width=40,
                     command=lambda: wyjscie(lista_watku, dzienne_zapotrzebowanie, dzienna_suma, lista_preferencji,
                                             "zapotrzebowanie.csv", "data.txt", "preferencje.csv"))
Button_exit.grid(row=4, column=0)

root.mainloop()
