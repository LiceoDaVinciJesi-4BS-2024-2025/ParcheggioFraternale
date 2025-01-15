# Lorenzo Fraternale
# 4BS
# Esercizi OOP: Parcheggio

# Livello 1
from veicolo import Veicolo
class Auto(Veicolo):
    def __init__(self,targa:str,marca="",modello ="",colore="",cilindrata=0,alimentazione="",passeggeri=0,kgDiMerce=0):
        super().__init__(targa,marca,modello,colore,cilindrata,alimentazione)
        self.__passeggeriMassimi = 4
        if passeggeri > self.__passeggeriMassimi:
            raise ValueError("Troppi passeggeri (l'autista non è un passeggero)")
        self.__passeggeri = abs(passeggeri)
        self.__kgDiMerceMassimi = 100
        if kgDiMerce > self.__kgDiMerceMassimi:
            raise ValueError("Carico troppo pesante")
        self.__kgDiMerce = abs(kgDiMerce)
    
    @property
    def passeggeriMassimi(self):
        return self.__passeggeriMassimi
        
    @property
    def passeggeri(self):
        return self.__passeggeri
        
    @property
    def kgDiMerceMassimi(self):
        return self.__kgDiMerceMassimi
    
    @property
    def kgDiMerce(self):
        return self.__kgDiMerce
    
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    
    def __repr__(self):
        return str(self.__dict__)

if __name__ == "__main__":
    laMiaMacchina = Auto("ZZ999ZZ","Ferrari","296GTS","rosso",9999900,"Benzina",0,0)
    print(laMiaMacchina)