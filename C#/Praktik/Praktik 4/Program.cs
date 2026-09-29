using System;

class Latihan_4{
    static void Main(string[] args){

        Console.Write("Masukkan Password : ");
        int Password = int.Parse(Console.ReadLine());

        if(Password == 1234){
            Console.WriteLine("Password Anda Benar!");
        } 
        else{
            Console.WriteLine("Password Anda Salah!");
        }

    }
}
