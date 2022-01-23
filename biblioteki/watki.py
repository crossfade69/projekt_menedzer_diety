from datetime import datetime
from time import sleep
#from biblioteki import zapotrzebowanie as z
# Funkcje związane z wątkiem działającym w tle

def porownaj_daty(data):
    if datetime.now().strftime("%d:%m:%Y") == data:
        return True
    else:
        return False

# funkcja, która będzie działać na oddzielnym wątku. Co sekundę będzie sprawdzać datę i w przypadku jej zmiany, zostanie modyfikacja daty.
# lista_wątku zawiera odpowiedzio: Indeks 0 to data, indeks 1 to zmienna boolean, odpowiedzialna za działanie pętli while. A więc odpowiada za działanie wątku.
def run(lista_watku, aktualna_suma):
    while lista_watku[1]:
        if not porownaj_daty(lista_watku[0]):
            lista_watku[0] = datetime.now().strftime("%d:%m:%Y")
            aktualna_suma.wyczysc()
        sleep(1)

# funkcja stop() zmieni wartość boolean zmiennej pod indeksem 1 w lista_watku na wartość False, co spowoduje przerwanie pętli while, co spowoduje zakończenie działania
#funkcji run(), to spowoduje zakończenie działania wątku. Funkcja stop() zostaje użyta przy zakończeniu całego programu
def stop(lista_watku):
    lista_watku[1] = False


