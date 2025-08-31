from unittest import result
import mysql.connector
import pandas as pd
import numpy as np

def connect_db():
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'Ijj4@swt1',
        database = 'perpustakaan'  
    )
    return mydb

# tuliskan credential database untuk create connection
def pandas_df():
    mydb = connect_db()
    database = 'perpustakaan'  # ganti dengan nama database Anda

    # create access to DB
    mycursor = mydb.cursor()
    # tulis query SQL
    query = '''select * from perpustakaan1'''
    # mengeksekusi query
    mycursor.execute(query)
    # gather all result
    result = mycursor.fetchall()

    # menampilkan hasil dalam bentuk table dengan pandas
    df = pd.DataFrame(result, columns=mycursor.column_names)
    return df
# def pandas_df2(query=any, values=any):
#     mydb = connect_db()
#     database = 'perpustakaan'

#     # create access to DB
#     mycursor = mydb.cursor()
#     # tulis query SQL
#     if query and values:
#         mycursor.execute(query, values)
#     else:
#         query = '''select * from perpustakaan1'''
#         mycursor.execute(query)
#     # gather all result
#     result = mycursor.fetchall()

# # menampilkan hasil dalam bentuk table dengan pandas
# df = pd.DataFrame(result, columns=mycursor.column_names)
def show_menu():
    while True:
        menu = input(f'''
                     ####################################
                        Selamat Datang di Perpustakaan
                     ####################################
Pilihan Menu:
    1. Tampilkan 10 data buku
    2. Tambah data buku
    3. Hapus data buku
    4. Cari data buku
    5. Hitung rata-rata kolom numeric
    6. Tampilkan visualisasi data
    7. Keluar dari program

            Masukkan pilihan menu: 
    ''')
        if menu == "1":
            mydb = connect_db()
            mycursor = mydb.cursor()
            df = pandas_df()
            print(df.head(10))
            print("Menampilkan 10 data buku")
            input("Tekan Enter untuk melanjutkan...")
            # continue
            mycursor.close()
            mydb.close()
            continue
        elif menu == "2":
        # Tambah data buku
            print("Menambah data buku")
            mydb = connect_db()
            mycursor = mydb.cursor()
            df = pandas_df()
            id_buku = input("Masukkan ID Buku: ")
            if id_buku in df['ID'].values:
                print(f"ID Buku '{id_buku}' sudah ada.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            else:
                # print(f"ID Buku '{id_buku}' tersedia.")
                # continue
                judul_buku = input("Masukkan Judul Buku: ")
                pengarang = input("Masukkan Pengarang: ")
                kategori = input("Masukkan Kategori: ")
                penerbit = input("Masukkan Penerbit: ")
                tahun_terbit = input("Masukkan Tahun Terbit: ")
                jumlah_buku = input("Masukkan Jumlah Buku: ")
                kota = input("Masukkan Kota: ")
                pages = input("Masukkan Jumlah Halaman: ")

                # Query untuk menambah data buku
                query = '''INSERT INTO perpustakaan1 (ID, judul_buku, pengarang, kategori_buku, penerbit, tahun_terbit, jumlah_buku, kota, pages)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
                values = (id_buku, judul_buku, pengarang, kategori, penerbit, tahun_terbit, jumlah_buku, kota, pages)
                mycursor.execute(query, values)
                mydb.commit()
                print("Data buku berhasil ditambahkan dengan ID:", id_buku)
                input("Tekan Enter untuk melanjutkan...")
                mycursor.close()
                mydb.close()
                continue
        elif menu == "3":
            # Hapus data buku
            mydb = connect_db()
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM perpustakaan1")
            result = mycursor.fetchall()
            df = pd.DataFrame(result, columns=mycursor.column_names)
            print(df)
            id_buku = input("Masukkan ID Buku yang akan dihapus: ")
            if id_buku not in df['ID'].values:
                print(f"ID Buku '{id_buku}' tidak ditemukan.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            else:
                query = '''DELETE FROM perpustakaan1 WHERE ID = %s'''
                mycursor.execute(query, (id_buku,))
                print("Data buku berhasil dihapus dengan ID:", id_buku)
                mydb.commit()
                mycursor.close()
                mydb.close()
            input("Tekan Enter untuk melanjutkan...")
            continue
        elif menu == "4":
             

            menu = input('''   Masukkan pilihan sub-menu:
                         1. Cari data buku berdasarkan kategori
                         2. Cari data buku berdasarkan judul
            ''')

            if menu == "1":
                # Cari data buku
                mydb = connect_db()
                mycursor = mydb.cursor()
                mycursor.execute("SELECT * FROM perpustakaan1")
                result = mycursor.fetchall()
                df = pd.DataFrame(result, columns=mycursor.column_names)
                df = df.dropna(subset=['kategori_buku', 'jumlah_buku', 'pages'])   
                keyword = input("Masukkan kata kunci pencarian: ")
                results = df[df['kategori_buku'].str.contains(keyword, case=False)]
                if not results.empty:
                    print("Hasil pencarian:")
                    print(results)
                else:
                    print("Data buku tidak ditemukan.")
                input("Tekan Enter untuk melanjutkan...")
            elif menu == "2":
                keyword = input("Masukkan kata kunci pencarian: ")
                results = df[df['judul_buku'].str.contains(keyword, case=False)]
                if not results.empty:
                    print("Hasil pencarian:")
                    print(results)
                else:
                    print("Data buku tidak ditemukan.")
        elif menu == "5":
            menu = input('''   Masukkan pilihan sub-menu:
                         1.Hitung rata-rata jumlah buku
                         2.Hitung rata-rata tahun terbit
                         3.Hitung rata-rata jumlah halaman
                         4.Hitung rata-rata jumlah buku per kategori
            ''')
            if menu == "1":
                # Hitung rata-rata jumlah buku
                if 'jumlah_buku' in df.columns:
                    average = df['jumlah_buku'].mean()
                    print(f"Rata-rata jumlah buku: {average}")
                else:
                    print("Kolom 'jumlah_buku' tidak ditemukan.")
                input("Tekan Enter untuk melanjutkan...")
            elif menu == "2":
                # Hitung rata-rata tahun terbit
                if 'tahun_terbit' in df.columns:
                    average = df['tahun_terbit'].mean()
                    print(f"Rata-rata tahun terbit: {average}")
                else:
                    print("Kolom 'tahun_terbit' tidak ditemukan.")
            elif menu == "3":
                # Hitung rata-rata jumlah halaman
                if 'pages' in df.columns:
                    average = df['pages'].mean()
                    print(f"Rata-rata jumlah halaman: {average}")
                else:
                    print("Kolom 'pages' tidak ditemukan.")
            elif menu == "4":
                # Hitung rata-rata jumlah buku per kategori
                if 'kategori_buku' in df.columns and 'jumlah_buku' in df.columns:
                    average = df.groupby('kategori_buku')['jumlah_buku'].mean()
                    print("Rata-rata jumlah buku per kategori:")
                    print(average)
                else:
                    print("Kolom 'kategori_buku' atau 'jumlah_buku' tidak ditemukan.")
        elif menu == "6":
            # Tampilkan visualisasi data
            import matplotlib.pyplot as plt
            import seaborn as sns
            df = pandas_df()
            df = df.dropna(subset=['kategori_buku', 'jumlah_buku', 'pages'])
            sns.set(style="whitegrid")
            menu = input('''   Masukkan pilihan sub-menu:
                         1.Tampilkan jumlah halaman per kategori
                         2.Tampilkan jumlah buku per kategori
                         3.Tampilkan jumlah buku dan halaman per kategori using seaborn
            ''')
            if menu == "1":
                plt.title('Distribusi Jumlah Pages per Kategori',fontdict={'fontsize': 16, 'fontweight': 'bold'})
                sns.histplot(data=df, x='pages', hue='kategori_buku', multiple='stack', bins=30, stat='density')
                plt.xlabel('Jumlah Pages',fontdict={'fontsize': 12, 'fontweight': 'bold'})
                plt.ylabel('Kepadatan',fontdict={'fontsize': 12, 'fontweight': 'bold'})
                plt.show()                
            elif menu == "2":
                plt.title('Distribusi Jumlah buku per Kategori',fontdict={'fontsize': 16, 'fontweight': 'bold'})
                sns.histplot(data=df, x='jumlah_buku', hue='kategori_buku', multiple='stack', bins=30, stat='density')
                plt.xlabel('Jumlah Buku',fontdict={'fontsize': 12, 'fontweight': 'bold'})
                plt.ylabel('Kepadatan',fontdict={'fontsize': 12, 'fontweight': 'bold'})
                plt.show()
            elif menu == "3":
                if 'jumlah_buku' in df.columns and 'pages' in df.columns:    
                    df.groupby('kategori_buku').agg({'jumlah_buku': 'sum', 'pages': 'sum'}).plot(kind='bar', stacked=True, figsize=(10, 6), colormap='Set2')
                    plt.title('Jumlah Buku dan Halaman per Kategori')
                    plt.xlabel('Kategori')
                    plt.ylabel('Jumlah')
                    plt.show()    
                else:
                    print("Kolom 'jumlah_buku' atau 'pages' tidak ditemukan.")
            else:
                print("Kolom 'kategori' tidak ditemukan dalam data.")
            input("Tekan Enter untuk melanjutkan...")
        elif menu == "7":
            # Keluar dari program
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Menu tidak valid.")
            input("Tekan Enter untuk melanjutkan...")
if __name__ == "__main__":
    show_menu()
