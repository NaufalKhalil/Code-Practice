using System;

namespace Code_Practice{
    class L007_Validasi_Input_Nilai{
        static void Main(string[] args){

            Console.Write("Masukkan Nilai : ");
            double Nilai = double.Parse(Console.ReadLine());

            if (Nilai < 0 ){
                Console.WriteLine("[Error] Nilai tidak valid!");
            }
            else if (Nilai < 60){
                Console.WriteLine("Kurang");
            }
            else if (Nilai < 70){
                Console.WriteLine("Cukup");
            }
            else if (Nilai < 80){
                Console.WriteLine("Baik");
            }
            else if (Nilai <= 100){
                Console.WriteLine("Sangat Baik");
            } else {
                Console.WriteLine("[Error] Nilai tidak valid!");
            }


        }
    }
}