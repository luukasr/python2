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


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [
            Hissi(alin_kerros, ylin_kerros)
            for _ in range(hissien_lkm)
        ]

    def aja_hissiä(self, hissi_numero, kohdekerros):
        if 0 <= hissi_numero < len(self.hissit):
            print(f"\nAjetaan hissiä {hissi_numero + 1} kerrokseen {kohdekerros}.")
            self.hissit[hissi_numero].siirry_kerrokseen(kohdekerros)
        else:
            print("Virhe: Ei olemassa olevaa hissiä tällä numerolla.")


# Pääohjelma
if __name__ == "__main__":
    # Luodaan talo, jossa on 3 hissiä ja kerrokset 1-10
    talo = Talo(1, 10, 3)

    # Ajetaan ensimmäistä hissiä kerrokseen 5
    talo.aja_hissiä(0, 5)

    # Ajetaan toista hissiä kerrokseen 10
    talo.aja_hissiä(1, 10)

    # Ajetaan kolmatta hissiä kerrokseen 3
    talo.aja_hissiä(2, 3)

    # Palataan ensimmäisellä hissillä alimpaan kerrokseen
    talo.aja_hissiä(0, 1)
