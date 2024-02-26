dict_guru= {
    't01' : {
        'nama':'Bayu',
        'password':'123456'
    },
    't02' : {
        'nama':'Abdi',
        'password':'P@ssw0rd'
    }
}
list_penugasan = ['tugas','UTS','UAS']
dict_nilai_siswa = {
        'S001':{
            'nama': 'Benedict Emanuel Sutrisna',
            'Tugas': 75,
            'UTS': 60,
            'UAS': 67

        },
        'S002':{
            'nama': 'Cahyo Wicaksono',
            'Tugas': 85,
            'UTS': 70,
            'UAS': 77
        },
        'S003':{
            'nama': 'Deva Marina',
            'Tugas': 78,
            'UTS': 80,
            'UAS': 67
        }
    }

#validasi input user
def validasi(val_type,var_input,batas=[0,0]):
    global dict_nilai_siswa
    match val_type:
        case 'numeric': #validasi apakah inputan berupa angka
            return var_input.isnumeric()
        
        case 'cek_ID': #validasi apakah inputan ID terdapat dalam dict_nilai_siswa
            return var_input in dict_nilai_siswa.keys()

        case 'cek_batas': #validasi apakah nilai inputan berada dalam batas angka
            if var_input >= batas[0] and var_input <= batas[1]:
                return True
            else:
                return False

#membuat data murid baru
def create_siswa ():
    global dict_nilai_siswa
    global list_penugasan
    print('ID Siswa', dict_nilai_siswa.keys())
    ID_siswa = input ('\nMasukan ID siswa:')

    if validasi('cek_ID',ID_siswa) == True:
        print(f'error!, {ID_siswa} sudah ada dalam daftar')
        ulang = input('masukkan y, jika anda ingin mengulang: ')

        if ulang.lower() == 'y':
            create_siswa()
            return
        else:
            return
        
    else:
        nama = input('masukkan nama siswa: ')
        dict_nilai_siswa[ID_siswa]={'nama':nama}
        for i in list_penugasan:
            while True:
                nilai = input(f'masukkan nilai {i} : ')
                if validasi('numeric',nilai):
                    nilai = int(nilai)
                    if validasi('cek_batas',nilai,[0,100]):
                        dict_nilai_siswa[ID_siswa][i] = nilai
                        break
                    else:
                        print('error, nilai harus berupa angka diantara 0 dan 100')
                else:
                    print('error, nilai harus berupa angka diantara 0 dan 100')
        print(f'siswa {ID_siswa} berhasil masuk daftar siswa')

    ulang = input('input y jika anda ingin menambah siswa lagi: ')
    if ulang.lower() == 'y':
        create_siswa()
        return
        
    return

#menampilkan data semua murid
def read_all():
    global dict_nilai_siswa
    global list_penugasan
    print('')
    for student in dict_nilai_siswa.keys():
        print(f'ID: {student}\t',end='|')
        for nilai in dict_nilai_siswa[student].keys():
            print(f'{nilai}: {dict_nilai_siswa[student].get(nilai)}\t',end='|')
        print('\n')

#menamilkan data murid tertentu
def read_spesifik_ID():
    global dict_nilai_siswa
    global list_penugasan
    
    print('ID Siswa', dict_nilai_siswa.keys())
    ID_murid = input('Masukkan ID murid: ')

    if validasi('cek_ID',ID_murid):
        print(f'\nID: {ID_murid}\t',end='|')

        for nilai in dict_nilai_siswa[ID_murid].keys():
            print(f'{nilai}: {dict_nilai_siswa[ID_murid].get(nilai)}\t',end='|')

    else:
        ulang = input('error! ID siswa tidak ada dalam data siswa. \nmasukkan y untuk mencoba lagi: ')

        if ulang.lower() == 'y':
            read_spesifik_ID()
    
    return

#menu untuk read, terdiri atas menampilkan semua data murid atau murid tertentu
def menu_read():
    print('''
1. Tampilkan semua data siswa
2. Mencari siswa bedasarkan ID
''')
    menu = input('masukkan nomor menu: ')
    match menu:
        case '1':
            read_all()
        case '2':
            read_spesifik_ID()
        case _:
            ulang = input('error! inputan menu harus angka 1 atau 2. \nmasukkan y untuk mencoba lagi: ')
            if ulang.lower() == 'y':
                menu_read()
    
    ulang = input('\ninput y jika anda ingin mangulang fitur tampilan: ')
    if ulang.lower() == 'y':
        menu_read()
    return

#mengvalidasi dan menerima inputan ID murid
def cek_id_input():
    ID_murid = input('masukkan ID murid: ')
    if validasi('cek_ID',ID_murid):
        return ID_murid
    else:
        print(f'error!, {ID_murid} tidak ada dalam daftar')
        ulang = input('masukkan y jika anda ingin mengulang pencarian: ')
        if ulang.lower() == 'y':
            cek_id_input()
        return 

