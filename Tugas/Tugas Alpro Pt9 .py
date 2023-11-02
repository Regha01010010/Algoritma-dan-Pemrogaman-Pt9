"""
MADE BY KELOMPOK 9
Find More at https://github.com
Member :
1. Refany Dwi Lestari       170
2. Regha Rahmadian Bintang  156
3. M Ibnu Nadhif            161
"""
#Refany


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
