import pyinputplus as pyip 
from tabulate import tabulate
from datetime import datetime

"""Membuat Menu Aplikasi yang bertujuan untuk memudahkan guru dalam 
melakukan askses penilaian tugas/ujian dan data siswa """

#==============================================================================================================================
# data collection 
# data dummynya (nama, kelas, tanggal_registrasi(year), nama_ortu, no telp, jenis kelamin, dan alamat  )
#==============================================================================================================================
dict_data_siswa = {
    2001: {"nama":"Andi","kelas":"Kelas 10","tanggal_registrasi":"2025","nama_ortu":"Budi","no_telp":"0811","jenis_kelamin":"Laki-laki","alamat":"Jl. Cengkeh 1"},
    2002: {"nama":'Bela',"kelas":"Kelas 10","tanggal_registrasi":"2026","nama_ortu":"Mulyono","no_telp":"0812","jenis_kelamin":"Perempuan","alamat":"Jl. Cengkeh 2"},
    2003: {"nama":'Coki',"kelas":"Kelas 11","tanggal_registrasi":"2024","nama_ortu":"Dani","no_telp":"0813","jenis_kelamin":"Laki-laki","alamat":"Jl. Cengkeh 3"},
    2004: {"nama":"Dina","kelas":"Kelas 11","tanggal_registrasi":"2025","nama_ortu":"Bahlil","no_telp":"0814","jenis_kelamin":'Perempuan',"alamat":"Jl. Bunga 4"},
    2005: {"nama":"Ejak","kelas":"Kelas 12","tanggal_registrasi":"2024","nama_ortu":"Fani","no_telp":"0815","jenis_kelamin":"Laki-laki","alamat":"Jl. Bunga 5"},
    2006: {"nama":"Fira","kelas":"Kelas 12","tanggal_registrasi":"2023","nama_ortu":"Gatot","no_telp":"0816","jenis_kelamin":"Perempuan","alamat":"Jl. Bunga 6"}}

# dict nilai dipisah untuk memudahkan dalam proses ekstraksi(akses) codenya
dict_data_nilai = {
    2001: {"Matematika": {"Tugas 1":80,"Ujian Harian":85,"Ujian Akhir":90}, "B. Indonesia": {"Tugas 1":75,"Ujian Harian":80,"Ujian Akhir":85}, "B. Inggris": {"Tugas 1":90,"Ujian Harian":95,"Ujian Akhir":88}, "IPA": {"Tugas 1":85,"Ujian Harian":80,"Ujian Akhir":92}, "IPS": {"Tugas 1":88,"Ujian Harian":85,"Ujian Akhir":89}},
    2002: {"Matematika": {"Tugas 1":95,"Ujian Harian":90,"Ujian Akhir":92}, "B. Indonesia": {"Tugas 1":85,"Ujian Harian":88,"Ujian Akhir":90}, "B. Inggris": {"Tugas 1":80,"Ujian Harian":82,"Ujian Akhir":85}, "IPA": {"Tugas 1":90,"Ujian Harian":85,"Ujian Akhir":88}, "IPS": {"Tugas 1":92,"Ujian Harian":90,"Ujian Akhir":95}},
    2003: {"Matematika": {"Tugas 1":70,"Ujian Harian":75,"Ujian Akhir":78}, "B. Indonesia": {"Tugas 1":80,"Ujian Harian":82,"Ujian Akhir":85}, "B. Inggris": {"Tugas 1":75,"Ujian Harian":78,"Ujian Akhir":80}, "IPA": {"Tugas 1":72,"Ujian Harian":70,"Ujian Akhir":75}, "IPS": {"Tugas 1":85,"Ujian Harian":80,"Ujian Akhir":82}},
    2004: {"Matematika": {"Tugas 1":88,"Ujian Harian":90,"Ujian Akhir":85}, "B. Indonesia": {"Tugas 1":90,"Ujian Harian":92,"Ujian Akhir":88}, "B. Inggris": {"Tugas 1":95,"Ujian Harian":90,"Ujian Akhir":92}, "IPA": {"Tugas 1":85,"Ujian Harian":88,"Ujian Akhir":90}, "IPS": {"Tugas 1":80,"Ujian Harian":85,"Ujian Akhir":82}},
    2005: {"Matematika": {"Tugas 1":100,"Ujian Harian":95,"Ujian Akhir":98}, "B. Indonesia": {"Tugas 1":90,"Ujian Harian":88,"Ujian Akhir":92}, "B. Inggris": {"Tugas 1":95,"Ujian Harian":98,"Ujian Akhir":100}, "IPA": {"Tugas 1":98,"Ujian Harian":95,"Ujian Akhir":96}, "IPS": {"Tugas 1":90,"Ujian Harian":92,"Ujian Akhir":95}},
    2006: {"Matematika": {"Tugas 1":65,"Ujian Harian":70,"Ujian Akhir":75}, "B. Indonesia": {"Tugas 1":70,"Ujian Harian":75,"Ujian Akhir":80}, "B. Inggris": {"Tugas 1":80,"Ujian Harian":85,"Ujian Akhir":82}, "IPA": {"Tugas 1":68,"Ujian Harian":72,"Ujian Akhir":70}, "IPS": {"Tugas 1":75,"Ujian Harian":78,"Ujian Akhir":80}}}

