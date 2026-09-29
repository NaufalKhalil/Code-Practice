using System;

class Tugas_4
{
    static void Main(string[] args)
    {
        double PokokSWDKLLJ = 0;
        string Jenis_kendaraan = "";
        string Opsi_kendaraan = "";
        int Bulan_keterlambatan = 0;
        double PokokPKB = 0;
        double DendaPKB = 0;
        double DendaSWDKLLJ = 0;
        double TotalPembayaran = 0;
        string Garis = "-------------------------------------";

        Console.WriteLine("====== PROGRAM PAJAK KENDARAAN ======");
        Console.WriteLine("[1] Kendaraan Roda 2");
        Console.WriteLine("[2] Kendaraan Roda 4");
        Console.WriteLine(Garis);
        Console.Write("=> Pilih jenis kendaraan anda : ");
        Opsi_kendaraan = Console.ReadLine();

        if (Opsi_kendaraan == "1"){
            Jenis_kendaraan = "Roda 2";
            PokokSWDKLLJ = 35000;
        }
        else if (Opsi_kendaraan == "2"){
            Jenis_kendaraan = "Roda 4";
            PokokSWDKLLJ = 143000;
        }

        if (Opsi_kendaraan == "1" || Opsi_kendaraan == "2"){
            Console.Write("=> Masukkan Pokok PKB (Rp) : ");
            PokokPKB = double.Parse(Console.ReadLine());
            
            Console.Write("=> Masukkan Jumlah Bulan Keterlambatan (0-24) : ");
            Bulan_keterlambatan = int.Parse(Console.ReadLine());

            if (Bulan_keterlambatan < 0 || Bulan_keterlambatan > 24){
                Console.WriteLine(Garis);
                Console.WriteLine("[Error] Bulan keterlambatan harus di antara 0 hingga 24 bulan!");
            }
            else {
                
                if (Bulan_keterlambatan == 0){
                    DendaPKB = 0;
                    DendaSWDKLLJ = 0;
                }
                else if (Bulan_keterlambatan >= 1 && Bulan_keterlambatan <= 3){
                    DendaPKB = 0.10 * PokokPKB; 
                    if (Opsi_kendaraan == "1"){
                        DendaSWDKLLJ = 25000;
                    }
                    else {
                        DendaSWDKLLJ = 50000;
                    }
                }
                else if (Bulan_keterlambatan > 3){
                    int bulanKelebihan = Bulan_keterlambatan - 3;
                    DendaPKB = (0.25 * PokokPKB) + (0.01 * bulanKelebihan * PokokPKB);

                    if (Opsi_kendaraan == "1"){
                        DendaSWDKLLJ = 50000;
                    }
                    else {
                        DendaSWDKLLJ = 100000;
                    }
                }

                TotalPembayaran = PokokPKB + PokokSWDKLLJ + DendaPKB + DendaSWDKLLJ;

                Console.WriteLine(Garis);
                Console.WriteLine("         STRUK HASIL HITUNG PAJAK    ");
                Console.WriteLine(Garis);
                Console.WriteLine($"Jenis Kendaraan     : {Jenis_kendaraan}");
                Console.WriteLine($"Keterlambatan       : {Bulan_keterlambatan} Bulan");
                Console.WriteLine($"Pokok PKB           : Rp {PokokPKB}");
                Console.WriteLine($"Pokok SWDKLLJ       : Rp {PokokSWDKLLJ}");
                Console.WriteLine($"Denda PKB           : Rp {DendaPKB}");
                Console.WriteLine($"Denda SWDKLLJ       : Rp {DendaSWDKLLJ}");
                Console.WriteLine(Garis);
                Console.WriteLine($"TOTAL PEMBAYARAN    : Rp {TotalPembayaran}");
                Console.WriteLine(Garis);
                Console.WriteLine("Nama Operator        : Naufal Khalil Rakhasyah");
                Console.WriteLine(Garis);
                
            }
        }
        else {
            Console.WriteLine("[Error] Anda harus memasukkan input yang valid!");
        }
    }
}
