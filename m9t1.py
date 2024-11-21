class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        # Asetetaan rekisteritunnus ja huippunopeus parametreina
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        # Alustetaan nopeus ja kuljettu matka nolliksi
        self.nopeus = 0
        self.kuljettu_matka = 0

    def tulosta_tiedot(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus} km/h")
        print(f"Tämänhetkinen nopeus: {self.nopeus} km/h")
        print(f"Kuljettu matka: {self.kuljettu_matka} km")


# Pääohjelma
if __name__ == "__main__":
    # Luodaan uusi Auto-olio
    auto = Auto("ABC-123", 142)
    # Tulostetaan auton kaikki ominaisuudet
    auto.tulosta_tiedot()
