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
    
class StosRoboczy(Stos):
    def __init__(self):
        super().__init__()
    
class StosKoncowy(Stos):
    def __init__(self, kolor):
        super().__init__()
        self.kolor = kolor
    
class StosDobierania(Stos):
    def __init__(self):
        super().__init__()
        
    
