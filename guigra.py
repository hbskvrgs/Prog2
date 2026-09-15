import pygame
from gra import *
from klasygry import *

pygame.init()

szerokosc=1200
wysokosc=800
odstep = 30
ZIELONY = (20, 120, 60)
BIALY = (255, 255, 255)
CZARNY = (0, 0, 0)
CZERWONY = (200, 0, 0)
NIEBIESKI = (40, 70, 140)
SZARY = (120, 120, 120)

widok=pygame.display.set_mode((szerokosc,wysokosc))
pygame.display.set_caption("Pasjans")

czcionka = pygame.font.SysFont("arial",22)
czcionka_mala = pygame.font.SysFont("arial",18)

gra = Gra()

stos_zrodlowy = None
pozycja_karty = None
komunikat = "Wybierz stos zrodlowy 1-7"
def tekst_karty(karta):
    if karta is None:
        return ""
    wartosc = karta.figura.value
    if wartosc == 1:
        figura = "A"
    elif wartosc == 11:
        figura = "J"
    elif wartosc == 12:
        figura = "Q"
    elif wartosc == 13:
        figura = "K"
    else:
        figura = str(wartosc)
    tekst = (figura+ " "+ karta.kolor.value)
    return tekst

def rysuj_pusta_karte(x,y):
    prostokat = pygame.Rect( x,y,szerokosc_karty,wysokosc_karty)
    pygame.draw.rect(widok,SZARY,prostokat,2)

def rysuj_karte(karta,x,y):
    prostokat = pygame.Rect( x,y,szerokosc_karty,wysokosc_karty)
    if karta.odkryta == False:
        pygame.draw.rect(widok,NIEBIESKI,prostokat)
        pygame.draw.rect(widok,CZARNY,prostokat,2)
        return
    pygame.draw.rect(widok,BIALY,prostokat)
    pygame.draw.rect(widok,CZARNY,prostokat,2)
    if karta.barwa == "czerwony":
        kolor_napisu = CZERWONY
    else:
        kolor_napisu = CZARNY
    tekst = tekst_karty(karta)
    napis = czcionka.render(tekst,True,kolor_napisu)
    widok.blit(napis,(x + 8,y + 8))
  
def rysuj_napis(tekst,x,y,mala):
    if mala == True:
        napis = czcionka_mala.render(tekst,True,BIALY)
    else:
        napis = czcionka.render(tekst,True,BIALY)
    widok.blit(napis,(x,y))

def rysuj_stos_dobierania():
    rysuj_napis("Dobieranie",30,90,True)
    if gra.stos_dobierania.czy_pusty():
        rysuj_pusta_karte(30,115)
    else:
        karta = (gra.stos_dobierania.wierzchnia())
        rysuj_karte(karta,30,115)

def rysuj_stos_odrzuconych():
    rysuj_napis("Odrzucone",160,90,True)
    if gra.stos_odrzuconych.czy_pusty():
        rysuj_pusta_karte(160,115)
    else:
        karta = (gra.stos_odrzuconych.wierzchnia())
        rysuj_karte(karta,160,115)

def rysuj_stosy_koncowe():
    x = 550
    for kolor in Kolor:
        stos = (gra.stosy_koncowe[kolor])
        rysuj_napis(kolor.value,x,90,True)
        if stos.czy_pusty():
            rysuj_pusta_karte(x,115)
        else:
            karta = stos.wierzchnia()
            rysuj_karte(karta,x,115)
        x = x + 125
      
def rysuj_stosy_robocze():
    x_poczatek = 30
    y_poczatek = 320
    s = 0
    while s < 7:
        stos = (gra.stosy_robocze[s])
        x = (x_poczatek + s * 150)
        rysuj_napis(str(s + 1),x + 40,y_poczatek - 35,False)
    
        if stos.czy_pusty():
            rysuj_pusta_karte(x,y_poczatek)
        indeks = 0
        for karta in stos.karty:
            y = (y_poczatek+ indeks * odstep)
            rysuj_karte(karta,x,y)
            indeks = indeks + 1
        s = s + 1

