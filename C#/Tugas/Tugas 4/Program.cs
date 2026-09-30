using System;

class Tugas_4 {
    static void Main(string[] args) {


        string Jenis_kendaraan = "";
        string Opsi_kendaraan = "";
        int Bulan_keterlambatan = 0;
        double Pokok_swdkllj = 0;
        double Pokok_pkb = 0;
        double Denda_pkb = 0;
        double Denda_swdkllj = 0;
        double Total_pembayaran = 0;
        string Garis = "-------------------------------------";

        Console.WriteLine("====== PROGRAM PAJAK KENDARAAN ======");
        Console.WriteLine("[1] Kendaraan Roda 2");
        Console.WriteLine("[2] Kendaraan Roda 4");
        Console.WriteLine(Garis);
        Console.Write("=> Pilih jenis kendaraan anda : ");
        Opsi_kendaraan = Console.ReadLine();

        if (Opsi_kendaraan == "1"){
            Jenis_kendaraan = "Roda 2";
            Pokok_swdkllj = 35000;
        }
        else if (Opsi_kendaraan == "2"){
            Jenis_kendaraan = "Roda 4";
            Pokok_swdkllj = 143000;
        }

        if (Opsi_kendaraan == "1" || Opsi_kendaraan == "2"){
            Console.Write("=> Masukkan Pokok PKB (Rp) : ");
            Pokok_pkb = double.Parse(Console.ReadLine());

            Console.Write("=> Masukkan Jumlah Bulan Keterlambatan (0-24) : ");
            Bulan_keterlambatan = int.Parse(Console.ReadLine());

            if (Bulan_keterlambatan < 0 || Bulan_keterlambatan > 24){
                Console.WriteLine(Garis);
                Console.WriteLine("[Error] Bulan keterlambatan harus di antara 0 hingga 24 bulan!");
            }
            else{
                if (Bulan_keterlambatan == 0){
                    Denda_pkb = 0;
                    Denda_swdkllj = 0;
                }
                else if (Bulan_keterlambatan >= 1 && Bulan_keterlambatan <= 3){
                    Denda_pkb = 0.10 * Pokok_pkb;
                    if (Opsi_kendaraan == "1"){
                        Denda_swdkllj = 25000;
                    }
                    else{
                        Denda_swdkllj = 50000;
                    }
                }
                else if (Bulan_keterlambatan > 3){
                    Denda_pkb = (0.25 * Pokok_pkb) + (0.01 * Bulan_keterlambatan * Pokok_pkb);
                    if (Opsi_kendaraan == "1"){
                        Denda_swdkllj = 50000;
                    }
                    else{
                        Denda_swdkllj = 100000;
                    }
                }

                Total_pembayaran = Pokok_pkb + Pokok_swdkllj + Denda_pkb + Denda_swdkllj;

                Console.WriteLine(Garis);
                Console.WriteLine("          STRUK HASIL HITUNG PAJAK   ");
                Console.WriteLine(Garis);
                Console.WriteLine("Jenis Kendaraan  : " + Jenis_kendaraan);
                Console.WriteLine("Keterlambatan    : " + Bulan_keterlambatan + " Bulan");
                Console.WriteLine("Pokok PKB        : Rp" + Pokok_pkb); 
                Console.WriteLine("Pokok SWDKLLJ    : Rp" + Pokok_swdkllj);
                Console.WriteLine("Denda PKB        : Rp" + Denda_pkb);
                Console.WriteLine("Denda SWDKLLJ    : Rp" + Denda_swdkllj);
                Console.WriteLine(Garis);
                Console.WriteLine("TOTAL PEMBAYARAN : Rp" + Total_pembayaran);
                Console.WriteLine(Garis);
                Console.WriteLine("Nama Operator    : Naufal Khalil Rakhasyah");
                Console.WriteLine(Garis);
            }
        }
        else {
            Console.WriteLine("[Error] Anda harus memasukkan input yang valid!");
        }
    }
}

