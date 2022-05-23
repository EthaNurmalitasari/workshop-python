# **Tutorial Flaskr** #
## **Project Layout** ##
Buat direktori proyek dan masukkan:
```
 $ mkdir flask-tutorial
 $ cd flask-tutorial
```
Kemudian ikuti petunjuk instalasi untuk menyiapkan lingkungan virtual Python dan menginstal Flask untuk proyek Anda.

Tutorial akan menganggap Anda bekerja dari direktori `flask-tutorial ` mulai sekarang. Nama file di bagian atas setiap blok kode relatif terhadap direktori ini.

Aplikasi Flask bisa sesederhana dengan satu file.

hello.py
```py
from flask import Flask

 app = Flask(__name__)


 @app.route('/')
 def hello():
     return 'Hello, World!'
```
Namun, ketika sebuah proyek semakin besar, menjadi sangat sulit untuk menyimpan semua kode dalam satu file. Proyek Python menggunakan paket untuk mengatur kode menjadi beberapa modul yang dapat diimpor jika diperlukan, dan tutorial ini juga akan melakukannya.

Direktori proyek akan berisi:
- `flaskr/`, paket Python yang berisi kode aplikasi dan file Anda.
- `tes/`, direktori yang berisi modul uji.
- `venv/`, lingkungan virtual Python tempat Flask dan dependensi lainnya diinstal.
- File instalasi untuk memberi tahu Python cara menginstal proyek Anda
- Konfigurasi kontrol versi, seperti git. Anda harus membiasakan menggunakan beberapa jenis kontrol versi untuk semua proyek Anda, berapa pun ukurannya.
- File proyek lain yang mungkin Anda tambahkan di masa mendatang.

Pada akhirnya, tata letak proyek Anda akan terlihat seperti ini:
```
 /home/user/Projects/flask-tutorial
 ├── flaskr/
 │   ├── __init__.py
 │   ├── db.py
 │   ├── schema.sql
 │   ├── auth.py
 │   ├── blog.py
 │   ├── templates/
 │   │   ├── base.html
 │   │   ├── auth/
 │   │   │   ├── login.html
 │   │   │   └── register.html
 │   │   └── blog/
 │   │       ├── create.html
 │   │       ├── index.html
 │   │       └── update.html
 │   └── static/
 │       └── style.css
 ├── tests/
 │   ├── conftest.py
 │   ├── data.sql
 │   ├── test_factory.py
 │   ├── test_db.py
 │   ├── test_auth.py
 │   └── test_blog.py
 ├── venv/
 ├── setup.py
 └── MANIFEST.in
```
Jika Anda menggunakan kontrol versi, file berikut yang dihasilkan saat menjalankan proyek Anda harus diabaikan. Mungkin ada file lain berdasarkan editor yang Anda gunakan. Secara umum, abaikan file yang tidak Anda tulis. Misalnya, dengan git:

.gitignore
```
 venv/

 *.pyc
 __pycache__/

 instance/

 .pytest_cache/
 .coverage
 htmlcov/

 dist/
 build/
 *.egg-info/
```

# **Pengaturan Aplikasi** #
## **Pabrik Aplikasi** ##
Buat direktori `flaskr` dan tambahkan file `__init__.py`. `__init__.py` berfungsi ganda, hal ini akan berisi pabrik aplikasi, dan memberitahu Python bahwa direktori flaskr harus diperlakukan sebagai sebuah paket.
```
 $ mkdir flaskr
```
flaskr/init.py
```py
import os

 from flask import Flask


 def create_app(test_config=None):
     # create and configure the app
     app = Flask(__name__, instance_relative_config=True)
     app.config.from_mapping(
         SECRET_KEY='dev',
         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
     )

     if test_config is None:
         # load the instance config, if it exists, when not testing
         app.config.from_pyfile('config.py', silent=True)
     else:
         # load the test config if passed in
         app.config.from_mapping(test_config)

     # ensure the instance folder exists
     try:
         os.makedirs(app.instance_path)
     except OSError:
         pass

     # a simple page that says hello
     @app.route('/hello')
     def hello():
         return 'Hello, World!'

     return app
```

`create_app` adalah fungsi pabrik aplikasi. Anda akan menambahkannya nanti di tutorial, tetapi itu sudah banyak membantu.

1.) `app = Flask(__name__, instance_relative_config=True)` membuat instance Flask.
- `__name__` adalah nama modul Python saat ini. Aplikasi perlu mengetahui lokasinya untuk menyiapkan beberapa jalur, dan `__name__` adalah cara yang nyaman.
- `instance_relative_config=True` memberi tahu aplikasi bahwa file konfigurasi relatif terhadap folder instance. Folder instans terletak di luar paket `flaskr` dan dapat menyimpan data lokal yang tidak boleh dikomit ke kontrol versi, seperti rahasia konfigurasi dan file database.

2.) `app.config.from_mapping()` menyetel beberapa konfigurasi default yang akan digunakan aplikasi menggunakan:

- `SECRET_GUY` digunakan oleh Flask dan ekstensi untuk menjaga keamanan data. Ini disetel ke 'dev' untuk memberikan nilai yang nyaman selama pengembangan, tetapi harus diganti dengan nilai acak saat digunakan.
- `DATABASE` adalah jalur tempat file database SQLite akan disimpan. Hal tersebut di bawah app.`instance_path`, yang merupakan jalur yang telah dipilih Flask untuk folder instance.

3.) `app.config.from_pyfile()` menimpa konfigurasi default dengan nilai yang diambil dari file `config.py` di folder instance jika ada. Misalnya, saat menerapkan, ini dapat digunakan untuk mengatur `SECRET_KEY` yang sebenarnya.

- `test_config` juga dapat diteruskan ke pabrik, dan akan digunakan sebagai pengganti konfigurasi instans. Ini agar pengujian yang akan Anda tulis nanti dalam tutorial dapat dikonfigurasi secara independen dari nilai pengembangan apa pun yang telah Anda konfigurasikan.

4.) `os.makedirs()` memastikan bahwa `app.instance_path` tersedia. Flask tidak membuat folder instance secara otomatis, tetapi perlu dibuat karena proyek Anda akan membuat file database SQLite di sana.

5.) `@app.route()` membuat rute sederhana sehingga Anda dapat melihat aplikasi bekerja sebelum masuk ke tutorial selanjutnya. Hal ini membuat koneksi antara URL `/hello` dan fungsi yang mengembalikan respons, string `'Hello, World!'` pada kasus ini.

## **Jalankan Aplikasinya** ##
Sekarang Anda dapat menjalankan aplikasi Anda menggunakan perintah `flask`. Dari terminal, beri tahu Flask di mana menemukan aplikasi Anda, lalu jalankan dalam mode pengembangan. Ingat, Anda masih harus berada di direktori `tutorial flask `tingkat atas, bukan dengan paket `flaskr`.

Mode pengembangan menampilkan debugger interaktif setiap kali halaman memunculkan pengecualian, dan memulai ulang server setiap kali Anda membuat perubahan pada kode. Anda dapat membiarkannya berjalan dan hanya memuat ulang halaman browser saat Anda mengikuti tutorial.

CMD
```
 > set FLASK_APP=flaskr
 > set FLASK_ENV=development
 > flask run
```

Anda akan melihat output yang mirip dengan ini:

 * Serving Flask app "flaskr"
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 855-212-761

 Kunjungi http://127.0.0.1:5000/hello di browser dan Anda akan melihat pesan “Hello, World!”. Selamat, Anda sekarang menjalankan aplikasi web Flask Anda!

Jika program lain sudah menggunakan port 5000, Anda akan melihat OSError: [Errno 98] atau OSError: [WinError 10013] saat server mencoba memulai. Lihat Alamat untuk cara menanganinya.

