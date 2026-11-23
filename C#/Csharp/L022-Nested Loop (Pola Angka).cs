using System;

namespace Code_Practice{
    class L022_Nested_Loop_Pola_Angka{
        static void Main(string[] args){

            for (int i = 1; i <= 4; i++)
            {
                for (int j = 1; j <= i; j++)
                {
                    Console.Write($"{j} ");
                }
                Console.WriteLine();
            }

        }
    }
}
