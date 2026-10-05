PLIK_WEJSCIOWY = "dane_tekstowe_do_sortowania.txt"
PLIK_WYJSCIOWY = "posortowane.txt"


def wczytaj_dane(nazwa_pliku):
    plik = open(nazwa_pliku, "r", encoding="utf-8")
    linie = plik.readlines()
    plik.close()

    dane = []
    for linia in linie:
        tekst = linia.strip()
        if tekst != "":
            dane.append(tekst)
    return dane


def wyswietl_menu():
    print()
    print("1. Wyświetl dane")
    print("2. Posortuj dane")
    print("3. Zakończ program")
    wybor = input("Wybierz opcję (1-3): ")
    return wybor.strip()


def wyswietl_dane(dane):
    print()
    print("Zawartość pliku " + PLIK_WEJSCIOWY + ":")
    numer = 1
    for element in dane:
        print(str(numer) + ". " + element)
        numer = numer + 1


def posortuj_dane(dane):
    posortowane = dane.copy()
    posortowane.sort()
    return posortowane


def zapisz_dane(dane, nazwa_pliku):
    plik = open(nazwa_pliku, "w", encoding="utf-8")
    for element in dane:
        plik.write(element + "\n")
    plik.close()


def main():
    dane = wczytaj_dane(PLIK_WEJSCIOWY)
    print("Wczytano " + str(len(dane)) + " pozycji z pliku " + PLIK_WEJSCIOWY + ".")

    dziala = True
    while dziala:
        wybor = wyswietl_menu()

        if wybor == "1":
            wyswietl_dane(dane)
        elif wybor == "2":
            posortowane = posortuj_dane(dane)
            zapisz_dane(posortowane, PLIK_WYJSCIOWY)
            print()
            print("Dane po sortowaniu:")
            for element in posortowane:
                print(element)
            print("Zapisano do pliku " + PLIK_WYJSCIOWY + ".")
        elif wybor == "3":
            print("Koniec programu.")
            dziala = False
        else:
            print("Nieprawidłowa opcja. Wpisz 1, 2 lub 3.")


main()