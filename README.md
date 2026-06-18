# etl-project-dicoding
This project implements an ETL (Extract, Transform, Load) pipeline to collect, clean, and store fashion product data from the Fashion Studio website. The pipeline automatically scrapes product information, performs data cleaning and transformation, and loads the processed data into multiple storage platforms for further analysis.

Pastikan anda sudah mendownload 'pytest', dengan menggunakan perintah berikut:

python -m pip install pytest pytest-cov

Jika menggunakan google sheets pastikan anda sudah mendownload library python dengan kode berikut:

pip install google-auth google-api-python-client

# Cara Menjalankan ETL Pipeline

Untuk menjalankan proses ETL (Extract, Transform, Load), gunakan perintah berikut di terminal:

python main.py

Perintah ini akan:

* Mengambil data dari website https://fashion-studio.dicoding.dev
* Melakukan transformasi data (cleaning, konversi harga ke rupiah, dll)
* Menyimpan hasil ke file CSV (products.csv)
* Menyimpan hasil ke Google Sheets

# Cara Menjalankan Unit Test

Untuk menjalankan unit test pada proyek ini, gunakan perintah berikut:

python -m pytest tests

Perintah ini akan menjalankan seluruh pengujian pada folder tests yang mencakup:

* test_extract.py
* test_transform.py
* test_load.py

# Cara Menjalankan Test Coverage

Untuk melihat coverage dari unit test, jalankan:

python -m coverage run -m pytest tests

Kemudian tampilkan hasil coverage dengan:

python -m coverage report

Test coverage pada proyek ini berada di atas 20% sehingga memenuhi kriteria submission.

# URL Google Sheets

Berikut adalah URL Google Sheets yang digunakan untuk menyimpan data hasil ETL:

https://docs.google.com/spreadsheets/d/1V2EcRs0n-OP7MNixN7UIf42ZqffgBD4oQGKPKx7gdY0/edit?usp=sharing

# PostgreSQL
Pastikan PostgreSQL aktif di localhost
Database: etl_db
User: postgres
Password: postgres

# Catatan Tambahan

* File google-sheets-api.json digunakan sebagai kredensial untuk mengakses Google Sheets API.
* Pastikan file tersebut berada di direktori yang sama dengan main.py.
* Pastikan Google Sheets telah diberikan akses Editor kepada service account.
* Pastikan dependencies telah diinstall sesuai dengan requirements.txt sebelum menjalankan program.
