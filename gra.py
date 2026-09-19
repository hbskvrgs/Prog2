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
        self.rozdaj_karty()
        
    def rozdaj_karty(self):
        s=0
        while s<7:
            k=0
            while k<=s:
                karta=self.talia.dobierz()
                if k==s:
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
        if self.stos_odrzuconych.czy_pusty():
            return False
        while not self.stos_odrzuconych.czy_pusty():
            karta= self.stos_odrzuconych.zdejmij()
            self.stos_dobierania.dodaj(karta)
        return True

    def przenies_odrzucona_na_roboczy(self, s):
        if s<0:
            return False
        if s>=7:
            return False
        if self.stos_odrzuconych.czy_pusty():
            return False
        karta = self.stos_odrzuconych.wierzchnia()
        stos_docelowy = self.stosy_robocze[s]
        mozna= stos_docelowy.czy_mozna_dodac(karta)
        if mozna==False:
            return False
        karta = self.stos_odrzuconych.zdejmij()
        stos_docelowy.dodaj(karta)
        return True

    def przenies_odrzucona_na_koncowy(self):
        if self.stos_odrzuconych.czy_pusty():
            return False
        karta = self.stos_odrzuconych.wierzchnia()
        stos_koncowy = self.stosy_koncowe[karta.kolor]
        if not stos_koncowy.czy_mozna_dodac(karta):
            return False
        karta = self.stos_odrzuconych.zdejmij()
        stos_koncowy.dodaj_karte(karta)
        return True

    def przenies_roboczy_na_koncowy(self,s):
        if s<0:
            return False
        if s>=7:
            return False
        stos_roboczy = self.stosy_robocze[s]
        if stos_roboczy.czy_pusty():
            return False
        karta = stos_roboczy.wierzchnia()
        stos_koncowy = self.stosy_koncowe[karta.kolor]
        if not stos_koncowy.czy_mozna_dodac(karta):
            return False
        stos_roboczy.zdejmij()
        stos_koncowy.dodaj_karte(karta)
        stos_roboczy.odkryj_wierzchnia()
        return True

    def przenies_roboczy_na_roboczy(self,s_zrodlowy,idx,s_docelowy):
        if s_zrodlowy<0:
            return False
        if s_zrodlowy>=7:
            return False
        if s_docelowy<0:
            return False
        if s_docelowy>=7:
            return False
        if s_zrodlowy==s_docelowy:
            return False
        zrodlo = self.stosy_robocze[s_zrodlowy]
        cel = self.stosy_robocze[s_docelowy]
        sekwencja = zrodlo.pobierz_sekwencje(idx)
        if len(sekwencja)==0:
            return False
        mozna= cel.czy_mozna_dodac_sekwencje(sekwencja)
        if mozna==False:
            return False
        sekwencja = zrodlo.usun_sekwencje(idx)
        for karta in sekwencja:
            cel.karty.append(karta)
        zrodlo.odkryj_wierzchnia()
        return True

    def przenies_koncowy_na_roboczy(self, kolor,s):
        if s<0:
            return False
        if s>=7:
            return False
        stos_koncowy = self.stosy_koncowe[kolor]
        stos_roboczy = self.stosy_robocze[s]
        if stos_koncowy.czy_pusty():
            return False
        karta = stos_koncowy.wierzchnia()
        mozna= stos_roboczy.czy_mozna_dodac(karta)
        if mozna==False:
            return False
        stos_koncowy.zdejmij()
        stos_roboczy.dodaj(karta)
        return True
        

    def czy_wygrana(self):
        for kolor in Kolor:
            s=self.stosy_koncowe[kolor]
            if s.czy_pelny()==False:
                return False
        return True
