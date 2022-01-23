def ustal_zapotrzebowanie(waga, wzrost, wiek, plec, aktywnosc):
    # W przypadku kobiety zmienna plec ma wartość True, natomiast w przypadku mężczyzny ma wartość False
    if plec:
        kalorie = (9.6 * waga) + (1.8 * wzrost) - (4.7 * wiek) + 655
    else:
        kalorie = (13.7 * waga) + (5 * wzrost) - (6.8 * wiek) + 66
    ''' Instrukcja warunkowa pełniąca funkcje switch'a
    1 - siedzący - jeśli wykonujesz minimalne ćwiczenia lub nie wykonujesz żadnych ćwiczeń, pomnóż BMR przez 1,2
    2 - lekko aktywny - jeśli ćwiczysz lekko od jednego do trzech dni w tygodniu, pomnóż BMR przez 1,375
    3 - umiarkowanie aktywny - jeśli ćwiczysz umiarkowanie od trzech do pięciu dni w tygodniu, pomnóż BMR przez 1,55
    4 - bardzo aktywny - jeśli intensywnie ćwiczysz przez sześć do siedmiu dni w tygodniu, pomnóż swój BMR przez 1,725
    5 - ekstra aktywny - jeśli wykonujesz bardzo ciężkie ćwiczenia przez sześć do siedmiu dni w tygodniu lub wykonujesz pracę fizyczną, pomnóż BMR przez 1,9
    '''
    if aktywnosc == 1:
        kalorie = round(1.2 * kalorie, 2)
    elif aktywnosc == 2:
        kalorie = round(1.375 * kalorie, 2)
    elif aktywnosc == 3:
        kalorie = round(1.55 * kalorie, 2)
    elif aktywnosc == 4:
        kalorie = round(1.725 * kalorie, 2)
    else:
        kalorie = round(1.9 * kalorie, 2)

    bialka = round((0.15 * kalorie) / 5.65, 2)
    tluszcze = round((0.30 * kalorie) / 9.45, 2)
    weglowodany = round((0.55 * kalorie) / 4.1, 2)

    return kalorie, bialka, tluszcze, weglowodany


class Zapotrzebowanie():

    def __init__(self, waga = 0.0, wzrost = 0.0, wiek = 0, plec = False, aktywnosc = 0, kcal = 0.0, bialka = 0.0, tluszcze = 0.0, weglowodany = 0.0):
        if waga != 0 or wzrost != 0 or wiek != 0 or aktywnosc != 0:

            kalorie, bialka, tluszcze, weglowodany = ustal_zapotrzebowanie(waga, wzrost, wiek, plec, aktywnosc)

            self.__kalorie = kalorie
            self.__bialka = bialka
            self.__tluszcze = tluszcze
            self.__weglowodany = weglowodany
        else:
            self.__kalorie = kcal
            self.__bialka = bialka
            self.__tluszcze = tluszcze
            self.__weglowodany = weglowodany

    def dodaj_kalorie(self, kalorie):
        self.__kalorie += kalorie

    def dodaj_bialka(self, bialka):
        self.__bialka += bialka

    def dodaj_tluszcze(self, tluszcze):
        self.__tluszcze += tluszcze

    def dodaj_weglowodany(self, weglowodany):
        self.__weglowodany += weglowodany

    def set_kalorie(self, kalorie):
        self.__kalorie = kalorie

    def set_bialka(self, bialka):
        self.__bialka = bialka

    def set_tluszcze(self, tluszcze):
        self.__tluszcze = tluszcze

    def set_weglowodany(self, weglowodany):
        self.__weglowodany = weglowodany

    def get_kalorie(self):
        return self.__kalorie

    def get_bialka(self):
        return self.__bialka

    def get_tluszcze(self):
        return self.__tluszcze

    def get_weglowodany(self):
        return self.__weglowodany

    def wyczysc(self):
        self.__kalorie = 0.0
        self.__bialka = 0.0
        self.__tluszcze = 0.0
        self.__weglowodany = 0.0

    def modyfikacja(self, waga, wzrost, wiek, plec, aktywnosc):

        kalorie, bialka, tluszcze, weglowodany = ustal_zapotrzebowanie(waga, wzrost, wiek, plec, aktywnosc)

        self.__kalorie = kalorie
        self.__bialka = bialka
        self.__tluszcze = tluszcze
        self.__weglowodany = weglowodany


