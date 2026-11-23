using System;
using System.Numerics;

namespace Code_Practice{
    class L016_Validasi_Harga_Barang{
        static void Main(string[] args){

            int Total_belanja = 0;

            while (true){
                int Harga_barang = 0;    
                Console.Write("Masukkan harga barang (0 untuk selesai) : ");
                Harga_barang = int.Parse(Console.ReadLine());
                if (Harga_barang < 0)
                {
                    Console.WriteLine("[Error] Harga barang tidak valid!");
                }
                else if (Harga_barang == 0)
                {
                    Console.WriteLine();
                    Console.WriteLine($"Total belanja : {Total_belanja}");
                    break;
                }
                else
                {
                    Total_belanja += Harga_barang;
                }
            }

        }
    }
}
