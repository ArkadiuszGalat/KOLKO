#%%
class Kot:
    def __init__(self) -> None:
        self.imie=''
        self.kolorOczu=''
        self.siersc=''
        self.dlug=0
        self.waga=0
    def miaucz():
        print("Miau!!")
    def spanie(self):
        if self.waga<=10:
            print('spi 1 godzinę')
        elif self.waga > 10:
            print('śpi 3 godziny')
    def jedzenie(self):
        if self.waga >=16:
            print('Kot nie jest w stanie więcej jeść!!!!')
        else:
            self.waga+=1
            print('kot zjadł 1 posiłek')
        