# **Tentukan dan Akses Database** #
## **Hubungkan ke Database** ##
Hal pertama yang harus dilakukan ketika bekerja dengan database SQLite dan sebagian besar perpustakaan database Python lainnya adalah membuat koneksi ke database tersebut. Setiap kueri dan operasi dilakukan menggunakan koneksi, yang ditutup setelah pekerjaan selesai.

Dalam aplikasi web, koneksi ini biasanya terkait dengan permintaan. Hal itu dibuat di beberapa titik saat menangani permintaan, dan ditutup sebelum respons dikirim.

flaskr/db.py
```py
 import sqlite3

 import click
 from flask import current_app, g
 from flask.cli import with_appcontext


 def get_db():
     if 'db' not in g:
         g.db = sqlite3.connect(
             current_app.config['DATABASE'],
             detect_types=sqlite3.PARSE_DECLTYPES
         )
         g.db.row_factory = sqlite3.Row

     return g.db


 def close_db(e=None):
     db = g.pop('db', None)

     if db is not None:
         db.close()
```
g adalah objek khusus yang unik untuk setiap permintaan. Hal ini digunakan untuk menyimpan data yang mungkin diakses oleh beberapa fungsi selama permintaan. Koneksi disimpan dan digunakan kembali alih-alih membuat koneksi baru jika get_db dipanggil untuk kedua kalinya dalam permintaan yang sama.

current_app adalah objek khusus lain yang menunjuk ke aplikasi Flask yang menangani permintaan. Karena Anda menggunakan pabrik aplikasi, maka tidak ada objek aplikasi saat menulis sisa kode Anda. get_db akan dipanggil ketika aplikasi telah dibuat dan menangani permintaan, sehingga current_app dapat digunakan.

sqlite3.connect() digunakan untuk membuat koneksi ke file yang ditunjuk oleh kunci konfigurasi DATABASE. File ini tidak harus ada, dan tidak akan ada sampai Anda menginisialisasi database nanti.

## **Buat Tabel** ##
Dalam SQLite, data disimpan dalam tabel dan kolom. Hal ini perlu dibuat sebelum Anda dapat menyimpan dan mengambil data. Flaskr akan menyimpan user di tabel pengguna, dan posting di tabel post. Buat file dengan perintah SQL yang diperlukan untuk membuat tabel kosong:

flaskr/schema.sql
```sql
 DROP TABLE IF EXISTS user;
 DROP TABLE IF EXISTS post;
 
 CREATE TABLE user (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   username TEXT UNIQUE NOT NULL,
   password TEXT NOT NULL
 );

 CREATE TABLE post (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   author_id INTEGER NOT NULL,
   created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   title TEXT NOT NULL,
   body TEXT NOT NULL,
   FOREIGN KEY (author_id) REFERENCES user (id)
 );
```
Tambahkan fungsi Python yang akan menjalankan perintah SQL ini ke file db.py:

flaskr/db.py
```py
def init_db():
     db = get_db()

     with current_app.open_resource('schema.sql') as f:
         db.executescript(f.read().decode('utf8'))


 @click.command('init-db')
 @with_appcontext
 def init_db_command():
     """Clear the existing data and create new tables."""
     init_db()
     click.echo('Initialized the database.')
```

`open_resource()` membuka file relatif terhadap paket flaskr, yang berguna karena Anda tidak perlu tahu di mana lokasi itu saat menerapkan aplikasi nanti. get_db mengembalikan koneksi database, yang digunakan untuk mengeksekusi perintah yang dibaca dari file.

`click.command()` mendefinisikan perintah baris perintah yang disebut init-db yang memanggil fungsi init_db dan menunjukkan pesan sukses kepada pengguna. Anda dapat membaca Antarmuka Baris Perintah untuk mempelajari lebih lanjut tentang menulis perintah.

## **Daftar dengan Aplikasi** ##
Fungsi `close_db` dan `init_db_command` perlu didaftarkan dengan instance aplikasi. jika tidak, mereka tidak akan digunakan oleh aplikasi. Namun, karena Anda menggunakan fungsi pabrik, instans tersebut tidak tersedia saat menulis fungsi. Sebagai gantinya, tulis fungsi yang mengambil aplikasi dan melakukan pendaftaran.

flaskr/db.py
```py
 def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```

`app.teardown_appcontext()` untuk memberi tahu Flask untuk memanggil fungsi itu saat membersihkan setelah mengembalikan respons.

`app.cli.add_command()` untuk menambahkan perintah baru yang dapat dipanggil dengan perintah flask.

Impor dan panggil fungsi ini dari pabrik. Tempatkan kode baru di akhir fungsi pabrik sebelum mengembalikan aplikasi.

flaskr/init.py
```py
def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    return app
```

## **Inisialisasi File Database** ##
Sekarang init-db telah terdaftar dengan aplikasi, maka dapat dipanggil menggunakan perintah flask.

Catatan Jika Anda masih menjalankan server dari halaman sebelumnya, Anda dapat menghentikan server, atau menjalankan perintah ini di terminal baru. Jika Anda menggunakan terminal baru, ingatlah untuk mengubah direktori proyek Anda dan mengaktifkan env seperti yang dijelaskan di Instalasi. Anda juga harus mengatur `FLASK_APP` dan `FLASK_ENV` seperti yang ditunjukkan pada halaman sebelumnya.

Jalankan perintah `init-db`:
```
 $ flask init-db
 Initialized the database.
```
Sekarang akan ada file `flaskr.sqlite` di folder `instance` di proyek Anda.


# **Cetak Biru dan Tampilan** #
## **Buat Cetak Biru** ##
Cetak Biru adalah cara untuk mengatur sekelompok tampilan terkait dan kode lainnya. Daripada mendaftarkan tampilan dan kode lain secara langsung dengan aplikasi, mereka terdaftar dengan cetak biru. Kemudian cetak biru didaftarkan dengan aplikasi ketika tersedia di fungsi pabrik.

Flaskr akan memiliki dua cetak biru, satu untuk fungsi otentikasi dan satu lagi untuk fungsi posting blog. Kode untuk setiap cetak biru akan dimasukkan ke dalam modul terpisah. Karena blog perlu mengetahui tentang autentikasi, Anda akan menulis autentikasi terlebih dahulu.

flaskr/auth.py
```py
 import functools

 from flask import (
     Blueprint, flash, g, redirect, render_template, request, session, url_for
 )
 from werkzeug.security import check_password_hash, generate_password_hash

 from flaskr.db import get_db

 bp = Blueprint('auth', __name__, url_prefix='/auth')
```
Ini menciptakan Cetak Biru bernama `'auth'`. Seperti objek aplikasi, cetak biru perlu tahu di mana itu didefinisikan, jadi `__name__` diteruskan sebagai argumen kedua. `url_prefix` akan ditambahkan ke semua URL yang terkait dengan cetak biru.

Impor dan daftarkan cetak biru dari pabrik menggunakan `app.register_blueprint()`. Tempatkan kode baru di akhir fungsi pabrik sebelum mengembalikan aplikasi.

flaskr/init.py
```py
def create_app():
    app = ...
    # existing code omitted

    from . import auth
    app.register_blueprint(auth.bp)

    return app
```
Cetak biru otentikasi akan memiliki tampilan untuk mendaftarkan pengguna baru dan untuk log in dan log out.

# **Tampilan Pertama: Daftar** #
Ketika pengguna mengunjungi URL `/auth/register`, tampilan `register` akan mengembalikan HTML dengan formulir untuk mereka isi. Ketika mereka mengirimkan formulir, itu akan memvalidasi input mereka dan menampilkan formulir lagi dengan pesan kesalahan atau membuat pengguna baru dan pergi ke halaman login.

