using System;

namespace Code_Practice{
    class L024_Nested_Loop_Pola_Bintang_Terbalik{
        static void Main(string[] args){

            while(true){
                Console.Write("Masukkan tinggi bintang : ");
                string tinggi_bintang = Console.ReadLine()!; 
                if (int.TryParse(tinggi_bintang, out int hasil_tinggi)){
                    for (int i = hasil_tinggi; i >= 1; i--)
                    {
                        Console.WriteLine();
                        for (int j = 1; j <= i; j++)
                        {
                            Console.Write("* ");
                        }
                    }
                    Console.WriteLine("\n[Info] Program selesai!");
                    break;
                }
                else
                {
                    Console.WriteLine("[Error] Masukkan sebuah angka!\n");
                    continue;
                }
            }

        }
    }
}
