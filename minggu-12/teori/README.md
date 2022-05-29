# __JUPYTER__ #
## __Installing Jupyter__ ##
__JupyterLab__

Instal JupyterLab dengan pip:
```
pip install jupyterlab
```
`Catatan : Jika Anda menginstal JupyterLab dengan conda atau mamba, sebaiknya gunakan saluran conda-forge`

Setelah terinstal, luncurkan JupyterLab dengan:
```
jupyter-lab
```
__Jupyter Notebook__

Instal Notebook Jupyter klasik dengan:
```
pip install notebook
```
Untuk menjalankan buku catatan:
```
jupyter notebook
```

# __STRUKTUR DATA__ #
Mengenal Lebih Dalam Daftar List 📋

Berikut ini merupakan daftar list yang ada pada python:

`list.append(x)` berguna untuk menambahkan anggota/item ke dalam list. tepatnya pada akhir list yang fungsinya sama dengan `a[len(a):] = [x]`

`list.extend(iterable)` berfungsi untuk menambahkan list dalam 1(satu) kata dan deretan angka menjadi nilai sebuah list atau memperpanjang daftar list dengan menambahkan semua item dari iterable. Setara dengan `a[len(a):] = iterable`.

`list.insert(i, x) ` berfungsi untuk memasukkan sebuah item ke dalam list pada posisi tertentu. Argumen pertama dalam parameter i merupakan sebuah indeks jadi dapat dicontohkan `a.insert(0, x)`. kemudian juga kita dapat membuatnya seperti `a.insert(len(a), x)` hal ini setara dengan `a.append(x)`.

`list.remove(x)` berfungsi menghapus item x dari daftar list. perintah tersebut akan menampilkan output `ValueError` ketika tidak ada item pada list.

`list.pop([i])` berfungsi menghapus item pada posisi yang diberikan dalam daftar, dan dikembalikan. Jika tidak ada indeks yang ditentukan, `a.pop()` akan menghapus dan mengembalikan item terakhir dalam daftar list.

`list.clear()` berfungsi menghapus semua item dari daftar list. Hal ini setara dengan `del a[:].`

`list.index(x[, start[,end]])` berfungsi mengembalikan indeks dari 0 dalam daftar item pertama yang nilainya sama dengan x. Dalam hal ini akan menimbulkan `ValueError` jika tidak ada item seperti itu dalam list. Argumen opsional start dan end ditafsirkan seperti dalam notasi slice dan digunakan untuk membatasi pencarian ke urutan tertentu dari daftar. Indeks yang dikembalikan dihitung relatif terhadap awal urutan penuh daripada argumen start.

`list.count(x)` berfungsi mengembalikan atau menghitung nilai berapa kali item x yang muncul dalam daftar.

`list.sort(*, key=None, reverse=False)` berfungsi mengurutkan item daftar di tempat (argumen dapat digunakan untuk mengurutkan sesuai customization).

`list.reverse()` berfungsi mengembelikan elemen daftar list pada tempatnya.

`list.copy()` berfungsi mengembalikan salinan daftar list yang dangkal. Dalam hal ini sama dengan implementasi dari a[:].

Kemudian berikut ini merupakan contoh dari sebagian penggunaan dari metode daftar list:
```python
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```

Untuk metode seperti `insert`, `remove`, atau `sort` hanya mengubah daftar list tidak memiliki nilai pengembalian yang dicetak dimana nilai yang dikembalikan adalah standar `None`. Dalam hal ini prinsip desain untuk semua struktur data yang bisa berubah mutable dalam Python.

## __5.1.1. Menggunakan Daftar Lists sebagai Tumpukan (Stacks)__ ##
Stack adalah kumpulan data yang terurut sesuai bagaimana data tersebut ditambahkan atau dihapus. Proses pada stack terjadi pada satu ujung. di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil ("last-in, first-out"). Untuk menambahkan item ke atas tumpukan, gunakanlah `append()`. Kemudian untuk mengambil item dari atas tumpukan, gunakanlah `pop()` tanpa indeks eksplisit. Sebagai contoh:
```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```

