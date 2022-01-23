# Menedżer diety
Program ma na celu dostosować użytkownikowi na podstawie jego metryki (waga, wzrost, wiek, styl życia itd.) dzienne zapotrzebowanie składników odżywczych w celu zadbania o jego zdrowie. Ma to mieć zastosowanie w użytku codziennym, jako aplikacja pomagająca utrzymać daną dietę.
Aby tego dokonać, program wykonuje różnego rodzaju obliczenia na podstawie wprowadzonych przez użytkownika danych, takie jak obliczenie dziennego zapotrzebowania. Program pozwala też na sortowanie bazy danych (listy potraw, z przypisanymi wartościami odżywczymi oraz czy jest to danie wegetariańskie lub wegańskie) dołączonej do programu, zapisanej w formacie csv, a także resetowanie aktualnego stanu spożycia wraz z kolejnym dniem.

Dane wejściowe: 				
-wiek (int) 					 
-waga (float) 					
-wzrost (float)					 
-płeć (bool) 					 
-czy_wegetarianin (bool)			
-czy_weganin (bool) 				 
-czy_wegetarianin (bool) 
-czy_weganin (bool)

Dane wyjściowe:
-zapotrzebowanie(obiekt) zawierający:
* dzienna_suma_kalorii 
* dzienna_suma_białka,
* dzienna_suma_tłuszczy,
* dzienna_suma_cukrów
-lista potraw (obiekt potraw)

Działanie
Tak jak opisano wyżej, aby program zadziałał poprawnie muszą zostać wprowadzone dane dotyczące naszego wzrostu, wagi itd. w rubryce „Dane użytkownika”. Należy też wybrać nasz styl życia (siedzący, lekko aktywny itd.). Po wprowadzeniu danych zatwierdzamy nasze ustawienia.
W rubryce „Aktualny stan spożycia” przedstawione jest dzienne zapotrzebowanie na składniki odżywcze i kalorie naszego użytkownika oraz ile obecnie składników spożył  w ciągu dnia.
Lista przepisów pozwala na wybór danej potrawy z listy zawartej w bazie danych. Listę tą można sortować rosnąco lub malejąco względem nazwy, kalorii, ilości białek, tłuszczy lub węglowodanów. Po wybraniu potrawy należy kliknąć „wybierz”. Otwiera się wtedy okno,  w którym należy wpisać ile gramów danej potrawy zamierza zjeść użytkownik. Następnie wartości wybranej potrawy są mnożone przez spożytą ilość i są dodawane do aktualnego stanu spożycia.
„Podsumowanie” porównuje ze sobą aktualne spożycie i dzienne zapotrzebowanie, oraz pokazuje czy użytkownik poprawnie utrzymuje swoją dietę (w danych wartościach odżywczych wpisuje „za mało …”/„za dużo …”).
Opcja „Zapisz i wyjdź” zapisuje wprowadzone dane oraz dzienne spożycie. Aktualne spożycie także jest zapisywane, jednak wraz z uruchomieniem programu następnego dnia wartość ta zostanie wyzerowana.

Wykorzystane rozwiązania
Wykorzystywana baza danych jest plikiem csv, która zajmuje bardzo mało pamięci w porównaniu do pozostałych formatów. Same wartości odżywcze potraw są zapisywane w formie krotek.
Do sortowania potraw z listy służy samodzielnie stworzona funkcja „Quicksort” bazująca na algorytmie szybkiego sortowania o tej samej nazwie
