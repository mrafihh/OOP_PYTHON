***JAWABAN PRAKTIKUM***

1. HP Hero 1 menjadi 500

---

2. Parameter lawan harus berupa objek, bukan string, karena method serang perlu mengakses atribut dan method milik lawan seperti hp dan    diserang(). Dengan objek, perubahan HP terjadi pada lawan yang sebenarnya, sesuai konsep OOP. 

---

3. Error yang muncul adalah AttributeError: 'Mage' object has no attribute 'name'. Error ini terjadi karena pada constructor Mage, fungsi super().__init__(name, hp, attack_power) tidak dipanggil, sehingga atribut name, hp, dan attack_power milik class Hero tidak dibuat pada objek Mage.  
Fungsi super() berperan untuk memanggil constructor class induk (Hero) agar seluruh atribut dasar Hero dapat diwariskan dan digunakan oleh class anak (Mage). Tanpa super(), objek Mage hanya memiliki atribut yang didefinisikan di dalam class Mage sendiri (yaitu mana).

---

4.  1. Nilai HP tetap muncul, tidak terjadi error. Hal ini   karena Python menggunakan konsep Name Mangling, di mana atribut __hp secara internal diubah menjadi _Hero__hp, sehingga masih bisa diakses secara paksa.

    2. Setelah logika if dan elif dihapus, pemanggilan hero1.set_hp(-100) akan membuat HP Hero menjadi -100. Hal ini terjadi karena tidak ada lagi validasi yang membatasi nilai HP.  
    Keberadaan method Setter sangat penting karena berfungsi sebagai penjaga integritas data, yaitu memastikan HP tetap berada dalam batas logis (tidak negatif atau berlebihan). Tanpa setter yang tervalidasi, data game bisa menjadi tidak masuk akal dan merusak alur permainan.

---

5.  1. Error yang muncul adalah TypeError: Can't instantiate abstract class Hero without an implementation for abstract method 'serang'. Artinya, Python menolak membuat objek Hero karena class tersebut belum mengimplementasikan method serang() yang wajib ada sesuai kontrak dari abstract class GameUnit.  
Konsekuensinya, jika kita lupa membuat method yang sudah dijanjikan di interface (abstract class), maka class tersebut tidak bisa dijadikan objek dan program akan langsung error. Abstract class berfungsi sebagai aturan/kontrak agar semua class turunan memiliki method penting yang sama. 

    2. Class **`GameUnit`** tidak boleh dibuat menjadi objek karena merupakan **abstract class** yang memiliki method abstrak yang belum diimplementasikan.  
    Fungsi **`GameUnit`** adalah sebagai **kontrak**, agar semua class turunan wajib memiliki method `serang()` dan `info()`, sehingga struktur program tetap konsisten.

---

6.  1. Program berjalan lancar tanpa mengubah kode looping. Kesimpulannya, polimorfisme memungkinkan programmer menambahkan karakter baru dengan perilaku berbeda tanpa mengubah kode yang sudah ada, sehingga program lebih fleksibel, rapi, dan mudah dikembangkan di masa depan.

    2. Yang terjadi, Archer tidak menjalankan serangan panah, melainkan memakai method serang() milik class Hero (parent), sehingga keluar output “Hero menyerang dengan tangan kosong.”  Hal ini terjadi karena dalam polimorfisme, Python akan memanggil method dengan nama yang sama seperti yang dipanggil di program (serang()). Jika nama method di child class berbeda (tembak_panah), maka method tersebut tidak dianggap override, sehingga Python kembali menggunakan method milik parent class.


***OUTPUT***
1.  500  
    Hero: Layla | HP: 500 | Power: 15  
    Hero: Zilong | HP: 120 | Power: 20

---

2.  500  
    Hero: Layla | HP: 500 | Power: 15  
    Hero: Zilong | HP: 120 | Power: 20  

    --- Pertarungan Dimulai ---  
    Layla menyerang Zilong!  
    Zilong terkena damage 15. Sisa HP: 105  
    Zilong menyerang Layla!  
    Layla terkena damage 20. Sisa HP: 480  

---

3. Error yang muncul:  ![error3](eror3.png)

---

4.  1. Mencoba akses paksa: 100
    2. Mencoba akses paksa: -100

---

5.  1. error yang muncul:  ![error 5.1](eror5.1.png)
    2. error yang muncul:  ![error 5.2](eror5.2.png)

---

6.  1. --- PERANG DIMULAI ---  
Eudora (Mage) menembakkan Bola Api! Boom!  
Miya (Archer) memanah dari jauh! Jleb!  
Zilong (Fighter) memukul dengan pedang! Slash!  
Gord (Mage) menembakkan Bola Api! Boom!  
Angela tidak menyerang, tapi menyembuhkan teman!  
    2. Yang terjadi, Archer tidak menjalankan serangan panah, melainkan memakai method serang() milik class Hero (parent), sehingga keluar output “Hero menyerang dengan tangan kosong.”
