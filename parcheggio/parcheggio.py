# Lorenzo Fraternale
# 4BS
# Esercizi OOP: Parcheggio
import postoMezzo
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
        
        postoAutoVuoto = postoMezzo.PostoMezzo("auto")
        postoMotoVuoto = postoMezzo.PostoMezzo("moto")
        
        for n in range(1000):
            self.__listaParcheggiAuto.append(postoAutoVuoto)
        for n in range(200):
            self.__listaParcheggiMoto.append(postoMotoVuoto)
    
    @property
    def listaParcheggiAuto(self):
        return self.__listaParcheggiAuto
    @property
    def listaParcheggiMoto(self):
        return self.__listaParcheggiMoto
    
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)


    def postiLiberi(self,tipoVeicolo):
        conta = 0
        if tipoVeicolo == "auto":
            for posto in self.__listaParcheggiAuto:
                if posto.targaMezzoParcheggiato == "":
                    conta += 1
            
        elif tipoVeicolo == "moto":
            for posto in self.__listaParcheggiMoto:
                if posto.targaMezzoParcheggiato == "":
                    conta += 1
        else:
            return "Non puoi parcheggiare il veicolo"
        return conta

    def parcheggia(self,tipoVeicolo,targa,numeroOreSosta):
        if self.postiLiberi(tipoVeicolo) > 0:
            if tipoVeicolo == "moto":
                self.__guadagno += 1.2*numeroOreSosta
                for postoMoto in self.__listaParcheggiMoto:
                    if postoMoto.èOccupato() == False:
                        postoMoto.parcheggia(targa,numeroOreSosta)
                        break
            elif tipoVeicolo == "auto":
                self.__guadagno += 1.5*numeroOreSosta
                for postoAuto in self.__listaParcheggiAuto:
                    if postoAuto.èOccupato() == False:
                        postoAuto.parcheggia(targa,numeroOreSosta)
                        break
            else:
                return "Non puoi parcheggiare il veicolo"
        return


if __name__ == "__main__":
    mioParcheggio = Parcheggio()
    print(mioParcheggio.postiLiberi("auto"))
    mioParcheggio.parcheggia("auto","SC235KD",3)
    print(mioParcheggio.postiLiberi("auto"))