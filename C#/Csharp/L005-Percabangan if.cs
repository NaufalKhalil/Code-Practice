using System;

namespace Code_Practice{
    class L005_Percabangan_if{
        static void Main(string[] args){

            Console.Write("Masukkan Angka : ");
            double Angka = double.Parse(Console.ReadLine()); 

            if (Angka == 0 ){
                Console.WriteLine("Angka tersebut adalah nol.");
            }
            else if (Angka > 0 ){
                Console.WriteLine("Angka tersebut adalah positif.");
            }
            else {
                Console.WriteLine("Angka tersebut adalah negatif.");
            }

        }
    }
}