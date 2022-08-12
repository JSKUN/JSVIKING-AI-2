import os
from PIL import Image, ImageFilter
import webbrowser
import calendar
import subprocess
import re 
import pyfiglet
import sys
import socket
from datetime import datetime
import time
import ascii_magic
import random
tolak = 'Anda membutuhkan Password untuk mengakses file :)'

def hapus():
   os.system('cls')

def convert(img, tipe):
    img = Image.open(img)

    img.save(f'img2.{tipe}')

def crop(img,x1,y1,x2,y2):
    img = Image.open(img)

    img2 = img.crop((x1,y1,x2,y2))
    img2.save('img2.png')

def resize(img,width,height):
    img = Image.open(img)

    img2 = img.resize((width,height))
    img2.save('img2.png')

def color(img):
    img = Image.open(img)
    w,h = img.size
    img2 = Image.new(('RGBA'),(w,h))
    for wi in range(w):
         for he in range(h):
            r, g, b = img.getpixel((wi,he))
            gray = int(r * 0.212 + g * 0.715 + b * 0.0746)
            img2.putpixel((wi, he), (gray, gray,gray,255))
    img2.save('img2.png')

def enhancer(name,enhance_type):
    if enchanche == 1:
        enchanche2 = name.filter(ImageFilter.BLUR)
    elif enchanche == 2:
        enchanche2 = name.filter(ImageFilter.DETAIL)
    elif enchanche == 3:
        enchanche2 = name.filter(ImageFilter.CONTOUR)
    elif enchanche == 4:
        enchanche2 = name.filter(ImageFilter.EDGE_ENCHANCE)
    elif enchanche == 5:
        enchanche2 = name.filter(ImageFilter.EMBOSS)
    elif enchanche == 6:
        enchanche2 = name.filter(ImageFilter.SHARPEN)
    elif enchanche == 7:
        enchanche2 = name.filter(ImageFilter.SMOOTH)

    enchanche2.save('enchanched.png')



hapus()

print(pyfiglet.figlet_format('Jsviking AI 2'))
print('Sumber code bisa lihat sini: https://github.com/JSKUN/JSVIKING-AI-2.git')
print('Loading Please Wait ...')
print(' ')
time.sleep(2)

nama = input('[None:None] Masukkan nama: ')
password = input(f'[{nama.capitalize()}:None] Masukkan password: ')

hapus()

