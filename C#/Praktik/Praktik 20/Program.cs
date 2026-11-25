using System;

class Program_20
{
    static void Tampilkan_Hasil(string NIM, string Nama, string Nomor_HP, string Alamat)
    {
        Console.WriteLine($"{NIM, -10} {Nama, -16} {Nomor_HP, -15} {Alamat}");
    }
    static void Main(string[] args)
    {

        Console.Write("Jumlah data yang akan di input : ");
        int Jumlah_Data = int.Parse(Console.ReadLine()!);

        string[] Nama = new string[Jumlah_Data];
        string[] NIM = new string[Jumlah_Data];
        string[] Nomor_HP = new string[Jumlah_Data];
        string[] Alamat = new string[Jumlah_Data];

       for (int i = 0; i < Jumlah_Data; i++)
        {
            Console.WriteLine($"\n--- Data Mahasiswa ke-{i + 1} ---");
            
            Console.Write("Masukkan nama anda : ");
            Nama[i] = Console.ReadLine()!;

            Console.Write("Masukkan NIM anda : ");
            NIM[i] = Console.ReadLine()!;

            Console.Write("Masukkan Nomor Handphone anda : ");
            Nomor_HP[i] = Console.ReadLine()!;

            Console.Write("Masukkan Alamat anda : ");
            Alamat[i] = Console.ReadLine()!;
        }

        Console.Clear();

        Console.WriteLine("================================================================");
        Console.WriteLine("                     BIODATA MAHASISWA");
        Console.WriteLine("                     PRODI TRMG POLMED");
        Console.WriteLine("================================================================");
        Console.WriteLine($"{"NIM", -10} {"Nama", -16} {"No.HP", -15} Alamat");
        Console.WriteLine("================================================================");
        
        for (int i = 0; i < Jumlah_Data; i++)
        {
            Tampilkan_Hasil(NIM[i], Nama[i], Nomor_HP[i], Alamat[i]);    
        }
        
        Console.WriteLine("================================================================");

    }
}