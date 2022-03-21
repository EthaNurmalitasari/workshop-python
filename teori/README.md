# **Penanganan Error dan Exception** #
Berikut ini merupakan beberapa error dalam python:

### **Syntax Errors** ###
Kesalahan sintaks, juga dikenal sebagai kesalahan penguraian, mungkin merupakan jenis keluhan paling umum yang Anda dapatkan saat Anda masih belajar Python. 

### **Exceptions** ###
Bahkan jika suatu pernyataan atau ekspresi secara sintaksis benar, hal itu dapat menyebabkan kesalahan ketika dilakukan upaya untuk mengeksekusinya. Kesalahan yang terdeteksi selama eksekusi disebut pengecualian dan tidak fatal tanpa syarat

### **Handling Exceptions** ###
Dimungkinkan untuk menulis program yang menangani pengecualian yang dipilih
Jika tidak ada pengecualian yang terjadi, klausa kecuali akan dilewati dan eksekusi pernyataan try selesai.
Jika pengecualian terjadi selama eksekusi klausa try, sisa klausa akan dilewati. Kemudian, jika tipenya cocok dengan pengecualian yang dinamai kata kunci kecuali, klausa kecuali dijalankan, dan kemudian eksekusi dilanjutkan setelah blok coba/kecuali.

### **Raising Exceptions** ###
Pernyataan raisi tertentu terjadi. Satu-satunya argumen untuk dinaikkan menunjukkan pengecualian yang akan diajukan. Ini harus berupa instance pengecualian atau kelas pengecualian (kelas yang berasal dari Pengecualian). Jika kelas pengecualian dilewatkan, itu akan secara implisit dipakai dengan memanggil konstruktornya tanpa argumen

### **Exception Chaining** ###
Pernyataan raisi memungkinkan opsional yang memungkinkan pengecualian rantai. Rantai pengecualian terjadi secara otomatis ketika pengecualian dinaikkan di dalam bagian kecuali atau akhirnya. Ini dapat dinonaktifkan dengan menggunakan dari None idiom

### **User-defined Exceptions** ###
Exceptions biasanya harus diturunkan dari kelas Exceptions, baik secara langsung maupun tidak langsung. Kelas Kelas pengecualian dapat didefinisikan yang melakukan apa pun yang dapat dilakukan kelas lain, tetapi biasanya dibuat sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan untuk Kelas pengecualian dapat didefinisikan yang melakukan apa pun yang dapat dilakukan kelas lain, tetapi biasanya dibuat sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan untuk Kelas pengecualian dapat didefinisikan yang melakukan apa pun yang dapat dilakukan kelas lain, tetapi biasanya dibuat sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan untuk Exceptions. dapat didefinisikan yang melakukan apa pun yang dapat dilakukan kelas lain, tetapi biasanya dibuat sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan untuk Exceptions.

### **Defining Clean-up Actions** ###
Pernyataan try memiliki klausa opsional lain yang dimaksudkan untuk mendefinisikan tindakan pembersihan yang harus dilakukan dalam semua keadaan. Dalam aplikasi dunia nyata, klausa last berguna untuk melepaskan sumber daya eksternal (seperti file atau koneksi jaringan), terlepas dari apakah penggunaan sumber daya itu berhasil.

### **Predefined Clean-up Actions** ###
Beberapa objek menentukan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek berhasil atau gagal.