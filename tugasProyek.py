from abc import ABC, abstractmethod

class BarangElektronik(ABC):
    """
    Abstract Class untuk barang elektronik.
    Tidak bisa diinstansiasi langsung.
    """
    def __init__(self, nama, harga_dasar, stok_awal=0):
        self.nama = nama
        self.__harga_dasar = harga_dasar
        self.__stok = stok_awal
    

    @property
    def stok(self):
        return self.__stok
    
    @property
    def harga_dasar(self):
        return self.__harga_dasar
    
    
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
            return False
        self.__stok += jumlah
        print(f"Berhasil menambahkan stok {self.nama}: {self.__stok} unit.")
        return True
    

    def kurangi_stok(self, jumlah):
        if jumlah > self.__stok:
            print(f"Stok {self.nama} tidak mencukupi!")
            return False
        self.__stok -= jumlah
        return True
    

    @abstractmethod
    def tampilkan_detail(self, jumlah_beli):
        pass
    
    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass


class Laptop(BarangElektronik):
    """
    Class untuk produk Laptop dengan pajak 10%
    """
    def __init__(self, nama, harga_dasar, processor, stok_awal=0):
        super().__init__(nama, harga_dasar, stok_awal)
        self.processor = processor
    
    def hitung_harga_total(self, jumlah):
        """Hitung total harga dengan pajak 10%"""
        pajak = self.harga_dasar * 0.10
        harga_per_unit = self.harga_dasar + pajak
        return harga_per_unit * jumlah, pajak
    
    def tampilkan_detail(self, jumlah_beli):
        """Tampilkan detail laptop yang dibeli"""
        total, pajak = self.hitung_harga_total(jumlah_beli)
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f"   Harga Dasar: Rp {self.harga_dasar:,} | Pajak(10%): Rp {pajak:,.0f}")
        print(f"   Beli: {jumlah_beli} unit | Subtotal: Rp {total:,.0f}")
        return total


class Smartphone(BarangElektronik):
    """
    Class untuk produk Smartphone dengan pajak 5%
    """
    def __init__(self, nama, harga_dasar, kamera, stok_awal=0):
        super().__init__(nama, harga_dasar, stok_awal)
        self.kamera = kamera
    
    def hitung_harga_total(self, jumlah):
        """Hitung total harga dengan pajak 5%"""
        pajak = self.harga_dasar * 0.05
        harga_per_unit = self.harga_dasar + pajak
        return harga_per_unit * jumlah, pajak
    
    def tampilkan_detail(self, jumlah_beli):
        """Tampilkan detail smartphone yang dibeli"""
        total, pajak = self.hitung_harga_total(jumlah_beli)
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f"   Harga Dasar: Rp {self.harga_dasar:,} | Pajak(5%): Rp {pajak:,.0f}")
        print(f"   Beli: {jumlah_beli} unit | Subtotal: Rp {total:,.0f}")
        return total


def proses_transaksi(daftar_barang):
    """
    Fungsi untuk memproses transaksi dari berbagai jenis barang.
    Parameter: daftar_barang = [(objek_barang, jumlah_beli), ...]
    """
    print("\n--- STRUK TRANSAKSI ---")
    total_tagihan = 0
    
    for index, (barang, jumlah) in enumerate(daftar_barang, 1):
        print(f"\n{index}. ", end="")
        # Polymorphism: Method yang dipanggil berbeda tergantung tipe objek
        subtotal = barang.tampilkan_detail(jumlah)
        total_tagihan += subtotal
        
        # Kurangi stok
        barang.kurangi_stok(jumlah)
    
    print("\n" + "="*40)
    print(f"TOTAL TAGIHAN: Rp {total_tagihan:,.0f}")
    print("="*40)

def main():
    print("--- SETUP DATA ---")
    
    # 1. Admin membuat data produk
    laptop1 = Laptop("ROG Zephyrus", 20000000, "Ryzen 9")
    smartphone1 = Smartphone("iPhone 13", 15000000, "12MP")
    
    # 2. Admin mengisi stok
    laptop1.tambah_stok(10)
    
    # 3. Admin mencoba mengisi stok dengan angka negatif (harus ditolak)
    smartphone1.tambah_stok(-5)
    
    # 4. Admin mengisi stok dengan benar
    smartphone1.tambah_stok(20)
    
    # 5. User membeli barang
    keranjang = [
        (laptop1, 2),      # Beli 2 laptop
        (smartphone1, 1)   # Beli 1 smartphone
    ]
    
    # 6. Proses transaksi
    proses_transaksi(keranjang)
    
    # 7. Cek sisa stok
    print(f"\n--- SISA STOK ---")
    print(f"{laptop1.nama}: {laptop1.stok} unit")
    print(f"{smartphone1.nama}: {smartphone1.stok} unit")


if __name__ == "__main__":
    main()