list_mata_pelajaran = ["Matematika", "B. Indonesia", "B. Inggris", "IPA", "IPS"]
list_kelas = ["Kelas 10", "Kelas 11", "Kelas 12"]
jenis_tugas = {
    "Matematika": ["Tugas 1", "Ujian Harian", "Ujian Akhir"],
    "B. Indonesia": ["Tugas 1", "Ujian Harian", "Ujian Akhir"],
    "B. Inggris": ["Tugas 1", "Ujian Harian", "Ujian Akhir"],
    "IPA": ["Tugas 1", "Ujian Harian", "Ujian Akhir"],
    "IPS": ["Tugas 1", "Ujian Harian", "Ujian Akhir"]}

# Fungsi login guru 
#==========================================================================================
# guru diminta untuk login sampai valid sebelum dapat mengakses menu aplikasi 
def login_awal() : 
    print("============================\nSELAMAT DATANG DI StudentHUB \n============================")
    print("Silahkan Login Terlebih Dahulu Untuk Mengakses Menu Guru")
    username="guru"
    password = "123"
    while True :
        input_username = input("Silahkan Masukkan Username :")
        input_password = input("Silahkan Masukkan password :")

        if input_username == username and input_password == password:
            print("Login Berhasil!")
            break
        else :
            print("Username atau Password salah!, Silahkan coba lagi!")
            continue # agar balik ke while awal untuk minta input ulang

# fungsi tampilan menu 
def menampilkan_menu_utama():
    print("""\n===================================
   MENU UTAMA StudentHUB
===================================
1. Registrasi Siswa Baru
2. Lihat Profil Siswa
3. Lihat Rapor & Ranking
4. Tambah Tugas/Ujian Baru
5. Input / Update Nilai Siswa
6. Hapus Data
7. Keluar Program""")
#==========================================================================================

