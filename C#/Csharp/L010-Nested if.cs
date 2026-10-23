using System;

namespace Code_Practice{
    class L010_Nested_if{
        static void Main(string[] args){

            Console.Write("Username : ");
            string Username = Console.ReadLine();
            
            if (Username == "admin"){
                Console.Write("Password : ");
                string Password = Console.ReadLine();
                if (Password == "12345"){
                    Console.WriteLine("Selamat Datang Dev!");
                }
                else {
                    Console.WriteLine("[Info] Password Salah!");
                }
            }
            else {
                Console.WriteLine("[Info] Username Tidak ditemukan!");
            }

        }
    }
}