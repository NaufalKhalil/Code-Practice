using System;

namespace Code_Practice{
    class L020_Validasi_Input_dengan_TryParse{
        static void Main(string[] args){

            Console.Clear();

            bool perulangan = true;
            int Total_belanja = 0;
            int Jumlah_barang = 0;

            while (perulangan == true)
            {
                Console.WriteLine();
                Console.WriteLine("=== MENU KASIR ===");
                Console.WriteLine("1. Tambah belanja");
                Console.WriteLine("2. Keluar");
                
                Console.Write("Pilih menu : ");
                string opsi = Console.ReadLine()!;
            
                if (!int.TryParse(opsi, out int pilihan_Opsi))
                {
                    Console.WriteLine("[Error] input anda tidak valid (harus berupa angka)!");    
                    continue; 
                }
                Console.WriteLine();

                switch (pilihan_Opsi)
                {
                    case 1:
                        Console.Clear();
                        while (true){        
                            Console.Write("Masukkan harga barang (0 untuk selesai) : ");
                            string Harga_barang = Console.ReadLine()!;
                            
                            if (!int.TryParse(Harga_barang, out int Harga_barang_))
                            {
                                Console.WriteLine("[Error] Harga barang tidak valid!"); 
                                continue; 
                            }
                            else if (Harga_barang_ == 0)
                            {
                                perulangan = false; 
                                break;
                            }
                            else if (Harga_barang_ > 0)
                            {
                                Total_belanja += Harga_barang_;
                                Jumlah_barang ++;
                            }
                            else
                            {
                                Console.WriteLine("[Error] Harga barang tidak valid!"); 
                                continue;
                            }
                        }

                        if (perulangan == false)
                        {
                            Console.Clear();
                            Console.WriteLine("=====================================");
                            Console.WriteLine("          TOTAL BELANJA ANDA         ");
                            Console.WriteLine("=====================================");
                            Console.WriteLine($"- Total belanja : Rp{Total_belanja:N0}");
                            Console.WriteLine($"- Jumlah barang : {Jumlah_barang}");
                            Console.WriteLine("=====================================");
                        }
                        break;
                    case 2:
                        Console.Clear();
                        Console.WriteLine("[Info] Keluar dari program");
                        perulangan = false;
                        break;
                    default:
                        Console.Clear();
                        Console.WriteLine("[Error] Opsi anda tidak ada di menu!");
                        break;
                }
            }

        }
    }
}
