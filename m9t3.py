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

    def kulje(self, tunnit):
        # Lisätään kuljettuun matkaan nykyisen nopeuden mukainen matka
        self.kuljettu_matka += self.nopeus * tunnit

    def tulosta_tiedot(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus} km/h")
        print(f"Tämänhetkinen nopeus: {self.nopeus} km/h")
        print(f"Kuljettu matka: {self.kuljettu_matka:.1f} km")


# Pääohjelma
if __name__ == "__main__":
    # Luodaan uusi Auto-olio
    auto = Auto("ABC-123", 142)
    # Tulostetaan auton alkuperäiset tiedot
    auto.tulosta_tiedot()

    # Kiihdytetään autoa
    auto.kiihdytä(60)  # +60 km/h
    print("\nAuto kiihdytti 60 km/h.")
    auto.tulosta_tiedot()

    # Ajetaan 1.5 tuntia
    auto.kulje(1.5)
    print("\nAuto ajoi 1.5 tuntia.")
    auto.tulosta_tiedot()

    # Kiihdytetään ja ajetaan uudestaan
    auto.kiihdytä(30)  # +30 km/h
    print("\nAuto kiihdytti 30 km/h lisää.")
    auto.tulosta_tiedot()

    auto.kulje(2)  # Ajetaan 2 tuntia
    print("\nAuto ajoi 2 tuntia lisää.")
    auto.tulosta_tiedot()
