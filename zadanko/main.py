PLIK_WEJSCIOWY = "dane_tekstowe_do_sortowania.txt"
PLIK_WYJSCIOWY = "dane_tekstowe_po_sortowaniu.txt"

def wczytaj_dane(nazwa_pliku):
    plik = open(nazwa_pliku)
    linie = plik.readlines()
    plik.close()

    dane = []
    for linia in linie:
        tekst = linia.strip()
        if tekst != "":
            dane.append(tekst)
    return dane


def wyswietl_dane():
    print()
    print("1. Wyswietl dane")
    print("2. Posortuj dane")
    print("3. Zakoncz program")
    wybor = input("Wybierz 1-2-3")
    return wybor.strip()

def wyswietl_dane(dane):
    print("Zawartosc pliku: " + PLIK_WEJSCIOWY)
    numer = 1
    for element in dane:
        print(str(numer) + element)
        numer = numer + 1

def posortuj_dane(dane):
    posortowane = dane.copy()
    posortowane.sort()
    return posortowane

def zapisz_dane(dane, nazwa_pliku):
    plik = open(nazwa_pliku, "r")
    for element in dane:
        plik.write(element, "w")
    plik.close()