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
        


    def postiLiberi(self,tipoVeicolo):
        conta = 0
        if tipoVeicolo == "auto":
            for posto in self.__listaParcheggiAuto:
                if posto.targaMezzoParcheggiato == "":
                    conta += 1
            return conta
            
        elif tipoVeicolo == "moto":
            for posto in self.__listaParcheggiMoto:
                if posto.targaMezzoParcheggiato == "":
                    conta += 1
            return conta
        else:
            return "Non puoi parcheggiare il veicolo"
        return

    def parcheggia(self,tipoVeicolo,targa,numeroOreSosta):
        if self.postiLiberi(tipoVeicolo) > 0:
            if tipoVeicolo == "moto":
                return str(1.2*numeroOreSosta) + " euro"
            elif tipoVeicolo == "auto":
                return str(1.5*numeroOreSosta) + " euro"
            else:
                return "Non puoi parcheggiare il veicolo"
                

if __name__ == "__main__":
    mioParcheggio = Parcheggio()
    print(mioParcheggio.postiLiberi("auto"))
    print(mioParcheggio.parcheggia("auto","SC235KD",3))