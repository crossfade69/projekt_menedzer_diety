import csv
from biblioteki import zapotrzebowanie as z
from biblioteki.watki import porownaj_daty
from datetime import datetime

def zczytaj_dane(plik):
    with open(plik) as plikCSV:
        czytnikCSV = csv.reader(plikCSV, delimiter=';')

        # wczytanie nazw kolumn
        pola = tuple(next(czytnikCSV))

        # wczytanie danych
        wiersze = [wiersz for wiersz in czytnikCSV if wiersz]

        for i in range(0,len(wiersze)):
            wiersze[i][1] = float(wiersze[i][1])
            wiersze[i][2] = float(wiersze[i][2])
            wiersze[i][3] = float(wiersze[i][3])
            wiersze[i][4] = float(wiersze[i][4])
            wiersze[i][5] = bool(int(wiersze[i][5]))
            wiersze[i][6] = bool(int(wiersze[i][6]))
            wiersze[i] = tuple(wiersze[i])

    return wiersze



def odczyt_zapisanej_daty(plik_daty):
    with open(plik_daty) as plikDaty:
        data = plikDaty.read()
    return data


def odczyt_preferencji(plik_preferencji):
    with open(plik_preferencji) as plikCSV:
        czytnikCSV = csv.reader(plikCSV, delimiter=',')
        lista = [wiersz for wiersz in czytnikCSV if wiersz]

    lista_preferencji = []
    lista_preferencji.append(bool(int(lista[1][0])))
    lista_preferencji.append(bool(int(lista[1][1])))
    return lista_preferencji


def odczyt_zapisanych_danych(plik_daty, plik):

    with open(plik_daty) as plikDaty:
        data = plikDaty.read()

    with open(plik) as plikCSV:
        czytnikCSV = csv.reader(plikCSV, delimiter=',')

        lista = [wiersz for wiersz in czytnikCSV if wiersz]
        # wczytanie dziennego zapotrzebowania
        dzienne_zapotrzebowanie = z.Zapotrzebowanie(kcal=float(lista[1][0]), bialka=float(lista[1][1]),
                                                  tluszcze=float(lista[1][2]), weglowodany=float(lista[1][3]))

        # wczytanie aktualnego stanu
        if porownaj_daty(data):
            aktualny_stan = z.Zapotrzebowanie(kcal=float(lista[2][0]), bialka=float(lista[2][1]),
                                            tluszcze=float(lista[2][2]), weglowodany=float(lista[2][3]))

            return dzienne_zapotrzebowanie, aktualny_stan, data
        else:
            aktualny_stan = z.Zapotrzebowanie()
            aktualna_data = datetime.now().strftime("%d:%m:%Y")
            return dzienne_zapotrzebowanie, aktualny_stan, aktualna_data


def zapisz_dane(dzienne_zapotrzebowanie, aktualny_stan, plik):
    with open(plik, mode='w') as plikCSV:
        pola = ['Kalorie', 'Białka', 'Tłuszcze', 'Węglowodany']
        lista = [{'Kalorie': dzienne_zapotrzebowanie.get_kalorie(), 'Białka': dzienne_zapotrzebowanie.get_bialka(), 'Tłuszcze': dzienne_zapotrzebowanie.get_tluszcze(),
                'Węglowodany': dzienne_zapotrzebowanie.get_weglowodany()}, {'Kalorie': aktualny_stan.get_kalorie(), 'Białka': aktualny_stan.get_bialka(),
                'Tłuszcze': aktualny_stan.get_tluszcze(), 'Węglowodany': aktualny_stan.get_weglowodany()}]
        writer = csv.DictWriter(plikCSV, fieldnames=pola)

        writer.writeheader()
        for x in lista:
            writer.writerow(x)


def zapisz_date(plik_daty, data):
    with open(plik_daty, mode='w') as plikDaty:
        plikDaty.write(data)


def zapisz_preferencje(plik_preferencji,isVegetarian, isVegan):
    with open(plik_preferencji, mode='w') as plikCSV:
        pola = ['Wegetarianin','Weganin']
        lista = [{pola[0]: int(isVegetarian), pola[1]: int(isVegan)}]
        writer = csv.DictWriter(plikCSV, fieldnames=pola)

        writer.writeheader()
        for x in lista:
            writer.writerow(x)