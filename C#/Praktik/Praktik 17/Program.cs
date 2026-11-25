using System;

class Program_17
{
    
    static void Tampilkan_Header()
    {
        Console.WriteLine("===============================");
        Console.WriteLine("      IDENTITAS MAHASISWA      ");
        Console.WriteLine("===============================");
    }

    static void Tampilkan_Data(string Nama, string NIM, string Prodi)
    {
        Console.WriteLine($"Nama    : {Nama}");
        Console.WriteLine($"NIM     : {NIM}");
        Console.WriteLine($"Prodi   : {Prodi}");
    }

    static void Main()
    {
        Tampilkan_Header();
        Tampilkan_Data("Naufal Khalil Rakhasyah", "2605191024", "Teknologi Rekayasa Multimedia Grafis");
    }

}