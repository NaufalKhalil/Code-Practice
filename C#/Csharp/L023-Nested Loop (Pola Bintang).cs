using System;

namespace Code_Practice{
    class L023_Nested_Loop_Pola_Bintang{
        static void Main(string[] args){

            for (int i = 1; i <= 5; i++)
            {
                for (int j = 1; j <= i; j++)
                {
                    Console.Write("* ");
                }
                Console.WriteLine();
            }

        }
    }
}
