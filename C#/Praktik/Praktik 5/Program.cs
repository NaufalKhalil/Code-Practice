using System;

class Praktik_5{
    static void Main(string[] args){
        
        Console.Write("Masukkan Nilai anda :");
        int Nilai = int.Parse(Console.ReadLine());
        string Predikat;

        if (Nilai >= 90){
            Predikat = "A";
        } 
        else if(Nilai >= 85){
            Predikat = "A-";
        }
        else if(Nilai >= 80){
            Predikat = "B+";
        }
        else if(Nilai >= 75){
            Predikat = "B";
        }
        else {
            Predikat = "B-";
        }

    }
}