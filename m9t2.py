class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        # Asetetaan rekisteritunnus ja huippunopeus parametreina
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        # Alustetaan nopeus ja kuljettu matka nolliksi
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        # Lasketaan uusi nopeus
        uusi_nopeus = self.nopeus + nopeuden_muutos
        # Varmistetaan, ettei nopeus ylitä huippunopeutta tai alita nollaa
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def tulosta_tiedot(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus} km/h")
        print(f"Tämänhetkinen nopeus: {self.nopeus} km/h")
        print(f"Kuljettu matka: {self.kuljettu_matka} km")


# Pääohjelma
if __name__ == "__main__":
    # Luodaan uusi Auto-olio
    auto = Auto("ABC-123", 142)
    # Tulostetaan auton alkuperäiset tiedot
    auto.tulosta_tiedot()

    # Kiihdytetään autoa
    auto.kiihdytä(30)  # +30 km/h
    auto.kiihdytä(70)  # +70 km/h
    auto.kiihdytä(50)  # +50 km/h
    # Tulostetaan auton nopeus kiihdytysten jälkeen
    print(f"\nNopeus kiihdytysten jälkeen: {auto.nopeus} km/h")

    # Suoritetaan hätäjarrutus
    auto.kiihdytä(-200)  # -200 km/h
    # Tulostetaan auton nopeus hätäjarrutuksen jälkeen
    print(f"Nopeus hätäjarrutuksen jälkeen: {auto.nopeus} km/h")
