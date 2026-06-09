# Soal 11.1
## Metode:
- Thomas Algorithm
- Penyelesaian Sistem Linear

## Penjelasan:
Program menyelesaikan sistem persamaan linear tridiagonal menggunakan operasi matriks pada NumPy.

## Output:
Nilai x1, x2, dan x3 dari sistem persamaan.

## Kesimpulan:
Sistem persamaan tridiagonal dapat diselesaikan secara efisien menggunakan metode numerik dan operasi matriks.


# Soal 11.2
## Metode:
- LU Decomposition
- Matrix Inverse

## Penjelasan:
Program menghitung invers matriks menggunakan dekomposisi LU dengan bantuan pustaka SciPy.

## Output:
Matriks invers hasil perhitungan.

## Kesimpulan:
LU Decomposition mempermudah proses pencarian invers matriks dan penyelesaian sistem linear.



# Soal 11.3
## Metode:
- Thomas Algorithm

## Penjelasan:
Program menyelesaikan sistem tridiagonal yang muncul pada metode Crank-Nicolson untuk persamaan diferensial parsial.

## Output:
Nilai temperatur T1, T2, T3, dan T4.

## Kesimpulan:
Thomas Algorithm sangat efisien untuk menyelesaikan sistem persamaan tridiagonal.



# Soal 11.4
## Metode:
- Cholesky Decomposition

## Penjelasan:
Program memverifikasi hasil dekomposisi Cholesky dengan mengalikan matriks L dan transpose-nya.

## Output:
- Matriks L
- Hasil perkalian L × LT

## Kesimpulan:
Jika hasil perkalian L × LT sama dengan matriks awal, maka dekomposisi Cholesky valid.


# Soal 11.5
## Metode:
- Cholesky Decomposition

## Penjelasan:
Program menyelesaikan sistem persamaan linear menggunakan dekomposisi Cholesky.

## Output:
Nilai solusi sistem persamaan.

## Kesimpulan:
Cholesky Decomposition memberikan solusi yang efisien untuk matriks simetris positif definit.


# Soal 11.6
## Metode:
- Cholesky Decomposition

## Penjelasan:
Program menghitung matriks segitiga bawah L dari dekomposisi Cholesky.

## Output:
Matriks L.

## Kesimpulan:
Dekomposisi Cholesky dapat digunakan untuk menyederhanakan penyelesaian sistem persamaan linear.



# Soal 11.7
## Metode:
- Cholesky Decomposition

## Penjelasan:
Program melakukan dekomposisi Cholesky pada matriks diagonal.

## Output:
Matriks hasil dekomposisi Cholesky.

## Kesimpulan:
Untuk matriks diagonal positif, hasil Cholesky berupa akar kuadrat dari elemen diagonal.



# Soal 11.8
## Metode:
- Gauss-Seidel
- Overrelaxation

## Penjelasan:
Program menyelesaikan sistem persamaan linear menggunakan metode Gauss-Seidel dengan faktor relaksasi untuk mempercepat konvergensi.

## Output:
Nilai solusi hasil iterasi.

## Kesimpulan:
Overrelaxation dapat mempercepat proses menuju solusi apabila faktor relaksasi dipilih dengan tepat.

---

# Soal 11.9
## Metode:
- Gauss-Seidel

## Penjelasan:
Program menghitung konsentrasi pada sistem reactor menggunakan metode iteratif Gauss-Seidel.

## Output:
Nilai konsentrasi akhir masing-masing variabel.

## Kesimpulan:
Metode Gauss-Seidel efektif untuk menyelesaikan sistem linear yang memenuhi syarat konvergensi.



# Soal 11.10
## Metode:
- Jacobi Iteration

## Penjelasan:
Program menyelesaikan sistem persamaan linear menggunakan metode iterasi Jacobi.

## Output:
Nilai solusi hasil iterasi.

## Kesimpulan:
Metode Jacobi menggunakan nilai iterasi sebelumnya secara penuh pada setiap langkah perhitungan.

---

# Soal 11.11
## Metode:
- Gauss-Seidel

## Penjelasan:
Program menyelesaikan sistem persamaan linear menggunakan pendekatan iteratif Gauss-Seidel.

## Output:
Nilai x1, x2, dan x3.

## Kesimpulan:
Metode Gauss-Seidel umumnya lebih cepat konvergen dibanding metode Jacobi.



# Soal 11.12
## Metode:
- Gauss-Seidel Relaxation

## Penjelasan:
Program menerapkan teknik relaksasi pada metode Gauss-Seidel untuk meningkatkan kestabilan dan kecepatan konvergensi.

## Output:
Nilai solusi iteratif.

## Kesimpulan:
Relaksasi dapat membantu mempercepat atau menstabilkan proses iterasi.


# Soal 11.13
## Metode:
- Gauss-Seidel Overrelaxation

## Penjelasan:
Program menggunakan teknik overrelaxation untuk mempercepat pencapaian solusi.

## Output:
Nilai solusi akhir.

## Kesimpulan:
Overrelaxation sering digunakan untuk mempercepat konvergensi pada sistem yang sudah konvergen.


# Soal 11.14
## Metode:
- Analisis Konvergensi
- Gauss-Seidel Method

