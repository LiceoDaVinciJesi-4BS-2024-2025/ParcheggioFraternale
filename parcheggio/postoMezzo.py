# Lorenzo Fraternale
# 4BS
# Esercizi OOP: Parcheggio

# Livello 2
import datetime
class PostoMezzo:
    from veicolo import Veicolo
    
    def __init__(self,tipoVeicolo):
        if tipoVeicolo in ("auto","moto"):
            self.__tipoVeicolo = tipoVeicolo
            self.__targaMezzoParcheggiato = ""
            self.__oraArrivoMezzoParcheggiato = 0
    
    @property
    def tipoVeicolo(self):
        return self.__tipoVeicolo
    
    @property
    def targaMezzoParcheggiato(self):
        return self.__targaMezzoParcheggiato
    
    @property
    def oraArrivoMezzoParcheggiato(self):
        return self.__oraArrivoMezzoParcheggiato
    
#     @tipoVeicolo.setter
#     def tipoVeicolo(self,value):
#         if value in ("moto","auto"):
#             self.__tipoVeicolo = value
#         return
    
#     @targaMezzoParcheggiato.setter
#     def targaMezzoParcheggiato(self,value):
#         if targa[0] in "ABCDEFGHIJKLMNOPQRSTUVWQYZ" and targa[1] in "ABCDEFGHIJKLMNOPQRSTUVWQYZ":
#             if targa[2] in "0123456789" and targa[3] in "0123456789" and targa[4] in "0123456789":
#                 if targa[5] in "ABCDEFGHIJKLMNOPQRSTUVWQYZ" and targa[6] in "ABCDEFGHIJKLMNOPQRSTUVWQYZ":
#                     self.__targaMezzoParcheggiato = value
#         return
    
#     @oraArrivoMezzoParcheggiato.setter
#     def oraArrivoMezzoParcheggiato(self,numeroOreSosta):
#         adesso = datetime.datetime.now()
#         oreSosta = datetime.timedelta(hours = numeroOreSosta)
#         self.__oraArrivoMezzoParcheggiato = adesso + oreSosta
#         return
    
    
    def èOccupato(self):
        if self.__targaMezzoParcheggiato == "":
            return False
        return True
    
    def parcheggia(self,targa):
        targaValida = False
        if self.__targaMezzoParcheggiato == "":
            if targa[0] in "ABCDEFGHIJKLMNOPQRSTUVWQYZ" and targa[1] in "ABCDEFGHIJKLMNOPQRSTUVWQYZ":
                if targa[2] in "0123456789" and targa[3] in "0123456789" and targa[4] in "0123456789":
                    if targa[5] in "ABCDEFGHIJKLMNOPQRSTUVWQYZ" and targa[6] in "ABCDEFGHIJKLMNOPQRSTUVWQYZ":
                        targaValida = True
                        self.__targaMezzoParcheggiato = targa
                        
            if not targaValida:
                raise ValueError("Targa non valida")
            self.__oraArrivoMezzoParcheggiato = datetime.datetime.now()
            #oreSosta = datetime.timedelta(hours = oreSosta)
            #self.__oraTermineMezzoParcheggiato = adesso + oreSosta
        return
    
    def libera(self,targa):
        self.__targaMezzoParcheggiato = ""
        self.__oraArrivoMezzoParcheggiato = 0
    
    def __str__(self):
        return f"Posto {self.__tipoVeicolo}, {self.__targaMezzoParcheggiato}, {self.__oraArrivoMezzoParcheggiato}"
    def __repr__(self):
        return str(self.__dict__)
        

if __name__ == "__main__":
    postoAuto1 = PostoMezzo("auto")
    print(postoAuto1)