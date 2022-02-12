# **TUTORIAL PYTHON**
## **Dasar Teori**
Python adalah bahasa pemrograman yang mudah dipelajari dan kuat. Ini memiliki struktur data tingkat tinggi yang efisien dan pendekatan yang sederhana namun efektif untuk pemrograman berorientasi objek. Sintaks Python yang elegan dan pengetikan dinamis, bersama dengan sifatnya yang ditafsirkan, menjadikannya bahasa yang ideal untuk pembuatan skrip dan pengembangan aplikasi yang cepat di banyak area di sebagian besar platform.
Penerjemah Python dan perpustakaan standar yang luas tersedia secara bebas dalam bentuk sumber atau biner untuk semua platform utama dari situs web Python, https://www.python.org/, dan dapat didistribusikan secara bebas. Situs yang sama juga berisi distribusi dan petunjuk ke banyak modul, program dan alat Python pihak ketiga gratis, dan dokumentasi tambahan.

Interpreter Python mudah diperluas dengan fungsi dan tipe data baru yang diimplementasikan dalam C atau C++ (atau bahasa lain yang dapat dipanggil dari C). Python juga cocok sebagai bahasa ekstensi untuk aplikasi yang dapat disesuaikan.


## **Bab 1** ##
Jika Anda seorang pengembang perangkat lunak profesional, Anda mungkin harus bekerja dengan beberapa pustaka C/C++/Java tetapi menemukan siklus tulis/kompilasi/uji/kompilasi ulang yang biasa terlalu lambat. Mungkin Anda sedang menulis rangkaian pengujian untuk pustaka semacam itu dan merasa menulis kode pengujian merupakan tugas yang membosankan. Atau mungkin Anda telah menulis sebuah program yang dapat menggunakan bahasa ekstensi, dan Anda tidak ingin merancang dan mengimplementasikan bahasa yang sama sekali baru untuk aplikasi Anda.

Anda dapat menulis skrip shell Unix atau file batch Windows untuk beberapa tugas ini, tetapi skrip shell paling baik dalam memindahkan file dan mengubah data teks, tidak cocok untuk aplikasi atau game GUI. Anda dapat menulis program C/C++/Java, tetapi membutuhkan banyak waktu pengembangan untuk mendapatkan program draf pertama. Python lebih mudah digunakan, tersedia di sistem operasi Windows, macOS, dan Unix, dan akan membantu Anda menyelesaikan pekerjaan dengan lebih cepat.

Python mudah digunakan, tetapi merupakan bahasa pemrograman nyata, menawarkan lebih banyak struktur dan dukungan untuk program besar daripada yang dapat ditawarkan oleh skrip shell atau file batch. Di sisi lain, Python juga menawarkan lebih banyak pemeriksaan kesalahan daripada C, dan, sebagai bahasa tingkat sangat tinggi, ia memiliki tipe data tingkat tinggi bawaan, seperti array dan kamus fleksibel. Karena tipe datanya yang lebih umum, Python dapat diterapkan ke domain masalah yang jauh lebih besar daripada Awk atau bahkan Perl, namun banyak hal setidaknya semudah di Python seperti dalam bahasa tersebut.

## **Bab 2** ##
_**Menggunakan Interpreter Python**_
Interpreter Python biasanya diinstal sebagai /usr/local/bin/python3.10 pada mesin yang tersedia; menempatkan /usr/local/bin di jalur pencarian shell Unix. 

Fitur pengeditan baris penerjemah mencakup pengeditan interaktif, penggantian riwayat, dan penyelesaian kode pada sistem yang mendukung pustaka GNU Readline. Mungkin pemeriksaan tercepat untuk melihat apakah pengeditan baris perintah didukung adalah mengetik Control-P ke prompt Python pertama yang Anda dapatkan. Jika berbunyi bip, Anda memiliki pengeditan baris perintah; lihat Lampiran Pengeditan Input Interaktif dan Substitusi Riwayat untuk pengenalan kunci. Jika tidak ada yang terjadi, atau jika ^P digemakan, pengeditan baris perintah tidak tersedia; Anda hanya dapat menggunakan spasi mundur untuk menghapus karakter dari baris saat ini.

