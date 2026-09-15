using System;

namespace Code_Practice{
    class L008_Operator_Logika_AND{
        static void Main(string[] args){

            Console.Write("Masukkan umur anda : ");
            int Umur = int.Parse(Console.ReadLine());

            if (Umur >= 0 && Umur <= 12){
                Console.WriteLine("Anak - Anak");
            }
            else if (Umur >= 13 && Umur <= 17){
                Console.WriteLine("Remaja");
            }
            else if (Umur >= 18 && Umur <= 59){
                Console.WriteLine("Dewasa");
            }
            else if (Umur >= 60 ){
                Console.WriteLine("Lansia");
            }
            else {
                Console.WriteLine("[Error] Usia anda tidak valid!");
            }

        }
    }
}