## 🕵️‍♂️ Based Fake Account Detector

Alat analisis berbasis aturan (*rule-based system*) yang ringan untuk mengidentifikasi akun media sosial palsu/bot menggunakan data perilaku. Alat ini dikembangkan khusus untuk keperluan **Modul Forensik Digital** sebagai sarana demonstrasi teknik deteksi praktis dan audit data perilaku tanpa bergantung pada model *Machine Learning* (ML) atau API platform pihak ketiga.

## 📝 Deskripsi Proyek

Akun palsu menimbulkan berbagai risiko keamanan digital, mulai dari penyebaran spam, penipuan finansial, hingga manipulasi opini publik melalui informasi yang salah (*misinformation*).

Aplikasi ini menggunakan pendekatan **Heuristic Rules** (sistem pakar berbasis aturan) dengan menganalisis jejak digital perilaku akun—seperti usia akun, rasio pengikut, frekuensi unggahan, tingkat interaksi, dan kelengkapan profil. Proyek ini juga dilengkapi dengan fitur **Exploratory Data Analysis (EDA)** untuk memberikan visualisasi distribusi data sebelum proses klasifikasi dilakukan, sehingga analis forensik dapat memvalidasi ketepatan ambang batas (*threshold*) aturan yang digunakan.

---

## 🧠 Kriteria Deteksi & Pembobotan Forensik
Akun akan diaudit dan diberi skor kecurigaan akumulatif. Jika total skor mencapai atau melebihi **3.0 Poin**, akun tersebut akan diklasifikasikan sebagai **"Palsu (Fake)"**.

| Metrik Penilaian | Kondisi Heuristik | Poin | Deskripsi Forensik |
| :--- | :--- | :--- | :--- |
| **Usia Akun** | `< 180 hari` | **1.5** | Akun baru sering digunakan untuk operasi kilat (hit-and-run). |
| **Rasio Pengikut** | `< 0.1` | **1.5** | Jumlah pengikut (*followers*) jauh lebih sedikit dibanding yang diikuti (*following*). |
| **Frekuensi Posting** | `< 0.1` atau `> 10` / hari | **1.5** | Akun tidak aktif sama sekali ATAU terlalu hiperaktif (indikasi bot automatisasi). |
| **Tingkat Keterlibatan** | `< 0.02` (2%) | **1.0** | Interaksi (*likes/comments*) yang sangat rendah dari audiens. |
| **Foto Profil Default** | `BENAR (True)` | **0.5** | Tidak ada kustomisasi identitas visual pada akun. |

---

## Instalasi & Penggunaan
​1. Prasyarat (Prerequisites)
​Pastikan perangkat Anda sudah terinstal Python 3.8 atau versi yang lebih baru.
​2. Kloning atau Buat Folder Proyek
​Buat folder baru di komputer Anda dan susun file sesuai dengan struktur direktori di atas.
​3. Instalasi Library Pihak Ketiga
​Buka Terminal atau Command Prompt (CMD) di dalam direktori proyek, lalu instal pustaka data science dan visualisasi yang dibutuhkan dengan perintah berikut :
```
pip install pandas matplotlib seaborn
```
4. Menjalankan Aplikasi
​Eksekusi file utama (main.py) untuk memulai proses audit forensik :
```
python main.py
```

## Alur Kerja Aplikasi Saat Dijalankan

- ​Memuat Data: Aplikasi membaca file mock_data.csv yang berisi sampel data profil media sosial.
- ​Visualisasi EDA: Jendela grafik pertama akan muncul menampilkan 4 histogram distribusi data perilaku akun. Garis putus-putus merah menandakan batas aturan forensik yang kita tetapkan. (Tutup jendela grafik ini untuk melanjutkan ke tahap deteksi).
- ​Audit Berbasis Aturan : Engine detector.py menghitung skor kecurigaan untuk setiap akun berdasarkan kriteria bobot.
- ​Laporan Terminal : Hasil klasifikasi beserta detail poin breakdown per aturan dicetak secara rapi dalam bentuk tabel di terminal.
- ​Ringkasan Hasil : Jendela grafik kedua akan muncul menampilkan bar chart komparasi jumlah akun yang teridentifikasi sebagai "Asli" versus "Palsu".
