class Laptop:
    def __init__(self, merek, kegunaan):
        self.merek = merek
        self.kegunaan = kegunaan

    def info(self):
        print(f"Laptop ini adalah {self.merek} untuk pemakaian {self.kegunaan}.")

class gaming(Laptop):
    def kegunaan_gaming(self):
        print("Ini adalah Laptop gaming.")
    
    def cek_diamond_problem(self):
        print("Cek diamond problem di kelas Gaming.")

class Kantor(Laptop):
    def kegunaan_Kantor(self):
        print("Ini adalah Laptop Kantor.")
    
    def cek_diamond_problem(self):
        print("Cek diamond problem di kelas Kantor.")

class jenislaptop(gaming, Kantor):
    def info_Jenis_laptop(self):
        print("Ini adalah Jenis laptop.")

jenis_laptop1 = jenislaptop("ADVAN", "Sepeda Motor")
jenis_laptop1.info()
jenis_laptop1.kegunaan_gaming()
jenis_laptop1.kegunaan_Kantor()
jenis_laptop1.cek_diamond_problem()