while True:
    Perintah = input(f'[{nama.capitalize()}:Active] Masukkan Perintah: ')
    sekarang = datetime.now()
    if Perintah.capitalize() == 'Chus':
        pwchecker = input('Masukkan password: ')
        if pwchecker == password:
            nama = input('Masukkan nama baru: ')
        else:
            print(tolak)
        print(' ')

    elif Perintah.capitalize() == 'Chpass':
        pwchecker = input('Masukkan password lama: ')
        if pwchecker == password:
            nama = input('Masukkan password baru: ')
        else:
            print(tolak)
        print(' ')

    elif Perintah.capitalize() == 'Waktu':
        print('Waktu sekarang adalah: ',sekarang.strftime('%X'))
        print(' ')

    elif Perintah.capitalize() == 'Hari':
        print('Waktu sekarang adalah: ',sekarang.strftime('%A'))
        print(' ')

    elif Perintah.capitalize() == 'Waktu dan tanggal':
        print('Waktu sekarang adalah: ',sekarang.strftime('%c'))
        print(' ')

    elif Perintah.capitalize() == 'Tanggal':
        print('Tanggal hari ini adalah: ',sekarang.strftime('%x'))
        print(' ')

    elif Perintah.capitalize() == 'Cuaca':
        print('Pergi ke sini (https://www.accuweather.com/)')
        print(' ')

    elif Perintah.capitalize() == 'Warna':
        pwchecker = input('Masukkan password: ')
        if pwchecker == password:
            hapus()
            print('Perintah ini akan memakan waktu lama untuk menganalisis gambar besar')
            lokasigambar = (input('Masukkan lokasi file: '))
            warna = []
            warna2 = []
            gambar = Image.open(lokasigambar)
            Width, Height = gambar.size

            for w in range(Width):
                for h in range(Height):
                    warna.append(gambar.getpixel((w, h)))
                    
                    
            print('Jumlah pixel',len(warna))
            for elemen in warna:
                if elemen not in warna2:
                    warna2.append(elemen)
            print('Warna yang terdeteksi: ',len(warna2),'buah')
        else:
            print(tolak)
        print(' ')

    elif Perintah.capitalize() == 'Kalkulator':
        perhitungan = input('Masukkan perhitungan: ')
        print('Hasil perhitungan: ',perhitunganeval(perhitungan))
        print(' ')

    elif Perintah.capitalize() == 'Keluar':
        hapus()
        break

    elif Perintah.capitalize() == 'Wikipedia':
        cari = input('Masukkan kata yang mau dicari: ')
        hapus()
        try:
            webbrowser.open(f'https://wikipedia.org/wiki/{cari}')
        except:
            print('Tidak ditemukan')
        print(' ')

    elif Perintah.capitalize() == 'Internet':
        cari = input('Masukkan kata yang mau dicari: ')
        hapus()
        try:
            webbrowser.open(f'https://duckduckgo.com/?q={cari}')
        except:
            print('Tidak ditemukan')
        print(' ')

    elif Perintah.capitalize() == 'Github':
        cari = input('Masukkan kata yang mau dicari: ')
        hapus()
        try:
            webbrowser.open(f'https://github.com/search?q={cari}')
        except:
            print('Tidak ditemukan')
        print(' ')

    elif Perintah.capitalize() == "Kalender":
        tahun = int(input("masukkan tahun:"))
        kal = calendar.calendar(tahun)
        print(kal)
        print("waktu sekarang: ")
        waktu_sekarang = sekarang.strftime('%a-%b-%Y')
        print(waktu_sekarang)
        print(' ')
    
    elif Perintah.capitalize() == "Wifi":

        command_output = subprocess.run(
            ["netsh", "wlan", "show", "profiles"], capture_output=True
        ).stdout.decode()
        profile_names = re.findall(
            "All User Profile     : (.*)\r", command_output)

        wifi_list = []

        if len(profile_names) != 0:
            for name in profile_names:
                wifi_profile = {}
                profile_info = subprocess.run(
                    ["netsh", "wlan", "show", "profile", name], capture_output=True
                ).stdout.decode()

                if re.search("Security key           : Absent", profile_info):
                    continue
                else:
                    wifi_profile["Nama"] = name
                    profile_info_pass = subprocess.run(
                        ["netsh", "wlan", "show", "profile", name, "key=clear"],
                        capture_output=True,
                    ).stdout.decode()
                    password = re.search(
                        "Key Content            : (.*)\r", profile_info_pass
                    )

                    if password == None:
                        wifi_profile["password"] = None
                    else:
                        wifi_profile["password"] = password[1]
                        wifi_list.append(wifi_profile)

        for x in range(len(wifi_list)):
            print(wifi_list[x])
        print(' ')
    
    elif Perintah.capitalize() == 'Cmd':
        os.system('start')
        print(' ')
    elif Perintah.capitalize() == 'Nano':
        pwchecker = input('Masukkan password: ')
        if pwchecker == password:
            try:
                file = input('Masukkan nama dan bentuk file: ')
                os.system(f'nano {file}')
            except:
                file = input('Masukkan nama dan bentuk file: ')
                os.system(f'sudo nano {file}')
        else:
            tolak
        print(' ')

    elif Perintah.capitalize() == 'Hapus':
        hapus()

    elif Perintah.capitalize() == 'Git':
        pwchecker = input('Masukkan password: ')
        if pwchecker == password:
            repo = input('Masukkan link github yang akan di salin: ')
            try:
                os.system(f'git clone {repo}')
            except:
                print('Anda belum menginstall git')
        else:
            tolak
        print(' ')

    elif Perintah.capitalize() == 'Neofetch':
        try:
            os.system('neofetch')
        except:
            print('Anda belum menginstall neofetch')
        print(' ')

    elif Perintah.capitalize() == 'Code':
        pwchecker = input('Masukkan password: ')
        if pwchecker == password:
            try:
                file = input('Masukkan nama dan bentuk file: ')
                os.system('code {file}')
            except:
                print('Anda belum menginstall VScode')
        else:
            tolak
        print(' ')
    
    elif Perintah.capitalize() == 'Ipconfig':
        os.system('Ipconfig')
        print(' ')
    
    elif Perintah.capitalize() == 'Technoblade':
        print(pyfiglet.figlet_format('Technoblade never dies'))
        print(' ')
    
    elif Perintah.capitalize() == 'Suhu':
        suhu = input("Masukan suhu (Misal: 30C, 20F, 21K, 44R): ")
        drjt = int(suhu[:-1])
        inputan = suhu[-1]

        if inputan.upper() == "C":
            hasil1 = float((9 * drjt) / 5 + 32)
            hasil2 = float(drjt + 273.15)
            hasil3 = float(4/5 * drjt)
            jenisX = "Celcius"
            jenis1 = "Fahrenheit"
            jenis2 = "Kelvin"
            jenis3 = "Reamur"
                        
        elif inputan.upper() == "F":
            hasil1 = float((drjt - 32) * 5 / 9)
            hasil2 = float(((drjt - 32) * 5 / 9) + 273.15)
            hasil3 = float(4/9 * (drjt-32))
            jenisX = "Fahrenheit"
            jenis1 = "Celsius"
            jenis2 = "Kelvin"
            jenis3 = "Reamur"
        elif inputan.upper() == "K":
            hasil1 = float(drjt - 273.15)
            hasil2 = float(((drjt - 273.15) * 9 / 5)+32)
            hasil3 = float(4/5 * (drjt-273))
            jenisX = "Kelvin"
            jenis1 = "Celcius"
            jenis2 = "Fahrenheit"
            jenis3 = "Reamur"
        elif inputan.upper() == "R":
            hasil1 = float((5/4) * drjt)
            hasil2 = float((9/4 * drjt) + 32)
            hasil3 = float((5/4 * drjt) + 273)
            jenisX = "Reamur"
            jenis1 = "Celcius"
            jenis2 = "Fahrenheit"
            jenis3 = "Kelvin"
        else:
            print("Inputan tidak sesuai!! Perhatikan Penulisan Input")

        print(drjt,jenisX,"=","{:.1f}".format(hasil1),jenis1)
        print(drjt,jenisX,"=","{:.1f}".format(hasil2),jenis2)
        print(drjt,jenisX,"=","{:.1f}".format(hasil3),jenis3)
        print(' ')

    elif Perintah.capitalize() == 'Kontras':
        pwchecker = input('Masukkan password: ')
        if pwchecker == password:
            hapus()
            print('Perintah ini akan memakan waktu lama untuk menganalisis gambar besar')
            lokasigambar = (input('Masukkan lokasi file: '))
            
            source = Image.open(lokasigambar)
            width, height = source.size
            result = Image.new("RGBA", (width,height))

            kecerahan = int(input('Masukkan kecerahan: '))

            for w in range(width):
                for h in range(height):
                    r, g, b = source.getpixel((w, h))
                    if kecerahan < 0 :
                        result.putpixel((w, h), ((kecerahan-(kecerahan * 2))- r, (kecerahan-(kecerahan * 2)) - g, (kecerahan-(kecerahan * 2)) - b, 255))
                    elif kecerahan > 0 :
                        result.putpixel((w, h), (kecerahan + r, kecerahan + g, kecerahan + b, 255))
                    elif kecerahan == 0 :
                        pass
            
            result.save('Save.png')
        else:
            print(tolak)
        print(' ')

    elif Perintah.capitalize() == 'Filter':
        pwchecker = input('Masukkan password: ')
        if pwchecker == password:
            hapus()
            print('Perintah ini akan memakan waktu lama untuk menganalisis gambar besar')
            lokasigambar = (input('Masukkan lokasi file: '))

            print('(1) Blur \n (2) Detail \n (3) Contour \n (4) Edge_enchance \n (5) Emboss \n (6) Sharpen \n (7) Smooth')
            enchanche = int(input('Pilih jenis filter (nomor): '))

            img2 = Image.open(lokasigambar)
            enhancer(img2, enchanche)

            print('Sudah difilter')
        else:
            print(tolak)
        print(' ')

    elif Perintah.capitalize() == 'Crop':
        pwchecker = input('Masukkan password: ')
        if pwchecker == password:
            hapus()
            img = str(input('Masukkan lokasi gambar: '))
            x1 = int(input('Masukkan Kordinat1: '))
            y1 = int(input('Masukkan Kordinat2: '))
            x2 = int(input('Masukkan Kordinat3: '))
            y2 = int(input('Masukkan Kordinat4: '))
            crop(img,x1,y1,x2,y2)
        else:
            print(tolak)
        print(' ')
    
    elif Perintah.capitalize() == 'Convert':
        pwchecker = input('Masukkan password: ')
        if pwchecker == password:
            hapus()
            img = str(input('Masukkan gambar: '))
            tipe = str(input('Masukkan tipe file: '))

            convert(img,tipe)
        else:
            print(tolak)
        print(' ')


    elif Perintah.capitalize() == 'Resize':
        pwchecker = input('Masukkan password: ')
        if pwchecker == password:
            hapus()
            img = str(input('Masukkan gambar: '))
            height = int(input('Masukkan panjang: '))
            width = int(input('Masukkan lebar: '))

            resize(img,height,width)
        else:
            print(tolak)
        print(' ')

    elif Perintah.capitalize() == 'Gray':
        pwchecker = input('Masukkan password: ')
        if pwchecker == password:
            hapus()
            img = str(input('Masukkan gambar: '))
            color(img)
        else:
            print(tolak)
        print(' ')

    elif Perintah.capitalize() == 'Pip':
        print('1 = List \n 2 = Install \n 3 = Uninstall \n 4 = Update')
        pilihan = str(input('Pilihan: '))

        if pilihan == '1':
            os.system('pip list')

        elif pilihan == '2':
            lib = input("Masukkan library yang di install: ")  

            os.system(f'pip install {lib}')
        elif pilihan == '3':
            lib = input("Masukkan library yang di uninstall: ")     

            os.system(f'pip uninstall {lib}')

        elif pilihan == '4':
            os.system('python.exe -m pip install --upgrade pip')
        print(' ')

    elif Perintah.capitalize() == 'Batu gunting kertas':
        skork = 0 
        skoru = 0
        for i in range(11):
            pilihan = input('Masukkan pilihan (Batu Gunting Kertas): ')
            pilihanl = ['Batu','Gunting','Kertas']
            komputer = random.choice(pilihanl)

            if pilihan.capitalize() == 'Batu' and komputer.capitalize() == 'Kertas':
                print('Komputer menang') 
                skork += 1
            elif pilihan.capitalize() == 'Gunting' and komputer.capitalize() == 'Batu':
                print('Koputer menang')
                skoru += 1
            elif pilihan.capitalize() == 'Kertas' and komputer.capitalize() == 'Gunting':
                print('Komputer menang')
                skork += 1
            elif pilihan.capitalize() == 'Batu' and komputer.capitalize() == 'Gunting':
                print('User menang')
                skoru += 1
            elif pilihan.capitalize() == 'Gunting' and komputer.capitalize() == 'Kertas':
                print('User menang')
                skork += 1
            elif pilihan.capitalize() == 'Kertas' and komputer.capitalize() == 'Batu':
                print('User menang')
                skoru += 1
            elif pilihan.capitalize() == komputer.capitalize():
                print('Seri')
        print(' ')
        print(' ')
        if skork > skoru:
            print(f'Komputer menang dengan skor {skork}')
            print(f'Skor user {skoru}')
        elif skoru > skork:
            print(f'User menang dengan skor {skoru}')
            print(f'Skor komputer {skork}')
        elif skoru == skork:
            print('Seri')
        print(' ')
    
    elif Perintah.capitalize() == 'Ascii':
        tipe = input('Text/Gambar: ')

        if tipe.capitalize() == 'Gambar':
            pwchecker = input('Masukkan password: ')
            if pwchecker == password:
                file  = input('Masukkan lokasi file: ')
                output = ascii_magic.from_image_file(file,columns = 100, char='#')
                ascii_magic.to_terminal(output)
        elif tipe.capitalize() == 'Text':
            text = input('Masukkan text: ')
            print(pyfiglet.figlet_format(text))
        print(' ')