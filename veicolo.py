# Lorenzo Fraternale
# 4BS
# Esercizi OOP: Parcheggio

# Livello 0
class Veicolo:
    def __init__(self,targa:str,marca="",modello ="",colore="",cilindrata=0,alimentazione=""):
        marche = ["Ferrari","Mercedes","Lotus","Lamborghini","Audi","Fiat","Volkswagen"]
        if targa[0] and targa[1] in "ABCDEFGHIJKLMNOPQRSTUVWQYZ":
            if targa[2] and targa[3] and targa[4] in "0123456789":
                if targa[5] and targa[6] in "ABCDEFGHIJKLMNOPQRSTUVWQYZ":
                    self.__targa = targa
        else:
            raise ValueError("Targa non valida")
        if marca in marche:
            self.__marca = marca
        else:
            raise ValueError("Marca inesistente")
        colori = ["rosso","blu","nero","grigio","bianco","verde"]
        if colore in colori:
            self.__colore = colore
        else:
            raise ValueError("Colore inesistente")
        if cilindrata % 100 == 0:
            self.__cilindrata = cilindrata
        else:
            raise ValueError("Cilindrata inesistente")
        if alimentazione not in ["Benzina","Gasolio","Metano","Elettrico"]:
            raise ValueError("Alimentazione inesistente")
        else:
            self.__alimetazione = alimentazione
        
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

