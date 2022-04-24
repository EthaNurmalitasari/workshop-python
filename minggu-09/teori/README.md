# __Virtual Environments and Packages__ #
## __12.1. Introduction__ ##
Aplikasi Python akan sering menggunakan paket dan modul yang tidak datang sebagai bagian dari perpustakaan standar. Aplikasi terkadang memerlukan versi pustaka tertentu, karena aplikasi mungkin mengharuskan bug tertentu telah diperbaiki atau aplikasi mungkin ditulis menggunakan versi antarmuka pustaka yang sudah usang.

Ini berarti tidak mungkin satu instalasi Python memenuhi persyaratan setiap aplikasi. Jika aplikasi A membutuhkan versi 1.0 dari modul tertentu tetapi aplikasi B membutuhkan versi 2.0, maka persyaratan tersebut bertentangan dan menginstal versi 1.0 atau 2.0 akan membuat satu aplikasi tidak dapat berjalan.

Solusi untuk masalah ini adalah membuat lingkungan virtual, pohon direktori mandiri yang berisi instalasi Python untuk versi Python tertentu, ditambah sejumlah paket tambahan.

Aplikasi yang berbeda kemudian dapat menggunakan lingkungan virtual yang berbeda. Untuk mengatasi contoh sebelumnya dari persyaratan yang saling bertentangan, aplikasi A dapat memiliki lingkungan virtual sendiri dengan versi 1.0 terinstal sementara aplikasi B memiliki lingkungan virtual lain dengan versi 2.0. Jika aplikasi B memerlukan pustaka yang ditingkatkan ke versi 3.0, ini tidak akan memengaruhi lingkungan aplikasi A.

## __12.2. Creating Virtual Environments__ ##
Modul yang digunakan untuk membuat dan mengelola lingkungan virtual disebut venv. venv biasanya akan menginstal versi Python terbaru yang Anda miliki. Jika Anda memiliki beberapa versi Python di sistem Anda, Anda dapat memilih versi Python tertentu dengan menjalankan python3 atau versi mana pun yang Anda inginkan.

Untuk membuat lingkungan virtual, tentukan direktori tempat Anda ingin meletakkannya, dan jalankan modul venv sebagai skrip dengan jalur direktori:
```
python3 -m venv tutorial-env
```
Ini akan membuat direktori tutorial-env jika tidak ada, dan juga membuat direktori di dalamnya yang berisi salinan interpreter Python dan berbagai file pendukung.

Lokasi direktori umum untuk lingkungan virtual adalah `.venv`. Nama ini membuat direktori biasanya tersembunyi di shell Anda dan dengan demikian menyingkir sambil memberinya nama yang menjelaskan mengapa direktori itu ada. Ini juga mencegah bentrokan dengan file definisi variabel lingkungan .`env` yang didukung oleh beberapa perkakas.

Setelah Anda membuat lingkungan virtual, Anda dapat mengaktifkannya.

Di Windows, jalankan:
```
tutorial-env\Scripts\activate.bat
```
Di Unix atau MacOS, jalankan:
```
source tutorial-env/bin/activate
```
(Skrip ini ditulis untuk bash shell. Jika Anda menggunakan csh atau cangkang ikan, ada alternatif skrip `Activate.csh` dan `Activate.fish` yang harus Anda gunakan.)

Mengaktifkan lingkungan virtual akan mengubah prompt shell Anda untuk menunjukkan lingkungan virtual apa yang Anda gunakan, dan memodifikasi lingkungan sehingga menjalankan `python` akan memberi Anda versi tertentu dan instalasi Python. Sebagai contoh:
```python
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
...python
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>
```

## __12.3. Managing Packages with pip__ ##
Anda dapat menginstal, memutakhirkan, dan menghapus paket menggunakan program bernama pip. Secara default `pip` akan menginstal paket dari Python Package Index, <https://pypi.org>. Anda dapat menelusuri Indeks Paket Python dengan membukanya di browser web Anda.

`pip` memiliki sejumlah sub-perintah: “install”, “uninstall”, “freeze”, dll. (Lihat panduan Instalasi Modul Python untuk dokumentasi lengkap untuk `pip`.)

Anda dapat menginstal versi terbaru dari sebuah paket dengan menentukan nama paket:
```python
(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3
```
Anda juga dapat menginstal versi paket tertentu dengan memberikan nama paket diikuti dengan `==` dan nomor versi:
```python
(tutorial-env) $ python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0
```
Jika Anda menjalankan kembali perintah ini, pip akan melihat bahwa versi yang diminta sudah diinstal dan tidak melakukan apa pun. Anda dapat memberikan nomor versi yang berbeda untuk mendapatkan versi itu, atau Anda dapat menjalankan `pip install --upgrade` untuk memutakhirkan paket ke versi terbaru:
```python
(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0
```
`pip uninstall` diikuti oleh satu atau lebih nama paket akan menghapus paket dari lingkungan virtual.

`pip show` akan menampilkan informasi tentang paket tertentu:
```python
(tutorial-env) $ pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:
```
`pip list` akan menampilkan semua paket yang diinstal di lingkungan virtual:
```python
(tutorial-env) $ pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```
`pip freeze` akan menghasilkan daftar serupa dari paket yang diinstal, tetapi outputnya menggunakan format yang diharapkan oleh `pip install`. Konvensi umum adalah meletakkan daftar ini dalam file `requirements.txt`:
```python
(tutorial-env) $ pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```
`requirements.txt` kemudian dapat dikomit ke kontrol versi dan dikirimkan sebagai bagian dari aplikasi. Pengguna kemudian dapat menginstal semua paket yang diperlukan dengan `install -r`:
```python
(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0
```
pip memiliki lebih banyak opsi. Lihat panduan Instalasi Modul Python untuk dokumentasi lengkap untuk `pip`. Ketika Anda telah menulis sebuah paket dan ingin membuatnya tersedia di Python Package Index, lihat panduan Mendistribusikan Modul Python.