import turtle
import math
import random

# 1. Pengaturan Jendela Layar
layar = turtle.Screen()
layar.setup(width=1000, height=1000)
layar.bgcolor("black")
layar.title("Simulasi Tata Surya dengan Garis Edar Orbit")

# Matikan animasi otomatis agar rendering instan
turtle.tracer(0, 0)

# 2. Fungsi Pembantu untuk Membuat Objek Astronomi
def buat_objek(warna, ukuran, bentuk="circle"):
    t = turtle.Turtle()
    t.shape(bentuk)
    t.color(warna)
    t.shapesize(ukuran)
    t.penup()
    return t

# Fungsi khusus untuk menggambar garis edar (jalur orbit) planet berbentuk lingkaran
def gambar_garis_edar(radius, warna):
    penggambar = turtle.Turtle()
    penggambar.speed(0)
    penggambar.hideturtle()
    penggambar.penup()
    # Pindah ke posisi bawah lingkaran orbit
    penggambar.goto(0, -radius)
    penggambar.pendown()
    penggambar.color(warna)
    penggambar.pensize(1)
    penggambar.circle(radius)

# Membuat Matahari di Pusat
matahari = buat_objek("yellow", 3.0)

# 3. Konfigurasi Planet dan Jumlah Bulan Berdasarkan Data Terbaru
data_planet = [
    ["Bumi", "blue", 1.0, 120, 0.015, 1, ["Bulan"]],
    ["Jupiter", "orange", 2.2, 240, 0.008, 115, ["Io", "Europa", "Ganymede", "Callisto"]],
    ["Saturnus", "khaki", 1.8, 360, 0.005, 293, ["Titan", "Rhea", "Iapetus", "Dione", "Tethys"]],
    ["Uranus", "lightcyan", 1.4, 460, 0.003, 29, ["Titania", "Oberon", "Umbriel", "Ariel"]],
    ["Neptunus", "royalblue", 1.3, 550, 0.002, 16, ["Triton", "Proteus", "Nereid"]]
]

# 4. Membangun Struktur Sistem Planet, Bulan, dan Menggambar Jalur Orbit
daftar_sistem = []

for nama, warna, ukuran, jarak, kec, total_bulan, bulan_utama in data_planet:
    # Gambar garis edar permanen untuk planet ini di latar belakang
    gambar_garis_edar(jarak, "darkgray")
    
    objek_planet = buat_objek(warna, ukuran)
    sudut_planet = random.uniform(0, 2 * math.pi)
    
    daftar_bulan_planet = []
    
    # Generate semua bulan secara otomatis
    for i in range(total_bulan):
        if i < len(bulan_utama):
            ukuran_bulan = 0.3
            warna_bulan = "lightgray"
            jarak_bulan = 18 + (i * 5)
        else:
            ukuran_bulan = 0.1
            warna_bulan = "gray"
            jarak_bulan = random.uniform(15, 45)
            
        objek_bulan = buat_objek(warna_bulan, ukuran_bulan)
        sudut_bulan = random.uniform(0, 2 * math.pi)
        kec_bulan = random.uniform(0.03, 0.1)
        
        daftar_bulan_planet.append([objek_bulan, jarak_bulan, kec_bulan, sudut_bulan])
        
    daftar_sistem.append([objek_planet, jarak, kec, sudut_planet, daftar_bulan_planet])

# 5. Loop Animasi Utama
while True:
    for sistem in daftar_sistem:
        planet, r_planet, v_planet, sudut_p, list_bulan = sistem
        
        # Hitung & update posisi Planet mengitari Matahari
        x_planet = r_planet * math.cos(sudut_p)
        y_planet = r_planet * math.sin(sudut_p)
        planet.goto(x_planet, y_planet)
        
        # PERBAIKAN 1: Update sudut planet pada indeks ke-3
        sistem[3] += v_planet
        
        # Hitung & update semua posisi Bulan mengitari Planet ini
        for bulan in list_bulan:
            t_bulan, r_bulan, v_bulan, sudut_b = bulan
            
            # Koordinat bulan = Posisi Planet Saat Ini + Jarak Orbit Bulan
            x_bulan = x_planet + (r_bulan * math.cos(sudut_b))
            y_bulan = y_planet + (r_bulan * math.sin(sudut_b))
            t_bulan.goto(x_bulan, y_bulan)
            
            # PERBAIKAN 2: Update sudut bulan pada indeks ke-3
            bulan[3] += v_bulan
            
    # Refresh layar secara manual
    turtle.update()

