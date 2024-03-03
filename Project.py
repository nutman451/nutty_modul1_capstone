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
list_penugasan = ['Tugas','UTS','UAS']
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

        case 'format_ID':
            if var_input[0]== 'S' and len(var_input)== 4 and var_input[1:].isnumeric():
                return True
            else:
                return False

#menampilkan ID dan nama setiap siswa dalam dictionary
def show_ID_name():
    global dict_nilai_siswa
    print('')
    for ID in dict_nilai_siswa.keys():
        print(f'ID: {ID}, nama: {dict_nilai_siswa[ID]['nama']}')

#menampilkan semua informasi siswa sesuai ID yang dimasukkan
def show_student_info(ID):
    global dict_nilai_siswa
    print(f'\nID: {ID}')
    for key in dict_nilai_siswa[ID].keys():
        print(f'{key}: {dict_nilai_siswa[ID][key]}')
    print('')

#membuat data murid baru
def create_siswa ():
    global dict_nilai_siswa
    global list_penugasan
    print('ID Siswa', dict_nilai_siswa.keys())
    ID_siswa = input ('Masukan ID siswa baru: ')

    if validasi('format_ID',ID_siswa)== True:
        if validasi('cek_ID',ID_siswa) == True:
            print(f'error!, {ID_siswa} sudah ada dalam daftar')
            ulang = input('masukkan y, untuk mengulang proses buat data siswa baru: ')

            if ulang.lower() == 'y':
                create_siswa()
                return
            else:
                return
            
        else:
            nama = input('masukkan nama siswa baru: ')
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
    else:
        print(f'error!, {ID_siswa} tidak sesuai format ID siswa (S###, # = angka)')
        ulang = input('masukkan y, untuk mengulang proses buat data siswa baru: ')

        if ulang.lower() == 'y':
            create_siswa()
            return

    ulang = input('masukkan y, untuk mengulang proses buat data siswa baru: ')
    if ulang.lower() == 'y':
        create_siswa()
        
    return

#menampilkan data semua murid
def read_all():
    global dict_nilai_siswa
    global list_penugasan
    print('')
    for student in dict_nilai_siswa.keys():
        print(f'ID: {student}\t',end='|')
        for nilai in dict_nilai_siswa[student].keys():
            temp = dict_nilai_siswa[student].get(nilai)
            if nilai == 'nama':
                if len(temp) >8:
                    temp = temp[:7]+'_'
            print(f'{nilai}: {temp}\t',end='|')
        print('')
    print('\n')

#menampilkan data murid tertentu
def read_spesifik_ID():
    global dict_nilai_siswa
    global list_penugasan
    
    show_ID_name()
    ID_murid = input('Pilih ID murid: ')

    if validasi('cek_ID',ID_murid):
        print(f'\nID: {ID_murid}\t',end='|')

        for nilai in dict_nilai_siswa[ID_murid].keys():
            print(f'{nilai}: {dict_nilai_siswa[ID_murid].get(nilai)}\t',end='|')
        print('\n')

    else:
        ulang = input('error! ID siswa tidak ada dalam data siswa. \nmasukkan y untuk mengulang pencarian siswa: ')

        if ulang.lower() == 'y':
            read_spesifik_ID()
    
    return

#menampilkan siswa dengan nilai penugasan yang dibawah nilai KKM sesuai dengan penugasan yang dipilih user
def read_bawah_KKM(penugasan):
    global dict_nilai_siswa
    print('')
    for student in dict_nilai_siswa.keys():
        if dict_nilai_siswa[student][penugasan] < 70:
            print(f'ID: {student}\t',end='|')
            if len(dict_nilai_siswa[student]['nama']) >8:
                print(f'nama: {dict_nilai_siswa[student]['nama'][:8]+'_'}\t',end='|')
            else:
                print(f'nama: {dict_nilai_siswa[student]['nama']}\t',end='|')
            print(f'{penugasan}: {dict_nilai_siswa[student][penugasan]}\t',end='|')
            print('')
    print('\n')

