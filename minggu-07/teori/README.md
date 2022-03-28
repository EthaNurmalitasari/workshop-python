# **OOP di Python** #
### **Classes** ###
Menyediakan sarana untuk menggabungkan data dan fungsionalitas bersama-sama. Membuat kelas baru membuat tipe objek baru, memungkinkan instance baru dari tipe itu dibuat. Setiap instance kelas dapat memiliki atribut yang dilampirkan untuk mempertahankan statusnya. Instance kelas juga dapat memiliki metode (didefinisikan oleh kelasnya) untuk memodifikasi statusnya

### **A Word About Names and Objects** ###
Objek memiliki individualitas, dan beberapa nama (dalam beberapa cakupan) dapat diikat ke objek yang sama. Ini dikenal sebagai aliasing dalam bahasa lain. Aliasing memiliki efek yang mungkin mengejutkan pada semantik kode Python yang melibatkan objek yang bisa berubah seperti daftar, kamus, dan sebagian besar jenis lainnya. Ini biasanya digunakan untuk kepentingan program, karena alias berperilaku seperti pointer dalam beberapa hal

### **Python Scopes and Namespaces** ###
Sebelum memperkenalkan kelas, pertama-tama saya harus memberi tahu Anda sesuatu tentang aturan ruang lingkup Python. Definisi kelas memainkan beberapa trik rapi dengan ruang nama, dan Anda perlu mengetahui cara kerja ruang lingkup dan ruang nama untuk memahami sepenuhnya apa yang terjadi. Namespace adalah pemetaan dari nama ke objek. Sebagian besar ruang nama saat ini diimplementasikan sebagai kamus Python, tetapi itu biasanya tidak terlihat dengan cara apa pun (kecuali untuk kinerja), dan mungkin berubah di masa mendatang. Contoh ruang nama adalah: kumpulan nama bawaan (berisi fungsi seperti abs(), dan nama pengecualian bawaan); nama global dalam modul; dan nama lokal dalam pemanggilan fungsi.

### **Class Definition Syntax** ###
Definisi kelas, seperti definisi fungsi (pernyataan def) harus dijalankan sebelum memiliki efek apa pun. (Anda bisa menempatkan definisi kelas di cabang pernyataan if, atau di dalam fungsi.)

### **Class Objects** ###
Objek kelas mendukung dua jenis operasi: referensi atribut dan instantiasi.
Referensi atribut menggunakan sintaks standar yang digunakan untuk semua referensi atribut di Python: obj.name. Nama atribut yang valid adalah semua nama yang ada di ruang nama kelas saat objek kelas dibuat.

### **Instance Objects** ###
Atribut data sesuai dengan "variabel instan" di Smalltalk, dan "anggota data" di C++. Atribut data tidak perlu dideklarasikan; seperti variabel lokal, mereka muncul saat pertama kali ditugaskan. Misalnya, jika x adalah instance MyClass yang dibuat di atas, potongan kode berikut akan mencetak nilai 16, tanpa meninggalkan jejak.