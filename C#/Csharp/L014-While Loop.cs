using System;

namespace Code_Practice{
    class L014_While_Loop{
        static void Main(string[] args){

            while(true){
                Console.Write("Masukan Angka [1 - 5] : ");
                int Angka = int.Parse(Console.ReadLine());
                if (Angka >= 1 && Angka <= 5){
                    Console.WriteLine("Angka valid!");
                    break;
                }
                else{
                    Console.WriteLine("[Error] Angka tidak valid!");
                }
            }
            
        }
    }
}