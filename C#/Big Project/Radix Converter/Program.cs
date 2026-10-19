using System;
using System.Linq;

namespace Radix_Converter{

    class C_Main{
        public static void Main(string[] args){

            string[] Opsi_pilihan = { "A", "B", "C", "D"};

            C_Tampilan_menu.Menu_utama();
            string Jenis_data_awal = C_Input_user.Input_angka_awal(Opsi_pilihan);



        }
    }

    class C_Tampilan_menu{
         
        public static void Menu_utama(){
            
            Console.WriteLine("===== RADIX CONVERTER =====");
            Console.WriteLine("[A] Biner (2)");
            Console.WriteLine("[B] Oktal (8)");
            Console.WriteLine("[C] Desimal (10)");
            Console.WriteLine("[D] Hexadesimal (16)");

        } 

    }

    class C_Input_user{

        public static string Input_angka_awal(string[] Opsi_pilihan){

            Console.Write("=> Jenis data apa yang akan anda input? :");
            string Jenis_data = Console.ReadLine();
            Jenis_data = Jenis_data.ToUpper();

            while(! Opsi_pilihan.Contains(Jenis_data)){
                Console.WriteLine("[Error] Silahkan memilih opsi yang valid");
                Console.Write("=> Jenis data apa yang akan anda input? :");
                Jenis_data = Console.ReadLine();
                Jenis_data = Jenis_data.ToUpper();
            }

            return Jenis_data;

        }

    }

}