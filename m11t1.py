# Yliluokka Julkaisu
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


# Aliluokka Kirja
class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumaara):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}")
        print(f"  Kirjailija: {self.kirjailija}")
        print(f"  Sivumäärä: {self.sivumaara}")


# Aliluokka Lehti
class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}")
        print(f"  Päätoimittaja: {self.paatoimittaja}")


# Pääohjelma
if __name__ == "__main__":
    # Luodaan julkaisut
    lehti = Lehti("Aku Ankka", "Aki Hyyppä")
    kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    # Tulostetaan tiedot
    lehti.tulosta_tiedot()
    print()
    kirja.tulosta_tiedot()