#CRUD dalam bentuk reguler function 
#============================================================================================
# Piih Menu NO.1 Registrasi Siswa Baru (membuat fungsi reg_siswa_baru) ---> function CREATE 
#============================================================================================
def reg_siswa_baru() : #guru diminta untuk menginput beberapa data siswa
    print("===========================\n== Registrasi Siswa Baru ==") 
    print("===========================")
    while True : # loop agar guru menginput nama sampai valid
        print("Masukkan '0' untuk Batal atau kembali ke Menu Utama")
        add_nama = input("Masukkan Nama Lengkap Siswa: ").title().strip()
        if add_nama == "0":
            print("Terima kasih, Registrasi dibatalkan.")
            return # Ini untuk langsung balik ke menu utama
        if add_nama.replace(" ", "").isalpha(): #untuk cek kondisi jika tidak sengaja input nomor
            break # jika kondisi benar, lanjut ke input selanjutnya
        else:
            print(" Maaf, Nama tidak valid! Input hanya boleh berisi huruf")
    
    add_kelas = pyip.inputMenu(list_kelas, prompt="Pilih Kelas :\n", numbered=True) #memberi pilihan kelas dari list kelas yang ada
    add_ortu= pyip.inputStr("Masukkan Nama Wali/Ortu : ",blockRegexes=[r'\d'],applyFunc=lambda x:x.title().strip())   
    add_telp = pyip.inputStr("Masukkan No Telp (Angka) : ", blockRegexes=[r'[a-zA-Z]']) #tambahan validasi input hanya angka
    add_kelamin = pyip.inputMenu(["Laki-laki", "Perempuan"], prompt="Pilih Jenis Kelamin :\n", numbered=True)
    add_alamat = input("Masukkan Alamat : ").strip()
    tanggal_sekarang = datetime.now().strftime("%Y") #extrak tahun saja

    if len(dict_data_siswa)!=0: # kondisi untuk membuat id baru
        id_baru = max(dict_data_siswa.keys()) + 1
    else: #jika dictnya kosong
        id_baru = 2001
    dict_data_siswa[id_baru] = {"nama":add_nama,"kelas":add_kelas,"tanggal_registrasi":tanggal_sekarang,"nama_ortu":add_ortu,"no_telp":add_telp,"jenis_kelamin":add_kelamin,"alamat":add_alamat}

    dict_data_nilai[id_baru] = {} #dict data nilai kosong untuk siswa baru 
    for mapel in list_mata_pelajaran: #pakai loop, agar otomatis menambahkan nilai ujian dan tugas menjadi 0
        dict_data_nilai[id_baru][mapel] = {}
        for tugas in jenis_tugas[mapel]:
            dict_data_nilai[id_baru][mapel][tugas]= 0
            
    print(f"Siswa dengan nama : {add_nama} berhasil ditambahkan dengan ID  :{id_baru}!")
#===============================================================================================

# jika piih menu NO.2 Lihat Profil Siswa (membuat fungsi menampilkan_profil) ---- function READ 
#================================================================================================
def menampilkan_profil(): #guru dapat melihat profil siswa berdasarkan kelas atau semuanya
    while True:    
        print("========================\n== Data Profil Siswa ==")
        print("=======================")
        menu_profil=list_kelas + ["Tampilkan Semua Data", "Kembali"] #list menu untuk pyinput
        print("Pilih Data yang mau ditampilkan:")
        pilihan=pyip.inputMenu(menu_profil,numbered=True)
        tabel_profil=[] #list kosong untuk tabulate dan menampung looping
        judul_kolom=["ID","Nama","Kelas","L/P","No Telp","Wali","Tahun"]
        if pilihan=="Kembali": 
            break
        elif pilihan=="Tampilkan Semua Data":
            print("\n== Data Semua Siswa ==")
            for id_siswa,info in dict_data_siswa.items():
                tahun=info.get("tanggal_registrasi","-") # pakai get supaya menghindari eror jika tahunnya tidak ada
                baris=[id_siswa,info["nama"],info["kelas"],info["jenis_kelamin"],info["no_telp"],info["nama_ortu"],tahun]
                tabel_profil.append(baris)

        else: # pilihan jika milih salah satu kelas
            print(f"\n== Data {pilihan} ==")
            for id_siswa,info in dict_data_siswa.items():
                if info["kelas"]==pilihan:
                    tahun=info.get("tanggal_registrasi","-")
                    baris=[id_siswa,info["nama"],info["kelas"],info["jenis_kelamin"],info["no_telp"],info["nama_ortu"],tahun]
                    tabel_profil.append(baris)
        if len(tabel_profil)==0:
            print("Data tidak ditemukan")
        else: 
            print(tabulate(tabel_profil,headers=judul_kolom,tablefmt="grid")) 
#========================================================================================================

