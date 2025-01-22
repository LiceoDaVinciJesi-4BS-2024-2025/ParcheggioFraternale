# Lorenzo Fraternale
# 4BS
# Esercizi OOP: Parcheggio

# Esercizio

from pathlib import Path
parcheggioPath = Path.cwd() / "park.data"
if parcheggioPath.exists():
    file = open("park.data","r")
    postiAutoLiberi = file[0]
    postiMotoLiberi = file[1]
    file.close()
else:
    postiAutoLiberi = 1000
    postiMotoLiberi = 200

postiAutoTot = 1000
postiMotoTot = 200

def postiLiberi(tipoVeicolo):
    if tipoVeicolo == "auto":
        return postiAutoLiberi
    elif tipoVeicolo == "moto":
        return postiMotoLiberi
    else:
        print("Non puoi parcheggiare il veicolo")
    return

if __name__ == "__main__":
    print(postiLiberi("moto"))