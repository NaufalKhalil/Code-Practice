using System;

namespace Code_Practice{
    class L011_Switch_dan_Operasi{
        static void Main(string[] args){

            Console.Write("Masukkan angka pertama : ");
            double Angka_pertama = double.Parse(Console.ReadLine());
            Console.Write("Masukkan operator (+ - * /) : ");
            string Operator = Console.ReadLine();
            Console.Write("Masukkan angka kedua : ");
            double Angka_kedua = double.Parse(Console.ReadLine());

            switch (Operator){
                case "+":
                    double Hasil = (Angka_pertama + Angka_kedua);
                    break;
                case "-":
                    double Hasil = (Angka_pertama - Angka_kedua);
                    break;
                case "*":
                    double Hasil = (Angka_pertama * Angka_kedua);
                    break;
                case "/":
                    double Hasil = (Angka_pertama / Angka_kedua);
                    break;
                default:
                    string Hasil = ("[Error] Operator tidak valid!");
                    break;
            }

        }
    }
}