Untuk saat ini Anda hanya akan menulis kode tampilan. Pada halaman berikutnya, Anda akan menulis template untuk menghasilkan formulir HTML.

flaskr/auth.py
```py
@bp.route('/register', methods=('GET', 'POST'))
 def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')
```
Inilah yang dilakukan fungsi tampilan register: 

1.) @bp.route mengaitkan URL `/register` dengan fungsi tampilan register. Ketika Flask menerima permintaan ke `/auth/register`, ia akan memanggil tampilan register dan menggunakan nilai kembalian sebagai respons.

2.) Jika pengguna mengirimkan formulir, request.method akan menjadi 'POST'. Dalam hal ini, mulailah memvalidasi input.

3.) request.form adalah tipe khusus dari pemetaan dict yang mengirimkan kunci dan nilai formulir. Pengguna akan memasukkan username dan kata password.

4.) Pastikan username dan password tidak kosong.

5.) Jika validasi berhasil, masukkan data pengguna baru ke dalam database.

- db.execute mengambil kueri SQL dengan ? placeholder untuk setiap input pengguna, dan tupel nilai untuk menggantikan placeholder. Pustaka database akan menangani pelepasan nilai sehingga Anda tidak rentan terhadap serangan injeksi SQL.

- Untuk keamanan, kata sandi tidak boleh disimpan dalam database secara langsung. Sebagai gantinya, generate_password_hash() digunakan untuk hash kata sandi dengan aman, dan hash itu disimpan. Karena kueri ini memodifikasi data, db.commit() perlu dipanggil setelahnya untuk menyimpan perubahan.

- Sebuah sqlite3.IntegrityError akan terjadi jika nama pengguna sudah ada, yang harus ditampilkan kepada pengguna sebagai kesalahan validasi lain.

6.) Setelah menyimpan pengguna, mereka diarahkan ke halaman login. url_for() menghasilkan URL untuk tampilan login berdasarkan namanya. Ini lebih baik daripada menulis URL secara langsung karena memungkinkan Anda mengubah URL nanti tanpa mengubah semua kode yang tertaut ke sana. redirect() menghasilkan respons redirect ke URL yang dihasilkan.

7.) Jika validasi gagal, kesalahan akan ditampilkan kepada pengguna. flash() menyimpan pesan yang dapat diambil saat merender template.

8.) Ketika pengguna awalnya menavigasi ke auth/register, atau ada kesalahan validasi, halaman HTML dengan formulir pendaftaran akan ditampilkan. render_template() akan merender template yang berisi HTML, yang akan Anda tulis di langkah tutorial berikutnya.

### Login ###

This view follows the same pattern as the register view above. flaskr/auth.py
```py
 @bp.route('/login', methods=('GET', 'POST'))
 def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')
```

Ada beberapa perbedaan dari tampilan register:

1.) Pengguna ditanyai terlebih dahulu dan disimpan dalam variabel untuk digunakan nanti.

fetchone() mengembalikan satu baris dari kueri. Jika kueri tidak mengembalikan hasil, kueri mengembalikan None. Nanti, fetchall() akan digunakan, yang mengembalikan daftar semua hasil.

2.) check_password_hash() meng-hash kata sandi yang dikirimkan dengan cara yang sama seperti hash yang disimpan dan membandingkannya dengan aman. Jika cocok, kata sandi valid.

3.) session adalah dict yang menyimpan data di seluruh permintaan. Saat validasi berhasil, id pengguna disimpan di sesi baru. Data disimpan dalam cookie yang dikirim ke browser, dan browser kemudian mengirimkannya kembali dengan permintaan berikutnya. Flask menandatangani data dengan aman sehingga tidak dapat dirusak.

Sekarang id pengguna disimpan dalam sesi, itu akan tersedia pada permintaan berikutnya. Di awal setiap permintaan, jika pengguna masuk, informasi mereka harus dimuat dan tersedia untuk tampilan lain.

flaskr/auth.py
```py
@bp.before_app_request
 def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
```
`bp.before_app_request()` mendaftarkan fungsi yang berjalan sebelum fungsi tampilan, apa pun URL yang diminta. `load_logged_in_user` memeriksa apakah id pengguna disimpan dalam sesi dan mendapatkan data pengguna tersebut dari database, menyimpannya di g.user, yang berlangsung selama permintaan. Jika tidak ada id pengguna, atau jika id tidak ada, g.user akan menjadi None.

### Logout ###
Untuk keluar, Anda harus menghapus id pengguna dari session. Kemudian muat `login_in_user` tidak akan memuat pengguna pada permintaan berikutnya.

flaskr/auth.py
```py
 @bp.route('/logout')
 def logout():
    session.clear()
    return redirect(url_for('index'))
```

## **Memerlukan Otentikasi di Tampilan Lain** ##
Membuat, mengedit, dan menghapus posting blog akan mengharuskan pengguna untuk masuk. Seorang dekorator dapat digunakan untuk memeriksa ini untuk setiap tampilan yang diterapkannya.

flaskr/auth.py
```py
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
```
Dekorator ini mengembalikan fungsi tampilan baru yang membungkus tampilan asli yang diterapkannya. Fungsi baru memeriksa apakah pengguna dimuat dan dialihkan ke halaman login sebaliknya. Jika pengguna dimuat, tampilan asli dipanggil dan berlanjut secara normal. Anda akan menggunakan dekorator ini saat menulis tampilan blog.

### Titik akhir dan URL ###
Fungsi url_for() menghasilkan URL ke tampilan berdasarkan nama dan argumen. Nama yang terkait dengan tampilan juga disebut titik akhir, dan secara default sama dengan nama fungsi tampilan.

Misalnya, tampilan hello() yang ditambahkan ke pabrik aplikasi sebelumnya dalam tutorial memiliki nama 'hello' dan dapat ditautkan dengan url_for('hello'). Jika dibutuhkan argumen, yang akan Anda lihat nanti, itu akan ditautkan dengan menggunakan url_for('hello', who='World').

Saat menggunakan cetak biru, nama cetak biru didahulukan dengan nama fungsi, jadi titik akhir untuk fungsi login yang Anda tulis di atas adalah 'auth.login' karena Anda menambahkannya ke cetak biru 'auth'.

## **Templates** ##
Anda telah menulis tampilan autentikasi untuk aplikasi Anda, tetapi jika Anda menjalankan server dan mencoba membuka salah satu URL, Anda akan melihat kesalahan TemplateNotFound. Itu karena tampilan memanggil render_template(), tetapi Anda belum menulis template. File template akan disimpan di direktori templates di dalam paket flaskr.

Template adalah file yang berisi data statis serta placeholder untuk data dinamis. Sebuah template diberikan dengan data tertentu untuk menghasilkan dokumen akhir. Flask menggunakan perpustakaan template Jinja untuk merender template.

Dalam aplikasi Anda, Anda akan menggunakan template untuk merender HTML yang akan ditampilkan di browser pengguna. Di Flask, Jinja dikonfigurasi untuk autoescape data apa pun yang dirender dalam template HTML. Ini berarti aman untuk merender input pengguna; karakter apa pun yang mereka masukkan yang dapat mengacaukan HTML, seperti < dan > akan diloloskan dengan nilai aman yang terlihat sama di browser tetapi tidak menimbulkan efek yang tidak diinginkan.

Jinja terlihat dan berperilaku seperti Python. Pembatas khusus digunakan untuk membedakan sintaks Jinja dari data statis dalam template. Apa pun antara {{ dan }} adalah ekspresi yang akan menjadi output ke dokumen akhir. {% dan %} menunjukkan pernyataan aliran kontrol seperti if dan for. Tidak seperti Python, blok dilambangkan dengan tag awal dan akhir daripada lekukan karena teks statis dalam blok dapat mengubah lekukan.

