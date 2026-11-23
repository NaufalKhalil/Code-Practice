using System;

class Program_17
{
    static void Main()
    {
        int Hitungan = 0;
        DuaMain(Hitungan);
        
    }
    static void TigaMain(int Hitungan)
    {
        Console.WriteLine("Halo");
        Hitungan ++;
        if (Hitungan <= 101){
            DuaMain(Hitungan);
        }
    }
    static void DuaMain(int Hitungan)
    {
        Console.WriteLine("Hello");
        Hitungan ++;
        TigaMain(Hitungan);
    }

}