# Lorenzo Fraternale
# 4BS
# Esercizi OOP: Parcheggio

# Livello 2
class PostoMezzo:
    from veicolo import Veicolo
    import datetime
    def __init__(self,tipoVeicolo):
        if tipoVeicolo in ("auto","moto"):
            self.__tipoVeicolo = tipoVeicolo
            self.__targaMezzoParcheggiato = ""
            self.__dataTermineMezzoParcheggiato = 0
    
    @property
    def tipoVeicolo(self):
        return self.__tipoVeicolo
    
    @property
    def targaMezzoParcheggiato(self):
        return self.__targaMezzoParcheggiato
    
    @property
    def oraTermineMezzoParcheggiato(self):
        return self.__oraTermineMezzoParcheggiato
        
    
    def parcheggia(self,targa,dataTermineParcheggio):
        if self.__targaMezzoParcheggiato == "":
            if targa[0] in "ABCDEFGHIJKLMNOPQRSTUVWQYZ" and targa[1] in "ABCDEFGHIJKLMNOPQRSTUVWQYZ":
                if targa[2] in "0123456789" and targa[3] in "0123456789" and targa[4] in "0123456789":
                    if targa[5] in "ABCDEFGHIJKLMNOPQRSTUVWQYZ" and targa[6] in "ABCDEFGHIJKLMNOPQRSTUVWQYZ":
                        self.__targaMezzoParcheggiato = targa
            else:
                raise ValueError("Targa non valida")
            self.__dataTermineMezzoParcheggiato = dataTermineParcheggio
        return
    
    def __str__(self):
        return f"Posto {self.__tipoVeicolo}, {self.__targaMezzoParcheggiato}, {self.__dataTermineMezzoParcheggiato}"

if __name__ == "__main__":
    postoAuto1 = PostoMezzo("auto")
    print(postoAuto1)