# edit sebuah kolom dalam sebuah baris
def single_oopdate(ID_murid):
    global dict_nilai_siswa
    print(f'\nID: {ID_murid}\t',end='|')
    for nilai in dict_nilai_siswa[ID_murid].keys():
        print(f'{nilai}: {dict_nilai_siswa[ID_murid].get(nilai)}\t',end='|')

    kolom = input('\nmasukkan data siswa yang ingin diubah: ')
    if kolom in dict_nilai_siswa[ID_murid].keys():
        old_value = dict_nilai_siswa[ID_murid][kolom]
        while True:
            nilai = input(f'\nmasukkan data {kolom} : ')
            if kolom == 'nama':
                dict_nilai_siswa[ID_murid][kolom] = nilai
                print(f'data [{ID_murid}] [{kolom}] berhasil diubah dari [{old_value}] menjadi [{dict_nilai_siswa[ID_murid][kolom]}]')
                break
            else:
                if validasi('numeric',nilai):
                    nilai = int(nilai)
                    if validasi('cek_batas',nilai,[0,100]):
                        print(f'data {ID_murid} {kolom} berhasil diubah dari {old_value} menjadi {dict_nilai_siswa[ID_murid][kolom]}')
                        print(f'Perubahan {kolom} {ID_murid} = {nilai} sukses')
                        break
                    else:
                        print('error, nilai harus berupa angka diantara 0 dan 100')
                else:
                    print('error, nilai harus berupa angka diantara 0 dan 100')
    else:
        print(f'error!, {kolom} tidak ada dalam daftar')
        ulang = input(f'masukkan y jika anda ingin mengulang perubahan data {[ID_murid]}: ')
        if ulang.lower() == 'y':
            single_oopdate(ID_murid)

# update semua kolom dalam baris
def multi_oopdate(ID_murid):
    global dict_nilai_siswa
    global list_penugasan
    nama = input('masukkan nama siswa: ')
    dict_nilai_siswa[ID_murid]={'nama':nama}
    for i in list_penugasan:
        while True:
            nilai = input(f'masukkan nilai {i} : ')
            if validasi('numeric',nilai):
                nilai = int(nilai)
                if validasi('cek_batas',nilai,[0,100]):
                    dict_nilai_siswa[ID_murid][i] = nilai
                    break
                else:
                    print('error, nilai harus berupa angka diantara 0 dan 100')
            else:
                print('error, nilai harus berupa angka diantara 0 dan 100')
    print(f'siswa {ID_murid} berhasil diubah dalam daftar siswa')

# Menu edit
def menu_update():
    print('''
1. Mengubah satu data seorang murid
2. Mengubah semua data seorang murid
''')
    menu = input('masukkan nomor menu: ')
    if validasi('numeric',menu):
        menu = int(menu)
        if validasi('cek_batas',menu,[1,2]):
            print('ID Siswa', dict_nilai_siswa.keys())
            ID_murid = cek_id_input()
            if cek_id_input == None:
                menu_update()
                return
            else: 
                if menu == 1:
                    single_oopdate(ID_murid)
                else:
                    multi_oopdate(ID_murid)  
        else: 
            print('error! inputan menu di luar batas angka.')
    else:
        ('error! inputan menu bukan angka.') 

    ulang = input('\nmasukkan y untuk ke menu edit awal: ')
    if ulang.lower() == 'y':
        menu_update()
    return

#menghapus semua 
def delete_siswa():
    global dict_nilai_siswa
    print('ID Siswa', dict_nilai_siswa.keys())
    ID_murid = input('Masukkan ID murid yang ingin dihapus: ')
    if validasi('cek_ID',ID_murid):
        dict_nilai_siswa.pop(ID_murid)
        ulang = input(f'{ID_murid} berhasil dihapus\ninput y jika anda ingin menghapus siswa lagi: ')

    else:
        ulang = input('error! ID siswa tidak ada dalam data siswa. \nmasukkan y untuk menyoba lagi: ')

    if ulang.lower() == 'y':
        delete_siswa()
    return

#menu utama
def thisStudentScore(id_guru):
    global dict_guru
    global list_penugasan
    global dict_nilai_siswa
    while True:
        print(f'Selamat datang {dict_guru[id_guru]['nama']}')
        print('''
MENU UTAMA
================================================
1. Penambahan Siswa
2. Menu Tampilan
3. Perubahan nilai Siswa
4. Penghapusan Siswa
5. log out
''')
        menu = input('masukkan fitur yang ingin digunakan: ')
        match menu:
            case '1':
                create_siswa()
            case '2':
                menu_read()
            case '3':
                menu_update()
            case '4':
                delete_siswa()
            case '5':
                print('terima kasih dan sampai jumpa')
                return None
            case _:
                input('Error! input harus berupa angka diantara 1 dan 5\ntekan enter untuk kembali ke awal menu')

#menu login
def main():
    while True:
        print('''
Program thisStudentScore
========================
''')
        id_guru = input('masukkan ID guru untuk memulai login, atau masukkan "keluar" untuk keluar program \nmasukkan pengguna: ')
        if id_guru.lower() == 'keluar':
            print('program dimatikan')
            break
        password = input('masukkan password: ')
        if id_guru in dict_guru.keys():
            if dict_guru[id_guru]['password'] == password:
                id_guru = thisStudentScore(id_guru)
            else:
                input('Error! id atau password salah! tekan enter untuk mengulang login')
        else:
            input('Error! id atau password salah! tekan enter untuk mengulang login')

main()


