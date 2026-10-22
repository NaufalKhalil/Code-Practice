using System;
using System.Linq;

namespace Radix_Converter {

    class C_Main {
        public static void Main(string[] args) {

            string[] Opsi_pilihan = { "A", "B", "C", "D" };
            
            int[] Filter_angka_biner = { 0, 1 };
            int[] Filter_angka_oktal = { 0, 1, 2, 3, 4, 5, 6, 7 };
            int[] Filter_angka_desimal = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            object[] Filter_angka_hexadesimal = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F" };

            C_Tampilan_menu.Menu_utama();
            
            string Jenis_data_awal = C_Opsi_user.Data_awal(Opsi_pilihan);
            Jenis_data_awal = C_Opsi_user.Convert_opsi(Jenis_data_awal);
            
            string Jenis_data_akhir = C_Opsi_user.Data_akhir(Opsi_pilihan);
            Jenis_data_akhir = C_Opsi_user.Convert_opsi(Jenis_data_akhir);

            string Angka_input = C_Input_user.Ambil_data(Jenis_data_awal, Jenis_data_akhir);

        }
    }

    class C_Tampilan_menu {
        public static void Menu_utama() {
            Console.WriteLine("===== RADIX CONVERTER =====");
            Console.WriteLine("[A] Biner (2)");
            Console.WriteLine("[B] Oktal (8)");
            Console.WriteLine("[C] Desimal (10)");
            Console.WriteLine("[D] Hexadesimal (16)\n");
        } 
    }

    class C_Opsi_user {
        public static string Data_awal(string[] Opsi_pilihan) {
            Console.Write("=> Jenis data apa yang akan anda input? : ");
            string Jenis_data = Console.ReadLine();
            Jenis_data = Jenis_data.ToUpper();

            while (!Opsi_pilihan.Contains(Jenis_data)) {
                Console.WriteLine("[Error] Silahkan memilih opsi yang valid");
                Console.Write("=> Jenis data apa yang akan anda input? : ");
                Jenis_data = Console.ReadLine();
                Jenis_data = Jenis_data.ToUpper();
            }
            return Jenis_data;
        }

        public static string Data_akhir(string[] Opsi_pilihan) {
            Console.Write("=> Akan diubah ke jenis data apa? : ");
            string Jenis_data = Console.ReadLine();
            Jenis_data = Jenis_data.ToUpper();

            while (!Opsi_pilihan.Contains(Jenis_data)) {
                Console.WriteLine("[Error] Silahkan memilih opsi yang valid");
                Console.Write("=> Akan diubah ke jenis data apa? : ");
                Jenis_data = Console.ReadLine();
                Jenis_data = Jenis_data.ToUpper();
            }
            return Jenis_data;
        }

        public static string Convert_opsi(string Jenis_data) {
            string Jenis_angka = "";
            
            switch (Jenis_data) {
                case "A": Jenis_angka = "Biner"; break;
                case "B": Jenis_angka = "Oktal"; break;
                case "C": Jenis_angka = "Desimal"; break;
                case "D": Jenis_angka = "Hexadesimal"; break;
                default: Jenis_angka = "Desimal"; break;
            }
            return Jenis_angka;
        }
    }

    class C_Input_user {

        public static string Ambil_data(string Jenis_data_awal, string Jenis_data_akhir) {
            
            Console.Write($"=> Masukkan angka {Jenis_data_awal} yang akan diubah menjadi angka {Jenis_data_akhir} : ");           
            string Input_mentah = Console.ReadLine();

            switch (Jenis_data_awal) {
                case "Biner":
                    if (Input_mentah )
                case "Oktal":
                    break;
                case "Desimal":
                    break;
                case "Hexadesimal":
                    Input_mentah = Input_mentah.ToUpper(); 
                    break;
            }

            return Input_mentah;
        }
    }
}