### Tata Letak Dasar ###
Setiap halaman dalam aplikasi akan memiliki tata letak dasar yang sama di sekitar badan yang berbeda. Alih-alih menulis seluruh struktur HTML di setiap template, setiap template akan memperluas template dasar dan menimpa bagian tertentu.

flaskr/templates/base.html
```html
<!doctype html>
 <title>{% block title %}{% endblock %} - Flaskr</title>
 <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
 <nav>
  <h1>Flaskr</h1>
  <ul>
    {% if g.user %}
      <li><span>{{ g.user['username'] }}</span>
      <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
    {% else %}
      <li><a href="{{ url_for('auth.register') }}">Register</a>
      <li><a href="{{ url_for('auth.login') }}">Log In</a>
    {% endif %}
  </ul>
 </nav>
 <section class="content">
  <header>
    {% block header %}{% endblock %}
  </header>
  {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
  {% endfor %}
  {% block content %}{% endblock %}
 </section>
```

`g` tersedia secara otomatis di template. Berdasarkan jika `g.user` disetel (dari `load_logged_in_user)`, nama pengguna dan tautan keluar akan ditampilkan, atau tautan untuk mendaftar dan masuk akan ditampilkan. `url_for()` juga tersedia secara otomatis, dan digunakan untuk menghasilkan URL ke tampilan alih-alih menuliskannya secara manual.

Setelah judul halaman, dan sebelum konten, template mengulang setiap pesan yang dikembalikan oleh `get_flash_messages()`. Anda menggunakan flash() dalam tampilan untuk menampilkan pesan kesalahan, dan ini adalah kode yang akan menampilkannya.

Ada tiga blok yang ditentukan di sini yang akan diganti di templat lain:

1.) `{% block title %}` akan mengubah judul yang ditampilkan di tab browser dan judul jendela.

2.) `{% block header %}` mirip dengan judul tetapi akan mengubah judul yang ditampilkan pada halaman.

3.) `{% block content %}` adalah tempat isi setiap halaman pergi, seperti formulir login atau posting blog.

Template dasar berada langsung di direktori templates. Agar yang lain tetap teratur, templat untuk cetak biru akan ditempatkan di direktori dengan nama yang sama dengan cetak biru.

### Register ###
flaskr/templates/auth/register.html
```py
{% extends 'base.html' %}

 {% block header %}
  <h1>{% block title %}Register{% endblock %}</h1>
 {% endblock %}

 {% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Register">
  </form>
 {% endblock %}
```

`{% extends 'base.html' %}` memberitahu Jinja bahwa template ini harus menggantikan blok dari template dasar. Semua konten yang dirender harus muncul di dalam tag `{% block %}` yang menggantikan blok dari template dasar.

Pola berguna yang digunakan di sini adalah menempatkan `{% block title %}` di dalam `{% block header %}`. Ini akan mengatur blok judul dan kemudian menampilkan nilainya ke dalam blok header, sehingga jendela dan halaman berbagi judul yang sama tanpa menulisnya dua kali.

Tag `input` menggunakan atribut `required`.Hal ini memberitahu browser untuk tidak mengirimkan formulir sampai kolom tersebut diisi. Jika pengguna menggunakan browser lama yang tidak mendukung atribut tersebut, atau jika mereka menggunakan sesuatu selain browser untuk membuat permintaan, Anda masih ingin memvalidasi data dalam tampilan Flask. Penting untuk selalu memvalidasi data di server sepenuhnya, bahkan jika klien juga melakukan validasi.

### Log In ###
Ini identik dengan templat daftar kecuali untuk judul dan tombol kirim.

flaskr/templates/auth/login.html
```html
{% extends 'base.html' %}

 {% block header %}
  <h1>{% block title %}Log In{% endblock %}</h1>
 {% endblock %}

 {% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Log In">
  </form>
 {% endblock %}
```

## **Daftarkan Pengguna** ##
Sekarang setelah template otentikasi ditulis, Anda dapat mendaftarkan pengguna. Pastikan server masih berjalan (flask run jika tidak), lalu buka http://127.0.0.1:5000/auth/register.

Coba klik tombol "Register" tanpa mengisi formulir dan lihat bahwa browser menampilkan pesan kesalahan. Coba hapus atribut required dari template register.html dan klik "Register" lagi. Alih-alih browser menampilkan kesalahan, halaman akan dimuat ulang dan kesalahan dari flash() dalam tampilan akan ditampilkan.

Isi nama pengguna dan kata sandi dan Anda akan diarahkan ke halaman login. Coba masukkan nama pengguna yang salah, atau nama pengguna yang benar dan kata sandi yang salah. Jika Anda masuk, Anda akan mendapatkan kesalahan karena belum ada tampilan indeks untuk dialihkan

## **File Statis** ##
Tampilan dan template autentikasi berfungsi, tetapi saat ini terlihat sangat sederhana. Beberapa CSS dapat ditambahkan untuk menambahkan gaya ke tata letak HTML yang Anda buat. Gaya tidak akan berubah, jadi ini adalah file statis, bukan template.

Flask secara otomatis menambahkan tampilan `static` yang mengambil jalur relatif ke direktori `flask/static` dan menyajikannya. Template base.html sudah memiliki tautan ke file style.css:
```css
 {{ url_for('static', filename='style.css') }}
 ```

Selain CSS, jenis file statis lainnya mungkin file dengan fungsi JavaScript, atau gambar logo. Semuanya ditempatkan di bawah direktori flaskr/static dan direferensikan dengan `url_for('static', filename='...')`.

Tutorial ini tidak berfokus pada cara menulis CSS, jadi Anda cukup menyalin yang berikut ke dalam file flaskr/static/style.css:

flaskr/static/style.css
```css
 html { font-family: sans-serif; background: #eee; padding: 1rem; }
 body { max-width: 960px; margin: 0 auto; background: white; }
 h1 { font-family: serif; color: #377ba8; margin: 1rem 0; }
 a { color: #377ba8; }
 hr { border: none; border-top: 1px solid lightgray; }
 nav { background: lightgray; display: flex; align-items: center; padding: 0 0.5rem; }
 nav h1 { flex: auto; margin: 0; }
 nav h1 a { text-decoration: none; padding: 0.25rem 0.5rem; }
 nav ul  { display: flex; list-style: none; margin: 0; padding: 0; }
 nav ul li a, nav ul li span, header .action { display: block; padding: 0.5rem; }
 .content { padding: 0 1rem 1rem; }
 .content > header { border-bottom: 1px solid lightgray; display: flex; align-items: flex-end; }
 .content > header h1 { flex: auto; margin: 1rem 0 0.25rem 0; }
 .flash { margin: 1em 0; padding: 1em; background: #cae6f6; border: 1px solid #377ba8; }
 .post > header { display: flex; align-items: flex-end; font-size: 0.85em; }
 .post > header > div:first-of-type { flex: auto; }
 .post > header h1 { font-size: 1.5em; margin-bottom: 0; }
 .post .about { color: slategray; font-style: italic; }
 .post .body { white-space: pre-line; }
 .content:last-child { margin-bottom: 0; }
 .content form { margin: 1em 0; display: flex; flex-direction: column; }
 .content label { font-weight: bold; margin-bottom: 0.5em; }
 .content input, .content textarea { margin-bottom: 1em; }
 .content textarea { min-height: 12em; resize: vertical; }
 input.danger { color: #cc2f2e; }
 input[type=submit] { align-self: start; min-width: 10em; }
```

