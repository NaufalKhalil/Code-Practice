using System;

namespace Code_Practice{
    class L026_Nested_Loop_Piramida_Terbalik{
        static void Main(string[] args){

            Console.Clear();

            while (true)
            {
                Console.Write("> Masukkan tinggi piramida berlian : ");
                string tinggi_piramida = Console.ReadLine()!;

                if (int.TryParse(tinggi_piramida, out int tinggi))
                {
                    Console.WriteLine();
                    for (int i = tinggi; i >= 1; i--)
                    {
                        for (int k = tinggi; k >= i; k--)
                        {
                            Console.Write("  ");
                        }
                        for (int j = 1; j <= (2 * i) - 1 ; j++)
                        {
                            Console.Write("* ");
                        }
                        Console.WriteLine();
                    }
                    Console.WriteLine("\n[Info] Program selesai!");
                    break;
                }
                
                Console.WriteLine("[Error] Anda harus masukkan sebuah angka!");
                
            }

        }
    }
}
