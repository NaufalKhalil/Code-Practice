using System;

namespace Code_Practice{
    class L0{
        static void Main(string[] args){

           Console.Write("Apakah Anda member? (true/false): ");
            string input = Console.ReadLine();

            // Mencoba mengubah string menjadi bool
            if (bool.TryParse(input, out bool statusMember))ss
            {
                Console.WriteLine($"Berhasil! Status member Anda adalah: {statusMember}");
            }
            else
            {
                Console.WriteLine("Input tidak valid! Harap ketik 'true' atau 'false'.");
                
            }
        }
    }
}