# jika piih menu NO.3 Lihat Rapor & Ranking (membuat fungsi menamenampilkan_rapor) ---- function READ 
#=========================================================================================================
def menampilkan_rapor(): #guru dapat melihat ranking berdasarkan kelas dan rapot detail persiswanya
    while True:
        print("==========================\n== MENU RAPOR & RANKING ==")
        print("==========================")
        menu_rapor = list_kelas +["Lihat Detail Nilai Siswa (Cari ID)", "Kembali"] #list menu untuk pyinput
        pilihan = pyip.inputMenu(menu_rapor,numbered=True,prompt="Pilih Menu :\n")
        
        if pilihan=="Kembali": 
            break
        elif pilihan in list_kelas: # logic kalo milih kelas langsung ranking
            print(f"== Ranking {pilihan} ==")
            tabel= []
            for id_siswa,info in dict_data_siswa.items():
                if info["kelas"]== pilihan:
                    total_nilai = 0
                    for mapel in list_mata_pelajaran: # loop mencari rata2 nilai per mata pelajaran karena setiap mata pelajaran ada tugas dan ujian
                        nilai_mapel=dict_data_nilai[id_siswa][mapel]
                        if len(nilai_mapel)>0: 
                            rata=sum(nilai_mapel.values())/len(nilai_mapel)
                        else: 
                            rata=0
                        total_nilai+=rata 
                    if len(list_mata_pelajaran)>0: # semua rata2 per matapelajaran itu dibagi lagi dengan jumlah mapel untuk dapat satu angka rata2
                        nilai_rata=total_nilai/len(list_mata_pelajaran)
                    else: 
                        nilai_rata=0
                    tabel.append([id_siswa,info["nama"],round(nilai_rata,2)])
                else: 
                    pass 
            if len(tabel)==0: # cek tabel kosong atau ada isi, gaada siswa
                print("Data kosong.")
            else:  #sorting dari nilai rata Terbesarpaling besar
                tabel.sort(key=lambda x:x[2],reverse=True)
                print(f"\n=== RANKING KELAS {pilihan} ===")
                print(tabulate(tabel,headers=["ID","Nama","Rata-Rata Akhir"],tablefmt="grid"))

        elif pilihan == "Lihat Detail Nilai Siswa (Cari ID)": # jika pilih detail untuk per siswa
            cari_id = pyip.inputInt("Masukkan ID Siswa: ")
            if cari_id in dict_data_siswa: #jika ada idnya
                nama = dict_data_siswa[cari_id]["nama"] 
                kelas = dict_data_siswa[cari_id]["kelas"]
                print(f"=== RAPOR DETAIL: {nama} ({kelas}) ===")
                tabel_detail= [] #list kosong untuk tabulate
                for mapel in list_mata_pelajaran: #loop satu2 mapel dan tugas2nya untuk dimasukkan ke tabel detail agar bisa ditampilkan 
                    nilai_mapel=dict_data_nilai[cari_id][mapel]
                    list_teks = [] # list kosong untuk menampung nilai tugas dan ujian setiap mata pelajaran, biar satu kolom gitu 
                    for jenis_tugas,angka in nilai_mapel.items():
                        teks = f"{jenis_tugas}:{angka}" # menggabungkan jenis tugas dan angka diubah jadi string
                        list_teks.append(teks) #trs dimasukkan ke dalam tabel list_tesk
                    teks_nilai=", ".join(list_teks) # di join lagi sama jenis tugas sampai habis
                    
                    if teks_nilai == "": #kondisi gaada tugas
                        teks_nilai = "-"
                    else: 
                        pass 
                    
                    if len(nilai_mapel)> 0: 
                        rata=sum(nilai_mapel.values())/len(nilai_mapel) #dapet nilai akhir dari setiap mapel 
                    else: 
                        rata=0
                    tabel_detail.append([mapel,teks_nilai,round(rata,2)]) 
                 #tampilin tabel jika semua kondisi dan proses loop sudah selesai   
                print(tabulate(tabel_detail,headers=["Mata Pelajaran","Rincian","Nilai Akhir"],tablefmt="grid"))
            else: print("ID tidak ditemukan.") #jika gaada idnya
#================================================================================================

