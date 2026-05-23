import pandas as pd

class FakeAccountDetector:
    def __init__(self, threshold=3.0):
        self.threshold = threshold

    def evaluate_account(self, row):
        """
        Mengevaluasi satu akun berdasarkan aturan heuristik forensik digital.
        Mengembalikan total skor dan kamus detail poin breakdown.
        """
        score = 0.0
        breakdown = {}

        # 1. Usia Akun (< 180 hari) -> 1.5 Poin
        if row['account_age_days'] < 180:
            score += 1.5
            breakdown['account_age_rule'] = 1.5
        else:
            breakdown['account_age_rule'] = 0.0

        # 2. Rasio Pengikut/Mengikuti (< 0.1) -> 1.5 Poin
        if row['follower_following_ratio'] < 0.1:
            score += 1.5
            breakdown['ratio_rule'] = 1.5
        else:
            breakdown['ratio_rule'] = 0.0

        # 3. Frekuensi Posting (< 0.1 atau > 10 unggahan/hari) -> 1.5 Poin
        if row['posts_per_day'] < 0.1 or row['posts_per_day'] > 10:
            score += 1.5
            breakdown['posting_freq_rule'] = 1.5
        else:
            breakdown['posting_freq_rule'] = 0.0

        # 4. Tingkat Keterlibatan (< 0.02) -> 1.0 Poin
        if row['engagement_rate'] < 0.02:
            score += 1.0
            breakdown['engagement_rule'] = 1.0
        else:
            breakdown['engagement_rule'] = 0.0

        # 5. Gambar Profil Default (TRUE/1) -> 0.5 Poin
        if row['has_default_profile_pic'] == 1:
            score += 0.5
            breakdown['profile_pic_rule'] = 0.5
        else:
            breakdown['profile_pic_rule'] = 0.0

        return score, breakdown

    def analyze_dataset(self, df):
        """
        Menganalisis seluruh dataframe dan menambahkan kolom skor serta kesimpulan.
        """
        scores = []
        verdicts = []
        
        for idx, row in df.iterrows():
            score, _ = self.evaluate_account(row)
            scores.append(score)
            verdicts.append("Palsu (Fake)" if score >= self.threshold else "Asli (Genuine)")
            
        df_result = df.copy()
        df_result['suspicion_score'] = scores
        df_result['verdict'] = verdicts
        return df_result
