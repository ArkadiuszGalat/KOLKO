#%%
class Zwierze:
    def __init__(self,nazwa, wiek, waga) -> None:
        self.nazwa=nazwa
        self.waga=waga
        self.wiek=wiek
    def podaj_dane(self):
        print(f'Jestem {self.nazwa}. Mam {self.wiek} lat i ważę {self.waga}.')
class Slon(Zwierze):
    pass
class Lew(Zwierze):
    def __init__(self):
        self.iloscKlow=4

class Papuga(Zwierze):
    def __init__(self,nazwa,dlg_skrzydel):
        self.iloscPior=4000
        self.nazwa=nazwa
        self.dlg_skrzydel=dlg_skrzydel
class Hybryda(Lew,Papuga):
    pass
hyb=Hybryda()
hyb.iloscKlow=2


Dumbo=Slon('Słonik Dumbo', 300, 4)
# Dumbo.nazwa='Słonik Dumbo'
# Dumbo.waga=300
# Dumbo.wiek=4

Simba=Lew()
Simba.iloscKlow=3
Simba.wiek=34
Simba.waga=300
Simba.nazwa="Simba lew"

Simba.podaj_dane()
Dumbo.podaj_dane()
