using System;
using System.Linq.Expressions;
using System.Runtime.InteropServices;
using System.Runtime.Serialization.Formatters;

class Program_13
{
    static void Main(string[] args)
    { 
        string Mengulang = "Y";
     
        while(Mengulang == "Y" || Mengulang == "y"){
            Console.Clear();
            Console.WriteLine("=====================================================");
            Console.WriteLine("          SISTEM KASIR MINIMARKET SERBA ADA          ");
            Console.WriteLine("=====================================================");

            Console.Write("Masukkan jumlah jenis barang : ");
            int Jumlah_Jenis_Barang = int.Parse(Console.ReadLine()!);

            string[] Nama_Barang = new string[Jumlah_Jenis_Barang];
            int[] Harga_Barang = new int[Jumlah_Jenis_Barang];
            int[] Jumlah_Beli = new int[Jumlah_Jenis_Barang];
            int[] Sub_Total = new int[Jumlah_Jenis_Barang];

            int Total_Belanja = 0;

            for(int i = 0; i < Jumlah_Jenis_Barang; i++)
            {
                Console.WriteLine($"\n--- Data Barang ke-{i + 1} ---");
                Console.Write("Nama Barang  : ");
                Nama_Barang[i] = Console.ReadLine()!.Trim();

                Console.Write("Harga (Rp)   : ");
                Harga_Barang[i] = int.Parse(Console.ReadLine()!);

                Console.Write("Jumlah Beli  : ");
                Jumlah_Beli[i] = int.Parse(Console.ReadLine()!);

                Sub_Total[i] = Harga_Barang[i] * Jumlah_Beli[i];
                Total_Belanja += Sub_Total[i];
            }

            //Menghitung Diskon

            double Diskon = 0;
            if (Total_Belanja >= 100000) //diskon 10% untuk 100rb
            {
                Diskon = 0.10 * Total_Belanja;
            }
            double Total_Bayar = Total_Belanja - Diskon;

            //Cetak struk pembayaran

            Console.Clear();
            Console.WriteLine("=====================================================");
            Console.WriteLine("                  STRUK PEMBAYARAN                   ");
            Console.WriteLine("                 MINIMARKET SERBA ADA                ");
            Console.WriteLine("=====================================================");
            Console.WriteLine($"{"No", -4}{"Nama Barang", -18}{"Harga", -10}{"qtY", -5}{"Sub Total", -12}");
            Console.WriteLine("-----------------------------------------------------");

            for (int i = 0; i < Jumlah_Jenis_Barang; i++)
            {
                string Nama_Formatted = Nama_Barang[i].Length > 16 ? Nama_Barang[i].Substring(0, 13) + "..." : Nama_Barang[i];
                Console.WriteLine($"{i + 1, -4}{Nama_Formatted, -18}{Harga_Barang[i], -10:N0}{Jumlah_Beli[i], -5}{Sub_Total[i], -12:N0}");
            }

            Console.WriteLine("-----------------------------------------------------");
            Console.WriteLine($"Total Belanja   : Rp {Total_Belanja, 12:N0}");
            Console.WriteLine($"Diskon (10%)    : Rp {Diskon, 12:N0}");
            Console.WriteLine($"Total Bayar     : Rp {Total_Bayar, 12:N0}");
            Console.WriteLine("=====================================================");
            Console.WriteLine("     TERIMA KASIH TELAH BERBELANJA DI TEMPAT KAMI    ");
            Console.WriteLine("=====================================================");

            Console.Write("Mengulang penginputan data kembali? [Y/N] : ");
            Mengulang = Console.ReadLine()!;
        }

        Console.WriteLine("\nProgram Selesai");

    }
}