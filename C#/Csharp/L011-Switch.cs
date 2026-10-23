using System;

namespace Code_Practice{
    class L011_Switch{
        static void Main(string[] args){

            Console.WriteLine("=== Menu ===");
            Console.WriteLine("1. Nasi Goreng");
            Console.WriteLine("2. Mie Goreng");
            Console.WriteLine("3. Ayam Geprek");
            Console.WriteLine("4. Soto");

            Console.WriteLine("------------");
            Console.Write("Pilih Menu : ");
            string Pilihan_user = Console.ReadLine();

            switch (Pilihan_user){
                case "1":
                    Console.WriteLine("Anda memilih Nasi Goreng");
                    break;
                case "2":
                    Console.WriteLine("Anda memilih Mie Goreng");
                    break;
                case "3":
                    Console.WriteLine("Anda memilih Ayam Geprek");
                    break;
                case "4":
                    Console.WriteLine("Anda memilih Soto");
                    break;
                default:
                    Console.WriteLine("[Error] Menu tidak tersedia!");
                    break;
            }

        }
    }
}