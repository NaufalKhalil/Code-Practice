using System;

class Praktik_10 {
    static void Main(string[] args) {

        string NIM = "";
        string Nama = "";
        string Validasi = "";

        while (Validasi != "T") {
            Console.Write("Masukkan NIM :");
            NIM = Console.ReadLine();

            Console.Write("Masukkan Nama :");
            Nama = Console.ReadLine();

            Console.Write("Input data lagi? [Y/T] : ");
            Validasi = Console.ReadLine(); 
        }

        Console.WriteLine("Selesai");
    }
}
