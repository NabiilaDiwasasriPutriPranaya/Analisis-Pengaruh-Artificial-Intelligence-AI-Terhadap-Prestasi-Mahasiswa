# Analisis-Pengaruh-Artificial-Intelligence-AI-Terhadap-Prestasi-Mahasiswa

## Diskripsi
Proyek ini mengeksplorasi dampak penggunaan AI terhadap metrik akademik seperti nilai dan kehadiran mahasiswa. Proyek ini menggunakan library Python seperti Pandas, Matplotlib, Seaborn, dan Statsmodels untuk manipulasi data, visualisasi, analisis statistik, dan pemodelan regresi.

## Dataset
Proyek menggabungkan tiga dataset CSV:
- `Data_Mahasiswa.csv`: Data demografis mahasiswa.
- `Performa_Akademik.csv`: Data kinerja akademik.
- `Penggunaan_AI.csv`: Metrik penggunaan AI.

Berikut ini adalah langkah-langkah untuk menganalisis data mahasiswa berdasarkan kode Python yang telah Anda sediakan:

### Langkah-Langkah dalam Analisis Data Mahasiswa

#### 1. Persiapan Prasyarat

Pastikan Python dan pustaka yang diperlukan telah terinstal. Jika belum, instal pustaka `pandas`, `matplotlib`, `seaborn`, dan `statsmodels` dengan menggunakan perintah berikut di terminal atau command prompt:

```bash
pip install pandas matplotlib seaborn statsmodels
```

#### 2. Persiapan File yang Dibutuhkan

Pastikan semua file CSV yang diperlukan telah ada dan berada di direktori yang sama dengan script Python (`analisis_data_mahasiswa.py`):

- `Data_Mahasiswa.csv`: Data umum mahasiswa yang mencakup informasi seperti ID, nama, jurusan, dan semester.
- `Performa_Akademik.csv`: Data performa akademik yang mencakup informasi seperti waktu belajar dan nilai sebelum dan sesudah menggunakan AI.
- `Penggunaan_AI.csv`: Data penggunaan AI yang mencakup informasi seperti jam penggunaan AI per minggu.

#### 3. Menjalankan Kode

Simpan script Python berikut sebagai `analisis_data_mahasiswa.py` dan jalankan dengan perintah berikut di terminal atau command prompt:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from mpl_toolkits.mplot3d import Axes3D

# 1. Muat data dari CSV
data_mahasiswa = pd.read_csv('Data_Mahasiswa.csv')
performa_akademik = pd.read_csv('Performa_Akademik.csv')
penggunaan_ai = pd.read_csv('Penggunaan_AI.csv')

# 2. Gabungkan data
merged_data = data_mahasiswa.merge(performa_akademik, on='ID').merge(penggunaan_ai, on='ID')

# 3. Hitung perubahan nilai dan kehadiran sebelum dan sesudah penggunaan AI
merged_data['Grade_Change'] = merged_data['Grades_After'] - merged_data['Grades_Before']
merged_data['Attendance_Change'] = merged_data['Attendance_After (%)'] - merged_data['Attendance_Before (%)']

# 4. Definisikan palet warna
palette = sns.color_palette("coolwarm", as_cmap=True)

# 5. Statistik deskriptif
print("Statistik Deskriptif:")
print(merged_data.describe())

# 6. Distribusi nilai dan kehadiran sebelum dan sesudah penggunaan AI
plt.figure(figsize=(10, 5))
sns.histplot(merged_data['Grades_Before'], kde=True, color=palette(0.2), label='Nilai Sebelum', bins=10)
sns.histplot(merged_data['Grades_After'], kde=True, color=palette(0.8), label='Nilai Sesudah', bins=10)
plt.title('Distribusi Nilai Sebelum dan Sesudah Penggunaan AI')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(merged_data['Attendance_Before (%)'], kde=True, color=palette(0.2), label='Kehadiran Sebelum', bins=10)
sns.histplot(merged_data['Attendance_After (%)'], kde=True, color=palette(0.8), label='Kehadiran Sesudah', bins=10)
plt.title('Distribusi Kehadiran Sebelum dan Sesudah Penggunaan AI')
plt.xlabel('Kehadiran (%)')
plt.ylabel('Frekuensi')
plt.legend()
plt.show()

