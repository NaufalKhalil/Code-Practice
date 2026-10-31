using System;

namespace Code_Practice{
    class L019_Validasi_Input_Kasir{
        static void Main(string[] args){

            bool perulangan = true;
            int Total_belanja = 0;
            int Jumlah_barang = 0;

            while (perulangan == true)
            {
                Console.WriteLine();
                Console.WriteLine("=== MENU KASIR ===");
                Console.WriteLine("1. Tambah belanja");
                Console.WriteLine("2. Lihat total belanja");
                Console.WriteLine("3. Keluar");
                
                Console.Write("Pilih menu : ");
                string opsi = Console.ReadLine();
                if (!int.TryParse(opsi, out int pilihan_Opsi))
                {
                    Console.WriteLine("[Error ]");    
                }
                Console.WriteLine();

                switch (opsi)
                {
                    case 1:
                        while (true){
                            int Harga_barang = 0;    
                            Console.Write("Masukkan harga barang (0 untuk selesai) : ");
                            Harga_barang = int.Parse(Console.ReadLine());
                            if (Harga_barang < 0)
                            {
                                Console.WriteLine("[Error] Harga barang tidak valid!");
                            }
                            else if (Harga_barang == 0)
                            {
                                break;
                            }
                            else
                            {
                                Total_belanja += Harga_barang;
                                Jumlah_barang ++;
                            }
                        }
                        break;
                    case 2:
                        Console.WriteLine($"Total belanja : {Total_belanja}");
                        Console.WriteLine($"Jumlah barang : {Jumlah_barang}");
                        break;
                    case 3:
                        Console.WriteLine("[Info] Keluar dari program");
                        perulangan = false;
                        break;  
                    default:
                        Console.WriteLine("[Error] Opsi anda tidak valid!");
                        break;
                }
            }

        }
    }
}
