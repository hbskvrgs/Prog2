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
                if numer_karty==numer_stosu:
                    karta.odkryj()
                else:
                    karta.zakryj()
                self.stosy_robocze[s].dodaj(karta)
                k=k+1
            s=s+1
        while not self.talia.czy_pusta():
            karta=self.talia.dobierz()
            self.stos_dobierania.dodaj(karta)
            

    def dobierz_karte(self):
        if self.stos_dobierania.czy_pusty():
            return self.odnow_stos_dobierania()
        karta=self.stos_dobierania.dobierz()
        self.stos_odrzuconych.dodaj(karta)
        return True

    def odnow_stos_dobierania(self):
        if sekf.stos_odrzuconych.czy_pusty():
            return False
        while not self.stos_odrzuconych.czy_pusty():
            karta= self.stos_odrzuconych.zdejmij()
            self.stos_dobierania.dodaj(karta)
        return True

    def przenies_odrzucona_na_roboczy(self, s):
        karta = self.stos_odrzuconych.wierzchnia()
        stos_docelowy = self.stosy_robocze[numer_stosu]
        mozna= stos_docelowy.czy_mozna_dodac(karta):
        if mozna==False:
            return False
        karta = self.stos_odrzuconych.zdejmij()
        stos_docelowy.dodaj(karta)
        return True

    def przenies_odrzucona_na_koncowy(self):

    def przenies_roboczy_na_koncowy(self):

    def przenies_roboczy_na_roboczy(self):

    def przenies_koncowy_na_roboczy(self):

    def czy_wygrana(self):
