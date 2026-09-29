using System;

class Program{
    static void Main(string[] args){
        
        int Panjang, Lebar, Hasil_Luas, Hasil_Keliling;
        Console.Write("Nilai Panjang : "); 
        Panjang = int.Parse(Console.ReadLine());
        Console.Write("Nilai Lebar : ");
        Lebar = int.Parse(Console.ReadLine());
        Hasil_Luas = 2 * (Panjang + Lebar);
        Hasil_Keliling = (Panjang * Lebar);
        Console.Writeln($"Luas Persegi Panjang     : {Hasil_Luas}");
        Console.Writeln($"Keliling Persegi Panjang : {Hasil_Keliling}");
    }
}