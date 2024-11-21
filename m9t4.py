import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit

    def tulosta_tiedot(self):
        return (f"{self.rekisteritunnus:<10} | {self.huippunopeus:>4} km/h "
                f"| {self.nopeus:>4} km/h | {self.kuljettu_matka:>6.1f} km")


# Pääohjelma
if __name__ == "__main__":
    # Luodaan lista 10 autosta
    autot = [
        Auto(f"ABC-{i+1}", random.randint(100, 200))
        for i in range(10)
    ]

    kilpailu_kaynnissa = True
    while kilpailu_kaynnissa:
        for auto in autot:
            # Nopeuden muutos väliltä -10 ja +15 km/h
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)

            # Liikkuminen yhden tunnin ajan
            auto.kulje(1)

            # Tarkistetaan, onko auto saavuttanut 10,000 km
            if auto.kuljettu_matka >= 10000:
                kilpailu_kaynnissa = False

    # Tulostetaan tulokset
    print(f"\n{'Rekisteri':<10} | {'Huippu':>6} | {'Nopeus':>6} | {'Kuljettu':>8}")
    print("-" * 40)
    for auto in autot:
        print(auto.tulosta_tiedot())
