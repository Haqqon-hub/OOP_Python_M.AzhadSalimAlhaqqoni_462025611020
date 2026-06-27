class SaldoMinimalError(Exception):

    def __init__(self, saldo_sekarang, jumlah_tarik, saldo_minimal):
        self.saldo_sekarang = saldo_sekarang
        self.jumlah_tarik = jumlah_tarik
        self.saldo_minimal = saldo_minimal
        pesan = (
            f"Penarikan sebesar Rp{jumlah_tarik:,.2f} ditolak. "
            f"Saldo akan menjadi Rp{(saldo_sekarang - jumlah_tarik):,.2f}, "
            f"di bawah saldo minimal Rp{saldo_minimal:,.2f}."
        )
        super().__init__(pesan)


class SaldoTidakCukupError(Exception):

    def __init__(self, saldo_sekarang, jumlah_tarik):
        self.saldo_sekarang = saldo_sekarang
        self.jumlah_tarik = jumlah_tarik
        pesan = (
            f"Saldo tidak cukup. Saldo Anda Rp{saldo_sekarang:,.2f}, "
            f"namun ingin menarik Rp{jumlah_tarik:,.2f}."
        )
        super().__init__(pesan)


class JumlahTidakValidError(Exception):

    def __init__(self, jumlah):
        self.jumlah = jumlah
        pesan = (
            f"Jumlah transaksi tidak valid: Rp{jumlah:,.2f}. "
            f"Jumlah harus lebih besar dari 0."
        )
        super().__init__(pesan)


class RekeningBank:

    SALDO_MINIMAL = 50_000  # Saldo minimal yang wajib tersisa di rekening

    def __init__(self, nomor_rekening, nama_pemilik, saldo_awal=0):
        self.nomor_rekening = nomor_rekening
        self.nama_pemilik = nama_pemilik
        self.saldo = saldo_awal

    def setor_tunai(self, jumlah):
        if jumlah <= 0:
            raise JumlahTidakValidError(jumlah)

        self.saldo += jumlah
        print(f"[INFO] Setor tunai berhasil. Saldo sekarang: Rp{self.saldo:,.2f}")
        return self.saldo

    def tarik_tunai(self, jumlah):
        if jumlah <= 0:
            raise JumlahTidakValidError(jumlah)

        if jumlah > self.saldo:
            raise SaldoTidakCukupError(self.saldo, jumlah)

        if (self.saldo - jumlah) < RekeningBank.SALDO_MINIMAL:
            raise SaldoMinimalError(self.saldo, jumlah, RekeningBank.SALDO_MINIMAL)

        self.saldo -= jumlah
        print(f"[INFO] Tarik tunai berhasil. Saldo sekarang: Rp{self.saldo:,.2f}")
        return self.saldo

    def cek_saldo(self):
        print(
            f"[INFO] Saldo rekening {self.nomor_rekening} "
            f"({self.nama_pemilik}): Rp{self.saldo:,.2f}"
        )
        return self.saldo

def proses_transaksi(rekening, jenis_transaksi, jumlah):
    print("-" * 60)
    print(f"Memproses transaksi: {jenis_transaksi.upper()} sebesar Rp{jumlah:,.2f}")

    try:
        if jenis_transaksi == "setor":
            rekening.setor_tunai(jumlah)
        elif jenis_transaksi == "tarik":
            rekening.tarik_tunai(jumlah)
        else:
            raise ValueError(f"Jenis transaksi '{jenis_transaksi}' tidak dikenal.")

    except SaldoMinimalError as e:
        print(f"[GAGAL] SaldoMinimalError: {e}")

    except SaldoTidakCukupError as e:
        print(f"[GAGAL] SaldoTidakCukupError: {e}")

    except JumlahTidakValidError as e:
        print(f"[GAGAL] JumlahTidakValidError: {e}")

    except Exception as e:
        # Menangkap exception lain yang tidak terduga
        print(f"[GAGAL] Terjadi error tak terduga: {e}")

    finally:
        print("Proses pemeriksaan transaksi telah selesai dilakukan.")


def main():
    print("=" * 60)
    print("SISTEM TRANSAKSI BANK SEDERHANA - EXCEPTION HANDLING LAB")
    print("=" * 60)

    rekening = RekeningBank("1234567890", "Budi Santoso", saldo_awal=200_000)
    rekening.cek_saldo()

    proses_transaksi(rekening, "setor", 100_000)

    proses_transaksi(rekening, "tarik", 50_000)

    proses_transaksi(rekening, "tarik", 220_000)

    proses_transaksi(rekening, "tarik", 1_000_000)

    proses_transaksi(rekening, "setor", -50_000)

    print("-" * 60)
    rekening.cek_saldo()
    print("=" * 60)

if __name__ == "__main__":
    main()
