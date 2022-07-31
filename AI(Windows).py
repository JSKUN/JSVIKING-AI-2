import os
from PIL import Image
import webbrowser
import calendar
import subprocess
import re 
import pyfiglet
import sys
import socket
from datetime import datetime
import time
tolak = 'Anda membutuhkan Password untuk mengakses file :)'

def hapus():
   os.system('cls')

hapus()

print(pyfiglet.figlet_format('Jsviking AI 2'))
print('Loading Please Wait ...')
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
        print('Waktu sekarang adalah: ',sekarang.strftime('%H:%M'))
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