class AlatPembayaran:

    def __init__(self, nama_pengguna, jumlah):
        self.nama_pengguna = nama_pengguna
        self.jumlah = jumlah

    def proses_bayar(self):
        print(f"[Generik] Memproses Rp{self.jumlah:,} untuk "
              f"{self.nama_pengguna} dengan metode tidak spesifik.")

    def info(self):
        print(f"Pengguna: {self.nama_pengguna} | Jumlah: Rp{self.jumlah:,}")

class KartuKredit(AlatPembayaran):

    def __init__(self, nama_pengguna, jumlah, nomor_kartu, limit):
        super().__init__(nama_pengguna, jumlah)
        self.nomor_kartu = nomor_kartu
        self.limit = limit

    def proses_bayar(self):
        akhir_kartu = self.nomor_kartu[-4:]
        if self.jumlah > self.limit:
            print(f"[Kartu Kredit] DITOLAK. Rp{self.jumlah:,} melebihi "
                  f"limit Rp{self.limit:,} (kartu ****{akhir_kartu}).")
        else:
            sisa = self.limit - self.jumlah
            print(f"[Kartu Kredit] BERHASIL Rp{self.jumlah:,} via kartu "
                  f"****{akhir_kartu}. Sisa limit: Rp{sisa:,}.")


class EWallet(AlatPembayaran):

    def __init__(self, nama_pengguna, jumlah, saldo, nama_aplikasi="E-Wallet"):
        super().__init__(nama_pengguna, jumlah)
        self.saldo = saldo
        self.nama_aplikasi = nama_aplikasi

    def proses_bayar(self):
        if self.jumlah > self.saldo:
            kurang = self.jumlah - self.saldo
            print(f"[{self.nama_aplikasi}] GAGAL. Saldo kurang "
                  f"Rp{kurang:,}.")
        else:
            self.saldo -= self.jumlah
            print(f"[{self.nama_aplikasi}] BERHASIL Rp{self.jumlah:,}. "
                  f"Sisa saldo: Rp{self.saldo:,}.")


class TransferBank(AlatPembayaran):

    def __init__(self, nama_pengguna, jumlah, bank_tujuan):
        super().__init__(nama_pengguna, jumlah)
        self.bank_tujuan = bank_tujuan

    def proses_bayar(self):
        print(f"[Transfer Bank] Mentransfer Rp{self.jumlah:,} ke "
              f"{self.bank_tujuan} a.n. {self.nama_pengguna}. "
              f"Estimasi proses 1-2 jam kerja.")

class Barter:

    def __init__(self, nama_pengguna, barang_ditukar):
        self.nama_pengguna = nama_pengguna
        self.barang_ditukar = barang_ditukar

    def proses_bayar(self):
        print(f"[Barter] {self.nama_pengguna} menukar barang "
              f"'{self.barang_ditukar}' sebagai ganti pembayaran tunai.")

def jalankan_transaksi(objek):

    print("-" * 60)
    print(f"Memproses objek bertipe: {type(objek).__name__}")
    try:
        objek.proses_bayar()
    except AttributeError:
        print(f"GAGAL: objek bertipe {type(objek).__name__} tidak "
              f"memiliki method proses_bayar().")

def main():
    print("=" * 60)
    print("DEMO METHOD OVERRIDING & DUCK TYPING")
    print("=" * 60)

    kartu = KartuKredit("Budi", 2_500_000, "1234567812345678", 5_000_000)
    ewallet = EWallet("Siti", 150_000, 100_000, nama_aplikasi="GoPay")
    transfer = TransferBank("Andi", 1_000_000, "Bank Mandiri")
    barter = Barter("Joko", "1 ekor kambing")  

    daftar_transaksi = [kartu, ewallet, transfer, barter]

    for objek in daftar_transaksi:
        jalankan_transaksi(objek)

if __name__ == "__main__":
    main()
