using System;

class Praktik_9{
    static void Main(string[] args){

        string passwordKunci = "csharp123";
        string inputUser = "";
        Console.WriteLine("=== Sistem Login Sederhana ===");
        
        while (inputUser != passwordKunci){

            Console.Write("Masukkan Password: ");
            inputUser = Console.ReadLine();
      
            if (inputUser != passwordKunci){
                Console.WriteLine("Password salah! Silakan coba lagi.\n");
            }
        }
      
        Console.WriteLine("✅ Akses Diterima! Selamat datang.");
    
    }     
}