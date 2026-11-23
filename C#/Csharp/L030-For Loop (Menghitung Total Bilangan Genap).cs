using System;

namespace Code_Practice
{
    class L030_For_Loop_Menghitung_Total_Bilangan_Genap
    {
        static void Main(string[] args)
        {
            Console.Clear();

            while (true)
            {
                Console.Write("Masukkan angka batas : ");
                string Input_Angka = Console.ReadLine()!;

                if (int.TryParse(Input_Angka, out int Angka))
                {
                    Console.WriteLine("=== HASIL PERHITUNGAN ===");
                    int Total = 0;

                    for (int i = 2; i <= Angka - 1; i += 2)
                    {
                        Total += i;
                        Console.Write(i);

                        if (i + 2 <= Angka - 1)
                        {
                            Console.Write(" + ");
                        }
                    }

                    if (Total > 0)
                    {
                        Console.Write(" = ");
                    }

                    Console.WriteLine(Total);
                    Console.WriteLine("[Info] Program Selesai");
                    break;
                }

                Console.WriteLine("[Error] Anda harus memasukkan sebuah angka");
            }
        }
    }
}
