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


# Aliluokka Sähköauto
class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


# Aliluokka Polttomoottoriauto
class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko


# Pääohjelma
if __name__ == "__main__":
    # Luodaan sähköauto ja polttomoottoriauto
    sahkoauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    # Asetetaan nopeudet
    sahkoauto.kiihdytä(150)  # Sähköauto 150 km/h
    polttomoottoriauto.kiihdytä(120)  # Polttomoottoriauto 120 km/h

    # Ajetaan 3 tuntia
    sahkoauto.kulje(3)
    polttomoottoriauto.kulje(3)

    # Tulostetaan matkamittarilukemat
    print(f"Sähköauton ({sahkoauto.rekisteritunnus}) matkamittarilukema: {sahkoauto.kuljettu_matka} km")
    print(f"Polttomoottoriauton ({polttomoottoriauto.rekisteritunnus}) matkamittarilukema: {polttomoottoriauto.kuljettu_matka} km")
