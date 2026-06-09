NAMA : BAGUS ALDY PUTRA
NIM : F5512510009
Kelas : Teknik Informatika A

Repository ini berisi penyelesaian Soal 11.1–11.28 menggunakan Python berdasarkan Bab 11 (Special Matrices and Gauss-Seidel) pada buku Numerical Methods for Engineers.


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

## Metode

* Analisis Konvergensi
* Metode Gauss-Seidel

## Penjelasan

Metode Gauss-Seidel merupakan salah satu metode numerik iteratif yang digunakan untuk menyelesaikan sistem persamaan linear. Berbeda dengan metode langsung seperti Eliminasi Gauss atau LU Decomposition yang menghasilkan solusi dalam sejumlah langkah tertentu, metode Gauss-Seidel memperoleh solusi melalui proses iterasi yang dilakukan berulang kali hingga mencapai tingkat galat (error) yang cukup kecil.

Pada metode ini, nilai variabel yang baru dihitung pada suatu iterasi langsung digunakan untuk menghitung variabel berikutnya dalam iterasi yang sama. Pendekatan tersebut menyebabkan metode Gauss-Seidel umumnya memiliki kecepatan konvergensi yang lebih baik dibandingkan metode Jacobi.

Konvergensi merupakan kondisi ketika hasil iterasi semakin mendekati solusi sebenarnya seiring bertambahnya jumlah iterasi. Sebaliknya, jika hasil iterasi semakin menjauh dari solusi atau berosilasi tanpa mendekati suatu nilai tertentu, maka metode dikatakan tidak konvergen atau mengalami divergensi.

Salah satu faktor utama yang menentukan keberhasilan konvergensi adalah karakteristik matriks koefisien. Metode Gauss-Seidel cenderung konvergen apabila matriks memenuhi syarat diagonal dominance, yaitu ketika nilai absolut elemen diagonal pada setiap baris lebih besar daripada jumlah nilai absolut elemen-elemen lainnya pada baris yang sama.

Selain itu, konvergensi juga dapat dianalisis melalui fungsi iterasi yang digunakan. Jika nilai turunan atau slope fungsi iterasi memiliki nilai absolut kurang dari satu, maka iterasi biasanya akan konvergen menuju solusi. Jika nilai absolut slope sama dengan satu, proses iterasi dapat mengalami osilasi atau konvergensi yang sangat lambat. Sedangkan apabila nilai absolut slope lebih besar dari satu, iterasi umumnya akan divergen dan tidak menghasilkan solusi yang stabil.

Pada kasus tertentu, nilai slope yang mendekati satu dapat menyebabkan hasil iterasi bergerak bolak-balik di sekitar solusi tanpa segera mencapainya. Fenomena ini dikenal sebagai osilasi iteratif dan dapat memperlambat proses konvergensi secara signifikan.

## Output

Program menampilkan penjelasan mengenai faktor-faktor yang memengaruhi konvergensi metode Gauss-Seidel, termasuk pengaruh diagonal dominance dan karakteristik slope fungsi iterasi.

## Kesimpulan

Keberhasilan metode Gauss-Seidel sangat bergantung pada sifat matriks koefisien dan fungsi iterasi yang digunakan. Matriks yang memenuhi diagonal dominance memiliki peluang lebih besar untuk menghasilkan konvergensi yang stabil. Sebaliknya, apabila syarat tersebut tidak terpenuhi atau nilai slope berada di luar rentang yang mendukung konvergensi, proses iterasi dapat mengalami osilasi maupun divergensi. Oleh karena itu, analisis konvergensi merupakan langkah penting sebelum menerapkan metode Gauss-Seidel pada suatu sistem persamaan linear.


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

# Soal 11.16
## Metode:
- Matrix Inverse
- Condition Number

## Penjelasan:
Program menghitung invers matriks dan condition number untuk mengevaluasi sensitivitas solusi terhadap perubahan data masukan.

## Output:
- Matriks invers
- Nilai condition number

## Kesimpulan:
Semakin besar condition number, semakin sensitif sistem terhadap kesalahan pembulatan.

---

# Soal 11.17
## Metode:
- Penyelesaian Sistem Persamaan Linear

## Penjelasan:
Program menyelesaikan sistem persamaan linear menggunakan metode eliminasi yang tersedia pada NumPy.

