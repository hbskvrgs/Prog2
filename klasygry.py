import random
from enum import Enum


class Kolor(Enum):
    KIER="kier"
    KARO="karo"
    TREFL="trefl"
    PIK="pik"

class Figura(Enum):
    AS=1
    DWA=2
    TRZY=3
    CZTERY=4
    PIEC=5
    SZESC=6
    SIEDEM=7
    OSIEM=8
    DZIEWIEC=9
    DZIESIEC=10
    WALET=11
    DAMA=12
    KROL=13

class Karta:
    def __init__(self, kolor, figura):
        self.kolor = kolor
        self.figura = figura
        self.odkryta = False
        
    @property
    def barwa(self):
        if self.kolor in (Kolor.TREFL, Kolor.PIK):
            return "czarny"
        return "czerwony"
        
    def odwroc(self):
        self.odkryta = not self.odkryta

    def odkryj(self):
        self.odkryta = True

    def zakryj(self):
        self.odkryta = False
        
    def __str__(self):
        if not self.odkryta:
            return "XX"
        nazwy_figur = {
            Figura.AS: "A",
            Figura.WALET: "J",
            Figura.DAMA: "Q",
            Figura.KROL: "K"
        }
        figura = nazwy_figur.get(
            self.figura,
            str(self.figura.value)
        )
        return f"{figura} {self.kolor.value}"

    def __repr__(self):
        return self.__str__()

class Talia:
    def __init__(self):
        self.karty = []
        for kolor in Kolor:
            for figura in Figura:
                karta=Karta(kolor, figura)
                self.karty.append(karta)
                
    def czy_pusta(self):
        return len(self.karty) == 0

    def __len__(self):
        return len(self.karty)
        
    def dobierz(self):
        if self.czy_pusta():
            return None
        return self.karty.pop()
         
    def tasuj(self):
        random.shuffle(self.karty)


class Stos:
    def __init__(self):
        self.karty = []
        
    def dodaj(self, karta):
        self.karty.append(karta)

    def zdejmij(self):
        if self.czy_pusty():
            return None

        return self.karty.pop()

    def wierzchnia(self):
        if self.czy_pusty():
            return None

        return self.karty[-1]

    def czy_pusty(self):
        return len(self.karty)==0

    def wyczysc(self):
        self.karty.clear()

    def __len__(self):
        return len(self.karty)

    def __str__(self):
        return " | ".join(
            str(karta)
            for karta in self.karty
        )
    
class StosRoboczy(Stos):
    def __init__(self):
        super().__init__()
    def czy_mozna_dodac(self, karta):
        if karta is None:
            return False
        if not karta.odkryta:
            return False
        if self.czy_pusty():
            return karta.figura == Figura.KROL
        wierzchnia_karta = self.wierzchnia()
        if not wierzchnia_karta.odkryta:
            return False
        poprawna_wartosc = (
            wierzchnia_karta.figura.value
            == karta.figura.value + 1
        )
        inna_barwa = (
            wierzchnia_karta.barwa
            != karta.barwa
        )
        return poprawna_wartosc and inna_barwa

    @staticmethod
    def czy_poprawna_sekwencja(karty):
        if not karty:
            return False
        for karta in karty:
            if not karta.odkryta:
                return False
        for i in range(len(karty) - 1):
            aktualna = karty[i]
            nastepna = karty[i + 1]
            poprawna_wartosc = (
                aktualna.figura.value
                == nastepna.figura.value + 1
            )
            inna_barwa = (
                aktualna.barwa
                != nastepna.barwa
            )
            if not poprawna_wartosc:
                return False
            if not inna_barwa:
                return False
        return True

    def czy_mozna_dodac_sekwencje(self, karty):
        if not karty:
            return False
        if not self.czy_poprawna_sekwencja(karty):
            return False
        pierwsza_karta = karty[0]
        return self.czy_mozna_dodac(pierwsza_karta)

    def pobierz_sekwencje(self, indeks):
        if indeks < 0:
            return []
        if indeks >= len(self.karty):
            return []
        sekwencja = self.karty[indeks:]
        if not self.czy_poprawna_sekwencja(sekwencja):
            return []
        return sekwencja

    def usun_sekwencje(self, indeks):
        sekwencja = self.pobierz_sekwencje(indeks)
        if not sekwencja:
            return []
        self.karty = self.karty[:indeks]
        return sekwencja

    def dodaj_sekwencje(self, karty):
        if not self.czy_mozna_dodac_sekwencje(karty):
            return False
        self.karty.extend(karty)
        return True

    def odkryj_wierzchnia(self):
        if self.czy_pusty():
            return False
        karta = self.wierzchnia()
        if karta.odkryta:
            return False
        karta.odkryj()
        return True
    
class StosKoncowy(Stos):
    def __init__(self, kolor):
        super().__init__()
        self.kolor = kolor
        
    def czy_mozna_dodac(self, karta):
        if karta is None:
            return False
        if not karta.odkryta:
            return False
        if karta.kolor != self.kolor:
            return False
        if self.czy_pusty():
            return karta.figura == Figura.AS
        wierzchnia_karta = self.wierzchnia()
        return (karta.figura.value== wierzchnia_karta.figura.value + 1)

    def dodaj_karte(self, karta):
        if not self.czy_mozna_dodac(karta):
            return False
        self.karty.append(karta)
        return True

    def czy_pelny(self):
        return len(self.karty) == 13
    
class StosDobierania(Stos):
    def __init__(self):
        super().__init__()
        
    def dodaj(self, karta):
        if karta is None:
            return 
        karta.zakryj()
        self.karty.append(karta)

    def dobierz(self):
        if self.czy_pusty():
            return None
        return self.karty.pop()

class StosOdrzuconych(Stos):
    def __init__(self):
        super().__init__()
        
    def dodaj(self, karta):
        if karta is None:
            return
        karta.odkryj()
        self.karty.append(karta)

    def dostepna_karta(self):
        return self.wierzchnia()
        
    
