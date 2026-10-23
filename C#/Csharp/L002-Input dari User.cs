using System;

namespace Code_Practice{
    class L002_Input_dari_User{
        static void Main(string[] args){

            Console.WriteLine("Masukkan Nama :");
            string nama = Console.ReadLine();
            Console.WriteLine("Masukkan Umur :");
            int umur = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine(nama);
            Console.WriteLine(umur);
        
        }    
    }
} 