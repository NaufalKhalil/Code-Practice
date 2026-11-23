using System;

class Praktik_11 {
    static void Main(string[] args) {

        string[] Nama = new string[2];
        int[] Nilai = new int[2];

        Nama[0] = "Naufal Khalil";
        Nama[1] = "Lyu Rizalina";
        
        Nilai[0] = 100;
        Nilai[1] = 95;

        Console.WriteLine("======================");
        Console.WriteLine("  Nama   |   Nilai  ");
        Console.WriteLine("======================");
        Console.WriteLine($"{Nama[0]} = {Nilai[0]}");
        Console.WriteLine($"{Nama[1]} = {Nilai[1]}");
        Console.WriteLine("======================");
    }
}
