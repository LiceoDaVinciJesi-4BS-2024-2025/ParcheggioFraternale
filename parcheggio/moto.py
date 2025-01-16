# Lorenzo Fraternale
# 4BS
# Esercizi OOP: Parcheggio

# Livello 1
from veicolo import Veicolo
class Moto(Veicolo):
    def __init__(self,targa:str,marca="",modello ="",colore="",cilindrata=0,alimentazione="",passeggeri=0,kgDiMerce=0):
        super().__init__(targa,marca,modello,colore,cilindrata,alimentazione)
        self.__passeggeriMassimi = 1
        if passeggeri > self.__passeggeriMassimi:
            raise ValueError("Troppi passeggeri (l'autista non è un passeggero)")
        self.__passeggeri = abs(passeggeri)
        self.__kgDiMerceMassimi = 7
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
    laMiaMoto = Moto("ZZ999ZZ","Ferrari","Moto","rosso",9999900,"Benzina",0,0)
    print(laMiaMoto)
    print(laMiaMoto.targa)
    print(laMiaMoto.marca)
    print(laMiaMoto.modello)
    print(laMiaMoto.colore)
    print(laMiaMoto.cilindrata)
    print(laMiaMoto.alimentazione)
    print(laMiaMoto.passeggeri)
    print(laMiaMoto.kgDiMerce)
    