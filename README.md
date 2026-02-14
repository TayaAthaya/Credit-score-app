# Aplikasi Prediksi Kelayakan Pinjaman (Loan Prediction App)

Proyek ini bertujuan untuk membangun model klasifikasi yang dapat memprediksi status kelayakan pinjaman seorang nasabah bank. Model ini dikembangkan menggunakan teknik pembelajaran mesin (machine learning) untuk menganalisis berbagai parameter profil nasabah.

## Link Aplikasi

Aplikasi web ini dapat diakses secara publik melalui tautan berikut: [https://credit-score-app-9eufarm5jay3dhy2hbeev4.streamlit.app/]

## Ringkasan Proyek

Aplikasi ini melewati beberapa tahapan pengembangan utama:

1. **Analisis Data Eksploratif (EDA):** Memahami korelasi antar variabel.
2. **Preprocessing:** Menangani data yang hilang (missing values) dan melakukan pengkodean variabel kategori (label encoding).
3. **Pemodelan:** Melatih algoritma untuk melakukan klasifikasi status pinjaman.
4. **Deployment:** Mengimplementasikan model ke dalam antarmuka web menggunakan Streamlit.

## Fitur dan Variabel

Model memproses data masukan yang meliputi:

* **Informasi Pribadi:** Jenis kelamin, status pernikahan, jumlah tanggungan, dan tingkat pendidikan.
* **Informasi Keuangan:** Pendapatan pemohon, pendapatan penjamin, dan jumlah pinjaman yang diajukan.
* **Faktor Utama:** Riwayat kredit nasabah dan area lokasi properti.

## Teknologi

* **Bahasa:** Python
* **Library Utama:** Pandas, Scikit-Learn, Streamlit
* **Algoritma:** Random Forest Classifier
* **Platform:** GitHub & Streamlit Cloud

## Kinerja Model

Berdasarkan hasil pengujian pada data uji, model Random Forest ini mencapai tingkat akurasi sebesar 83.19%. Dari hasil analisis, variabel Riwayat Kredit teridentifikasi sebagai fitur yang paling dominan dalam menentukan keputusan akhir model.

## Cara Instalasi Lokal

1. Pastikan Python sudah terinstal di komputer Anda.
2. Clone repositori ini.
3. Instal dependensi melalui terminal:
```bash
pip install -r requirements.txt

```

4. Jalankan aplikasi dengan perintah:
```bash
streamlit run app.py

```



---

Draf ini sudah terlihat seperti dokumentasi teknis standar. Apakah ada detail teknis tertentu yang ingin kamu pertajam lagi di dalamnya?