#menu pemilihan penugasan
def Menu_bawah_KKM():
    print('''

1. Tugas
2. UTS
3. UAS
''')
    menu = input('Pilih nomor menu untuk menentukan kriteria pencarian siswa: ')    
    match menu:
        case '1':
            read_bawah_KKM('Tugas')
        case '2':
            read_bawah_KKM('UTS')
        case '3':
            read_bawah_KKM('UAS')
        case _:
            ulang = input('error! pilihan diluar batasan\nmasukkan y untuk mengulang pilihan, inputan lain akan kembali ke menu sebelumnya :')
            if ulang.lower() == 'y':
                Menu_bawah_KKM()
    return

#menu untuk read, terdiri atas menampilkan semua data murid atau murid tertentu
def menu_read():
    print('''
1. Tampilkan semua data siswa
2. Mencari siswa bedasarkan ID
3. Tampilkan siswa bedasarkan penilaian yang dibawah KKM (nilai > 70)
''')
    menu = input('masukkan nomor menu: ')
    match menu:
        case '1':
            read_all()
        case '2':
            read_spesifik_ID()
        case '3':
            Menu_bawah_KKM()
        case _:
            ulang = input('error! pilihan diluar batasan\nmasukkan y untuk kembali ke sub menu tampil, inputan lain akan kembali ke menu utama: ')
            if ulang.lower() == 'y':
                menu_read()
    
    ulang = input('\nmasukkan y untuk kembali ke sub menu tampil, inputan lain akan kembali ke menu utama: ')
    if ulang.lower() == 'y':
        menu_read()
    return

# update semua kolom dalam baris
def multi_oopdate(ID_murid):
    global dict_nilai_siswa
    global list_penugasan
    edit_dict = {}
    show_student_info(ID_murid)
    nama = input('masukkan perubahan nama siswa: ')
    edit_dict.update({'nama':nama})
    for penugasan in list_penugasan:
        while True:
            nilai = input(f'masukkan perubahan nilai {penugasan} : ')
            if validasi('numeric',nilai):
                nilai = int(nilai)
                if validasi('cek_batas',nilai,[0,100]):
                    edit_dict.update({penugasan:nilai}) 
                    break
                else:
                    print('error, nilai harus berupa angka diantara 0 dan 100')
            else:
                print('error, nilai harus berupa angka diantara 0 dan 100')
    print(f'Perubahan data siswa {ID_murid}\n')
    for key in dict_nilai_siswa[ID_murid].keys():
        print(f'{key}: {dict_nilai_siswa[ID_murid][key]} -> {edit_dict[key]}')
    konfirm = input(f'\nMasukkan y untuk menetapkan perubahan, input lain akan membatalkan perubahan :')
    if konfirm == 'y':
        dict_nilai_siswa[ID_murid].update(edit_dict)
        print(f'Perubahan data {ID_murid} berhasil ditetapkan')
    else:
        print('perubahan dibatalkan')


#mengvalidasi dan menerima inputan ID murid
def cek_id_input():
    while True:
        show_ID_name()
        ID_murid = None
        ID_murid = input('Pilih ID murid: ')
        if validasi('cek_ID',ID_murid):
            return ID_murid
        else:
            print(f'error!, {ID_murid} tidak ada dalam daftar')
            ulang = input('masukkan y jika anda ingin mengulang pencarian: ')
            if ulang.lower() == 'y':
                continue
            else:
                return None


