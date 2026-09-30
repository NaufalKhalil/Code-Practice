using System;

class Praktik {
        static void Main(string[] args){
        
        string Room;
        int Harga = 0;

        Console.WriteLine("=== SELAMAT DATANG DI HOTEL BINTANG 5 ===");
        Console.WriteLine("1. VIP");
        Console.WriteLine("1. LUX");
        Console.WriteLine("1. STANDAR");
        Console.WriteLine("");
        Console.Write("=> Ketik Ruangan yang akan anda pesan : ");
        Room = Console.ReadLine();

        switch (Room){
                case "VIP":Harga = 30000; break;
                case "LUX": Harga = 5000; break;
                default : Harga = 1500; break; 
        }

        Console.WriteLine($"Harga ruangan yang harus anda bayarkan : ${Harga}");

    }    
}