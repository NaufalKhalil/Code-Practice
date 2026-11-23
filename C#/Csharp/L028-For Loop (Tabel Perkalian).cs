using System;

namespace Code_Practice{
    class L028_For_Loop_Tabel_Perkalian{
        static void Main(string[] args){
            
            Console.Clear();

            while (true)
            {
            
                Console.Write("Masukkan angka : ");
                string Input_Angka = Console.ReadLine()!;
                
                if (int.TryParse(Input_Angka, out int Angka))
                {
                    Console.WriteLine($"=== TABEL PERKALIAN {Angka} ===");
                    for (int i = 1; i <= 10; i++)
                    {
                        Console.WriteLine($"{Angka} x {i, -2} = {Angka * i}");
                    }
                    break;
                }

                Console.WriteLine("[Error] Anda harus memasukkan sebuah angka");
            
            }

        }
    }
}