Anda dapat menemukan versi style.css yang kurang ringkas dalam kode (contoh)[https://github.com/pallets/flask/blob/2.1.2/examples/tutorial/flaskr/static/style.css].

Anda dapat membaca lebih lanjut tentang CSS untuk dokumentasi Mozilla. Jika Anda mengubah file statis, segarkan halaman browser. Jika perubahan tidak muncul, coba bersihkan cache browser Anda.

## **Cetak Biru Blog** ##
Anda akan menggunakan teknik yang sama yang Anda pelajari saat menulis cetak biru otentikasi untuk menulis cetak biru blog. Blog harus mencantumkan semua posting, mengizinkan pengguna yang masuk untuk membuat posting, dan mengizinkan penulis posting untuk mengedit atau menghapusnya.

Saat Anda menerapkan setiap tampilan, jaga agar server pengembangan tetap berjalan. Saat Anda menyimpan perubahan Anda, coba buka URL di browser Anda dan ujilah.

### Cetak Biru ###
Tentukan cetak biru dan daftarkan di pabrik aplikasi.

flaskr/blog.py
```py
 from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
 )
 from werkzeug.exceptions import abort

 from flaskr.auth import login_required
 from flaskr.db import get_db

 bp = Blueprint('blog', __name__)
```

Impor dan daftarkan cetak biru dari pabrik menggunakan `app.register_blueprint()`. Tempatkan kode baru di akhir fungsi pabrik sebelum mengembalikan aplikasi.

flaskr/init.py
```py
 def create_app():
    app = ...
    # existing code omitted

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
```

Berbeda dengan cetak biru auth, cetak biru blog tidak memiliki url_prefix. Jadi tampilan index akan berada di /, tampilan buat di /create, dan seterusnya. Blog adalah fitur utama Flaskr, jadi masuk akal jika indeks blog akan menjadi indeks utama.

Namun, titik akhir untuk tampilan index yang ditentukan di bawah ini adalah blog.index. Beberapa tampilan autentikasi mengacu pada titik akhir index biasa. app.add_url_rule() mengaitkan nama titik akhir 'index' dengan / url sehingga url_for('index') atau url_for('blog.index') akan berfungsi, menghasilkan / URL yang sama.

Di aplikasi lain Anda mungkin memberikan cetak biru blog sebuah url_prefix dan menentukan tampilan index terpisah di pabrik aplikasi, mirip dengan tampilan hello. Maka endpoint dan URL index dan blog.index akan berbeda.

### Index ###
Indeks akan menampilkan semua posting, yang terbaru terlebih dahulu. JOIN digunakan agar informasi penulis dari tabel user tersedia di hasil.

flaskr/blog.py
```py
 @bp.route('/')
 def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)
```
flaskr/templates/blog/index.html
```html
 {% extends 'base.html' %}

 {% block header %}
  <h1>{% block title %}Posts{% endblock %}</h1>
  {% if g.user %}
    <a class="action" href="{{ url_for('blog.create') }}">New</a>
  {% endif %}
 {% endblock %}

 {% block content %}
  {% for post in posts %}
    <article class="post">
      <header>
        <div>
          <h1>{{ post['title'] }}</h1>
          <div class="about">by {{ post['username'] }} on {{ post['created'].strftime('%Y-%m-%d') }}</div>
        </div>
        {% if g.user['id'] == post['author_id'] %}
          <a class="action" href="{{ url_for('blog.update', id=post['id']) }}">Edit</a>
        {% endif %}
      </header>
      <p class="body">{{ post['body'] }}</p>
    </article>
    {% if not loop.last %}
      <hr>
    {% endif %}
  {% endfor %}
 {% endblock %}
```
Saat pengguna masuk, blok header menambahkan tautan ke tampilan create. Saat pengguna adalah penulis postingan, mereka akan melihat tautan “Edit” ke tampilan update untuk postingan tersebut. loop.last adalah variabel khusus yang tersedia di dalam Jinja untuk loop. Ini digunakan untuk menampilkan baris setelah setiap posting kecuali yang terakhir, untuk memisahkannya secara visual.

### Create ###
Tampilan create bekerja sama dengan tampilan register auth. Baik formulir ditampilkan, atau data yang diposting divalidasi dan postingan ditambahkan ke database atau kesalahan ditampilkan.

Dekorator login_required yang Anda tulis sebelumnya digunakan pada tampilan blog. Seorang pengguna harus login untuk mengunjungi tampilan ini, jika tidak mereka akan diarahkan ke halaman login.

flaskr/blog.py
```py
 @bp.route('/create', methods=('GET', 'POST'))
 @login_required
 def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')
```
flaskr/templates/blog/create.html
```py
 {% extends 'base.html' %}

 {% block header %}
  <h1>{% block title %}New Post{% endblock %}</h1>
 {% endblock %}

 {% block content %}
  <form method="post">
    <label for="title">Title</label>
    <input name="title" id="title" value="{{ request.form['title'] }}" required>
    <label for="body">Body</label>
    <textarea name="body" id="body">{{ request.form['body'] }}</textarea>
    <input type="submit" value="Save">
  </form>
 {% endblock %}
```

### Update ###
Baik tampilan update dan delete perlu mengambil post dengan id dan memeriksa apakah penulisnya cocok dengan pengguna yang masuk. Untuk menghindari duplikasi kode, Anda dapat menulis fungsi untuk mendapatkan post dan memanggilnya dari setiap tampilan.

flaskr/blog.py
```py
 def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post
```

`abort()` akan memunculkan pengecualian khusus yang mengembalikan kode status HTTP. Dibutuhkan pesan opsional untuk ditampilkan dengan kesalahan, jika tidak, pesan default akan digunakan. `404` berarti "Tidak Ditemukan", dan `403` berarti "Terlarang". (401 berarti "Tidak Sah", tetapi Anda mengarahkan ulang ke halaman login alih-alih mengembalikan status itu.)

Argumen `check_author` didefinisikan sehingga fungsi tersebut dapat digunakan untuk mendapatkan `post` tanpa memeriksa penulisnya. Ini akan berguna jika Anda menulis tampilan untuk menampilkan kiriman individual di halaman, di mana pengguna tidak masalah karena mereka tidak mengubah kiriman.

flaskr/blog.py
```py
 @bp.route('/<int:id>/update', methods=('GET', 'POST'))
 @login_required
 def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)
```

Berbeda dengan tampilan yang telah Anda tulis sejauh ini, fungsi update mengambil argumen, id. Itu sesuai dengan <int:id> di rute. URL asli akan terlihat seperti /1/update. Flask akan menangkap 1, memastikan itu int, dan meneruskannya sebagai argumen id. Jika Anda tidak menentukan int: dan sebagai gantinya melakukan <id>, itu akan menjadi string. Untuk menghasilkan URL ke halaman pembaruan, url_for() harus melewati id sehingga tahu apa yang harus diisi yaitu url_for('blog.update', id=post['id']). Ini juga ada di file index.html di atas.

Tampilan create dan update terlihat sangat mirip. Perbedaan utamanya adalah tampilan update menggunakan objek post dan kueri UPDATE alih-alih INSERT. Dengan beberapa pemfaktoran ulang yang cerdas, Anda dapat menggunakan satu tampilan dan template untuk kedua tindakan, tetapi untuk tutorial lebih jelas memisahkannya.

flaskr/template/blog/update.html
```html
 {% extends 'base.html' %}

 {% block header %}
  <h1>{% block title %}Edit "{{ post['title'] }}"{% endblock %}</h1>
 {% endblock %}

 {% block content %}
  <form method="post">
    <label for="title">Title</label>
    <input name="title" id="title"
      value="{{ request.form['title'] or post['title'] }}" required>
    <label for="body">Body</label>
    <textarea name="body" id="body">{{ request.form['body'] or post['body'] }}</textarea>
    <input type="submit" value="Save">
  </form>
  <hr>
  <form action="{{ url_for('blog.delete', id=post['id']) }}" method="post">
    <input class="danger" type="submit" value="Delete" onclick="return confirm('Are you sure?');">
  </form>
 {% endblock %}
```

Template ini memiliki dua bentuk. Yang pertama memposting data yang diedit ke halaman saat ini `(/<id>/update)`. Formulir lainnya hanya berisi tombol dan menentukan atribut action yang memposting ke tampilan hapus sebagai gantinya. Tombol menggunakan beberapa JavaScript untuk menampilkan dialog konfirmasi sebelum mengirimkan.

Pola `{{ request.form['title'] atau post['title'] }}` digunakan untuk memilih data apa yang muncul di formulir. Ketika formulir belum dikirim, data post asli muncul, tetapi jika data formulir yang tidak valid telah diposting, Anda ingin menampilkannya sehingga pengguna dapat memperbaiki kesalahan, jadi `request.form` digunakan sebagai gantinya. request adalah variabel lain yang secara otomatis tersedia di template.

### Delete ###
Tampilan hapus tidak memiliki template sendiri, tombol hapus adalah bagian dari `update.html` dan posting ke `/<id>/delete` URL. Karena tidak ada template, itu hanya akan menangani metode `POST` dan kemudian mengarahkan ulang ke tampilan index.

flaskr/blog.py
```py
 @bp.route('/<int:id>/delete', methods=('POST',))
 @login_required
 def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))
```

## **Make the Project Installable** ##
Membuat proyek Anda dapat diinstal berarti Anda dapat membuat file distribusi dan menginstalnya di lingkungan lain, sama seperti Anda menginstal Flask di lingkungan proyek Anda. Ini membuat penerapan proyek Anda sama dengan menginstal pustaka lain, jadi Anda menggunakan semua alat Python standar untuk mengelola semuanya.

Menginstal juga dilengkapi dengan manfaat lain yang mungkin tidak terlihat dari tutorial atau sebagai pengguna Python baru, termasuk:

- Saat ini, Python dan Flask memahami cara menggunakan paket flaskr hanya karena Anda menjalankan dari direktori proyek Anda. Menginstal berarti Anda dapat mengimpornya dari mana pun Anda menjalankannya.

- Anda dapat mengelola dependensi proyek Anda seperti halnya paket lain, jadi pip install yourproject.whl menginstalnya.

- Alat pengujian dapat mengisolasi lingkungan pengujian Anda dari lingkungan pengembangan Anda.

## **Penjelasan Proyek** ##
File `setup.py` menjelaskan proyek Anda dan file-file miliknya.

setup.py
```py
 from setuptools import find_packages, setup

 setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
 )
```
`packages` memberi tahu Python direktori paket apa (dan file Python yang dikandungnya) untuk disertakan. `find_packages()` menemukan direktori ini secara otomatis sehingga Anda tidak perlu mengetikkannya. Untuk menyertakan file lain, seperti direktori statis dan template, `include_package_data` disetel. Python membutuhkan file lain bernama `MANIFEST.in` untuk memberi tahu apa data lain ini.

MANIFEST.in
```
 include flaskr/schema.sql
 graft flaskr/static
 graft flaskr/templates
 global-exclude *.pyc
```

Ini memberitahu Python untuk menyalin semua yang ada di direktori static dan `template`, dan file `schema.sql`, tetapi untuk mengecualikan semua file bytecode.

Lihat panduan pengemasan resmi untuk penjelasan lain tentang file dan opsi yang digunakan.

### Instal Proyek ###
Gunakan pip untuk menginstal proyek Anda di lingkungan virtual.
```
 $ pip install -e .
```

Ini memberitahu pip untuk menemukan `setup.py` di direktori saat ini dan menginstalnya dalam mode yang dapat diedit atau pengembangan. Mode yang dapat diedit berarti bahwa saat Anda membuat perubahan pada kode lokal, Anda hanya perlu menginstal ulang jika Anda mengubah metadata tentang proyek, seperti dependensinya.

Anda dapat mengamati bahwa proyek sekarang diinstal dengan `pip list`.
```
 $ pip list

 Package        Version   Location
 -------------- --------- ----------------------------------
 click          6.7
 Flask          1.0
 flaskr         1.0.0     /home/user/Projects/flask-tutorial
 itsdangerous   0.24
 Jinja2         2.10
 MarkupSafe     1.0
 pip            9.0.3
 setuptools     39.0.1
 Werkzeug       0.14.1
 wheel          0.30.0
```

Tidak ada yang berubah dari cara Anda menjalankan proyek sejauh ini. `FLASK_APP` masih disetel ke flaskr dan flask run masih menjalankan aplikasi, tetapi Anda dapat memanggilnya dari mana saja, bukan hanya direktori `flask tutorial`.

## **Cakupan Tes** ##
Menulis pengujian unit untuk aplikasi Anda memungkinkan Anda memeriksa apakah kode yang Anda tulis berfungsi seperti yang Anda harapkan. Flask menyediakan klien uji yang mensimulasikan permintaan ke aplikasi dan mengembalikan data respons.

Anda harus menguji sebanyak mungkin kode Anda. Kode dalam fungsi hanya berjalan ketika fungsi dipanggil, dan kode di cabang, seperti blok if, hanya berjalan ketika kondisi terpenuhi. Anda ingin memastikan bahwa setiap fungsi diuji dengan data yang mencakup setiap cabang.

Semakin dekat Anda mencapai cakupan 100%, semakin nyaman Anda karena membuat perubahan tidak akan secara tiba-tiba mengubah perilaku lain. Namun, cakupan 100% tidak menjamin bahwa aplikasi Anda tidak memiliki bug. Secara khusus, itu tidak menguji bagaimana pengguna berinteraksi dengan aplikasi di browser. Meskipun demikian, cakupan pengujian merupakan alat penting untuk digunakan selama pengembangan.

Anda akan menggunakan pytest dan coverage untuk menguji dan mengukur kode Anda. Instal keduanya:
```
$ pip install pytest coverage
```

## **Pengaturan dan Perlengkapan** ##
Kode tes terletak di direktori test. Direktori ini berada di sebelah paket flaskr, bukan di dalamnya. File test/conftest.py berisi fungsi pengaturan yang disebut perlengkapan yang akan digunakan setiap tes. Pengujian dalam modul Python yang dimulai dengan test_, dan setiap fungsi pengujian dalam modul tersebut juga dimulai dengan test_.

Setiap pengujian akan membuat file database sementara baru dan mengisi beberapa data yang akan digunakan dalam pengujian. Tulis file SQL untuk memasukkan data itu.

tests/data.sql
```sql
 INSERT INTO user (username, password)
 VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

 INSERT INTO post (title, body, author_id, created)
 VALUES
  ('test title', 'test' || x'0a' || 'body', 1, '2018-01-01 00:00:00');
```

Perlengkapan app akan memanggil pabrik dan lulus `test_config` untuk mengonfigurasi aplikasi dan database untuk pengujian alih-alih menggunakan konfigurasi pengembangan lokal Anda.

tests/conftest.py
```py
 import os
 import tempfile

 import pytest
 from flaskr import create_app
 from flaskr.db import get_db, init_db

 with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


 @pytest.fixture
 def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


 @pytest.fixture
 def client(app):
    return app.test_client()


 @pytest.fixture
 def runner(app):
    return app.test_cli_runner()
```
`tempfile.mkstemp()` membuat dan membuka file sementara, mengembalikan deskriptor file dan jalur ke sana. Jalur DATABASE diganti sehingga mengarah ke jalur sementara ini, bukan folder instans. Setelah mengatur jalur, tabel database dibuat dan data uji dimasukkan. Setelah tes selesai, file sementara ditutup dan dihapus.

`TESTING` memberi tahu Flask bahwa aplikasi dalam mode uji. Flask mengubah beberapa perilaku internal sehingga lebih mudah untuk diuji, dan ekstensi lain juga dapat menggunakan tanda untuk mempermudah pengujian.

Perlengkapan client memanggil `app.test_client()` dengan objek aplikasi yang dibuat oleh perlengkapan aplikasi. Pengujian akan menggunakan klien untuk membuat permintaan ke aplikasi tanpa menjalankan server.

Perlengkapan runner mirip dengan client. app.test_cli_runner() membuat runner yang dapat memanggil perintah Click yang terdaftar dengan aplikasi.

Pytest menggunakan perlengkapan dengan mencocokkan nama fungsinya dengan nama argumen dalam fungsi pengujian. Misalnya, fungsi test_hello yang akan Anda tulis selanjutnya mengambil argumen client. Pytest mencocokkannya dengan fungsi perlengkapan client, memanggilnya, dan meneruskan nilai yang dikembalikan ke fungsi pengujian.

## **Pabrik** ##
Tidak banyak yang bisa diuji tentang pabrik itu sendiri. Sebagian besar kode akan dieksekusi untuk setiap tes, jadi jika ada yang gagal, tes lain akan memperhatikan.

Satu-satunya perilaku yang dapat berubah adalah melewati konfigurasi pengujian. Jika konfigurasi tidak diteruskan, harus ada beberapa konfigurasi default, jika tidak, konfigurasi harus diganti.

tests/test_factory.py
```py
 from flaskr import create_app


 def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


 def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
```
Anda menambahkan rute `hello` sebagai contoh saat menulis pabrik di awal tutorial. Ini mengembalikan "Hello, World!", Jadi tes memeriksa apakah respon data cocok.

## **Database** ##
Dalam konteks aplikasi, `get_db` harus mengembalikan koneksi yang sama setiap kali dipanggil. Setelah konteksnya, koneksi harus ditutup.

tests/test_db.py
```py
 import sqlite3

 import pytest
 from flaskr.db import get_db


 def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)
```
Perintah `init-db` harus memanggil fungsi `init_db` dan mengeluarkan pesan.

tes/test_db.py
```py
 def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('flaskr.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called
```
Pengujian ini menggunakan perlengkapan `monkeypatch` Pytest untuk mengganti fungsi `init_db` dengan fungsi yang mencatat bahwa fungsi tersebut telah dipanggil. Perlengkapan runner yang Anda tulis di atas digunakan untuk memanggil perintah `init-db` dengan nama.

## **Autentikasi** ##
Untuk sebagian besar tampilan, pengguna harus login. Cara termudah untuk melakukan ini dalam pengujian adalah membuat permintaan POST ke tampilan login dengan klien. Daripada menuliskannya setiap saat, Anda dapat menulis kelas dengan metode untuk melakukan hal tersebut, dan menggunakan perlengkapan untuk memberikannya kepada klien untuk setiap pengujian.

tes/conftest.py
```py
 class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


 @pytest.fixture
 def auth(client):
    return AuthActions(client)
```
Dengan perlengkapan auth, Anda dapat memanggil `auth.login()` dalam pengujian untuk masuk sebagai pengguna test, yang dimasukkan sebagai bagian dari data pengujian di perlengkapan app.

Tampilan `register` harus berhasil dirender pada `GET`. Pada `POST` dengan data formulir yang valid, itu harus diarahkan ke URL login dan data pengguna harus ada di database. Data yang tidak valid harus menampilkan pesan kesalahan.

tes/test_auth.py
```py
 import pytest
 from flask import g, session
 from flaskr.db import get_db


 def test_register(client, app):
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'username': 'a', 'password': 'a'}
    )
    assert response.headers["Location"] == "/auth/login"

    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM user WHERE username = 'a'",
        ).fetchone() is not None


 @pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ('test', 'test', b'already registered'),
 ))
 def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data
```
`client.get()` membuat permintaan `GET` dan mengembalikan objek Response yang dikembalikan oleh Flask. Demikian pula, `client.post() membuat permintaan POST, mengubah data menjadi data formulir.

Untuk menguji apakah halaman berhasil dirender, permintaan sederhana dibuat dan diperiksa untuk `200 OK status_code`. Jika rendering gagal, Flask akan mengembalikan kode 500 Internal Server Error.

header akan memiliki header Location dengan URL login saat tampilan register dialihkan ke tampilan login.

data berisi badan respons sebagai byte. Jika Anda mengharapkan nilai tertentu untuk dirender di halaman, periksa apakah ada dalam data. Bytes harus dibandingkan dengan byte. Jika Anda ingin membandingkan teks, gunakan get_data(as_text=True) sebagai gantinya.

`pytest.mark.parametrize` memberi tahu Pytest untuk menjalankan fungsi pengujian yang sama dengan argumen yang berbeda. Anda menggunakannya di sini untuk menguji berbagai masukan tidak valid dan pesan kesalahan tanpa menulis kode yang sama tiga kali.

Tes untuk tampilan login sangat mirip dengan tes untuk register. Daripada menguji data dalam database, session harus memiliki user_id yang ditetapkan setelah masuk.

tes/test_auth.py
```py
 def test_login(client, auth):
    assert client.get('/auth/login').status_code == 200
    response = auth.login()
    assert response.headers["Location"] == "/"

    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'


 @pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Incorrect username.'),
    ('test', 'a', b'Incorrect password.'),
 ))
 def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data