# 7. Distribusi perubahan nilai dan kehadiran
plt.figure(figsize=(10, 5))
sns.histplot(merged_data['Grade_Change'], kde=True, color=palette(0.5))
plt.title('Distribusi Perubahan Nilai Setelah Penggunaan AI')
plt.xlabel('Perubahan Nilai')
plt.ylabel('Frekuensi')
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(merged_data['Attendance_Change'], kde=True, color=palette(0.5))
plt.title('Distribusi Perubahan Kehadiran Setelah Penggunaan AI')
plt.xlabel('Perubahan Kehadiran (%)')
plt.ylabel('Frekuensi')
plt.show()

# 8. Analisis berdasarkan gender
plt.figure(figsize=(10, 5))
sns.boxplot(data=merged_data, x='Gender', y='Grade_Change', palette='coolwarm')
plt.title('Perubahan Nilai berdasarkan Gender')
plt.xlabel('Gender')
plt.ylabel('Perubahan Nilai')
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(data=merged_data, x='Gender', y='Attendance_Change', palette='coolwarm')
plt.title('Perubahan Kehadiran berdasarkan Gender')
plt.xlabel('Gender')
plt.ylabel('Perubahan Kehadiran (%)')
plt.show()

# 9. Analisis berdasarkan jurusan
plt.figure(figsize=(10, 5))
sns.boxplot(data=merged_data, x='Major', y='Grade_Change', palette='coolwarm')
plt.title('Perubahan Nilai berdasarkan Jurusan')
plt.xlabel('Jurusan')
plt.ylabel('Perubahan Nilai')
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(data=merged_data, x='Major', y='Attendance_Change', palette='coolwarm')
plt.title('Perubahan Kehadiran berdasarkan Jurusan')
plt.xlabel('Jurusan')
plt.ylabel('Perubahan Kehadiran (%)')
plt.show()

# 10. Analisis penggunaan AI terhadap perubahan nilai dan kehadiran
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(merged_data['Usage_Hours_per_Week'], merged_data['Grade_Change'], merged_data['Attendance_Change'], c=merged_data['Grade_Change'], cmap='coolwarm')
ax.set_title('Penggunaan AI vs Perubahan Nilai dan Kehadiran')
ax.set_xlabel('Jam Penggunaan AI per Minggu')
ax.set_ylabel('Perubahan Nilai')
ax.set_zlabel('Perubahan Kehadiran (%)')
fig.colorbar(scatter, ax=ax)
plt.show()