## __5.1.2. Menggunakan Daftar Lists sebagai Antrian (Queues)__ ##
Queue (Antrian) adalah kumpulan data yang berurut dimana penambahan data baru berada di satu ujung bernama ekor atau rear.

Seperti halnya Stack, Dimungkinkan juga untuk menggunakan daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil ("first-in, first-out"); namun, daftar tidak efisien untuk tujuan ini. Untuk mengimplementasikan antrian, gunakan collections.deque yang dirancang untuk menambahkan dan muncul dengan cepat dari kedua ujungnya. Sebagai contoh:
```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

## __5.1.3. Daftar List (Comprehensions)__ ##
List comprehension adalah cara mudah untuk mendefinisikan dan membuat list di Python.

List comprehension terdiri dari sebuah ekspresi diikuti oleh pernyataan for yang diletakkan di dalam tanda kurung [ ].Dengan menggunakan list comprehension kita bisa membuat list secara otomatis dalam satu baris perintah saja. Ini sangat berguna jika anggota list yang hendak kita buat cukup banyak.

Misalnya, anggap kita ingin membuat daftar squares, seperti:
```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Perhatikan bahwa ini akan membuat (atau menimpa) variabel bernama x yang masih ada setelah loop selesai. Untuk itu dapat menghitung daftar squares secara ringkas tanpa efek samping menggunakan:
```python
squares = list(map(lambda x: x**2, range(10)))
```

atau
```python
squares = [x**2 for x in range(10)]
```
Pemahaman daftar list comprehension terdiri dari tanda kurung yang berisi ekspresi diikuti oleh klausa for, lalu nol atau lebih klausa for atau if. Hasilnya akan menjadi daftar baru yang dihasilkan dari mengevaluasi ekspresi dalam konteks dari klausa for dan if yang mengikutinya. Sebagai contoh, listcomp ini menggabungkan elemen dari dua daftar jika tidak sama:
```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
sama juga dengan:
```python
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
Jika ekspresi adalah tuple (mis. (x, y) dalam contoh sebelumnya), ekspresi tersebut harus diberi kurung.
```python
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1, in <module>
    [x, x**2 for x in range(6)]
               ^
SyntaxError: invalid syntax
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
Pemahaman daftar list comprehensions dapat berisi ekspresi kompleks dan fungsi bersarang seperti:
```python
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

## __5.1.4. Pemahaman Daftar List Comprehensions Bersarang (Nested)__ ##
Daftar list comprehension dapat berupa ekspresi acak arbitrary, termasuk pemahaman daftar list comprehension lainnya.

Perhatikan contoh matriks 3x4 berikut yang diimplementasikan sebagai daftar list 3 dari daftar list panjang 4:
```python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```
Daftar list comprehension berikut akan mengubah baris dan kolom:
```python
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

listcomp bersarang dievaluasi dalam konteks for yang mengikutinya, jadi contoh ini setara dengan:
```python
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
atau sama dengan:
```python
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
Ketika terdapat pernyataan aliran flow yang kompleks. Fungsi zip() akan melakukan pekerjaan yang baik untuk kasus penggunaan ini:
```python
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