## Penjelasan:

Metode Gauss-Seidel merupakan salah satu metode iteratif yang digunakan untuk menyelesaikan sistem persamaan linear. Berbeda dengan metode langsung seperti Eliminasi Gauss, metode ini memperoleh solusi melalui proses pendekatan bertahap (iterasi) hingga mencapai tingkat kesalahan yang dapat diterima.

Pada soal ini dilakukan analisis mengenai kondisi konvergensi metode Gauss-Seidel. Konvergensi berarti bahwa nilai hasil iterasi akan semakin mendekati solusi sebenarnya seiring bertambahnya jumlah iterasi.

Salah satu faktor yang memengaruhi konvergensi adalah bentuk matriks koefisien. Metode Gauss-Seidel umumnya akan konvergen apabila matriks memenuhi kondisi **diagonal dominance**, yaitu nilai absolut elemen diagonal pada setiap baris lebih besar daripada jumlah nilai absolut elemen lain pada baris yang sama.

Selain itu, perilaku grafik fungsi iterasi juga dapat digunakan untuk menganalisis konvergensi. Jika kemiringan (slope) fungsi iterasi berada pada rentang:

| Kondisi Slope | Perilaku Iterasi |
|--------------|------------------|
| |g'(x)| < 1 | Konvergen |
| |g'(x)| = 1 | Konvergensi sangat lambat atau osilasi |
| |g'(x)| > 1 | Divergen |

Apabila nilai slope mendekati ±1, proses iterasi dapat mengalami osilasi, yaitu nilai solusi bergerak bolak-balik tanpa segera mendekati solusi sebenarnya. Dalam beberapa kasus, osilasi ini menyebabkan metode gagal mencapai konvergensi.

## Output:

Program menampilkan penjelasan mengenai hubungan antara nilai slope dan perilaku konvergensi metode Gauss-Seidel.

## Kesimpulan:

Keberhasilan metode Gauss-Seidel sangat dipengaruhi oleh sifat matriks dan karakteristik fungsi iterasi. Jika nilai slope berada di luar rentang yang mendukung konvergensi atau matriks tidak memenuhi syarat diagonal dominance, maka solusi dapat berosilasi atau bahkan divergen. Oleh karena itu, analisis konvergensi penting dilakukan sebelum menerapkan metode iteratif pada suatu sistem persamaan.



# Soal 11.15
## Metode:
- Analisis Divergensi
- Diagonal Dominance
- Metode Iteratif

## Penjelasan:

Pada metode iteratif seperti Jacobi dan Gauss-Seidel, tidak semua sistem persamaan linear dapat diselesaikan dengan baik. Salah satu penyebab kegagalan metode iteratif adalah tidak terpenuhinya kondisi **diagonal dominance** pada matriks koefisien.

Suatu matriks dikatakan memenuhi diagonal dominance apabila untuk setiap baris berlaku:

|aᵢᵢ| > Σ|aᵢⱼ| , untuk i ≠ j

Artinya, nilai absolut elemen diagonal utama harus lebih besar dibandingkan jumlah nilai absolut elemen lain pada baris yang sama.

Kondisi ini penting karena memastikan bahwa setiap variabel memiliki pengaruh terbesar terhadap persamaan tempat variabel tersebut berada. Jika kondisi ini tidak terpenuhi, maka pengaruh variabel lain menjadi terlalu besar sehingga proses iterasi dapat menjadi tidak stabil.

Pada matriks yang tidak memenuhi diagonal dominance, kemungkinan yang dapat terjadi adalah:

1. Iterasi tidak menuju solusi yang benar.
2. Nilai solusi terus bertambah besar pada setiap iterasi.
3. Terjadi osilasi yang tidak pernah mencapai titik konvergen.
4. Galat (error) semakin meningkat seiring bertambahnya iterasi.

Sebagai contoh, jika hasil iterasi pertama menghasilkan nilai tertentu dan iterasi berikutnya justru semakin menjauh dari solusi sebenarnya, maka sistem tersebut mengalami divergensi. Dalam kondisi seperti ini, metode iteratif tidak cocok digunakan tanpa melakukan transformasi atau pengaturan ulang sistem persamaan.

Beberapa cara untuk mengatasi masalah divergensi antara lain:

- Menukar urutan persamaan agar diperoleh diagonal dominance.
- Menggunakan faktor relaksasi yang sesuai.
- Menggunakan metode langsung seperti LU Decomposition atau Cholesky Decomposition.
- Melakukan penskalaan (scaling) pada sistem persamaan.

## Output:

Program memberikan penjelasan mengenai penyebab divergensi pada metode iteratif dan hubungan antara diagonal dominance dengan kestabilan solusi.

## Kesimpulan:

Diagonal dominance merupakan salah satu syarat penting untuk menjamin konvergensi metode iteratif. Jika syarat tersebut tidak terpenuhi, maka proses iterasi berpotensi mengalami divergensi sehingga solusi yang diperoleh menjadi tidak valid. Oleh karena itu, sebelum menggunakan metode Jacobi atau Gauss-Seidel, perlu dilakukan analisis terhadap struktur matriks koefisien yang digunakan.
