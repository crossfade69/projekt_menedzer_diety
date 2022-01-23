import string

alfabet_polski = {'a': 1, 'ą': 2, 'b': 3, 'c': 4, 'ć': 5, 'd': 6, 'e': 7, 'ę': 8, 'f': 9, 'g': 10, 'h': 11,
            'i': 12, 'j': 13, 'k': 14, 'l': 15, 'ł': 16, 'm': 17, 'n': 18, 'ń': 19, 'o': 20, 'ó': 21, 'p': 22,
            'q': 23, 'r': 24, 's': 25, 'ś': 26, 't': 27, 'u': 28, 'v': 29, 'w': 30, 'x': 31, 'y': 32, 'z': 33,
            'ź': 34, 'ż': 35, 'A': 1, 'Ą': 2, 'B': 3, 'C': 4, 'Ć': 5, 'D': 6, 'E': 7, 'Ę': 8, 'F': 9, 'G': 10,
            'H': 11, 'I': 12, 'J': 13, 'K': 14, 'L': 15, 'Ł': 16, 'M': 17, 'N': 18, 'Ń': 19, 'O': 20, 'Ó': 21, 'P': 22,
            'Q': 23, 'R': 24, 'S': 25, 'Ś': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 30, 'X': 31, 'Y': 32, 'Z': 33,
            'Ź': 34, 'Ż': 35,
            '0': -9, '1': -8, '2': -7, '3': -6, '4': -5, '5': -4, '6': -3, '7': -2, '8': -1, '9': 0}

def letter_greater(string1, string2):

    dlugosc_string1 = len(string1)
    dlugosc_string2 = len(string2)
    i = 0
    j = 0
    while i < dlugosc_string1 and j < dlugosc_string2:
        #znaki specjalne
        if string1[i] == ' ' and string2[j] == ' ':
            i += 1
            j += 1
        elif string1[i] == ' ' or string2[j] == ' ':
            break
        elif string1[i] in string.punctuation:
            i += 1
        elif string2[j] in string.punctuation:
            j += 1
        elif alfabet_polski[string1[i]] == alfabet_polski[string2[j]]:
            i += 1
            j += 1
        elif alfabet_polski[string1[i]] < alfabet_polski[string2[j]]:
            return True
        else:
            return False

    if i == dlugosc_string1 and dlugosc_string1 < dlugosc_string2:
        return True
    else:
        return False



def letter_less(string1, string2):
    dlugosc_string1 = len(string1)
    dlugosc_string2 = len(string2)
    i = 0
    j = 0
    while i < dlugosc_string1 and j < dlugosc_string2:
        if string1[i] in string.punctuation:
            i += 1
        elif string2[j] in string.punctuation:
            j += 1
        elif string1[i] == ' ' and string2[j] == ' ':
            i += 1
            j += 1
        elif string1[i] == ' ' or string2[j] == ' ':
            break
        elif alfabet_polski[string1[i]] == alfabet_polski[string2[j]]:
            i += 1
            j += 1
        elif alfabet_polski[string1[i]] > alfabet_polski[string2[j]]:
            return True
        else:
            return False

    if j == dlugosc_string2 and dlugosc_string1 > dlugosc_string2:
        return True
    else:
        return False

def digits_greater(number1, number2):
    if number1 < number2:
        return True
    else:
        return False

def digits_less(number1, number2):
    if number1 > number2:
        return True
    else:
        return False


def ustal_piwot(tab, pocz, kon, po_czym):
    from random import randint
    return tab[randint(pocz, kon)][po_czym]


def podziel(tab, pocz, kon, piwot, po_czym, fun_greater, fun_less, reverse):
    i = pocz
    j = kon
    if not reverse:
        while True:
            while fun_greater(tab[i][po_czym], piwot):
                i += 1
            while fun_less(tab[j][po_czym], piwot):
                j -= 1
            if i >= j:
                return j
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
            j -= 1
    else:
        while True:
            while fun_less(tab[i][po_czym], piwot):
                i += 1
            while fun_greater(tab[j][po_czym], piwot):
                j -= 1
            if i >= j:
                return j
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
            j -= 1


def quickSort(tab, pocz, kon, po_czym, fun_greater, fun_less, reverse=False):
    if kon > pocz:
        piwot = ustal_piwot(tab, pocz, kon, po_czym)
        sr = podziel(tab, pocz, kon, piwot, po_czym, fun_greater, fun_less, reverse)
        quickSort(tab, pocz, sr, po_czym, fun_greater, fun_less, reverse)
        quickSort(tab, sr+1, kon, po_czym, fun_greater, fun_less, reverse)

