## 🕵️‍♂️ Rule-Based Fake Account Detector (Modul Forensik Digital)
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
