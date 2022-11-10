Name = "Muhammad Daffa adillah,"
Kelas = "11-TKJ,"
Title = "Tugas Phyton,"
print (Name,Kelas,Title)

#Soal 1: Perbedaan Data Structure

#Jelaskan Perbedaan dari List, Tuple, Set dan Dictionary?
#List : nilai yang dipisahkan koma di dalam tanda kurung siku dan Berurutan dan memakai index
#Tuple : Tuple hampir mirip seperti list tetapi data dalam tuple bersifat tetap atau tidak dapat diubah
#Set : item yang bersifat Unik dan tidak berurutan
#Dictionary : pasangan kunci dan nilai (key:value) dan tidak berurutan

#---------------------------------------------------------------#

#Soal 2:Akses List
#Lengkapi kode untuk menghasilkan suatu output yang di harapkan
a = ['1','13b','aa1',1.32,22.1,2.24]
print (a[1:5])

#---------------------------------------------------------------#

#Soal 3: Akses Nested List
#Lengkapi kode untuk menghasilkan suatu output yang di harapkan
a = [
    [5,9,8],
    [0,0,6]
]
print (a[1][1:])

#---------------------------------------------------------------#

#Soal 4: List Manipulation
#Lengkapi kode untuk menghasilkan suatu output yang di harapkan
a = [
    [5,9,8],
    [0,0,6]
]
a[0][2] = 10
a[1][0] = 11
print (a)

#---------------------------------------------------------------#

#Soal 5: Delete Element List
#Lengkapi kode untuk menghasilkan suatu output yang di harapkan
areas = ['hallway',11.25,'kitchen',18.0,
        'chill zone',20.0,'bedroom',10.75,
        'bathroom',10.50,'poolhouse',
        24.5,'garage'
]
del areas[8:10]
print (areas)

#---------------------------------------------------------------#

#Soal 6: List Comprehension
#Gunakan metode **list comprehension** untuk mencari anggota dari S yang habis di bagi 2, kemudian assign hasilnya dalam bentuk list ke dalam variabel T.
S = [0,1,4,9,16,25,36,49,64,81]
T = [x for x in S if x %2 == 0]

print(T)

#---------------------------------------------------------------#

#Soal 8: Menambahkan key-value baru ke Dictionary
#Lengkapi kode untuk menghasilkan suatu output yang di harapkan
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
europe ["italia"] = "roma"
print (europe)

#---------------------------------------------------------------#

#Soal 9: Boolean Comparison
#- Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'and'
#- Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'or'
#- Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'not'

a = ("sama"=="sama")
b = ("sama"=="beda")
c = ("beda"=="beda")
 
if (a and b and c):
    print ("benar")
else :
    print ("salah")

if (a or b or c):
    print ("benar")
else :
    print ("salah")

if (not b, not a):
    print ("benar")
else :
    print ("salah")

#---------------------------------------------------------------#

#Soal 10: If-Else Statement

#Lengkapi kode untuk menghasilkan suatu output yang di harapkan
#Bualah sebuah if-else statement yang dimana akan mem-print 'High' jika grade adalah 'A' dan price lebih dari 100000, kemudian mem-print 'Medium' jika grade adalah 'A' dan price lebih dari 50000 dan memprint 'low' jika grade adalah 'A' dan price lebih kecil dan sama dengan 50000.

grade = 'A'
harga = 0 #Random harganya

if grade == 'A' and harga >100000:
    print ('high')
elif grade == 'A' and (harga <=100000 and harga >=50000):
    print ('sedang')
elif grade == 'A' and (harga <=50000 and harga >=1000):
    print ('kecil')
else:
    print ('Terlalu Kecil (Gak ada Harganya)')