# jika piih NO. 4. Tambah Tugas/Ujian Baru (membuat fungsi buat_tugas_baru()) ---- function CREATE 
#================================================================================================
def buat_tugas_baru(): #guru dapat membuat tugas atau ujian tambahan per mapelnya
    while True:
        print("=============================\n== TAMBAH TUGAS/UJIAN BARU ==")
        print("=============================")
        list_opsi = list_mata_pelajaran +["Kembali ke Menu Utama"]
        print("Pilih Mapel yang mau ditambah tugasnya:")
        pilih_mapel = pyip.inputMenu(list_opsi, numbered=True)

        if pilih_mapel == "Kembali ke Menu Utama": 
            break
        elif pilih_mapel != "Kembali ke Menu Utama" : # jika pilihnya mapel
            list_tugas_saat_ini = jenis_tugas[pilih_mapel]
            print(f"Info: Tugas di {pilih_mapel} saat ini:") #tampilin tugas yang sudah ada, supaya gak double nantinya
            print(list_tugas_saat_ini)
            nama_tugas_baru = input("Masukkan Nama Tugas Baru, masukkan 0 untuk batal: ").title().strip()
            if nama_tugas_baru == "0":
                print("Batal menambah tugas")
                continue 
            elif nama_tugas_baru in jenis_tugas[pilih_mapel]: #jika tugasnya sama persis maka gagal, dan ulang loopnya dr atas
                print(f"Gagal, Tugas {nama_tugas_baru} sudah ada!")
                continue
            else : #jika inputnya belom ada dari sebelomnya
                jenis_tugas[pilih_mapel].append(nama_tugas_baru) #tambah tugas baru untuk masuk ke list jenis tugas
                for id_siswa in dict_data_nilai.keys() : #buat nilai tugas baru 0 untuk semua siswa 
                    dict_data_nilai[id_siswa][pilih_mapel][nama_tugas_baru]= 0 
                print(f"Berhasil! Tugas {nama_tugas_baru} berhasil ditambahkan")
#================================================================================================

# jika piih NO. 5 (membuat fungsi update_nilai_siswa) ---- function UPDATE 
#================================================================================================
def update_nilai_siswa() : #guru dapat mengupdate ataupun menginput nilai baru untuk tiap siswanya
    while True:
        print("=============================\n== MENU UPDATE NILAI SISWA ==")
        print("=============================")
        id_dicari = pyip.inputInt("Masukkan ID Siswa, masukkan 0 untuk Kembali ke Menu Utama: ")
        if id_dicari == 0:
            break #kluar loop 
        if id_dicari in dict_data_siswa:
            nama_siswa =dict_data_siswa[id_dicari]["nama"]
            print(f"Siswa Ditemukan: {nama_siswa}")

            while True: #agar loop di siswa yang sama
                print(f"== Update Nilai: {nama_siswa} ==")
                list_opsi = list_mata_pelajaran + ["Input Semua Ujian Akhir", "kembali"] #pilihan mapel untuk di input atau update nilainya
                pilih_opsi = pyip.inputMenu(list_opsi, numbered=True, prompt="Pilih Menu:\n")

                if pilih_opsi == "kembali":
                    return # ke menu utama
                
                elif pilih_opsi == "Input Semua Ujian Akhir": #jika mau input semua mapel secara beruntun
                    print(f"Input Ujian Akhir {nama_siswa}")
                    for mapel in list_mata_pelajaran: #mencari mapel yang ada ujian akhir untuk di input atau di ubah nilainya
                        if "Ujian Akhir" in jenis_tugas[mapel]:
                            nilai_baru = pyip.inputInt(f"Nilai UAS {mapel} (0-100): ", min=0, max=100)
                            dict_data_nilai[id_dicari][mapel]["Ujian Akhir"]=nilai_baru #mengubah nilai yang sudah ada sebelumnya
                        else:
                            print(f"belum ada ujian akhir)")
                    print("Semua nilai ujian akhir sudah diupdate")
                else: #jika milih salah satu mata pelajaran 
                    print(f"Nilai {pilih_opsi} saat ini: {dict_data_nilai[id_dicari][pilih_opsi]}")
                    list_tugas = jenis_tugas[pilih_opsi]
                    pilih_tugas = pyip.inputMenu(list_tugas, numbered=True, prompt="Pilih Tugas yang mau diubah:\n")
                    nilai_baru = pyip.inputInt(f"\nMasukkan Nilai Baru untuk {pilih_tugas} (0-100): ", min=0, max=100)
                
                    dict_data_nilai[id_dicari][pilih_opsi][pilih_tugas] = nilai_baru
                    print("Data berhasil disimpan!")
        else:
            print("ID tidak ditemukan, silahkan coba lagi")
