using System;
using System.Numerics;

namespace Code_Practice{
    class L029_For_Loop_Menghitung_Total_Angka{
        static void Main(string[] args){

            Console.Clear();

            while (true)
            {
            
                Console.Write("Masukkan angka batas : ");
                string Input_Angka = Console.ReadLine()!;
                
                if (int.TryParse(Input_Angka, out int Angka))
                {
                    Console.WriteLine("=== HASIL PERHITUNGAN ===");
                    int Total = 0;
                    for (int i = 1; i <= Angka; i++)
                    {
                        Console.Write(i);
                        if (i != Angka)
                        {
                            Console.Write(" + ");
                        }
                        else
                        {
                            Console.Write(" = ");
                        }
                        Total += i;
                    }
                    Console.Write($"{Total}");
                    Console.WriteLine("[Info] Program Selesai");
                    break;
                }

                Console.WriteLine("[Error] Anda harus memasukkan sebuah angka");
            
            }

        }
    }
}
