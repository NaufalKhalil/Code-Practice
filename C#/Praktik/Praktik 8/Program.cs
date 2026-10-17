using System;

class Praktik_8 { 
    static void Main(string[] args) { 
        
        Console.Write("Masukkan 2 Digit NIM terakhir anda : "); 
        int NIM = int.Parse(Console.ReadLine()); 
        string hasil = ""; 

        for (int i = 0; i <= NIM; i++){
            if(i % 2 == 0){
                hasil = "Genap"; 
            } else { 
                hasil = "Ganjil"; 
            } 
        }

        Console.Write($"NIM {NIM} adalah {hasil}"); 
    } 
}