Interpreter beroperasi seperti shell Unix: ketika dipanggil dengan input standar yang terhubung ke perangkat tty, ia membaca dan mengeksekusi perintah secara interaktif; ketika dipanggil dengan argumen nama file atau dengan file sebagai input standar, ia membaca dan mengeksekusi skrip dari file itu.

**Argument Passing** Saat diketahui oleh penerjemah, nama skrip dan argumen tambahan setelahnya diubah menjadi daftar string dan ditetapkan ke variabel argv di modul sys. Anda dapat mengakses daftar ini dengan menjalankan import sys. Panjang daftar setidaknya satu; ketika tidak ada skrip dan tidak ada argumen yang diberikan, sys.argv[0] adalah string kosong. Ketika nama skrip diberikan sebagai '-' (artinya input standar), sys.argv[0] disetel ke '-'. Ketika perintah -c digunakan, sys.argv[0] disetel ke '-c'. Saat modul -m digunakan, sys.argv[0] disetel ke nama lengkap modul yang terletak. Opsi yang ditemukan setelah perintah -c atau modul -m tidak digunakan oleh pemrosesan opsi interpreter Python tetapi dibiarkan di sys.argv untuk ditangani oleh perintah atau modul.

**Interactive Mode** Ketika perintah dibaca dari tty, interpreter dikatakan dalam mode interaktif. Dalam mode ini ia meminta perintah berikutnya dengan prompt utama, biasanya tiga tanda lebih besar dari (>>>); untuk baris lanjutan, ia meminta dengan prompt sekunder, secara default tiga titik (...). Penerjemah mencetak pesan selamat datang yang menyatakan nomor versi dan pemberitahuan hak cipta sebelum mencetak perintah pertama:

**Source Code Encoding** Secara default, file sumber Python diperlakukan sebagai dikodekan dalam UTF-8. Dalam pengkodean itu, karakter sebagian besar bahasa di dunia dapat digunakan secara bersamaan dalam literal string, pengidentifikasi, dan komentar — meskipun pustaka standar hanya menggunakan karakter ASCII untuk pengidentifikasi, sebuah konvensi yang harus diikuti oleh kode portabel apa pun. Untuk menampilkan semua karakter ini dengan benar, editor Anda harus mengenali bahwa file tersebut adalah UTF-8, dan harus menggunakan font yang mendukung semua karakter dalam file.

## **Bab 3** ##
#### **Pengantar Informal Tentang Python** ####
Input dan output dibedakan dengan ada atau tidaknya prompt (>>> dan ...): untuk mengulang contoh, Anda harus mengetikkan semuanya setelah prompt, ketika prompt muncul; baris yang tidak dimulai dengan prompt adalah output dari interpreter.

Anda dapat mengaktifkan tampilan prompt dan output dengan mengklik >>> di sudut kanan atas kotak contoh. Jika Anda menyembunyikan perintah dan output sebagai contoh, maka Anda dapat dengan mudah menyalin dan menempelkan baris input ke penerjemah Anda.

Banyak contoh dalam manual ini, bahkan yang dimasukkan pada prompt interaktif, termasuk komentar. Komentar dalam Python dimulai dengan karakter hash, #, dan diperpanjang hingga akhir baris fisik.

**Numbers** Penerjemah bertindak sebagai kalkulator sederhana: Anda dapat mengetikkan ekspresi padanya dan itu akan menulis nilainya. Sintaks ekspresi sangat mudah: operator +, -, * dan / bekerja seperti kebanyakan bahasa lain (misalnya, Pascal atau C); tanda kurung (()) dapat digunakan untuk pengelompokan

**Strings** Selain angka, Python juga dapat memanipulasi string, yang dapat diekspresikan dalam beberapa cara. Mereka dapat diapit dalam tanda kutip tunggal ('...') atau tanda kutip ganda ("...") dengan hasil yang sama 2. \ dapat digunakan untuk menghindari tanda kutip

**Lists** Python mengetahui sejumlah tipe data gabungan, yang digunakan untuk mengelompokkan nilai-nilai lain. Yang paling serbaguna adalah daftar, yang dapat ditulis sebagai daftar nilai (item) yang dipisahkan koma di antara tanda kurung siku. Daftar mungkin berisi item dari jenis yang berbeda, tetapi biasanya semua item memiliki jenis yang sama