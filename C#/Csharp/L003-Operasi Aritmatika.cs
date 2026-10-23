using System;

namespace Code_Practice{
    class L003_Operasi_Aritmatika{
        static void Main(string[] args){

            Console.Write("Masukkan angka pertama :");
            int Angka_Pertama = Convert.ToInt32(Console.ReadLine());
            Console.Write("Masukkan angka kedua :");
            int Angka_Kedua = Convert.ToInt32(Console.ReadLine());

            int Hasil_Penjumlahan = Angka_Pertama + Angka_Kedua;
            int Hasil_Pengurangan = Angka_Pertama - Angka_Kedua;
            int Hasil_Perkalian = Angka_Pertama * Angka_Kedua;
            int Hasil_Pembagian = Angka_Pertama / Angka_Kedua;

            Console.WriteLine("Hasil Penjumlahan    : " + Hasil_Penjumlahan);
            Console.WriteLine("Hasil Pengurangan    : " + Hasil_Pengurangan);
            Console.WriteLine("Hasil Perkalian      : " + Hasil_Perkalian);
            Console.WriteLine("Hasil Pembagian      : " + Hasil_Pembagian);

        }
    }
}