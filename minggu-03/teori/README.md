# **STRUKTUR DATA** #
Struktur data adalah cara kita dalam menyimpan dan mengambil data. Anda mungkin sudah terbiasa dengan daftar dan kamus Python atau array Javascript dan objek. Jika demikian, Anda tahu bahwa daftar dan array berurutan dengan data yang diakses oleh indeks sementara kamus dan objek menggunakan kunci bernama untuk menyimpan dan mengambil informasi.

### **List / Daftar** ###
Berikut ini merupakan method list:
1. list.append(x)
2. list.extend(iterable)
3. list.insert(i, x)
4. list.remove(x)
5. list.pop([i])
6. list.clear()
7. list.index(x[, start[, end]])
8. list.count(x)
9. list.sort(*, key=None, reverse=False)
10. list.reverse()
11. list.copy()

### **Menggunakan Daftar Sebagai Tumpukan** ###
Metode daftar membuatnya sangat mudah untuk menggunakan daftar sebagai tumpukan, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil

### **Menggunakan Daftar Sebagai Antrian** ###
Selain menggunakan daftar sebagai tumpukan dapat juga untuk menggunakan daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil

### **Pemahaman Daftar** ###
Pemahaman daftar menyediakan cara ringkas untuk membuat daftar. Aplikasi umum adalah untuk membuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan ke setiap anggota dari urutan lain

### **Pemahaman Daftar Bersarang** ###
Ekspresi awal dalam pemahaman daftar dapat berupa ekspresi arbitrer, termasuk pemahaman daftar lainnya.

### **Del Statements** ###
Pernyataan del juga dapat digunakan untuk menghapus irisan dari daftar atau menghapus seluruh daftar (yang kita lakukan sebelumnya dengan menetapkan daftar kosong ke irisan)

### **Tuples & Sequences** ###
Tuple adalah kumpulan objek yang dipesan dan tidak dapat diubah. Tuple adalah urutan, seperti halnya daftar. Perbedaan antara tupel dan daftar adalah, tupel tidak dapat diubah tidak seperti daftar dan tupel menggunakan tanda kurung, sedangkan daftar menggunakan tanda kurung siku

### **Sets** ###
Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Set objek juga mendukung operasi matematika seperti serikat pekerja, persimpangan, perbedaan, dan perbedaan simetris.
Kurung kurawal atau fungsi set() dapat digunakan untuk membuat set.

### **Dictionaries** ###
Operasi utama pada kamus adalah menyimpan nilai dengan beberapa kunci dan mengekstrak nilai yang diberikan kunci tersebut.
Melakukan list(d) pada kamus mengembalikan daftar semua kunci yang digunakan dalam kamus, dalam urutan penyisipan

### **Looping Techniques** ###
Saat mengulang dictionary, kunci dan nilai yang sesuai dapat diambil secara bersamaan menggunakan metode items()

### **More on Conditions** ###
Kondisi yang digunakan dalam pernyataan while dan if dapat berisi operator apa saja, bukan hanya perbandingan. Perbandingan dapat digabungkan menggunakan operator Boolean dan dan atau, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan not.

### **Comparing Sequences and Other Types** ###
Objek urutan biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingan menggunakan urutan leksikografis: pertama dua item pertama dibandingkan, dan jika berbeda, ini menentukan hasil perbandingan; jika mereka sama, dua item berikutnya dibandingkan, dan seterusnya, sampai salah satu urutan habis.