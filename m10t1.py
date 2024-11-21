class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi siirtyi kerrokseen {self.nykyinen_kerros}.")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi siirtyi kerrokseen {self.nykyinen_kerros}.")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

    def siirry_kerrokseen(self, tavoite_kerros):
        print(f"Aloitetaan siirtyminen kerrokseen {tavoite_kerros}.")
        while self.nykyinen_kerros < tavoite_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > tavoite_kerros:
            self.kerros_alas()
        print(f"Hissi saapui kerrokseen {tavoite_kerros}.")


# Pääohjelma
if __name__ == "__main__":
    # Luodaan hissi, joka liikkuu kerrosten 1 ja 10 välillä
    hissi = Hissi(1, 10)

    # Siirrytään haluttuun kerrokseen (esim. 5)
    hissi.siirry_kerrokseen(5)

    # Siirrytään ylimpään kerrokseen
    hissi.siirry_kerrokseen(10)

    # Siirrytään takaisin alimpaan kerrokseen
    hissi.siirry_kerrokseen(1)
 