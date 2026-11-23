using System;

namespace Code_Practice{
    class L021_Nested_Loop_Perulangan_Bersarang{
        static void Main(string[] args){

            Console.WriteLine("=== JADWAL RUANGAN ===");

            for (int i = 1; i <= 3; i++)
            {
                Console.WriteLine($"\nRuangan {i}");
                
                for (int j = 1; j <= 2; j++)
                {
                    Console.WriteLine($"- Jadwal {j}");
                }
            }

        }
    }
}