```

Menggunakan `client` di blok `with` memungkinkan mengakses variabel konteks seperti session setelah respons dikembalikan. Biasanya, mengakses sesi di luar permintaan akan menimbulkan kesalahan.

Menguji `logout` adalah kebalikan dari `login`. session tidak boleh berisi `user_id` setelah logout.

tes/test_auth.py
```py
 def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session
```
### **Blog** ###
Semua tampilan blog menggunakan perlengkapan auth yang Anda tulis sebelumnya. Panggil `auth.login()` dan permintaan berikutnya dari klien akan masuk sebagai test pengguna.

Tampilan `index` harus menampilkan informasi tentang postingan yang ditambahkan dengan data pengujian. Saat masuk sebagai penulis, harus ada tautan untuk mengedit posting.

Anda juga dapat menguji beberapa perilaku autentikasi lagi saat menguji tampilan `index`. Saat tidak masuk, setiap halaman menampilkan tautan untuk masuk atau mendaftar. Saat masuk, ada tautan untuk keluar.

tes/tes_blog.py
```py
 import pytest
 from flaskr.db import get_db


 def test_index(client, auth):
    response = client.get('/')
    assert b"Log In" in response.data
    assert b"Register" in response.data

    auth.login()
    response = client.get('/')
    assert b'Log Out' in response.data
    assert b'test title' in response.data
    assert b'by test on 2018-01-01' in response.data
    assert b'test\nbody' in response.data
    assert b'href="/1/update"' in response.data
