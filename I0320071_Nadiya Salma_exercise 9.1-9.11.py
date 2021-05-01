# nomer 9.1
import sys

# mendefinisikan array konstan
HARI = ('Minggu','Senin','Selasa','Rabu','Kamis','Jumat','Sabtu')

def main():
    # meminta user memasukkan nomor hari
    nohari = int(input("Masukkan nomor hari [1..7]: "))

    if (nohari < 1) or (nohari > 7):
        print("Tidak ada hari ke-%s" % nohari)
        sys.exit(1)
    print("Hari ke-%d adalah %s" % (nohari,HARI[nohari-1]))

if __name__ == "__main__":
    main()


# nomer 9.2
import sys

# mendefinisikan array asosiatif
KAMUS = {
    "one": "satu",
    "two": "dua",
    "three": "tiga",
    "four": "empat",
    "five": "lima",
    "six": "enam",
    "seven": "tujuh",
    "eight": "delapan",
    "nine": "sembilan",
    "ten": "sepuluh"
    # ...
    }


def main():
    # meminta user memasukkan kata dalam bahasa inggris
    kata = input("Masukkan kata dalam bahasa inggris: ")

    if not (kata in KAMUS.keys()):
        print("'%s' tidak ditemukan di dalam kamus ini" % kata)
        sys.exit(1)

    print("Arti kata '%s' adalah '%s'" % (kata, KAMUS[kata]))


if __name__ == "__main__":
    main()

# nomer 9.3
# mendefinisikan array dua dimensi
A = [
    [23, 11, 54, 38, 76],
    [14, 12, 20, 22, 21],
    [10, 13, 18, 17, 24],
    [35, 33, 39, 32, 29]
    ]

BARIS = 4
KOLOM = 5


def main():
    print("Isi array A: ")
    # menampilkan elemen array dua dimensi = 0
    i = 0
    while i < BARIS:
        j = 0
        while j < KOLOM:
            print("%d " % A[i][j], end=" ")
            j += 1
        i += 1
        print()  # ganti baris


if __name__ == "__main__":
    main()

# soal 9.4

A = [
	[23, 11, 54, 38, 76],
	[14, 12, 20, 22, 21],
	[10, 13, 18, 17, 24],
	[35, 33, 39, 32, 29]
	]

#mengakses elemen array dua dimensi
for baris in A:
	for nilai in baris:
		print("%d " % nilai, end=" ")
	print()

# soal 9.5

A = [
	[
	  [10, 20, 30],
	  [40, 50, 60]
	],
	[
	  [11, 21, 31],
	  [41, 51, 61]
	]
	]

# mengakses elemen 10
print(A[0][0][0])

# mengakses elemen 50
print(A[0][1][1])

# soal 9.6

import array
A = array.array("i")

A.append(50)
A.append(-20)
A.append(30)
A.insert(1, 40)
A.remove(-20)

# menggunakan perintah for
for nilai in A:
    print("%d " % nilai, end=" ")

# menggunakan perintah while
i = 0
while i < len(A):
    print("%d " % A[i], end=" ")
    i += 1

A.index(30)

# soal 9. 7

import array

#mengonversi string ke dalam array.array
B = array.array('c')
B.fromstring("Python")

for karakter in B:
	print("%c " % karakter, end = " ")

#soal 9.8

import array

#mengonversi list ke dalam array.array
li = [10, 20, 30, 40, 50]
C = array.array('i')
C.fromlist(li)
type(C)

# <type 'array.array'>
for nilai in C:
	print("%d " % nilai, end=" ")

#soal 9.9

import array

A = array.array('i', [100, 200, 300, 400, 500])
print(A)

A[1] = -700	        #mengubah elemen kedua
A[4] = 800	        #mengubah elemen kelima
print(A)

#soal  9.10

import array

# mendefinisikan fungsi untuk mengurutkan elemen array
def sort(A):
    i = 0
    while i < len(A) - 1:
        j = len(A) - 1
        while j >= i + 1:
            if A[j] < A[j - 1]:
                temp = A[j]
                A[j] = A[j - 1]
                A[j - 1] = temp
            j -= 1
        i += 1


def main():
    A = array.array('i', [50, 10, 30, 40, 20])
    print("Sebelum diurutkan: ")
    for nilai in A:
        print("%d " % nilai, end=" ")
    print("\n")

    # mengurutkan array
    sort(A)

    print("Setelah diurutkan: ")
    for nilai in A:
        print("%d " % nilai, end=" ")


if __name__ == "__main__":
    main()

# soal 9.11

import array

# mendefinisikan fungsi untuk mengurutkan elemen array
def sort(A):
    i = 0
    while i < len(A) - 1:
        j = len(A) - 1
        while j >= i + 1:
            if A[j] < A[j - 1]:
                temp = A[j]
                A[j] = A[j - 1]
                A[j - 1] = temp
            j -= 1
        i += 1


def main():
    A = array.array('i', [50, 10, 30, 40, 20])
    print("Sebelum diurutkan: ")
    for nilai in A:
        print("%d " % nilai, end=" ")
    print("\n")

    # mengurutkan array
    sort(A)

    print("Setelah diurutkan: ")
    for nilai in A:
        print("%d " % nilai, end=" ")


if __name__ == "__main__":
    main()