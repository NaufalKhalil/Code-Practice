using System;

namespace Code_Practice{
    class L015_While_Loop_dengan_kondisi{
        static void Main(string[] args){

            int Angka = 0;

            while (Angka < 1 || Angka > 5)
            {
                Console.Write("Masukan Angka [1 - 5] : ");
                Angka = int.Parse(Console.ReadLine());

                if (Angka < 1 || Angka > 5)
                {
                    Console.WriteLine("[Error] Angka tidak valid!");
                }
            }

            Console.WriteLine("Angka valid!");
            
        }
    }
}