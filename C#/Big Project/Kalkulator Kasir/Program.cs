using System;

namespace Kalkulator_Kasir{
    
    class C_Main{
        public static void Main(string[] args){
            C_Tampilan_menu.D_Menu_utama();
            (int Harga_barang_1, int Jumlah_barang_1) = C_Input_user.D_Barang_1();
            (int Harga_barang_2, int Jumlah_barang_2) = C_Input_user.D_Barang_2();
            for (int i = 1; i <= 27; i++){
                Console.Write("=");
            }
            Console.WriteLine();
            (int Total_harga_barang_1, int Total_harga_barang_2, int Total_harga_barang_kotor) = C_Hitung_total.D_Total_harga_barang_kotor( Harga_barang_1, Harga_barang_2, Jumlah_barang_1, Jumlah_barang_2);
            C_Tampilan_menu.D_Struk( Harga_barang_1, Harga_barang_2, Jumlah_barang_1, Jumlah_barang_2, Total_harga_barang_1, Total_harga_barang_2, Total_harga_barang_kotor);
            C_Hitung_total.D_Total_harga_barang_bersih(Total_harga_barang_kotor);

        } 
    }

    class C_Tampilan_menu{
        public static void D_Menu_utama(){
            Console.WriteLine("==== Kalkulator Kasir =====");
        }
        public static void D_Struk(int Harga_barang_1, int Harga_barang_2, int Jumlah_barang_1, int Jumlah_barang_2, int Total_harga_barang_1, int Total_harga_barang_2, int Total_harga_barang_kotor){
            Console.WriteLine($"Barang pertama  : (Harga = Rp{Harga_barang_1}) x (Jumlah = {Jumlah_barang_1}) = {Total_harga_barang_1}");
            Console.WriteLine($"Barang kedua    : (Harga = Rp{Harga_barang_2}) x (Jumlah = {Jumlah_barang_2}) = {Total_harga_barang_2}");
            for (int i = 1; i <= 27; i++){
                Console.Write("=");
            }
            Console.WriteLine();
            Console.WriteLine($"Total kotor = Rp{Total_harga_barang_kotor}");
        }
    } 

    class C_Input_user{
        public static (int, int) D_Barang_1(){
            Console.Write("Harga barang pertama : ");
            int Harga_barang = int.Parse(Console.ReadLine());
            Console.Write("Jumlah barang pertama : ");
            int Jumlah_barang = int.Parse(Console.ReadLine());
            return (Harga_barang, Jumlah_barang);
        }
        public static (int, int) D_Barang_2(){
            Console.Write("Harga barang kedua : ");
            int Harga_barang = int.Parse(Console.ReadLine());
            Console.Write("Jumlah barang kedua : ");
            int Jumlah_barang = int.Parse(Console.ReadLine());
            return (Harga_barang, Jumlah_barang);
        } 
    }

    class C_Hitung_total{
        public static (int, int, int) D_Total_harga_barang_kotor(int Harga_barang_1, int Harga_barang_2, int Jumlah_barang_1, int Jumlah_barang_2){
            int Total_harga_barang_1 = (Harga_barang_1 * Jumlah_barang_1);
            int Total_harga_barang_2 = (Harga_barang_2 * Jumlah_barang_2);
            int Total_harga_barang_kotor = (Total_harga_barang_1 + Total_harga_barang_2);
            return (Total_harga_barang_1, Total_harga_barang_2, Total_harga_barang_kotor);
        }
        public static void D_Total_harga_barang_bersih(int Total_harga_barang_kotor){
            // Diskon 10% jika total belanja di atas/sama dengan Rp100.000
            if (Total_harga_barang_kotor >= 100000){
                double Total_harga_barang_bersih = (Total_harga_barang_kotor * 0.9);
                Console.WriteLine("Selamat anda mencapai minimum belanja Rp100.000 untuk diskon 10% dari total belanja!");
                Console.WriteLine($"Total belanja anda = {Total_harga_barang_kotor} - diskon 10% = {Total_harga_barang_bersih}");
                for (int i = 1; i <= 27; i++){
                    Console.Write("=");
                }
                Console.WriteLine();
            } else {
                for (int i = 1; i <= 27; i++){
                    Console.Write("=");
                }
                Console.WriteLine();
            }
        }
    }

}