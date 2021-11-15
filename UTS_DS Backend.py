
def menu ():
    print ("==================================MENU UTAMA====================================")
    print (" ")
    print ("  Kota Gandrung terletak di provinsi JAWA TIMUR, Kota tersebut bernama Kota Banyuwangi,")
    print ("  Sekarang Kamu ingin mengunjungi ADAT ISTIADAT atau OBJEK WISATA di Kabupaten Banyuwangi ?  ")
    print (" ")
    print ("1 Untuk mengunjungi ADAT ISTIADAT")
    print ("2 Untuk mengunjungi OBJEK WISATA")
    print (" ")

#Pembuka
print ("************************************************")
print ("======   Kamu Mau Masuk Kota Gandrung ?   ======")
print ("======  Isikan Data Diri Kamu Dulu Ya !!  ======")
print ("************************************************")
print (" ")
#Inputan
print ("Tuliskan Nama Kamu :")
nama = input()
print (" ")
print ("Tuliskan Alamat Kamu")
alamat = input()
print (" ")
print ("12+15")
print ("Berapa Hasil dari Penjumlahan Tersebut ?")
print ("Jawaban Kamu :")
umur = input()
if umur == ("27"):
    print (" ")
    print ("Yeay! Jawaban Kamu Benar")
    print (" ")
    print ("Selamat Datang di PROGRAM Kota Gandrung", nama)
    print (" ")
else:
    print ("Sayang sekali, jawaban kamu salah!")
    print ("Kamu dilarang masuk")
    print ("Terima Kasih")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    exit()
   
 
print ("***************** Program Kota Gandrung ini dirancang oleh  *******************")
print ("#                          Shintia Juli Rahmawati                             #")
print ("#                              NIM. 1120101896                                #")
print ("#                       UTS Dasar Pemograman Backend                          #")
print ("*******************************************************************************")
print (" ")

#Menampilkan
menu()
 
def adat():
    print (" ")
    print ("----Daftar pilihan ADAT ISTIADAT yang dapat kamu kunjungi di Banyuwangi----")
    print ("\n1.Tumpeng Sewu \n2.Mepe Kasur \n3.Ngopi Sepuluh Ewu \n4.Puter Kayun \n5.Kebo-Keboan \n6.Geredoan")
   
def wisata():
    print (" ")
    print ("---Daftar pilihan OBJEK WISATA yang dapat kamu kunjungi di Banyuwangi---")
    print ("\n1.Kawah Ijen \n2.Alas Purwo \n3.Teluk Ijo \n4.Pulau Merah \n5.Baluran \n6.Jawatan")
   
def out():
    print ("Apakah kamu sudah selesai dan ingin keluar dari program ?")
    print ("y untuk Menutup Program")
    print ("n untuk Kembali ke Menu Utama")
    print (" ")
    out = input("y/n =")
    if out == "Y":
        exit()
    elif out == "y":
        exit()
    elif out == "N":
        menu()
    elif out == "n":
        menu()
    else :
        print ("Maaf ada kesalahan saat menginput, Program akan segera tertutup")
        print (" ")
        print (" ")
        print (" ")
        print (" ")
        print (" ")
        print (" ")
        exit()
#LIST
#Adat
TumpengSewu = ("\n=> Jadwal Acara \n=> Persyaratan Mengikuti \n=> Contact Person")
MepeKasur = ("\n=> Jadwal Acara \n=> Persyaratan Mengikuti \n=> Contact Person")
NgopiSepuluhEwu = ("\n=> Jadwal Acara \n=> Persyaratan Mengikuti \n=> Contact Person")
PuterKayun = ("\n=> Jadwal Acara \n=> Persyaratan Mengikuti \n=> Contact Person")
KeboKeboan = ("\n=> Jadwal Acara \n=> Persyaratan Mengikuti \n=> Contact Person")
Geredoan = ("\n=> Jadwal Acara \n=> Persyaratan Mengikuti \n=> Contact Person")
#ObjekWisata
KawahIjen = ("\n=> Lokasi \n=> Lama Jarak Tempuh \n=> Estimasi Biaya \n=> Contact Person")
AlasPurwo = ("\n=> Lokasi \n=> Lama Jarak Tempuh \n=> Estimasi Biaya \n=> Contact Person")
TelukIjo = ("\n=> Lokasi \n=> Lama Jarak Tempuh \n=> Estimasi Biaya \n=> Contact Person")
PulauMerah = ("\n=> Lokasi \n=> Lama Jarak Tempuh \n=> Estimasi Biaya \n=> Contact Person")
Baluran = ("\n=> Lokasi \n=> Lama Jarak Tempuh \n=> Estimasi Biaya \n=> Contact Person")
Jawatan = ("\n=> Lokasi \n=> Lama Jarak Tempuh \n=> Estimasi Biaya \n=> Contact Person")
 
