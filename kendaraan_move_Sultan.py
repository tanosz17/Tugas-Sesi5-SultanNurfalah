#Sultan Nurfalah
#TI23H

class Kendaraan:
    def move(self):
        pass

class Mobil(Kendaraan):
    def move(self):
        print("Mobil berjalan di jalan raya.")

class Sepeda(Kendaraan):
    def move(self):
        print("Sepeda dikayuh di jalur sepeda.")

class Perahu(Kendaraan):
    def move(self):
        print("Perahu berlayar di atas air.")

# polymorphism
def gerakkan_kendaraan(kendaraan):
    kendaraan.move()

# penggunaan
mobil = Mobil()
sepeda = Sepeda()
perahu = Perahu()

for kendaraan in [mobil, sepeda, perahu]:
    gerakkan_kendaraan(kendaraan)
