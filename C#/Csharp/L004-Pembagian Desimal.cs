using System;

namespace Code_Practice{
    class L004_Pembagian_Desimal{
        static void Main(string[] args){
            
            Console.Write("Masukkan angka pertama   : ");
            double Angka_Pertama = double.Parse(Console.ReadLine());
            Console.Write("Masukkan angka kedua     : ");
            double Angka_Kedua = double.Parse(Console.ReadLine());
            
            Console.WriteLine(" ");
            
            double Hasil_Penjumlahan = Angka_Pertama + Angka_Kedua;
            double Hasil_Pengurangan = Angka_Pertama - Angka_Kedua;
            double Hasil_Perkalian = Angka_Pertama * Angka_Kedua;
            double Hasil_Pembagian = Angka_Pertama / Angka_Kedua; 
            
            Console.WriteLine("Hasil Penjumlahan    = " + Hasil_Penjumlahan);
            Console.WriteLine("Hasil Pengurangan    = " + Hasil_Pengurangan);
            Console.WriteLine("Hasil Perkalian      = " + Hasil_Perkalian);
            Console.WriteLine("Hasil Pembagian      = " + Hasil_Pembagian);

        }
    }
}