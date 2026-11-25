using System;
using System.Linq.Expressions;
using System.Runtime.CompilerServices;
class Praktik_21
{
    static string Input_String(string Input_Pesan)
    {
        string Input_Data;
        while(true){
            Console.Write($"{Input_Pesan, -28} : ");
            Input_Data = Console.ReadLine()!;

            while(true){
                Console.Write($"{Input_Pesan, 9} sudah benar? [Y/N] : ");
                string Accept_Input = Console.ReadLine()!.ToUpper();
                if (Accept_Input == "Y")
                {
                    Console.Clear();
                    return Input_Data;
                }
                else if(Accept_Input == "N")
                {
                    Console.Clear();
                    break;
                }
                else
                {
                    Console.WriteLine("[Error] Cukup ketik 'Y' / 'N' !");
                }
            }
        }
    }
    static double Input_Double(string Input_Pesan)
    {
        string Input_Data;
        while(true){
            
            double Hasil_Data;

            while (true){
                Console.Write($"{Input_Pesan, -28} : ");
                Input_Data = Console.ReadLine()!;
                if (double.TryParse(Input_Data, out Hasil_Data))
                {
                    break;
                }
                Console.WriteLine("[Error] Anda harus memasukkan angka yang valid!");
            }

            while(true){
                Console.Write($"{Input_Pesan, 9} sudah benar? [Y/N] : ");
                string Accept_Input = Console.ReadLine()!.ToUpper();
                if (Accept_Input == "Y")
                {
                    Console.Clear();
                    return Hasil_Data;
                }
                else if(Accept_Input == "N")
                {
                    Console.Clear();
                    break;
                }
                else
                {
                    Console.WriteLine("[Error] Cukup ketik 'Y' / 'N'!");
                }
            }
        }
    }

    static double Hitung_Gaji_Bersih(double gajiPokok1, double tunjangan1, double potongan1)
    {
        double gajiBersih = gajiPokok1 + tunjangan1 - potongan1;
        return gajiBersih;
    }
    
    static void Tampilkan(string NIK, string Nama, string Jabatan, double Gaji_Pokok, double Tunjangan, double Potongan_Gaji, double Gaji_Bersih)
    {
        Console.Clear();
        Console.WriteLine("======================================");
        Console.WriteLine("         PT.SHOE THAR DHOCK");
        Console.WriteLine("         SLIP GAJI KARYAWAN");
        Console.WriteLine("======================================");
        Console.WriteLine($"NIK         : {NIK}");
        Console.WriteLine($"Nama        : {Nama}");
        Console.WriteLine($"Jabatan     : {Jabatan}");
        Console.WriteLine($"Gaji Pokok  : Rp{Gaji_Pokok:N0}");
        Console.WriteLine($"tunjangan   : Rp{Tunjangan:N0}");
        Console.WriteLine($"Potongan    : Rp{Potongan_Gaji:N0}");
        Console.WriteLine($"Gaji Bersih : Rp{Gaji_Bersih:N0}");
        Console.WriteLine("======================================");
    }

    static void Main() 
    {
     
        string Input_NIK = Input_String("NIK");
        string Input_Nama = Input_String("Nama");
        string Input_Jabatan = Input_String("Jabatan");

        double Input_Gaji_Pokok = Input_Double("Gaji Pokok");
        double Input_Tunjangan = Input_Double("Tunjangan");
        double Input_Potongan_Gaji = Input_Double("Potongan Gaji");

        double Hasil_Gaji_Bersih = Hitung_Gaji_Bersih(Input_Gaji_Pokok, Input_Tunjangan, Input_Potongan_Gaji);

        Tampilkan(Input_NIK, Input_Nama, Input_Jabatan, Input_Gaji_Pokok, Input_Tunjangan, Input_Potongan_Gaji, Hasil_Gaji_Bersih);

    }
}