## __5.2. Pernyataan del__ ##
Pernyataan del dapat digunakan untuk menghapus irisan dari daftar list atau menghapus seluruh daftar list (yang kita lakukan sebelumnya dengan menetapkan daftar kosong pada slice). Sebagai contoh:
```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

`del` juga dapat digunakan untuk menghapus seluruh variabel:
```python
>>> del a
```

## __5.3. Tuples dan Urutan Sequences__ ##
Sebuah tuple adalah urutan objek Python yang tidak berubah. Perbedaan utama antara tupel dan daftarnya adalah bahwa tupel tidak dapat diubah tidak seperti List Python. Indexing dan slicing operation merupakan contoh tipe data dari sequence. Sebuah tuple terdiri dari sejumlah nilai yang dipisahkan oleh koma, misalnya:
```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```

Seperti yang kita lihat, pada output tuple selalu ditampilkan dengan tanda kurung, Meskipun tuple mungkin mirip dengan daftar, tuple sering digunakan dalam situasi yang berbeda dan untuk tujuan yang berbeda. Tuples adalah immutable, dan biasanya berisi urutan elemen yang heterogen yang diakses melalui unpacking atau pengindeksan (atau bahkan berdasarkan atribut dalam kasus namedtuples <collections.namedtuple>). Kemudian untuk daftar adalah :term: mutable(), dan elemen-elemennya biasanya homogen dan diakses dengan menyusuri iterating daftar list.

Masalah khusus adalah pembangunan tuple yang mengandung 0 atau 1 item: sintaksis memiliki beberapa kebiasaan quirks tambahan untuk mengakomodasi ini. Tuple kosong dibangun oleh sepasang kurung kosong; tupel dengan satu item dikonstruksi dengan mengikuti nilai dengan koma (tidak cukup untuk menyertakan nilai tunggal dalam tanda kurung). tidak disarankan, tapi efektif. Sebagai contoh:
```python
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```
Sebagai contoh pernyataan `t = 12345, 54321, 'hello!'` adalah contoh dari tuple packing: nilainya 12345, 54321 dan 'hello!' dikemas bersama-sama dalam tuple. dapat juga dioperasikan terbalik seperti:
```python
>>> x, y, z = t
```
Urutan membongkar mensyaratkan bahwa ada banyak variabel di sisi kiri tanda sama dengan ada elemen dalam urutan. Perhatikan bahwa banyak tugas benar-benar hanya kombinasi dari tuple packing dan urutan pembongkaran sequence unpacking.

## __5.4. Himpunan Set__ ##
Python juga menyertakan tipe data untuk sets. Himpunan atau Set adalah koleksi yang tidak terurut tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat.

sama seperti Kurung kurawal, fungsi set() dapat digunakan untuk membuat himpunan. Catatan: untuk membuat himpunan kosong Anda harus menggunakan set(), bukan {}.

Berikut ini adalah demonstrasi singkat:
```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```
Seperti halnya untuk list comprehensions, set comprehensions juga didukung:
```python
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```

## __5.5. Kamus Dictionaries__ ##
Tipe data lain yang berguna yang dibangun ke dalam Python adalah dictionary. Kamus dictionary kadang-kadang ditemukan dalam bahasa lain sebagai "assosiative memories" atau "assosiative array". Tidak seperti urutan sequences, yang diindeks oleh sejumlah angka, kamus dictionary diindeks oleh keys, yang dapat berupa jenis apa pun yang tidak dapat diubah immutable type. string dan angka selalu bisa menjadi kunci key.

Tuples dapat digunakan sebagai kunci jika hanya berisi string, angka, atau tuple; jika sebuah tuple berisi objek yang bisa berubah baik secara langsung atau tidak langsung, itu tidak dapat digunakan sebagai kunci key. Anda tidak dapat menggunakan daftar list sebagai kunci, karena daftar dapat dimodifikasi di tempat menggunakan penugasan indeks, penugasan slice, atau metode seperti append() dan extend().

Operasi utama pada kamus dictionary adalah menyimpan nilai dengan beberapa kunci key dan mengekstraksi nilai yang diberikan kunci key. Dimungkinkan juga untuk menghapus pasangan kunci:nilai dengan del. Jika Anda menyimpan menggunakan kunci yang sudah digunakan, nilai lama yang terkait dengan kunci itu dilupakan. Merupakan kesalahan untuk mengekstraksi nilai menggunakan kunci yang tidak ada.

Ini adalah contoh kecil menggunakan kamus dictionary:
```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```
Pembangun constructor dict() membangun kamus langsung dari urutan pasangan kunci-nilai:
```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

Selain itu, pemahaman kamus dict comprehensions dapat digunakan untuk membuat kamus dictionary dari ekspresi kunci dan nilai acak arbitrary:

