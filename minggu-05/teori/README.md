# **Input & Output** #
Ada beberapa cara untuk menampilkan output dari suatu program; data dapat dicetak dalam bentuk yang dapat dibaca manusia, atau ditulis ke file untuk digunakan di masa mendatang. Kali ini kita akan belajar tentang :

### **Fancier Output Formatting** ###
Untuk menggunakan literal string yang diformat, mulailah string dengan f atau F sebelum tanda kutip pembuka atau tanda kutip tiga. Di dalam string ini, Anda dapat menulis ekspresi Python antara karakter { dan } yang dapat merujuk ke variabel atau nilai literal. 
Metode string str.format() membutuhkan lebih banyak upaya manual. Anda masih akan menggunakan { dan } untuk menandai di mana variabel akan diganti dan dapat memberikan arahan pemformatan terperinci, tetapi Anda juga harus memberikan informasi yang akan diformat. Anda dapat mengonversi nilai apa pun menjadi string dengan fungsi repr() atau str(). Fungsi str() dimaksudkan untuk mengembalikan representasi nilai yang cukup dapat dibaca manusia, sedangkan repr() dimaksudkan untuk menghasilkan representasi yang dapat dibaca oleh penerjemah (atau akan memaksa SyntaxError jika tidak ada sintaks yang setara). Berikut beberapa macam formatting :

- **Formatted String Literals**

    Literal string yang diformat (disingkat juga disebut f-string) memungkinkan Anda memasukkan nilai ekspresi Python di dalam string dengan mengawali string dengan f atau F dan menulis ekspresi sebagai {expression}.

- **The String format() Method**

    Tanda kurung dan karakter di dalamnya (disebut bidang format) diganti dengan objek yang diteruskan ke metode str.format(). Angka dalam kurung dapat digunakan untuk merujuk ke posisi objek yang diteruskan ke metode str.format().

- **Manual String Formatting**

    Metode str.rjust() objek string membenarkan string di bidang dengan lebar tertentu dengan mengisinya dengan spasi di sebelah kiri. Ada metode serupa str.ljust() dan str.center(). Metode ini tidak menulis apa pun, mereka hanya mengembalikan string baru. Jika string input terlalu panjang, mereka tidak memotongnya, tetapi mengembalikannya tidak berubah

- **Old string formatting**

    Operator % (modulo) juga dapat digunakan untuk pemformatan string. Mengingat nilai % 'string', instance % dalam string diganti dengan nol atau lebih elemen nilai. Operasi ini biasa disebut dengan interpolasi string.

### **Reading and Writing Files** ###
Argumen pertama adalah string yang berisi nama file. Argumen kedua adalah string lain yang berisi beberapa karakter yang menjelaskan cara file akan digunakan. mode bisa 'r' ketika file hanya akan dibaca, 'w' hanya untuk menulis (file yang sudah ada dengan nama yang sama akan dihapus), dan 'a' membuka file untuk ditambahkan; setiap data yang ditulis ke file secara otomatis ditambahkan ke akhir. 'r+' membuka file untuk membaca dan menulis. Argumen mode adalah opsional; 'r' akan diasumsikan jika dihilangkan. Dalam mode teks, default saat membaca adalah mengonversi akhir baris khusus platform (\n di Unix, \r\n di Windows) menjadi hanya \n. Saat menulis dalam mode teks, defaultnya adalah mengonversi kemunculan \n kembali ke akhir baris khusus platform. Modifikasi di balik layar untuk data file ini baik untuk file teks, tetapi akan merusak data biner seperti itu dalam file JPEG atau EXE.

- **Methods of File Objects**

    Untuk membaca isi file, panggil f.read(size), yang membaca sejumlah data dan mengembalikannya sebagai string (dalam mode teks) atau objek byte (dalam mode biner). size adalah argumen numerik opsional. Ketika ukuran dihilangkan atau negatif, seluruh isi file akan dibaca dan dikembalikan; itu masalah Anda jika file dua kali lebih besar dari memori mesin Anda.

- **Saving structured data with json**

    String dapat dengan mudah ditulis dan dibaca dari sebuah file. Angka membutuhkan lebih banyak usaha, karena metode read() hanya mengembalikan string, yang harus diteruskan ke fungsi seperti int(), yang mengambil string seperti '123' dan mengembalikan nilai numeriknya 123. Bila Anda ingin menyimpan tipe data yang lebih kompleks seperti daftar dan kamus bersarang, parsing dan serialisasi dengan tangan menjadi rumit.Modul standar yang disebut json dapat mengambil hierarki data Python, dan mengubahnya menjadi representasi string; proses ini disebut serialisasi. Rekonstruksi data dari representasi string disebut deserializing. Antara serialisasi dan deserializing, string yang mewakili objek mungkin telah disimpan dalam file atau data, atau dikirim melalui koneksi jaringan ke beberapa mesin yang jauh.