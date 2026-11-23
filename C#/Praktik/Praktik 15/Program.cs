using System;

class Program_15
{
    static void Main()
    {
        int[,] A = { { 1, 2, 3 }, { 4, 5, 6 } };
        int[,] B = { { 7, 8, 9 }, { 10, 11, 12 } };
        int[,] C = new int[2, 3];
        string[] Baris_tambah = { " + ", "   " };
        string[] Baris_sama_dengan = { " = ", "   " };

        for (int i = 0; i < A.GetLength(0); i++)
        {
            string barisA = "";
            string barisB = "";
            string barisC = "";

            for (int j = 0; j < A.GetLength(1); j++)
            {
                C[i, j] = A[i, j] + B[i, j];
                barisA += $"{A[i, j],3}";
                barisB += $"{B[i, j],3}";
                barisC += $"{C[i, j],3}";
            } 

            Console.WriteLine($"{barisA} {Baris_tambah[i]} {barisB} {Baris_sama_dengan[i]} {barisC}");
        }

    }
}
