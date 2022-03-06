# **Modul di Python**	#
Modul pada python adalah file yang berisi definisi dan pernyataan Python. Nama file adalah nama modul dengan akhiran .py ditambahkan. Dalam sebuah modul, nama modul (sebagai string) tersedia sebagai nilai dari variabel global __name__.

### **More on Modules** ###
Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Pernyataan ini dimaksudkan untuk menginisialisasi modul. Setiap modul memiliki tabel simbol pribadinya sendiri, yang digunakan sebagai tabel simbol global oleh semua fungsi yang didefinisikan dalam modul. Dengan demikian, pembuat modul dapat menggunakan variabel global dalam modul tanpa mengkhawatirkan bentrokan yang tidak disengaja dengan variabel global pengguna. Modul dapat mengimpor modul lain. Merupakan kebiasaan tetapi tidak diharuskan untuk menempatkan semua pernyataan impor di awal modul (atau skrip, dalam hal ini). Ada beberapa varian import untuk mengimport nama dari modul langsung ke tabel simbol modul pengimpor. Sebagai contoh:

- Menjalankan modul sebagai skrip
- Jalur Pencarian Modul
- File Python "Dikompilasi"

### **Standard Modules** ###
Python hadir dengan pustaka modul standar, yang dijelaskan dalam dokumen terpisah. Beberapa modul dibangun ke dalam juru bahasa; ini menyediakan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk menyediakan akses ke sistem operasi primitif seperti panggilan sistem. Kumpulan modul tersebut adalah opsi konfigurasi yang juga bergantung pada platform yang mendasarinya. Misalnya, modul winreg hanya tersedia di sistem Windows.

### **The dir() Function** ###
Fungsi bawaan dir() digunakan untuk mengetahui nama yang didefinisikan oleh modul. Ini mengembalikan daftar string yang diurutkan

### **Packages** ###
Paket adalah cara menyusun namespace modul Python dengan menggunakan "nama modul bertitik". Misalnya, nama modul AB menunjuk submodule bernama B dalam paket bernama A. Sama seperti penggunaan modul menyelamatkan penulis modul yang berbeda dari harus khawatir tentang nama variabel global masing-masing, penggunaan nama modul bertitik menyelamatkan penulis. Misalkan Anda ingin merancang kumpulan modul ("paket") untuk penanganan file suara dan data suara yang seragam. Ada banyak format file suara yang berbeda (biasanya dikenali dari ekstensinya, misalnya: .wav, .aiff, .au). Yang termasuk dalam packages adalah:

- Importing * From a Package
- Intra-package References
- Packages in Multiple Directories