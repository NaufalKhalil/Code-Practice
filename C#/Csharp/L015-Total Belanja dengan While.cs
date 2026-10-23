using System;

namespace Code_Practice{
    class L015_Total_Belanja_dengan_While{
        static void Main(string[] args){
            int Total = 0;
            while(true){
                int Harga = 0;
                Console.Write("Masukkan harga barang (0 untuk selesai): ");
                Harga = int.Parse(Console.ReadLine());
                if (Harga == 0){
                    Console.WriteLine();
                    Console.WriteLine($"Total belanja : {Total}");
                    break;
                }
                Total += Harga;
            }

        }
    }
}
