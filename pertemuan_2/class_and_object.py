class universitas:
    nama = ''
    daerah = ''
    nim = ''
    
    def perkenalan(self):
        print(f"Ahlan wa sahlan di  {self.nama} yang berada di daerah {self.daerah}")

    def muqaddimah(self, nama):
        print(f"Hallo {nama}! Ahlan wa sahlan di {self.nama} yang berada di daerah {self.daerah}")
                      
class Mahasantri:
    pass

kampusA = universitas()
kampusB = universitas()

print(kampusA)
print(kampusB)

Mahasantri1 = Mahasantri()
Mahasantri1.ismun = "azhad salim"
Mahasantri1.prodi = "teknik informatika"
Mahasantri1.nim = "462025611020" 

Mahasantri2 = Mahasantri()
Mahasantri2.ismun = "ibed"
Mahasantri2.prodi = "farmasi"
Mahasantri2.nim = "4620254334020" 

print(Mahasantri1.ismun)
print(Mahasantri1.prodi)
print(Mahasantri1.nim)

print(Mahasantri2.ismun)
print(Mahasantri2.prodi)
print(Mahasantri2.nim)

kampusA.nama = "UNIDA Gontor"
kampusA.daerah = "Siman"

kampusB.nama = "UNIDA Gontor"
kampusB.daerah = "Robitoh"

print(kampusA.nama)
print(kampusA.daerah)
print(kampusB.nama)
print(kampusB.daerah)

kampus= universitas()
kampus.nama = kampusB.nama
kampus.daerah = kampusB.daerah
kampus.perkenalan()

informasi= universitas()
informasi.nama = "Universitas Darussalam Gontor"
informasi.daerah = "Siman, Ponorogo"
informasi.muqaddimah("Azhad")
