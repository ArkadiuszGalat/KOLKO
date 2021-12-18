#%%
#wersja moja
class kot:
    def __init__(self,imie1,rasa1,waga1):
        self.imie=imie1
        self.rasa=rasa1
        self.waga=waga1
    def miaucz(self):
        if self.waga>=10:
            return('Miaaaauuuuu')
        else:
            return('miau')
    def jedz(self):
        if self.waga>=10:
            return('Zjadłem 1kg karmy')
        else:
            return('Zjadłem 0,5 kg karmy')
kot_mały=kot('Filemon', 'domowy', 5)
kot_duży=kot('Bonifacy', 'domowy', 11)
print(f"{kot_mały.imie}: {kot_mały.miaucz()}.\n{kot_mały.jedz()}") 
print(f"{kot_duży.imie}: {kot_duży.miaucz()}.\n{kot_duży.jedz()}")