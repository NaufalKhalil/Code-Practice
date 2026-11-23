using System;

class Program_16
{
    static void Tampilkan_Biodata(string Nama, int Umur)
    {
        Console.WriteLine($"Nama    : {Nama}");
        Console.WriteLine($"Umur    : {Umur} tahun");
    }
    static void Main()
    {
        Tampilkan_Biodata("Naufal", 18);
        Tampilkan_Biodata("Quinsha", 17);
    }
}