def rysuj_gre():
    widok.fill(ZIELONY)
    rysuj_napis("D - dobierz O - odrzucone K - koncowy N - nowa gra ESC - anuluj",20,15,True)
    rysuj_napis(komunikat,20,45,False)
    rysuj_stos_dobierania()
    rysuj_stos_odrzuconych()
    rysuj_stosy_koncowe()
    rysuj_stosy_robocze()

def wyczysc_wybor():
    global stos_zrodlowy
    global pozycja_karty
    stos_zrodlowy = None
    pozycja_karty = None

dziala = True
while dziala == True:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            dziala = False
        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_d:
                wynik = (gra.dobierz_karte())
                if wynik == True:
                    komunikat = ("Dobrano karte")
                else:
                    komunikat = ("Brak kart do dobrania")

            elif zdarzenie.key == pygame.K_n:
                gra.nowa_gra()
                wyczysc_wybor()
                komunikat = (
                    "Rozpoczeto nowa gre")
              
            elif zdarzenie.key == pygame.K_ESCAPE:
                wyczysc_wybor()
                komunikat = ("Anulowano wybor")
            elif zdarzenie.key == pygame.K_o:
                if gra.stos_odrzuconych.czy_pusty():
                    komunikat = ("Stos odrzuconych jest pusty")
                else:
                    stos_zrodlowy = "odrzucony"
                    pozycja_karty = None
                    komunikat = (
                        "Wybrano odrzucone. "
                        "Wybierz 1-7 albo K")
            elif zdarzenie.key == pygame.K_k:
                if stos_zrodlowy == "odrzucony":
                    wynik = (gra.przenies_odrzucona_na_koncowy())
                    if wynik == True:
                        komunikat = ("Przeniesiono na stos koncowy")
                                                else:
                        komunikat = ("Nie mozna wykonac ruchu")
                    wyczysc_wybor()
                  
                elif stos_zrodlowy is not None:
                    wynik = (gra.przenies_roboczy_na_koncowy(stos_zrodlowy))
                    if wynik == True:
                        komunikat = ("Przeniesiono na stos koncowy")
                    else:
                        komunikat = ("Nie mozna wykonac ruchu")
                    wyczysc_wybor()
                else:
                    komunikat = ("Najpierw wybierz stos")
            elif (zdarzenie.key == pygame.K_1 or zdarzenie.key == pygame.K_2 or zdarzenie.key == pygame.K_3 or zdarzenie.key == pygame.K_4 or zdarzenie.key == pygame.K_5 or zdarzenie.key == pygame.K_6 or zdarzenie.key == pygame.K_7):
                if zdarzenie.key == pygame.K_1:
                    numer = 0
                elif zdarzenie.key == pygame.K_2:
                    numer = 1
                elif zdarzenie.key == pygame.K_3:
                    numer = 2
                elif zdarzenie.key == pygame.K_4:
                    numer = 3
                elif zdarzenie.key == pygame.K_5:
                    numer = 4
                elif zdarzenie.key == pygame.K_6:
                    numer = 5
                else:
                    numer = 6
                if stos_zrodlowy == "odrzucony":
                    wynik = (gra.przenies_odrzucona_na_roboczy(numer))
                    if wynik == True:
                        komunikat = (
                            "Przeniesiono karte "
                            "ze stosu odrzuconych")
                    else:
                        komunikat = ("Nie mozna wykonac ruchu")
                    wyczysc_wybor()
                elif stos_zrodlowy is None:
                    stos_zrodlowy = numer
                    komunikat = ("Wybrano stos "+ str(numer + 1)+ ". Wybierz pozycje karty 1-7")
                elif pozycja_karty is None:
                    pozycja_karty = numer
                    komunikat = ("Wybrano pozycje "+ str(numer + 1)+ ". Wybierz stos docelowy 1-7")
                else:
                    stos_docelowy = numer
                    wynik = (gra.przenies_roboczy_na_roboczy(stos_zrodlowy, pozycja_karty,stos_docelowy))
                    if wynik == True:
                        komunikat = ("Ruch wykonany")
                    else:
                        komunikat = ("Nie mozna wykonac ruchu")
                    wyczysc_wybor()

    if gra.czy_wygrana() == True:
        komunikat = ("Wygrana")
    rysuj_gre()
    pygame.display.flip()

pygame.quit()