## Output:
Nilai variabel x1, x2, dan x3.

## Kesimpulan:
Metode langsung memberikan solusi dengan cepat dan akurat untuk sistem berukuran kecil.

---

# Soal 11.18
## Metode:
- Penyelesaian Sistem Linear

## Penjelasan:
Program menyelesaikan sistem persamaan linear tiga variabel menggunakan fungsi numpy.linalg.solve().

## Output:
Vektor solusi sistem.

## Kesimpulan:
Solusi diperoleh dengan memanfaatkan operasi matriks secara efisien.

---

# Soal 11.19
## Metode:
- Hilbert Matrix
- Condition Number

## Penjelasan:
Program membentuk matriks Hilbert dan menghitung condition number untuk melihat tingkat ill-conditioning matriks.

## Output:
- Matriks Hilbert
- Nilai condition number

## Kesimpulan:
Matriks Hilbert terkenal sebagai matriks yang sangat sensitif terhadap kesalahan numerik.

---

# Soal 11.20
## Metode:
- Vandermonde Matrix

## Penjelasan:
Program membentuk matriks Vandermonde berdasarkan sekumpulan titik data.

## Output:
Matriks Vandermonde.

## Kesimpulan:
Matriks Vandermonde sering digunakan pada interpolasi polinomial.

---

# Soal 11.21
## Metode:
- Augmented Matrix

## Penjelasan:
Program menggabungkan matriks koefisien dengan vektor konstanta menjadi matriks augmented.

## Output:
Matriks augmented [A|B].

## Kesimpulan:
Matriks augmented digunakan sebagai dasar metode eliminasi Gauss.

---

# Soal 11.22
## Metode:
- Matrix Inverse

## Penjelasan:
Program menghitung invers matriks 2×2 menggunakan NumPy.

## Output:
Matriks invers.

## Kesimpulan:
Invers matriks dapat digunakan untuk menyelesaikan sistem linear berbentuk AX = B.

---

# Soal 11.23
## Metode:
- Analisis Thomas Algorithm
- Analisis Gauss-Seidel

## Penjelasan:
Program membandingkan efisiensi Thomas Algorithm dan Gauss-Seidel untuk sistem tridiagonal.

## Output:
Penjelasan perbandingan metode.

## Kesimpulan:
Thomas Algorithm lebih efisien karena memiliki kompleksitas O(n).

---

# Soal 11.24
## Metode:
- Thomas Algorithm

## Penjelasan:
Program mengimplementasikan Thomas Algorithm secara manual untuk menyelesaikan sistem tridiagonal.

## Output:
Vektor solusi sistem.

## Kesimpulan:
Thomas Algorithm sangat efektif untuk matriks tridiagonal.

---

# Soal 11.25
## Metode:
- Cholesky Decomposition

## Penjelasan:
Program menghitung matriks segitiga bawah L dari dekomposisi Cholesky.

## Output:
Matriks L.

## Kesimpulan:
Dekomposisi Cholesky lebih efisien dibanding LU untuk matriks simetris positif definit.

---

# Soal 11.26
## Metode:
- Gauss-Seidel Iteration

## Penjelasan:
Program menyelesaikan sistem persamaan linear menggunakan metode iteratif Gauss-Seidel.

## Output:
Nilai solusi yang diperoleh setelah iterasi konvergen.

## Kesimpulan:
Metode Gauss-Seidel memberikan solusi yang baik untuk sistem yang memenuhi diagonal dominance.

---

# Soal 11.27
## Metode:
- Persamaan Diferensial Numerik
- Visualisasi Grafik

## Penjelasan:
Program mensimulasikan solusi fungsi eksponensial dan menampilkan grafik hasilnya menggunakan Matplotlib.

## Output:
Grafik hubungan x dan y.

## Kesimpulan:
Visualisasi membantu memahami perilaku solusi numerik terhadap perubahan variabel.

---

# Soal 11.28
## Metode:
- Sistem Pentadiagonal

## Penjelasan:
Program menyelesaikan sistem persamaan linear dengan matriks pentadiagonal menggunakan metode penyelesaian langsung.

## Output:
Vektor solusi sistem.

## Kesimpulan:
Sistem pentadiagonal merupakan perluasan dari sistem tridiagonal dan sering muncul pada pemodelan numerik multidimensi.