#PERULANGAN
while 1:
    
    pilih = input("Masukan Angka pilihan Kamu, kemudian tekan enter :")
    if pilih == "1":
        adat()
        print ("\n")
        print ("ADAT mana yang ingin kamu kunjungi ?")
        print ("Masukkan angka 1 sampai 6 sesuai keinginan kamu ya!")
        print (" ")
        pilih = input("ADAT Pilihanku : ")
        if pilih == "1":
            print (" ")
            print ("***********************************TUMPENG SEWU*************************************")
            print ("Berikut informasi mengenai Adat Istiadat yang akan kamu kunjungi di Kota Banyuwangi:")
            print (TumpengSewu)
            print (" ")
            print ("SELAMAT MENGUNJUNGI ADAT TUMPENG SEWU")
            print ("\n")
            out()
        elif pilih == "2":
            print (" ")
            print ("*************************************MEPE KASUR*************************************")
            print ("Berikut informasi mengenai Adat Istiadat yang akan kamu kunjungi di Kota Banyuwangi:")
            print (MepeKasur)
            print (" ")
            print ("SELAMAT MENGUNJUNGI ADAT MEPE KASUR")
            print ("\n")
            out()
        elif pilih == "3":
            print (" ")
            print ("*********************************NGOPI SEPULUH EWU**********************************")
            print ("Berikut informasi mengenai Adat Istiadat yang akan kamu kunjungi di Kota Banyuwangi:")
            print (NgopiSepuluhEwu)
            print (" ")
            print ("SELAMAT MENGUNJUNGI ADAT NGOPI SEPULUH EWU")
            print ("\n")
            out()
        elif pilih == "4":
            print (" ")
            print ("**************************************PUTER KAYUN***********************************")
            print ("Berikut informasi mengenai Adat Istiadat yang akan kamu kunjungi di Kota Banyuwangi:")
            print (PuterKayun)
            print (" ")
            print ("SELAMAT MENGUNJUNGI ADAT PUTER KAYUN")
            print ("\n")
            out()
        elif pilih == "5":
            print (" ")
            print ("************************************KEBO-KEBOAN*************************************")
            print ("Berikut informasi mengenai Adat Istiadat yang akan kamu kunjungi di Kota Banyuwangi:")
            print (KeboKeboan)
            print (" ")
            print ("SELAMAT MENGUNJUNGI ADAT KEBO-KEBOAN")
            print ("\n")
            out()
        elif pilih == "6":
            print (" ")
            print ("***************************************GEREDOAN*************************************")
            print ("Berikut informasi mengenai Adat Istiadat yang akan kamu kunjungi di Kota Banyuwangi:")
            print (Geredoan)
            print (" ")
            print ("SELAMAT MENGUNJUNGI ADAT KEBO-KEBOAN")
            print ("\n")
            out()
        elif pilih > "6":
            out()
    #IF OBJEK WISATA
    elif pilih == "2":
        wisata()
        print ("\n")
        print ("OBJEK WISATA mana yang ingin kamu kunjungi ?")
        print ("Masukkan angka 1 sampai 6 sesuai keinginan kamu ya!")
        print (" ")
        pilih = input("OBJEK WISATA Pilihanku : ")
        if pilih == "1":
            print (" ")
            print ("***************************KAWAH IJEN*********************************")
            print ("Berikut informasi mengenai Objek Wisata yang akan kamu kunjungi di Kabupaten Banyuwangi :")
            print (KawahIjen)
            print (" ")
            print ("SELAMAT BERLIBUR DI OBJEK WISATA KAWAH IJEN")
            print ("\n")
            out()
        elif pilih == "2":
            print (" ")
            print ("***************************ALAS PURWO*********************************")
            print ("Berikut informasi mengenai Objek Wisata yang akan kamu kunjungi di Kabupaten Banyuwangi :")
            print (AlasPurwo)
            print (" ")
            print ("SELAMAT BERLIBUR DI OBJEK WISATA ALAS PURWO")
            print ("\n")
            out()
        elif pilih == "3":
            print (" ")
            print ("****************************TELUK IJO*******************************")
            print ("Berikut informasi mengenai Objek Wisata yang akan kamu kunjungi di Kabupaten Banyuwangi :")
            print (TelukIjo)
            print (" ")
            print ("SELAMAT BERLIBUR DI OBJEK WISATA TELUK IJO")
            print ("\n")
            out()
        elif pilih == "4":
            print (" ")
            print ("****************************PULAU MERAH*********************************")
            print ("Berikut informasi mengenai Objek Wisata yang akan kamu kunjungi di Kabupaten Banyuwangi :")
            print (PulauMerah)
            print (" ")
            print ("SELAMAT BERLIBUR DI OBJEK WISATA PULAU MERAH")
            print ("\n")
            out()
        elif pilih == "5":
            print (" ")
            print ("*****************************BALURAN********************************")
            print ("Berikut informasi mengenai Objek Wisata yang akan kamu kunjungi di Kabupaten Banyuwangi :")
            print (Baluran)
            print (" ")
            print ("SELAMAT BERLIBUR DI OBJEK WISATA BALURAN")
            print ("\n")
            out()
        elif pilih == "6":
            print (" ")
            print ("*****************************JAWATAN*********************************")
            print ("Berikut informasi mengenai Objek Wisata yang akan kamu kunjungi di Kabupaten Banyuwangi :")
            print (Jawatan)
            print (" ")
            print ("SELAMAT BERLIBUR DI OBJEK WISATA")
            print ("\n")
            out()
        elif pilih > "6":
            out()
 
 
    else:
        print (" ")
        print ("MOHON MAAF, pilihan yang dimasukkan tidak terdaftar")
        print ("Ingin coba Lagi [y/n] ? ")
        print ("y = Kembali ke Menu Utama")
        print ("n = Tutup Program")
        coba = input()
        if coba == "Y":
            menu()
        elif coba == "y":
            menu()
        elif coba == "N":
            exit()
        elif coba == "n":
            exit()
        else:
            print ("MAAF Kesalahan Menginput, Program akan segera tertutup")
            print (" ")
            print (" ")
            print (" ")
            print (" ")
            exit()