# edit sebuah kolom dalam sebuah baris
def single_oopdate(ID_murid):
    global dict_nilai_siswa
    print(f'\nID: {ID_murid}\t',end='|')
    kolom = menu_single_oopdate(ID_murid)
    if kolom in dict_nilai_siswa[ID_murid].keys():
        old_value = dict_nilai_siswa[ID_murid][kolom]
        while True:
            nilai = input(f'\nmasukkan perubahan data {kolom} : ')
            if kolom == 'nama':
                print(f'''[{ID_murid}] data [{kolom}] sebelum di-edit :{old_value}
[{ID_murid}] data [{kolom}] setelah di-edit :{nilai} 
''')
                confirm = input('masukkan y untuk melakukan perubahan, input lain akan membatalkan perubahan :')
                if confirm.lower() == 'y':
                    dict_nilai_siswa[ID_murid][kolom] = nilai
                    print(f'data [{ID_murid}] [{kolom}] berhasil diubah dari [{old_value}] menjadi [{dict_nilai_siswa[ID_murid][kolom]}]')
                    break
                else:
                    print('Perubahan dibatalkan')
            else:
                if validasi('numeric',nilai):
                    nilai = int(nilai)
                    if validasi('cek_batas',nilai,[0,100]):
                        print(f'''nilai [{ID_murid}] [{kolom}] sebelum di-edit :{old_value}
nilai [{ID_murid}] [{kolom}] setelah di-edit :{nilai} 
''')
                        confirm = input('masukkan y untuk melakukan perubahan, input lain akan membatalkan perubahan :')
                        if confirm.lower() == 'y':
                            dict_nilai_siswa[ID_murid][kolom] = nilai
                            print(f'data [{ID_murid}] [{kolom}] berhasil diubah dari [{old_value}] menjadi [{dict_nilai_siswa[ID_murid][kolom]}]')
                            break
                        else:
                            print('Perubahan dibatalkan')
                    else:
                        print('error, nilai harus berupa angka diantara 0 dan 100')
                else:
                    print('error, nilai harus berupa angka diantara 0 dan 100')
    else:
        ulang = input(f'masukkan y jika anda ingin mengulang perubahan data {[ID_murid]}: ')
        if ulang.lower() == 'y':
            single_oopdate(ID_murid)

#menu untuk memilih kolom data siswa yang akan di-edit
def menu_single_oopdate(ID_murid):
    global dict_nilai_siswa
    while True:
        for nilai in dict_nilai_siswa[ID_murid].keys():
            print(f'{nilai}: {dict_nilai_siswa[ID_murid].get(nilai)}\t',end='|')
        print('''
1. Nama
2. nilai Tugas
3. nilai UTS
4. nilai UAS
    ''')
        menu = input('Pilih nomor menu untuk menentukan data siswa yang di-edit: ')    
        match menu:
            case '1':
                return 'nama'
            case '2':
                return 'Tugas'
            case '3':
                return 'UTS'
            case '4':
                return 'UAS'
            case _:
                ulang = input('error! pilihan diluar batasan\nmasukkan y untuk mengulang pilihan, inputan lain akan kembali ke menu sebelumnya :')
                if ulang.lower() != 'y':
                    print('Pemilihan kolom dibatalkan')
                    return None
        

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
            ID_murid = cek_id_input()
            if ID_murid == None:
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
        print('error! inputan menu bukan angka.') 

    ulang = input('\nmasukkan y untuk kembali ke menu edit awal, inputan lain akan kembali ke menu utama :')
    if ulang.lower() == 'y':
        menu_update()
    return

#menghapus semua data siswa yang dipilih
def delete_siswa()-> None: 
    global dict_nilai_siswa
    show_ID_name()
    ID_murid = input('pilih ID murid yang ingin dihapus: ')
    if validasi('cek_ID',ID_murid):
        print(f'{ID_murid} ditemukan')
        show_student_info(ID_murid)
        konfirm = input(f'masukkan y untuk konfirmasi penghapusan {ID_murid}, inputan lain akan membatalkan penghapusan\ninput:')
        if konfirm.lower() == 'y':
            dict_nilai_siswa.pop(ID_murid)
            ulang = input(f'{ID_murid} berhasil dihapus\ninput y jika anda ingin menghapus siswa lagi, inputan lain akan kembali ke menu utama: ')
        else:
            ulang = input(f'penghapusan dibatalkan\ninput y jika anda ingin menghapus siswa lagi, inputan lain akan kembali ke menu utama: ')
    else:
        ulang = input('error! ID siswa tidak ada dalam data siswa. \nmasukkan y untuk mengulang proses penghapusan data siswa, inputan lain akan kembali ke menu utama: ')

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
        id_guru = input('masukkan ID guru untuk memulai login, atau masukkan "0" untuk keluar program \ninput: ')
        if id_guru == '0':
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

