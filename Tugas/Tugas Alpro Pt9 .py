"""
MADE BY KELOMPOK 9
Find More at https://github.com
Member :
1. Refany Dwi Lestari       170
2. Regha Rahmadian Bintang  156
3. M Ibnu Nadhif            161
"""
#Refany
#List menu pizza yang ditawarkan
Menu_Pizza = ["Frankfurter BBQ","Meat Monsta","Super Supreme","Super Supreme Chicken"]
#List pilihan crust yang ditawarkan
Pil_Crust = ["Pan","Stuffed Crust Sausage","Stuffed Crust Cheese","Cheesy Bites","Crown Crust"]
#list pilihan ukuran pizza yang ditawarkan
Pil_Size = ["Personal","Regular","Large"]

#Menampilkan ucapan selamat datang juga sebagai header
print(
"""
=================================
   SELAMAT DATANG DI PIZZA HUT
=================================
Silahkan Pilih Toping Pizza Anda
""")

#Menampilkan list dari Menu_Pizza agar dapat dilihat oleh user
for i,pizza in enumerate(Menu_Pizza):
    print(i+1,pizza) 
#Input dari user dan disimpan pada variable Pizza_Dipilih  sebagai integer
Pizza_Dipilih = int(input("Pilih Toping Pizza : "))
#Mengkoreksi apabila user memasukan angka yang tidak valid
while Pizza_Dipilih < 1 or Pizza_Dipilih > 4:
    print("Input Tidak Valid!")
    Pizza_Dipilih = int(input("Pilih Toping Pizza : "))
    
#Menampilkan ucapan untuk memilih jenis crust untuk pizza yang akan dipilih user 
print("\nSilahkan Pilih Crust Pizza Anda")

#Menampilkan list dari Pil_Crust agar dapat dilihat oleh user
for i,crust in enumerate(Pil_Crust):
    print(i+1,crust)
#Input dari user disimpan pada variabel Crust_Dipilih sebagai integer
Crust_Dipilih = int(input("Pilih Crust Untuk Pizza Anda : "))
#Mengkoreksi apabila user memasukan angka yang tidak valid
while Crust_Dipilih < 1 or Crust_Dipilih > 5:
    print("Input Tidak Valid!")
    Crust_Dipilih = int(input("Pilih Crust Untuk Pizza Anda : "))

#Menampilkan ucapan untuk memilih ukuran pizza yang akan dipilih user
print("\nSilahkan Pilih Ukuran Pizza Anda")

#Menampilkan list dari Pil_Size agar dapat dilihat oleh user
for i,size in enumerate(Pil_Size):
    print(i+1,size)
#Input dari user disimpan pada variabel Size_Dipilih sebagai integer
Size_Dipilih = int(input("Pilih Size Pizza Anda : "))
#Mengkoreksi apabila user memasukan angka yang tidak valid
while Size_Dipilih < 1 or Size_Dipilih > 3:
    print("Input Tidak Valid!")
    Size_Dipilih = int(input("Pilih Size Pizza Anda: "))

#Input user apakah ingin menambahkan ekstra keju pada pizza nya disimpan dalam variabel Extra_Keju sebagai bolean
Extra_Keju = input("\nIngin Tambahan Extra Keju Pada Pizza Anda? [y/n] : ").lower()   
#Mengkoreksi apabila user memasukan input yang tidak valid
while Extra_Keju != "y" and Extra_Keju != "n":
    print("Input Tidak Valid!")
    Extra_Keju = input("\nIngin Tambahan Extra Keju Pada Pizza Anda? [y/n] : ").lower()
#Jika Extra_Keju adalah y maka Extra keju di update menjadi True
if Extra_Keju == "y":
    Extra_Keju = True
#jika tidak Extra_keju di update menjadi False
else:
    Extra_Keju = False                       

#Regha
#Fungsi untuk mengkalkulasi harga dari semua input pilihan user
def PizzaHut(crust,size,cheese):
    Harga_Total = 0
    if crust == 1:
        if size == 1:
            Harga_Total += 43637
            if cheese == True: 
                Harga_Total += 13636
        if size == 2:
            Harga_Total += 100910
            if cheese == True:
                Harga_Total += 16365
        if size == 3:
            Harga_Total += 132727
            if cheese == True:
                Harga_Total += 19091
    elif crust == 2:
        if size == 1:
            Harga_Total += 52727
            if cheese == True:
                Harga_Total += 13636
        if size == 2:
            Harga_Total += 117273
            if cheese == True:
                Harga_Total += 16365
        if size == 3:
            Harga_Total += 155455
            if cheese == True:
                Harga_Total += 19091
    elif crust == 3:
        if size == 1:
            Harga_Total += 55455
            if cheese == True:
                Harga_Total += 13636
        if size == 2:
            Harga_Total += 120909
            if cheese == True:
                Harga_Total += 16365
        if size == 3:
            Harga_Total += 160000
            if cheese == True:
                Harga_Total += 19091
    elif crust == 4:
        if size == 1:
            Harga_Total += 57273
            if cheese == True:
                Harga_Total += 13636
        if size == 2:
            Harga_Total +=  123636
            if cheese == True:
                Harga_Total += 16365
        if size == 3:
            Harga_Total += 164545
            if cheese == True:
                Harga_Total += 19091
    elif crust == 5:
        if size == 1:
            Harga_Total += 55455
            if cheese == True:
                Harga_Total += 13636
        if size == 2:
            Harga_Total += 120910
            if cheese == True:
                Harga_Total += 16365
        if size == 3:
            Harga_Total += 160000
            if cheese == True:
                Harga_Total += 19091

    return Harga_Total

#Nadhif
#Jika Extra_Keju adalah True, Menampilkan bill output dengan tambahan Extra keju
if Extra_Keju == True:
    print(
    f"""
    =====================================
                BILL PIZZA
    =====================================
    Pizza         : {Menu_Pizza[Pizza_Dipilih-1]} Ukuran {Pil_Size[Size_Dipilih-1]}
    Pilihan Crust : {Pil_Crust[Crust_Dipilih-1]}
    Extra Keju


    
    Total Harga   : Rp.{PizzaHut(Crust_Dipilih,Size_Dipilih,Extra_Keju)}
    =====================================
     TERIMAKASIH TELAH MEMBELI PIZZA DI
                PIZZA HUT
    =====================================
    """)
#Selain itu, Menampilkam bill output tanpa tambahan extra keju
else:
    print(
    f"""
    ====================================
                BILL PIZZA
    ====================================
    Pizza         : {Menu_Pizza[Pizza_Dipilih-1]} Ukuran {Pil_Size[Size_Dipilih-1]}
    Pilihan Crust : {Pil_Crust[Crust_Dipilih-1]}



    Total Harga   : Rp.{PizzaHut(Crust_Dipilih,Size_Dipilih,Extra_Keju)}
    =====================================
     TERIMAKASIH TELAH MEMBELI PIZZA DI
                PIZZA HUT
    =====================================
    """)
print("hello world!")
