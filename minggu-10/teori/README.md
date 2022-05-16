# __Akses ke Basis Data__ #
## __Build a Python App with CockroachDB and psycopg2__ ##
### __Buat cluster gratis__ ###
1. Jika Anda belum melakukannya, daftar akun CockroachDB Cloud.
2. Masuk ke akun Cloud CockroachDB Anda.
3. Pada halaman Cluster, klik Create Cluster.
4. Pada halaman Buat cluster Anda, pilih Tanpa Server.
Kecuali Anda mengubah anggaran bulanan, cluster ini akan gratis selamanya.
5. Klik Buat klaster.
Cluster Anda akan dibuat dalam beberapa detik dan dialog Buat pengguna SQL akan ditampilkan.

### __Buat pengguna SQL__ ###
Dialog Create SQL user memungkinkan Anda membuat pengguna dan kata sandi SQL baru.
1. Masukkan nama pengguna di bidang SQL user atau gunakan yang disediakan secara default.
2. Klik Generate & save password.
3. Salin kata sandi yang dihasilkan dan simpan di lokasi yang aman.
4. Klik Next.

### __Dapatkan sertifikat root__ ###
Dialog Connect to cluster menampilkan informasi tentang cara menghubungkan ke cluster Anda.
1. Pilih General connection string dari dropdown Select option.
2. Buka terminal baru di komputer lokal Anda, dan jalankan perintah CA Cert download command yang disediakan di bagian Download CA Cert. Driver client yang digunakan dalam tutorial ini memerlukan sertifikat ini untuk terhubung ke CockroachDB Cloud.

### __Dapatkan connection string__ ###
Buka bagian General connection string , lalu salin connection string yang disediakan dan simpan di lokasi yang aman.

Catatan : String koneksi sudah diisi sebelumnya dengan nama pengguna, kata sandi, nama cluster, dan detail lainnya. Kata sandi Anda, khususnya, hanya akan diberikan sekali. Simpan di tempat yang aman (Cockroach Labs merekomendasikan pengelola kata sandi) untuk terhubung ke cluster Anda di masa mendatang. Jika Anda lupa kata sandi, Anda dapat mengatur ulang dengan membuka halaman SQL Users.

### __Dapatkan sample code__ ###
Kloning repo Github kode sampel :

```python
$ git clone https://github.com/cockroachlabs/hello-world-python-psycopg2
```

Kode sampel di `example.py` melakukan hal berikut:

- Membuat accounts table dan menyisipkan beberapa baris
- Mentransfer dana antara dua akun dalam suatu transaksi
- Hapus akun dari tabel sebelum keluar sehingga Anda dapat menjalankan kembali `example.py`.

Untuk menangani kesalahan percobaan ulang transaksi, kode menggunakan pengulangan percobaan tingkat aplikasi yang, jika terjadi kesalahan, tidur sebelum mencoba transfer dana lagi. Jika menemukan kesalahan coba lagi, ia tidur untuk interval yang lebih lama, menerapkan backoff eksponensial.

### __Instal driver psycopg2__ ###
`psycopg2-binary` adalah satu-satunya dependensi modul pihak ketiga aplikasi sampel.

Untuk menginstal `psycopg2-binary`, jalankan perintah berikut:
```python
$ pip install psycopg2-binary
```
Untuk cara lain menginstal psycopg2, lihat official documentation.
### __Jalankan kode__ ###
1. Setel `DATABASE_URL` environment variable ke connection string ke cluster CockroachDB Cloud Anda:

```python
$ export DATABASE_URL="{connection-string}"
```

Di mana `{connection-string}` string koneksi yang Anda peroleh dari CockroachDB Cloud Console.

Aplikasi menggunakan connection string yang disimpan ke `DATABASE_URL` environment variable untuk terhubung ke cluster Anda dan mengeksekusi kode.

2. Jalankan kode :
```python
$ cd hello-world-python-psycopg2
```
```python
$ python example.py
```
Output harus menunjukkan saldo akun sebelum dan sesudah transfer dana:
```python
Balances at Sun May 15 08:11:02 2022:
(1, 1000)
(2, 250)
Balances at Sun May 15 08:11:02 2022:
(1, 900)
(2, 350)
```

