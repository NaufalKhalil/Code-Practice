using System;

class Program_18
{
    static double Hitung_Sub_Total(double Harga, int Jumlah)
    {
        return Harga * Jumlah;
    }

    static double Hitung_Diskon(double Sub_Total, double Persen_Diskon)
    {
        return Sub_Total * Persen_Diskon / 100;
    }

    static double Hitung_Total(double Sub_Total, double Diskon)
    {
        return Sub_Total - Diskon;
    }

    static void Tampilkan_Hasil(double Harga, int Jumlah, double Sub_Total, double Diskon, double Total)
    {
        Console.WriteLine($"Harga satuan : Rp{Harga:N0}");
        Console.WriteLine($"Jumlah : {Jumlah}");
        Console.WriteLine($"Subtotal : Rp{Sub_Total:N0}");
        Console.WriteLine($"Diskon : Rp{Diskon:N0}");
        Console.WriteLine($"Total bayar : Rp{Total:N0}");
    }

    static void Main()
    {
        double Harga = 25000;
        int Jumlah = 4;
        double Persen_Diskon = 10;

        double Sub_Total = Hitung_Sub_Total(Harga, Jumlah);
        double Diskon = Hitung_Diskon(Sub_Total, Persen_Diskon);
        double Total = Hitung_Total(Sub_Total, Diskon);
        Tampilkan_Hasil(Harga,  Jumlah, Sub_Total, Diskon, Total);
    
    }
}