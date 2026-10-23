using System;

namespace Code_Practice{
    class L009_Operator_Logika_OR{
        static void Main(string[] args){

            Console.Write("Masukkan Hari : ");
            string Hari = Console.ReadLine();
            
            if (Hari == "Sabtu" || Hari == "Minggu"){
                Console.WriteLine("Hari libur");
            }
            else if (Hari == "Senin" || Hari == "Selasa" || Hari == "Rabu" || Hari == "Kamis" || Hari == "Jumat"){
                Console.WriteLine("Hari Kerja");
            }
            else {
                Console.WriteLine("[Error] Anda memasukkan hari yang tidak valid!");
            }

        }
    }
}