## __Akses ke Basis Data CockroachDB menggunakan SQLAlchemy__ ##
### __Dapatkan sample code__ ###
Kloning repo Github kode sampel :
```
$ git clone https://github.com/cockroachlabs/example-app-python-sqlalchemy/
```
Proyek ini memiliki struktur direktori seperti berikut ini :
```
├── README.md
├── dbinit.sql
├── main.py
├── models.py
└── requirements.txt
```
File `requirements.txt` tersebut menyertakan pustaka yang diperlukan untuk terhubung ke CockroachDB dengan SQLAlchemy, termasuk sqlalchemy-cockroachdb Python package, yang menjelaskan beberapa perbedaan antara CockroachDB dan PostgreSQL :
```python
psycopg2-binary
sqlalchemy
sqlalchemy-cockroachdb
```

File `dbinit.sql` menginisialisasi skema database yang digunakan aplikasi :
```python
CREATE TABLE accounts (
    id UUID PRIMARY KEY,
    balance INT8
);
```

Menggunakan SQLAlchemy `models.py` untuk memetakan tabel Accounts ke objek Python :
```python
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Account(Base):
    """The Account class corresponds to the "accounts" database table.
    """
    __tablename__ = 'accounts'
    id = Column(UUID(as_uuid=True), primary_key=True)
    balance = Column(Integer)
```

Menggunakan SQLAlchemy `main.py` untuk memetakan metode Python ke operasi SQL :
```python
"""This simple CRUD application performs the following operations sequentially:
    1. Creates 100 new accounts with randomly generated IDs and randomly-computed balance amounts.
    2. Chooses two accounts at random and takes half of the money from the first and deposits it
     into the second.
    3. Chooses five accounts at random and deletes them.
"""

from math import floor
import os
import random
import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_cockroachdb import run_transaction
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from models import Account

# The code below inserts new accounts.


def create_accounts(session, num):
    """Create N new accounts with random account IDs and account balances.
    """
    print("Creating new accounts...")
    new_accounts = []
    while num > 0:
        account_id = uuid.uuid4()
        account_balance = floor(random.random()*1_000_000)
        new_accounts.append(Account(id=account_id, balance=account_balance))
        seen_account_ids.append(account_id)
        print(f"Created new account with id {account_id} and balance {account_balance}.")
        num = num - 1
    session.add_all(new_accounts)


def transfer_funds_randomly(session, one, two):
    """Transfer money between two accounts.
    """
    try:
        source = session.query(Account).filter(Account.id == one).one()
    except NoResultFound:
        print("No result was found")
    except MultipleResultsFound:
        print("Multiple results were found")
    dest = session.query(Account).filter(Account.id == two).first()
    print(f"Random account balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")

    amount = floor(source.balance/2)
    print(f"Transferring {amount} from account {one} to account {two}...")

    # Check balance of the first account.
    if source.balance < amount:
        raise ValueError(f"Insufficient funds in account {one}")
    source.balance -= amount
    dest.balance += amount

    print(f"Transfer complete.\nNew balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")


def delete_accounts(session, num):
    """Delete N existing accounts, at random.
    """
    print("Deleting existing accounts...")
    delete_ids = []
    while num > 0:
        delete_id = random.choice(seen_account_ids)
        delete_ids.append(delete_id)
        seen_account_ids.remove(delete_id)
        num = num - 1

    accounts = session.query(Account).filter(Account.id.in_(delete_ids)).all()

    for account in accounts:
        print(f"Deleted account {account.id}.")
        session.delete(account)


if __name__ == '__main__':
    # For cockroach demo:
    # DATABASE_URL=postgresql://demo:<demo_password>@127.0.0.1:26257?sslmode=require
    # For CockroachCloud:
    # DATABASE_URL=postgresql://<username>:<password>@<globalhost>:26257/<cluster_name>.defaultdb?sslmode=verify-full&sslrootcert=<certs_dir>/<ca.crt>
    db_uri = os.environ['DATABASE_URL'].replace("postgresql://", "cockroachdb://")
    try:
        engine = create_engine(db_uri)
    except Exception as e:
        print("Failed to connect to database.")
        print(f"{e}")

    seen_account_ids = []

    run_transaction(sessionmaker(bind=engine),
                    lambda s: create_accounts(s, 100))

    from_id = random.choice(seen_account_ids)
    to_id = random.choice([id for id in seen_account_ids if id != from_id])

    run_transaction(sessionmaker(bind=engine),
                    lambda s: transfer_funds_randomly(s, from_id, to_id))

    run_transaction(sessionmaker(bind=engine), lambda s: delete_accounts(s, 5))
```