#================================================================================================

# jika piih NO. 6 (membuat fungsi delete_data) ---- function DELETE 
#================================================================================================
def delete_data(): #guru dapat menghapus data siswa ataupun ujian/tugas yang sudah dibuat
    print("=====================\n== Menu Hapus Data ==")
    print("=====================")
    list_opsi_hapus = ["Hapus Data Siswa", "Hapus Tugas/Ujian", "Kembali"]
    pilih_hapus = pyip.inputMenu(list_opsi_hapus, prompt="Pilih menu:\n", numbered=True)
    
    if pilih_hapus == "Kembali": #ke menu utama
        print("Kembali ke menu utama")
        return
    
    if pilih_hapus == "Hapus Data Siswa":
        hapus_id = pyip.inputInt("\nMasukkan ID Siswa yang ingin dihapus (Ketik 0 untuk Batal): ")
        if (hapus_id == 0): #ke menu utama
            return
            
        if hapus_id in dict_data_siswa: #jika idnya sudah cocok 
            hapus_nama = dict_data_siswa[hapus_id]["nama"]
            konfirmasi = pyip.inputYesNo(f"Yakin ingin menghapus data {hapus_nama}? (yes/no): ")
            if konfirmasi == "yes":
                dict_data_siswa.pop(hapus_id) #hapus dari dict nilai dan data siswa
                dict_data_nilai.pop(hapus_id)
                print(f"Data {hapus_nama} berhasil dihapus.")
            else:
                print("Penghapusan batal")
        else:
            print("ID tidak ada")     
    elif pilih_hapus == "Hapus Tugas/Ujian": #hapus tugas 
        opsi_mapel = list_mata_pelajaran + ["Kembali"]
        hapus_mapel = pyip.inputMenu(opsi_mapel, prompt="Pilih Mata Pelajaran:\n", numbered=True)
        if hapus_mapel == "Kembali": #ke menu utama
            return

        if len(jenis_tugas[hapus_mapel]) == 0: #kondisi gaada tugas dalam mapel
            print("Tidak ada tugas di mata pelajaran ini")
        else:
            opsi_tugas = jenis_tugas[hapus_mapel] + ["Kembali"]
            hapus_tugas = pyip.inputMenu(opsi_tugas, prompt="Pilih Tugas yang akan dihapus:\n", numbered=True) #ilih jenis tugas dalam mapel
            
            if hapus_tugas == "Kembali": 
                return #ke menu utama
            else :  
                konfirmasi = pyip.inputYesNo(f"Yakin menghapus {hapus_tugas} dari {hapus_mapel} untuk semua siswa? (yes/no): ")
                if konfirmasi == "yes": 
                    jenis_tugas[hapus_mapel].remove(hapus_tugas)
                    for id_siswa in dict_data_nilai: #loop untuk menghapus tugas dari semua siswa 
                        dict_data_nilai[id_siswa][hapus_mapel].pop(hapus_tugas)
                    print(f"Tugas {hapus_tugas} berhasil dihapus")
                else:
                    print("Penghapusan batal")
#================================================================================================================================

#eksekusi code
#================================================================================================================================
login_awal()
while True:
    menampilkan_menu_utama()
    pilih_menu = pyip.inputInt("\nMasukkan angka menu yang ingin dijalankan : ", min=1, max=7)
    
    if pilih_menu == 1: 
        reg_siswa_baru()
    elif pilih_menu == 2: 
        menampilkan_profil()
    elif pilih_menu == 3: 
        menampilkan_rapor()
    elif pilih_menu == 4:
        buat_tugas_baru()
    elif pilih_menu == 5: 
        update_nilai_siswa()
    elif pilih_menu == 6:
        delete_data()
    elif pilih_menu == 7: 
        print("yakin anda ingin keluar?")
        print("1. YES")
        print("2. NO")
        konfirmasi = pyip.inputInt("Pilih angka yang ingin dijalankan : ", min=1, max=2)
        if konfirmasi == 2 :
            continue
        else : 
            print("Terima kasih sudah menggunakan StudentHUB")
        break #keluar program
#==========================================================================================
