# Lorenzo Fraternale
# 4BS
# Esercizi OOP: Parcheggio

# Livello 0
class Veicolo:
    def __init__(self,targa:str,marca="",modello ="",colore="",cilindrata=0,alimentazione=""):
        marche = ["Ferrari","Mercedes","Lotus","Lamborghini","Audi","Fiat","Volkswagen"]
        if targa[0] in "ABCDEFGHIJKLMNOPQRSTUVWQYZ" and targa[1] in "ABCDEFGHIJKLMNOPQRSTUVWQYZ":
            if targa[2] in "0123456789" and targa[3] in "0123456789" and targa[4] in "0123456789":
                if targa[5] in "ABCDEFGHIJKLMNOPQRSTUVWQYZ" and targa[6] in "ABCDEFGHIJKLMNOPQRSTUVWQYZ":
                    self.__targa = targa
        else:
            raise ValueError("Targa non valida")
        if marca in marche or marca == "":
            self.__marca = marca
        else:
            raise ValueError("Marca inesistente")
        self.__modello = modello
        colori = ["rosso","blu","nero","grigio","bianco","verde"]
        if colore in colori or colore == "":
            self.__colore = colore
        else:
            raise ValueError("Colore inesistente")
        if cilindrata % 100 == 0:
            self.__cilindrata = cilindrata
        else:
            raise ValueError("Cilindrata inesistente")
        if alimentazione not in ["Benzina","Gasolio","Metano","Elettrico",""]:
            raise ValueError("Alimentazione inesistente")
        self.__alimentazione = alimentazione
        
    @property
    def targa(self):
        return self.__targa
    
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modello(self):
        return self.__modello
    
    @property
    def colore(self):
        return self.__colore
    
    @property
    def cilindrata(self):
        return self.__cilindrata
    
    @property
    def alimentazione(self):
        return self.__alimentazione
    
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    
    def __repr__(self):
        return str(self.__dict__)
    
    def __lt__(self,other):
        if self.__marca < other.marca:
            return True
        elif self.__marca == other.marca:
            if self.__modello < other.modello:
                return True
            elif self.__modello == other.modello:
                if self.__cilindrata < other.cilindrata:
                    return True
        return False
    

if __name__ == "__main__":
    ilMioVeicolo1 = Veicolo("ZZ999ZZ","Ferrari","296GTS","rosso",7000000,"Benzina")
    ilMioVeicolo2 = Veicolo("ZZ999ZZ","Audi","296GTS","blu",75643489900,"Benzina")
    lista = [ilMioVeicolo1,ilMioVeicolo2]
    lista.sort()
    print("\nC",lista)
    print(ilMioVeicolo1)
    print(ilMioVeicolo1)
    print(ilMioVeicolo1.targa)
    print(ilMioVeicolo1.marca)
    print(ilMioVeicolo1.modello)
    print(ilMioVeicolo1.colore)
    print(ilMioVeicolo1.cilindrata)
    print(ilMioVeicolo1.alimentazione)
    print(ilMioVeicolo1 < ilMioVeicolo2)
