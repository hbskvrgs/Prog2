from klasygry import *

class Gra:
    def __init__(self):
        self.talia = None
        self.stosy_robocze = []
        self.stosy_koncowe = {}
        self.stos_dobierania = None
        self.stos_odrzuconych = None
        self.nowa_gra()
        
    def nowa_gra(self):
        self.talia = Talia()
        self.talia.tasuj()
        self.stosy_robocze = []
        for i in range(7):
            stos=StosRoboczy()
            self.stosy_robocze.append(stos)
        for kolor in Kolor:
            stos=StosKoncowy(kolor)
            self.stosy_koncowe[kolor]=stos
        self.stos_dobierania = StosDobierania()
        self.stos_odrzuconych = StosOdrzuconych()
        self.rodzaj_karty()
        
    def rozdaj_karty(self):
        s=0
        while s<7:
            k=0
            while k<=s:
                karta=self.talia.dobierz()
                self.stosy_robocze[s].dodaj(karta)
                k=k+1
            s=s+1
            

    def dobierz_karte(self):

    def odnow_stos_dobierania(self):

    def przenies_odrzucona_na_roboczy(self):

    def przenies_odrzucona_na_koncowy(self):

    def przenies_roboczy_na_koncowy(self):

    def przenies_roboczy_na_roboczy(self):

    def przenies_koncowy_na_roboczy(self):

    def czy_wygrana(self):