```
Seorang pengguna harus masuk untuk `create`, `update`, dan `delete` untuk hapus tampilan. Pengguna yang masuk harus menjadi penulis posting untuk mengakses `update` dan `delete`, jika tidak, status Terlarang 403 akan dikembalikan. Jika post dengan id yang diberikan tidak ada, update dan delete akan mengembalikan `404 Not Found`.

tes/tes_blog.py
```py
 @pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
    '/1/delete',
 ))
 def test_login_required(client, path):
    response = client.post(path)
    assert response.headers["Location"] == "/auth/login"


 def test_author_required(app, client, auth):
    # change the post author to another user
    with app.app_context():
        db = get_db()
        db.execute('UPDATE post SET author_id = 2 WHERE id = 1')
        db.commit()

    auth.login()
    # current user can't modify other user's post
    assert client.post('/1/update').status_code == 403
    assert client.post('/1/delete').status_code == 403
    # current user doesn't see edit link
    assert b'href="/1/update"' not in client.get('/').data


 @pytest.mark.parametrize('path', (
    '/2/update',
    '/2/delete',
 ))
 def test_exists_required(client, auth, path):
    auth.login()
    assert client.post(path).status_code == 404
```
Tampilan `create` dan `update` harus merender dan mengembalikan status `200 OK` untuk permintaan `GET`. Ketika data yang valid dikirim dalam permintaan `POST`, create harus memasukkan data posting baru ke dalam database, dan update harus mengubah data yang ada. Kedua halaman harus menampilkan pesan kesalahan pada data yang tidak valid.

tes/tes_blog.py
```py
 def test_create(client, auth, app):
    auth.login()
    assert client.get('/create').status_code == 200
    client.post('/create', data={'title': 'created', 'body': ''})

    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM post').fetchone()[0]
        assert count == 2


 def test_update(client, auth, app):
    auth.login()
    assert client.get('/1/update').status_code == 200
    client.post('/1/update', data={'title': 'updated', 'body': ''})

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post['title'] == 'updated'


 @pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
 ))
 def test_create_update_validate(client, auth, path):
    auth.login()
    response = client.post(path, data={'title': '', 'body': ''})
    assert b'Title is required.' in response.data
