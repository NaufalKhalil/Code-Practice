using System;

namespace Code_Practice{
    class L016_While_dengan_Counter{
        static void Main(string[] args){

            int Angka = 0;
            int Percobaan = 0;

            while(Angka < 1 || Angka > 5){
                Percobaan += 1;
                Console.Write("Masukkan angka [1 - 5] : ");
                Angka = int.Parse(Console.ReadLine());
                
                if (Angka < 1 || Angka > 5){
                    Console.WriteLine("[Error] Anda harus memasukkan angka [1 - 5]!");
                }
            }

            Console.WriteLine("Angka valid!");
            Console.WriteLine($"Jumlah Percobaan : {Percobaan}");

        }
    }
}