using System;
class Program
{
    static double HitungNilaiAkhir(double tugas, double uts, double uas)
    {
        return (tugas * 0.30) + (uts * 0.30) + (uas * 0.40);
    }

    static string TentukanPredikat(double nilai)
    {
        if (nilai >= 85) return "A";
        else if (nilai >= 75) return "B";
        else if (nilai >= 60) return "C";
        else return "D";
    }

    static string TentukanStatus(double nilai)
        {
        return nilai >= 60 ? "LULUS" : "TIDAK LULUS";
        }

    static void TampilkanHasil(string nama, double nilai)
        {
            Console.WriteLine("\n=== HASIL PENILAIAN ===");
            Console.WriteLine($"Nama : {nama}");
            Console.WriteLine($"Nilai akhir: {nilai:F2}");
            Console.WriteLine($"Predikat : {TentukanPredikat(nilai)}");
            Console.WriteLine($"Status : {TentukanStatus(nilai)}");
        }
    static void Main()
    {
        Console.Write("Nama mahasiswa: ");
        string nama = Console.ReadLine() ?? "";
        Console.Write("Nilai tugas: ");
        double tugas = Convert.ToDouble(Console.ReadLine());
        Console.Write("Nilai UTS: ");
        double uts = Convert.ToDouble(Console.ReadLine());
        Console.Write("Nilai UAS: ");
        double uas = Convert.ToDouble(Console.ReadLine());
        double nilaiAkhir = HitungNilaiAkhir(tugas, uts, uas);
        TampilkanHasil(nama, nilaiAkhir);
    }
}