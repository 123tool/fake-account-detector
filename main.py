import os
import pandas as pd
from detector import FakeAccountDetector
from visualizer import run_eda_plots, plot_detection_results

def main():
    print("=" * 60)
    print("  DIGITAL FORENSICS MODULE: RULE-BASED FAKE ACCOUNT DETECTOR  ")
    print("=" * 60)
    
    # 1. Validasi file dataset
    dataset_path = 'mock_data.csv'
    if not os.path.exists(dataset_path):
        print(f"[ERROR] File '{dataset_path}' tidak ditemukan!")
        print("Pastikan Anda sudah membuat file mock_data.csv di folder yang sama.")
        return

    # 2. Membaca Data
    print(f"[*] Membaca data dari {dataset_path}...")
    df = pd.read_csv(dataset_path)
    print(f"[+] Berhasil memuat {len(df)} sampel akun.\n")

    # 3. Menjalankan Exploratory Data Analysis (EDA)
    print("[*] Menampilkan grafik Exploratory Data Analysis (EDA)...")
    print("    (Tutup jendela grafik untuk melanjutkan proses deteksi forensik)")
    run_eda_plots(df)

    # 4. Inisialisasi Engine Deteksi (Threshold default = 3.0)
    detector = FakeAccountDetector(threshold=3.0)
    
    print("\n[*] Menjalankan analisis berbasis aturan (Heuristic Rules)...")
    df_analyzed = detector.analyze_dataset(df)
    
    # 5. Menampilkan Hasil Deteksi di Terminal
    print("\n" + "=" * 85)
    print(f"{'USERNAME':<22} | {'SKOR':<6} | {'KESIMPULAN':<15} | {'DETAIL POIN (Age/Ratio/Post/Eng/Pic)'}")
    print("=" * 85)
    
    for idx, row in df_analyzed.iterrows():
        # Ambil ulang breakdown poin untuk keperluan log detail
        _, breakdown = detector.evaluate_account(row)
        
        detail_str = (
            f"({breakdown['account_age_rule']:.1f} / "
            f"{breakdown['ratio_rule']:.1f} / "
            f"{breakdown['posting_freq_rule']:.1f} / "
            f"{breakdown['engagement_rule']:.1f} / "
            f"{breakdown['profile_pic_rule']:.1f})"
        )
        
        print(f"{row['username']:<22} | {row['suspicion_score']:<6.1f} | {row['verdict']:<15} | {detail_str}")
        
    print("=" * 85)

    # 6. Menampilkan Statistik Ringkas
    total_fake = (df_analyzed['verdict'] == 'Palsu (Fake)').sum()
    total_genuine = (df_analyzed['verdict'] == 'Asli (Genuine)').sum()
    print(f"\n[+] Ringkasan Analisis:")
    print(f"    - Akun Asli   : {total_genuine} akun")
    print(f"    - Akun Palsu  : {total_fake} akun")

    # 7. Visualisasi Hasil Akhir
    print("\n[*] Menampilkan grafik ringkasan klasifikasi...")
    plot_detection_results(df_analyzed)
    print("[+] Selesai. Seluruh proses forensik sukses dieksekusi!")

if __name__ == "__main__":
    main()
