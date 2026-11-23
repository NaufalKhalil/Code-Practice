using System;

namespace Code_Practice{
    class L027_Nested_Loop_Diamond_Belah_Ketupat{
        static void Main(string[] args){

            Console.Clear();

            while (true)
            {
                Console.Write("> Masukkan Diameter Piramida berlian : ");
                string Diameter_Piramida = Console.ReadLine()!;

                if (int.TryParse(Diameter_Piramida, out int Diameter))
                {
                    Console.WriteLine();
                    for (int i = 1; i <= Diameter; i++)
                    {
                        for (int k = Diameter; k >= i; k--)
                        {
                            Console.Write("  ");
                        }
                        for (int j = 1; j <= (2 * i) - 1 ; j++)
                        {
                            Console.Write("* ");
                        }
                        Console.WriteLine();
                    }
                    for (int i = (Diameter - 1); i >= 1; i--)
                    {
                        for (int k = Diameter; k >= i; k--)
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
