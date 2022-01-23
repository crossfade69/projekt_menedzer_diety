from biblioteki import sortuj as s
from biblioteki import watki as w
from biblioteki import pliki as p
import threading

#Związane z menu i interfejsem

def dla_Wegan(dane):
    for i in range(len(dane)-1, -1, -1):
        if dane[i][6] == False:
            dane.pop(i)
    return dane


def dla_Wegetarian(dane):
    for i in range(len(dane)-1, -1, -1):
        if dane[i][5] == False:
            dane.pop(i)
    return dane

def dla_Wszystkich(dane, liczba_wszystkich, plik):
    if len(dane) == liczba_wszystkich:
        return dane
    else:
        odczytane = p.zczytaj_dane(plik)
        dane.clear()
        for i in range(0,len(odczytane)):
            dane.append(odczytane[i])
        return dane

def modyfikuj_dane(dane, plik, liczba_wszystkich, isWegetarian = False, isVegan = False):
    if isVegan == False and isWegetarian == False:
        return dla_Wszystkich(dane, liczba_wszystkich, plik)
    elif isVegan == True and isWegetarian == False:
        if len(dane) != liczba_wszystkich:
            dane = dla_Wszystkich(dane, liczba_wszystkich, plik)
        return dla_Wegan(dane)
    elif isVegan == False and isWegetarian == True:
        if len(dane) != liczba_wszystkich:
            dane = dla_Wszystkich(dane, liczba_wszystkich, plik)
        return dla_Wegetarian(dane)



"""

def dla_Wegan(dane):
    for i in range(len(dane)-1, -1, -1):
        if dane[i][6] == False:
            #del potrawy[i]
            dane.pop(i)


def dla_Wegetarian(dane):
    for i in range(len(dane)-1, -1, -1):
        if dane[i][5] == False:
            #del potrawy[i]
            dane.pop(i)

def dla_Wszystkich(dane, liczba_wszystkich, plik):
    if len(dane) != liczba_wszystkich:
        odczytane = p.zczytaj_dane(plik)
        dane.clear()
        for i in range(0,len(odczytane)):
            dane.append(odczytane[i])



def modyfikuj_dane(dane, plik, liczba_wszystkich, isWegetarian = False, isVegan = False):
    if isVegan == False and isWegetarian == False:
        dla_Wszystkich(dane, liczba_wszystkich, plik)
    elif isVegan == True and isWegetarian == False:
        if len(dane) != liczba_wszystkich:
            dane = dla_Wszystkich(dane, liczba_wszystkich, plik)
        dla_Wegan(dane)
    elif isVegan == False and isWegetarian == True:
        if len(dane) != liczba_wszystkich:
            dane = dla_Wszystkich(dane, liczba_wszystkich, plik)
        dla_Wegetarian(dane)

"""


def podsumowanie(dzienne_zapotrzebowanie, aktualna_suma):
    lista = []
    if (dzienne_zapotrzebowanie.get_kalorie()*0.9) >= aktualna_suma.get_kalorie():
        lista.append("Za mało kalorii")
    elif (dzienne_zapotrzebowanie.get_kalorie()*1.1) <= aktualna_suma.get_kalorie():
        lista.append("Za dużo kalorii")
    else:
        lista.append("W normie")

    # bialka
    if (dzienne_zapotrzebowanie.get_bialka()*0.9) >= aktualna_suma.get_bialka():
        lista.append("Za mało białek")
    elif (dzienne_zapotrzebowanie.get_bialka()*1.1) <= aktualna_suma.get_bialka():
        lista.append("Za dużo białek")
    else:
        lista.append("W normie")

    #tluszcze
    if (dzienne_zapotrzebowanie.get_tluszcze()*0.9) >= aktualna_suma.get_tluszcze():
        lista.append("Za mało tłuszczów")
    elif (dzienne_zapotrzebowanie.get_tluszcze()*1.1) <= aktualna_suma.get_tluszcze():
        lista.append("Za dużo tłuszczów")
    else:
        lista.append("W normie")

    #cukry
    if (dzienne_zapotrzebowanie.get_weglowodany()*0.9) >= aktualna_suma.get_weglowodany():
        lista.append("Za mało węglowodanów")
    elif (dzienne_zapotrzebowanie.get_weglowodany()*1.1) <= aktualna_suma.get_weglowodany():
        lista.append("Za dużo węglowodanów")
    else:
        lista.append("W normie")

    return lista

def dodaj_do_dziennej_sumy(aktualna_suma, kalorie, bialka, tluszcze, weglowodany):
    aktualna_suma.dodaj_kalorie(kalorie)
    aktualna_suma.dodaj_bialka(bialka)
    aktualna_suma.dodaj_tluszcze(tluszcze)
    aktualna_suma.dodaj_weglowodany(weglowodany)