# 11. Analisis korelasi
correlation_matrix = merged_data[['Usage_Hours_per_Week', 'Grade_Change', 'Attendance_Change']].corr()
print("Matriks Korelasi:")
print(correlation_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Matriks Korelasi')
plt.show()

# 12. Analisis regresi linear sederhana
X = merged_data['Usage_Hours_per_Week']
y = merged_data['Grade_Change']
X = sm.add_constant(X)  # menambahkan konstanta
model = sm.OLS(y, X).fit()
predictions = model.predict(X)

print(model.summary())

# Plot garis regresi
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(merged_data['Usage_Hours_per_Week'], merged_data['Grade_Change'], predictions, c=merged_data['Grade_Change'], cmap='coolwarm')
ax.set_title('Penggunaan AI vs Perubahan Nilai dengan Garis Regresi')
ax.set_xlabel('Jam Penggunaan AI per Minggu')
ax.set_ylabel('Perubahan Nilai')
ax.set_zlabel('Perubahan Nilai Terprediksi')
fig.colorbar(scatter, ax=ax)
plt.show()
```

#### 4. Penjelasan Kode

- **Langkah 1-2:** Memuat dan menggabungkan data dari file CSV menjadi satu DataFrame (`merged_data`).
- **Langkah 3:** Menghitung perubahan nilai (`Grade_Change`) dan kehadiran (`Attendance_Change`) setelah penggunaan AI.
- **Langkah 4-11:** Melakukan visualisasi dan analisis berbagai aspek data, termasuk distribusi, analisis berdasarkan gender dan jurusan, analisis penggunaan AI, korelasi, dan regresi linear sederhana.
- **Langkah 12:** Menampilkan hasil regresi linear sederhana antara jam penggunaan AI per minggu dan perubahan nilai.

## Analisis dan Visualisasi

1. **Statistik Deskriptif:**
   - Menyediakan statistik ringkas dari dataset yang digabungkan.

2. **Plot Distribusi:**
   - Memvisualisasikan distribusi nilai dan kehadiran sebelum dan setelah penggunaan AI.

3. **Analisis Perubahan:**
   - Mengeksplorasi perubahan nilai dan kehadiran setelah penggunaan AI melalui histogram.

4. **Analisis Berdasarkan Gender:**
   - Menganalisis perubahan nilai dan kehadiran berdasarkan gender menggunakan boxplot.

5. **Analisis Berdasarkan Jurusan:**
   - Menyelidiki perubahan nilai dan kehadiran berdasarkan jurusan menggunakan boxplot.

6. **Analisis Penggunaan AI:**
   - Menelusuri hubungan antara jam penggunaan AI per minggu, perubahan nilai, dan perubahan kehadiran menggunakan scatter plot 3D.

7. **Analisis Korelasi:**
   - Menghitung dan memvisualisasikan matriks korelasi antara penggunaan AI, perubahan nilai, dan perubahan kehadiran.

8. **Analisis Regresi Sederhana:**
   - Melakukan regresi linier sederhana untuk memprediksi perubahan nilai berdasarkan jam penggunaan AI per minggu dan memvisualisasikan garis regresi dalam plot 3D.

## Penggunaan

Untuk menjalankan analisis:
- Pastikan Python 3.x dan library yang diperlukan telah diinstal.
- Clone repository dan navigasi ke direktori proyek.
- Jalankan skrip Python utama (`analysis.py` atau nama file pilihan Anda).

```bash
python analysis.py
```

## Persyaratan
- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- Statsmodels

Instal library yang dibutuhkan menggunakan pip:

```bash
pip install pandas matplotlib seaborn statsmodels
```
##Pertanyaan dan Jwaban
Tentu! Berikut adalah beberapa pertanyaan yang terkait dengan analisis di atas, beserta jawaban yang bisa di visualisasikan menggunakan kode tersebut:

1. **Bagaimana distribusi nilai mahasiswa sebelum dan sesudah penggunaan AI?**
   - Jawaban: Anda dapat melihat histogram distribusi nilai sebelum dan sesudah penggunaan AI pada plot `Distribution of Grades Before and After AI Usage`.

2. **Bagaimana perubahan nilai mahasiswa setelah penggunaan AI?**
   - Jawaban: Distribusi perubahan nilai mahasiswa setelah penggunaan AI dapat dilihat pada plot `Distribution of Grade Changes After AI Usage`.

3. **Bagaimana distribusi kehadiran mahasiswa sebelum dan sesudah penggunaan AI?**
   - Jawaban: Anda dapat melihat histogram distribusi kehadiran sebelum dan sesudah penggunaan AI pada plot `Distribution of Attendance Before and After AI Usage`.

4. **Bagaimana perubahan kehadiran mahasiswa setelah penggunaan AI?**
   - Jawaban: Distribusi perubahan kehadiran mahasiswa setelah penggunaan AI dapat dilihat pada plot `Distribution of Attendance Changes After AI Usage`.

5. **Apakah ada perbedaan signifikan dalam perubahan nilai berdasarkan jenis kelamin?**
   - Jawaban: Boxplot `Grade Change by Gender` menunjukkan perubahan nilai berdasarkan jenis kelamin.

6. **Apakah ada perbedaan signifikan dalam perubahan kehadiran berdasarkan jenis kelamin?**
   - Jawaban: Boxplot `Attendance Change by Gender` menunjukkan perubahan kehadiran berdasarkan jenis kelamin.

7. **Apakah ada perbedaan signifikan dalam perubahan nilai berdasarkan jurusan?**
   - Jawaban: Boxplot `Grade Change by Major` menunjukkan perubahan nilai berdasarkan jurusan.

8. **Apakah ada perbedaan signifikan dalam perubahan kehadiran berdasarkan jurusan?**
   - Jawaban: Boxplot `Attendance Change by Major` menunjukkan perubahan kehadiran berdasarkan jurusan.

9. **Bagaimana hubungan antara jam penggunaan AI per minggu dan perubahan nilai mahasiswa?**
   - Jawaban: Scatter plot 3D `AI Usage vs Grade Change and Attendance Change` menunjukkan hubungan antara jam penggunaan AI per minggu dan perubahan nilai mahasiswa.

10. **Bagaimana korelasi antara penggunaan AI, perubahan nilai, dan perubahan kehadiran?**
    - Jawaban: Matriks korelasi `Correlation Matrix` menunjukkan korelasi antara penggunaan AI, perubahan nilai, dan perubahan kehadiran.

11. **Apakah jam penggunaan AI berpengaruh signifikan terhadap perubahan nilai mahasiswa?**
    - Jawaban: Hasil analisis regresi sederhana dan plot `AI Usage vs Grade Change with Regression Line` menunjukkan apakah ada pengaruh signifikan antara jam penggunaan AI dan perubahan nilai mahasiswa.

12. **Bagaimana prediksi perubahan nilai berdasarkan jam penggunaan AI?**
    - Jawaban: Plot 3D `AI Usage vs Grade Change with Regression Line` menunjukkan garis regresi dan prediksi perubahan nilai berdasarkan jam penggunaan AI.
![F1](https://github.com/NabiilaDiwasasriPutriPranaya/Analisis-Pengaruh-Artificial-Intelligence-AI-Terhadap-Prestasi-Mahasiswa/assets/167085600/37ef4a6a-9ffc-48fa-9e46-fa4627f94ccd)
![F2](https://github.com/NabiilaDiwasasriPutriPranaya/Analisis-Pengaruh-Artificial-Intelligence-AI-Terhadap-Prestasi-Mahasiswa/assets/167085600/18622c40-88bf-4db1-bafc-f69304bd5d7c)
![F3](https://github.com/NabiilaDiwasasriPutriPranaya/Analisis-Pengaruh-Artificial-Intelligence-AI-Terhadap-Prestasi-Mahasiswa/assets/167085600/bbf6ed81-
21f0-4657-8ffc-6b13f9286d71)
![F4](https://github.com/NabiilaDiwasasriPutriPranaya/Analisis-Pengaruh-Artificial-Intelligence-AI-Terhadap-Prestasi-Mahasiswa/assets/167085600/a49ff23c-9294-4d6c-98b6-4bfd6504ff23)
![F5](https://github.com/NabiilaDiwasasriPutriPranaya/Analisis-Pengaruh-Artificial-Intelligence-AI-Terhadap-Prestasi-Mahasiswa/assets/167085600/3198ee2f-a049-4299-90a2-505b7c18905e)
![F6](https://github.com/NabiilaDiwasasriPutriPranaya/Analisis-Pengaruh-Artificial-Intelligence-AI-Terhadap-Prestasi-Mahasiswa/assets/167085600/c67c994f-1f55-444c-8c7d-599a2d58fdea)
![F7](https://github.com/NabiilaDiwasasriPutriPranaya/Analisis-Pengaruh-Artificial-Intelligence-AI-Terhadap-Prestasi-Mahasiswa/assets/167085600/59699a01-d555-44f9-a995-d69a41dec5e5)
![F8](https://github.com/NabiilaDiwasasriPutriPranaya/Analisis-Pengaruh-Artificial-Intelligence-AI-Terhadap-Prestasi-Mahasiswa/assets/167085600/a0b6531f-d56e-4434-81fd-4b7520fcb219)
![F9](https://github.com/NabiilaDiwasasriPutriPranaya/Analisis-Pengaruh-Artificial-Intelligence-AI-Terhadap-Prestasi-Mahasiswa/assets/167085600/abda2395-82b0-4cd9-93c1-5718dee5034e)
![F11](https://github.com/NabiilaDiwasasriPutriPranaya/Analisis-Pengaruh-Artificial-Intelligence-AI-Terhadap-Prestasi-Mahasiswa/assets/167085600/7fec9838-d95e-4d8e-93ee-518d3d035fd9)
![F9](https://github.com/NabiilaDiwasasriPutriPranaya/Analisis-Pengaruh-Artificial-Intelligence-AI-Terhadap-Prestasi-Mahasiswa/assets/167085600/ab8d52fc-68cc-4765-aee8-b09264191b01)
