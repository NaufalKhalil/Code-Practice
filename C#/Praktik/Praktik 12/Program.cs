using System;

class Praktik_12 {
    static void Main(string[] args) {

        string[] Nama = new string[2];
        int[] Nilai = new int[2];

        for (int i = 0; i <= 1; i++)
        {
            Console.Write("Masukkan Nama : ");
            Nama[i] = Console.ReadLine();

            Console.Write("Masukkan Nilai :");
            Nilai[i] = int.Parse(Console.ReadLine());
            
            Console.WriteLine();
        }

        Console.WriteLine("======================");
        Console.WriteLine("  Nama   |   Nilai  ");
        Console.WriteLine("======================");
        
        for (int i = 0; i <= 1; i++)
        {
            Console.WriteLine($"{Nama[i]} {Nilai[i]}");
        }
        
        Console.WriteLine("======================");
    }
}
