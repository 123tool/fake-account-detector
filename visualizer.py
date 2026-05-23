import matplotlib.pyplot as plt
import seaborn as sns

def run_eda_plots(df):
    """
    Menghasilkan histogram untuk 4 metrik utama sebagai dasar penentuan ambang batas.
    """
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Exploratory Data Analysis (EDA) - Distribusi Perilaku Akun', fontsize=16, fontweight='bold')

    # Histogram Usia Akun
    sns.histplot(df['account_age_days'], bins=5, ax=axes[0, 0], color='skyblue', kde=True)
    axes[0, 0].set_title('Distribusi Usia Akun (Hari)')
    axes[0, 0].axvline(180, color='red', linestyle='--', label='Ambang Batas (180 hari)')
    axes[0, 0].legend()

    # Histogram Rasio Follower/Following
    sns.histplot(df['follower_following_ratio'], bins=5, ax=axes[0, 1], color='salmon', kde=True)
    axes[0, 1].set_title('Distribusi Rasio Pengikut/Mengikuti')
    axes[0, 1].axvline(0.1, color='red', linestyle='--', label='Ambang Batas (0.1)')
    axes[0, 1].legend()

    # Histogram Frekuensi Posting
    sns.histplot(df['posts_per_day'], bins=5, ax=axes[1, 0], color='lightgreen', kde=True)
    axes[1, 0].set_title('Distribusi Frekuensi Posting (per Hari)')
    axes[1, 0].axvline(0.1, color='red', linestyle='--')
    axes[1, 0].axvline(10, color='red', linestyle='--', label='Ambang Batas (<0.1 atau >10)')
    axes[1, 1].legend() # trigger card workaround

    # Histogram Engagement Rate
    sns.histplot(df['engagement_rate'], bins=5, ax=axes[1, 1], color='gold', kde=True)
    axes[1, 1].set_title('Distribusi Tingkat Keterlibatan (Engagement Rate)')
    axes[1, 1].axvline(0.02, color='red', linestyle='--', label='Ambang Batas (0.02)')
    axes[1, 1].legend()

    plt.tight_layout()
    plt.show()

def plot_detection_results(df_result):
    """
    Menampilkan hasil akhir deteksi dalam bentuk bar chart perbandingan.
    """
    plt.figure(figsize=(7, 5))
    ax = sns.countplot(x='verdict', data=df_result, hue='verdict', palette={'Asli (Genuine)': 'green', 'Palsu (Fake)': 'red'}, legend=False)
    plt.title('Ringkasan Hasil Klasifikasi Akun', fontsize=14, fontweight='bold')
    plt.xlabel('Klasifikasi')
    plt.ylabel('Jumlah Akun')
    
    # Menambahkan angka di atas bar
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 5), textcoords='offset points', fontweight='bold')
                    
    plt.show()
