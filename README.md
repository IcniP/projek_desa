# Website Profil Desa - Projek Desa

Ini adalah proyek pengembangan website profil desa yang dibangun menggunakan framework Django. Website ini bertujuan untuk menjadi pusat informasi digital bagi desa, menampilkan profil, struktur pemerintahan, berita terbaru, serta menyediakan platform bagi UMKM lokal untuk mendaftarkan dan mempromosikan usahanya.

Proyek ini dikembangkan sebagai bagian dari tugas kelompok.

## Tech Stack (Teknologi yang Digunakan)

-   **Backend:** Python, Django
-   **Frontend:** HTML, CSS, JavaScript
-   **Database:** SQLite (default Django)

## Prerequisites (Kebutuhan Awal)

Pastikan di komputer Anda sudah terinstall perangkat lunak berikut:

-   [Python](https://www.python.org/downloads/) (Versi 3.8 atau lebih baru)
-   `pip` (biasanya sudah terinstall bersama Python)
-   [Git](https://git-scm.com/downloads/)

---

## Panduan Instalasi dan Menjalankan Proyek

Berikut adalah langkah-langkah untuk meng-clone dan menjalankan proyek ini di komputer lokal Anda.
git clone [https://github.com/IcniP/projek_desa.git](https://github.com/IcniP/projek_desa.git)
Setelah itu, masuk ke dalam folder proyek:
cd projek_desa

2. Buat dan Aktifkan Virtual Environment
Sangat disarankan untuk menggunakan virtual environment (venv) agar dependensi proyek terisolasi.

Buat venv:
py -m venv venv

Aktifkan venv:
Windows (CMD/PowerShell):
venv\Scripts\activate
macOS / Linux:
source venv/bin/activate

Setelah aktif, Anda akan melihat (venv) di awal baris terminal Anda.

3. Install Dependensi Proyek
Install semua paket Python yang dibutuhkan oleh proyek, terutama Django.
pip install django
(Catatan untuk pengembang: Sebaiknya buat file requirements.txt dengan pip freeze > requirements.txt agar orang lain bisa menginstall dengan pip install -r requirements.txt)

5. Jalankan Migrasi Database
Langkah ini akan membuat skema database (tabel-tabel) berdasarkan model yang telah didefinisikan.

py manage.py migrate
5. Buat Superuser (Admin)

Buat akun admin untuk bisa mengakses halaman Django Admin (/admin).
py manage.py createsuperuser
Ikuti instruksi untuk memasukkan username, email, dan password.

6. Jalankan Development Server
Sekarang, jalankan server pengembangan Django.
py manage.py runserver
Server akan berjalan dan Anda bisa mengakses website di browser Anda melalui alamat:
http://127.0.0.1:8000/

Untuk menghentikan server, tekan Ctrl + C di terminal.

