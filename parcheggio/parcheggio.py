# Lorenzo Fraternale
# 4BS
# Esercizi OOP: Parcheggio
import veicolo
import auto
import moto
import postoMezzo
import datetime
# Esercizio
class Parcheggio:
    
    def __init__(self):
#         parcheggioPath = Path.cwd() / "park.data"
#         if parcheggioPath.exists():
#             file = open("park.data","r")
#             self.__postiAutoLiberi = file[0]
#             self.__postiMotoLiberi = file[1]
#             self.__listaParcheggiAuto = file[2]
#             self.__listaParcheggiMoto = file[3]
#             file.close()
#         else:
        self.__listaParcheggiAuto = []
        self.__listaParcheggiMoto = []
        self.__guadagno = 0
        
        for n in range(1000):
            self.__listaParcheggiAuto.append(postoMezzo.PostoMezzo("auto"))
        for n in range(200):
            self.__listaParcheggiMoto.append(postoMezzo.PostoMezzo("moto"))
    
    @property
    def listaParcheggiAuto(self):
        return self.__listaParcheggiAuto
    @property
    def listaParcheggiMoto(self):
        return self.__listaParcheggiMoto
    @property
    def guadagno(self):
        return self.__guadagno
    
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)


    def postiLiberi(self,tipoVeicolo):
        conta = 0
        if tipoVeicolo.lower() == "auto":
            for posto in self.__listaParcheggiAuto:
                if posto.targaMezzoParcheggiato == "":
                    conta += 1
        elif tipoVeicolo.lower() == "moto":
            for posto in self.__listaParcheggiMoto:
                if posto.targaMezzoParcheggiato == "":
                    conta += 1
        else:
            raise ValueError("Non puoi parcheggiare il veicolo")
        return conta

    def parcheggia(self,veicolo:veicolo.Veicolo):#,numeroOreSosta):
        if self.postiLiberi(veicolo.__class__.__name__) > 0:
            if veicolo.__class__.__name__ == "Moto":
                #self.__guadagno += 1.2*numeroOreSosta
                for postoMoto in self.__listaParcheggiMoto:
                    if postoMoto.èOccupato() == False:
                        postoMoto.parcheggia(veicolo.targa,numeroOreSosta)
                        return# 1.2*numeroOreSosta
            elif veicolo.__class__.__name__ == "Auto":
                #self.__guadagno += 1.5*numeroOreSosta
                for postoAuto in self.__listaParcheggiAuto:
                    if postoAuto.èOccupato() == False:
                        postoAuto.parcheggia(veicolo.targa)
                        return# 1.5*numeroOreSosta
            else:
                return "Non puoi parcheggiare il veicolo"
        return
    
    def libera(self,veicolo:veicolo.Veicolo):
        adesso = datetime.datetime.now()
        if veicolo.__class__.__name__ == "Moto":
            for postoMoto in self.__listaParcheggiMoto:
                if postoMoto.targaMezzoParcheggiato == veicolo.targa:
                    postoMoto.libera(veicolo.targa)
                    if postoMoto.oraArrivoMezzoParcheggiato != 0:
                        diff = adesso - postoMoto.oraArrivoMezzoParcheggiato
                        oreTotali = int(diff.total_seconds()) / 60 / 60
                        self.__guadagno += oreTotali*1.2
                        return f"{oreTotali*1.2} euro"
        elif veicolo.__class__.__name__ == "Auto":
            for postoAuto in self.__listaParcheggiAuto:
                if postoAuto.targaMezzoParcheggiato == veicolo.targa:
                    postoAuto.libera(veicolo.targa)
                    if postoAuto.oraArrivoMezzoParcheggiato != 0:
                        diff = adesso - postoAuto.oraArrivoMezzoParcheggiato
                        oreTotali = int(diff.total_seconds()) / 60 / 60
                        self.__guadagno += oreTotali*1.5
                        return f"{oreTotali*1.5} euro"
        return
                    
        


if __name__ == "__main__":
    laMiaAuto = auto.Auto("AB123CD")
    mioParcheggio = Parcheggio()
    print(mioParcheggio.listaParcheggiAuto)
    print(mioParcheggio.postiLiberi("auto"))
    mioParcheggio.parcheggia(laMiaAuto)
    #Faccio passare qualche secondo...
    for x in range(10000):
        print(x)
    print(mioParcheggio)
    print(mioParcheggio.postiLiberi("auto"))
    mioParcheggio.libera(laMiaAuto)
    print(mioParcheggio.guadagno)
    print(mioParcheggio)
    print(mioParcheggio.postiLiberi("auto"))
