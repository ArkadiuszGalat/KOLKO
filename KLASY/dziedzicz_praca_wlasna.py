#%%
# symulacja zmiany pod gita test1
from _typeshed import Self


class pojazd:
    def __init__(self) -> None:
        self.ile_kół=1
        self.rodzaj_napędu='mechaniczy' #można użyć enumerate
        self.rok_prod=1900
        
class samochód(pojazd):
    def __init__(self) -> None:
        self.nadwozie = "sedan"