Ketika kunci adalah string sederhana, kadang-kadang lebih mudah untuk menentukan pasangan menggunakan argumen kata kunci keyword arguments:
```python
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

## __5.6. Teknik Perulangan__ ##
Saat mengulang kamus dictionaries, kunci key dan nilai value terkait dapat diambil pada saat yang sama menggunakan metode items().
```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```
Saat mengulang melalui urutan, indeks posisi dan nilai terkait dapat diambil pada saat yang sama menggunakan fungsi `enumerate()`.
```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```
Untuk mengulang dua urutan atau lebih secara bersamaan, entri dapat dipasangkan dengan fungsi `zip()`.
```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```
Untuk mengulang urutan secara terbalik, pertama tentukan urutan dalam arah maju dan kemudian panggil fungsi `reversed()`.
```python
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
```
Untuk mengulangi sebuah urutan sequence dalam susunan yang diurutkan, gunakan fungsi sort() yang mengembalikan daftar terurut baru dengan membiarkan sumber tidak diubah.
```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear
```
Menggunakan set() pada sebuah urutan dapat menghilangkan elemen-elemen yang duplikat. Penggunaan sorted() yang dikombinasikan dengan set() terhadap sebuah urutan merupakan cara idiomatik untuk loop dari elemen-elemen unik dari urutan yang diurutkan.
```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
```
Terkadang tergoda untuk mengubah daftar list saat Anda mengulanginya; namun, seringkali lebih mudah dan aman untuk membuat daftar list baru.
```python
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```

## __5.7. Lebih lanjut tentang Kondisi__ ##
Kondisi yang digunakan dalam pernyataan while dan if dapat berisi operator apa pun, bukan hanya perbandingan.

Perbandingan bisa dibuat berantai. Sebagai contoh, a < b == c menguji apakah a kurang dari b dan apa b sama dengan c.

Perbandingan dapat digabungkan menggunakan operator Boolean and dan or, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan not. Ini memiliki prioritas lebih rendah daripada operator pembanding; di antara mereka, not memiliki prioritas tertinggi dan or terendah, sehingga A and not B or C setara dengan (A and (not B)) or C . Seperti biasa, tanda kurung dapat digunakan untuk mengekspresikan komposisi yang diinginkan.

Operator Boolean and dan or disebut operator short-circuit: argumen mereka dievaluasi dari kiri ke kanan, dan evaluasi berhenti segera setelah hasilnya ditentukan. Misalnya, jika A dan C bernilai benar tetapi B salah, A and B and C tidak mengevaluasi ekspresi C. Ketika digunakan sebagai nilai umum dan bukan sebagai Boolean, nilai kembalian dari operator hubung singkat short-circuit adalah argumen terakhir yang dievaluasi.

Dimungkinkan untuk menetapkan hasil perbandingan atau ekspresi Boolean lainnya ke variabel. Sebagai contoh,
```python
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```
Perhatikan bahwa dalam Python, tidak seperti C, penugasan di dalam ekspresi harus dilakukan secara eksplisit dengan operator walrus :=. Ini menghindari masalah kelas umum yang dihadapi dalam program C: mengetikkan = dalam ekspresi ketika == dimaksudkan.

## __5.8. Membandingkan Urutan Sequences dan Jenis Lainnya__ ##
Objek urutan sequence biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingan menggunakan pengurutan lexicographical:

pertama, dua item pertama dibandingkan, dan jika mereka berbeda ini menentukan hasil perbandingan; jika mereka sama, dua item berikutnya dibandingkan, dan seterusnya, sampai urutan mana pun habis.

Jika dua item yang akan dibandingkan adalah urutannya sendiri dari jenis yang sama, perbandingan leksikografis dilakukan secara rekursif. Jika semua item dari dua urutan membandingkan hasilnya sama, urutannya dianggap sama.

Jika satu urutan adalah sub-urutan awal dari yang lain, urutan yang lebih pendek adalah yang lebih kecil (lebih pendek). Pengurutan leksikografis untuk string menggunakan nomor titik kode Unicode untuk mengurutkan masing-masing karakter. Beberapa contoh perbandingan antara urutan dengan tipe yang sama:
```python
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```
Perhatikan bahwa membandingkan objek dari berbagai jenis dengan < atau > adalah sah asalkan objek memiliki metode perbandingan yang sesuai. Misalnya, tipe numerik campuran dibandingkan menurut nilai numeriknya, sehingga 0 sama dengan 0.0, dll. Jika tidak, alih-alih memberikan penyusunan acak, interpreter akan memunculkan pengecualian `TypeError`.