```
Tampilan `delete` harus dialihkan ke URL indeks dan pos seharusnya tidak ada lagi di database.

tes/tes_blog.py
```py
 def test_delete(client, auth, app):
    auth.login()
    response = client.post('/1/delete')
    assert response.headers["Location"] == "/"

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post is None
```

## **Menjalankan Tes** ##
Beberapa konfigurasi tambahan, yang tidak diperlukan tetapi membuat pengujian berjalan dengan cakupan yang lebih sedikit, dapat ditambahkan ke file `setup.cfg` proyek.

setup.cfg
```cfg
 [tool:pytest]
 testpaths = tests

 [coverage:run]
 branch = True
 source =
    flaskr
```

Untuk menjalankan tes, gunakan perintah pytest. Ini akan menemukan dan menjalankan semua fungsi pengujian yang telah Anda tulis.
```
 $ pytest

 ========================= test session starts ==========================
 platform linux -- Python 3.6.4, pytest-3.5.0, py-1.5.3, pluggy-0.6.0
 rootdir: /home/user/Projects/flask-tutorial, inifile: setup.cfg
 collected 23 items

 tests/test_auth.py ........                                      [ 34%]
 tests/test_blog.py ............                                  [ 86%]
 tests/test_db.py ..                                              [ 95%]
 tests/test_factory.py ..                                         [100%]

 ====================== 24 passed in 0.64 seconds =======================
```
Jika ada tes yang gagal, pytest akan menunjukkan kesalahan yang muncul. Anda dapat menjalankan `pytest -v` untuk mendapatkan daftar setiap fungsi pengujian daripada titik.

Untuk mengukur cakupan kode pengujian Anda, gunakan perintah `coverage` untuk menjalankan pytest alih-alih menjalankannya secara langsung.
```
 $ coverage run -m pytest
```
Anda dapat melihat laporan cakupan sederhana di terminal:
```
 $ coverage report

 Name                 Stmts   Miss Branch BrPart  Cover
 ------------------------------------------------------
 flaskr/__init__.py      21      0      2      0   100%
 flaskr/auth.py          54      0     22      0   100%
 flaskr/blog.py          54      0     16      0   100%
 flaskr/db.py            24      0      4      0   100%
 ------------------------------------------------------
 TOTAL                  153      0     44      0   100%
```
Laporan HTML memungkinkan Anda melihat baris mana yang tercakup dalam setiap file:
```
 $ coverage html
```
Ini menghasilkan file di direktori `htmlcov`. Buka htmlcov/index.html di browser Anda untuk melihat laporannya.

## **Terapkan ke Produksi** ##
### Bangun dan Pasang ###
Saat Anda ingin menyebarkan aplikasi Anda di tempat lain, Anda membangun file distribusi. Standar saat ini untuk distribusi Python adalah format roda, dengan ekstensi .whl. Pastikan perpustakaan roda diinstal terlebih dahulu:
```
 $ pip install wheel
```

Menjalankan setup.py dengan Python memberi Anda alat baris perintah untuk mengeluarkan perintah terkait build. Perintah bdist_wheel akan membuat file distribusi wheel.
```
 $ python setup.py bdist_wheel
```

Anda dapat menemukan file di `dist/flaskr-1.0.0-py3-none-any.whl`. Nama file dalam format {project name}-{version}-{python tag} -{abi tag}-{platform tag}.

Salin file ini ke komputer lain, siapkan virtualenv baru, lalu instal file dengan pip.
```
 $ pip install flaskr-1.0.0-py3-none-any.whl
```
Pip akan menginstal proyek Anda beserta dependensinya.

Karena ini adalah mesin yang berbeda, Anda perlu menjalankan `init-db` lagi untuk membuat database di folder instance.
```
 > set FLASK_APP=flaskr
 > flask init-db
```
Ketika Flask mendeteksi bahwa itu diinstal (tidak dalam mode yang dapat diedit), ia menggunakan direktori yang berbeda untuk folder instance. Anda dapat menemukannya di `venv/var/flaskr-instance` sebagai gantinya.

## **Konfigurasikan Kunci Rahasia** ##
di awal tutorial yang Anda berikan nilai default untuk SECRET_KEY. Ini harus diubah menjadi beberapa byte acak dalam produksi. Jika tidak, penyerang dapat menggunakan kunci 'dev' publik untuk memodifikasi cookie sesi, atau apa pun yang menggunakan kunci rahasia.

Anda dapat menggunakan perintah berikut untuk menampilkan kunci rahasia acak:
```
 $ python -c 'import secrets; print(secrets.token_hex())'

 '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
```

Buat file `config.py` di folder instance, yang akan dibaca oleh pabrik jika ada. Salin nilai yang dihasilkan ke dalamnya.

venv/var/flaskr-instance/config.py
```py
 SECRET_KEY = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823
```

Anda juga dapat mengatur konfigurasi lain yang diperlukan di sini, meskipun SECRET_KEY adalah satu-satunya yang diperlukan untuk Flaskr.

## **Jalankan dengan Server Produksi** ##
Saat menjalankan secara publik daripada dalam pengembangan, Anda tidak boleh menggunakan server pengembangan bawaan (flask run). Server pengembangan disediakan oleh Werkzeug untuk kenyamanan, tetapi tidak dirancang untuk menjadi sangat efisien, stabil, atau aman.

Sebagai gantinya, gunakan server WSGI produksi. Misalnya, untuk menggunakan Waitress, instal terlebih dahulu di lingkungan virtual:
```
 $ pip install waitress
```

Anda perlu memberi tahu Waitress tentang aplikasi Anda, tetapi itu tidak menggunakan FLASK_APP seperti yang dilakukan flask run. Anda perlu memberitahunya untuk mengimpor dan memanggil pabrik aplikasi untuk mendapatkan objek aplikasi.
```
 $ waitress-serve --call 'flaskr:create_app'

 Serving on http://0.0.0.0:8080
```
Lihat Opsi Penerapan untuk daftar berbagai cara untuk menghosting aplikasi Anda. Pelayan hanyalah sebuah contoh, dipilih untuk tutorial karena mendukung Windows dan Linux. Ada banyak lagi server WSGI dan opsi penerapan yang dapat Anda pilih untuk proyek Anda.

## **Terus Berkembang** ##
Anda telah belajar tentang beberapa konsep Flask dan Python di sepanjang tutorial. Kembali dan tinjau tutorial dan bandingkan kode Anda dengan langkah-langkah yang Anda ambil untuk sampai ke sana. Bandingkan proyek Anda dengan proyek contoh, yang mungkin terlihat sedikit berbeda karena sifat tutorial langkah demi langkah.