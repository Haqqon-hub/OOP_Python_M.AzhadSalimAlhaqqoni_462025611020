class Bagian:
    bagian = ''
    ruangan = ''

    @staticmethod
    def sambutan():
        print("halo selamat datang di sini")

    def perkenalan(self):
        print("anda mendapatkan di bagian", self.bagian, "di ruangan", self.ruangan)

bagian1 = Bagian()
bagian1.bagian = 'Penerimaan Mahasiswa Baru'
bagian1.ruangan = 'Zubair 101'
bagian1.sambutan()
bagian1.perkenalan()