## __Install requirements aplikasi__ ##
Tutorial ini digunakan virtualenv untuk manajemen dependency.
1. Install virtualenv :
```
$ pip install virtualenv
```
2. Di tingkat atas direktori proyek aplikasi, buat dan aktifkan virtual environment :
```
$ virtualenv env
```
```
$ source env/bin/activate
```
3. Install module yang diperlukan ke virtual environment :
```
$ pip install -r requirements.txt
```
## __Inisialisasi database__ ##
Setel `DATABASE_URL` environment variable ke connection string ke cluster Anda:
```
$ export DATABASE_URL="{connection-string}"
```
Di mana `{connection-string}` string koneksi yang Anda peroleh dari CockroachDB Cloud Console.

2. Untuk menginisialisasi database, gunakan cockroach sql perintah untuk mengeksekusi pernyataan SQL dalam file `dbinit.sql`:
```
$ cat dbinit.sql | cockroach sql --url $DATABASE_URL
```
Pernyataan SQL dalam file inisialisasi harus dijalankan akan menampilkan :
```
CREATE TABLE

Time: 102ms
```

## __Jalankan kode__  ##
File `main.py` menggunakan connection string yang disimpan ke `DATABASE_URL` environment variable untuk terhubung ke cluster Anda dan mengeksekusi kode.

Jalankan aplikasi:
```
$ python main.py
```
Aplikasi akan terhubung ke CockroachDB, dan kemudian melakukan beberapa penyisipan baris sederhana, pembaruan, dan penghapusan.

Outputnya akan terlihat seperti berikut:
```
Creating new accounts...
Created new account with id 534fe2fd-824b-4ea3-a8f8-5f7d6e8e51a3 and balance 675410.
Created new account with id 6c2d71ab-180b-4608-9045-7df461a01701 and balance 535972.
Created new account with id aed6c03b-4b4f-42d6-9c13-b7de02b528e7 and balance 817291.
...
Created new account with id a27bca32-cc27-4e23-8261-73486437943e and balance 485417.
Random account balances:
Account 5d064a2f-70a8-46b0-a141-5bf24403e705: 249601
Account 0a6c3c52-1d33-4906-8839-966e2a3e6694: 634961
Transferring 335073 from account 5d064a2f-70a8-46b0-a141-5bf24403e705 to account 0a6c3c52-1d33-4906-8839-966e2a3e6694...
Transfer complete.
New balances:
Account 5d064a2f-70a8-46b0-a141-5bf24403e705: 800977
Account 0a6c3c52-1d33-4906-8839-966e2a3e6694: 214557
Deleting existing accounts...
Deleted account b5cb0b18-520f-45db-b5ec-0141575a7536.
Deleted account 7f6361a3-1891-462e-bc6c-f289f77fd4c0.
Deleted account 6c55e9cb-71b5-46d9-8f29-644c6ba3e9d4.
Deleted account 2e20d57a-b837-499e-931f-f3140c7d2132.
Deleted account 1ff4085d-ef3f-4479-9884-1ece0f29afdf.
```

Dalam shell SQL yang terhubung ke cluster, Anda dapat memverifikasi bahwa baris berhasil dimasukkan, diperbarui, dan dihapus. Menggunakan perintah berikut :
```
SELECT COUNT(*) FROM accounts;
```
Pernyataan yang akan ditampilkan sebagai berikut :
```
  count
---------
     95
(1 row)
```