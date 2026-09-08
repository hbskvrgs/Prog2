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
        
    @property
    def barwa(self):
        if self.kolor in (Kolor.TREFL, Kolor.PIK):
            return "czarny"
        return "czerwony"

class Talia:

class Stos:
    
class StosRoboczy(Stos):
    
class StosKoncowy(Stos):
    
class StosDobierania(Stos):
    
