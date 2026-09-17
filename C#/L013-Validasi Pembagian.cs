using System;

namespace Code_practice{
    class L013_Validasi_Pembagian{
        static void Main(string[] args){

            Console.Write("Masukkan angka pertama : ");
            double Angka_pertama = double.Parse(Console.ReadLine());
            Console.Write("Masukkan operator (+ - * /) : ");
            string Operator = Console.ReadLine();
            Console.Write("Masukkan angka kedua : ");
            double Angka_kedua = double.Parse(Console.ReadLine());

            double Hasil = 0;
            string Error = "";

            switch (Operator){
                case "+": Hasil = Angka_pertama + Angka_kedua; break;
                case "-": Hasil = Angka_pertama - Angka_kedua; break;
                case "*": Hasil = Angka_pertama * Angka_kedua; break;
                case "/": Hasil = Angka_pertama / Angka_kedua; break;
                default : Error = "[Error] Operator/Angka yang anda masukkan tidak valid!"; break;
            }

            if (Operator == "/" && Angka_kedua == 0 ){
                Console.WriteLine("[Error] Tidak dapat membagi dengan nol!");
            }
            else{
                if (Error == "[Error] Operator/Angka yang anda masukkan tidak valid!"){
                    Console.WriteLine(Error);
                } else{
                    Console.WriteLine(Hasil);
                }
            }

        }
    }
}