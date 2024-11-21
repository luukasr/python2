import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{'Rekisteri':<10}{'Nopeus (km/h)':<15}{'Matka (km)':<10}")
        print("-" * 35)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<10}{auto.nopeus:<15}{auto.kuljettu_matka:<10}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False


# Pääohjelma
if __name__ == "__main__":
    # Luodaan autot
    autot = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(rekisteritunnus, huippunopeus))

    # Luodaan kilpailu
    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    print(f"Kilpailu '{kilpailu.nimi}' alkaa!")

    tunti = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunti += 1

        # Tulostetaan tilanne 10 tunnin välein
        if tunti % 10 == 0:
            print(f"\nTunti {tunti}:")
            kilpailu.tulosta_tilanne()

    # Tulostetaan lopullinen tilanne
    print(f"\nKilpailu päättyi tunnilla {tunti}!")
    kilpailu.tulosta_tilanne()
