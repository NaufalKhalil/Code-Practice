using System;

class Program_14
{
    static void Main(string[] args)
    {
        Console.WriteLine("\nNomor 1 :");
        // No 1 : menyimpan panjang string
        string Nama = "Bob";
        int Panjang_String = Nama.Length;
        Console.WriteLine(Panjang_String);

        Console.WriteLine("\nNomor 2 :");
        // No 2 : Menggabungkan string menggunakan operator +
        string Tulisan_1 = "Hello";
        string Tulisan_2 = "World";
        Console.WriteLine(Tulisan_1 + " " + Tulisan_2);
        // Bisa juga menggunakan method concat()
        Console.WriteLine(string.Concat(Tulisan_1, " ", Tulisan_2));

        Console.WriteLine("\nNomor 3 :");
        // No 3 : Mengakses karakter terpisah dalam string, dengan menggunaan indeks
        string Kata_Saya = "Hello";
        char Kata_Pertama = Kata_Saya[0];
        Console.WriteLine(Kata_Pertama);

        Console.WriteLine("\nNomor 4 :");
        // No 4 : Substring()
        string Word = "howareyou";
        string sub = Word.Substring(3, 6);
        Console.WriteLine(sub);

        Console.WriteLine("\nNomor 5 :");
        // No 5 : IndexOf()
        string Sentence_Kata = "how$are$you";
        int i = Sentence_Kata.IndexOf("$");
        string Kata_Dia = Sentence_Kata.Substring(0, i);  
        Console.WriteLine(Kata_Dia);

        Console.WriteLine("\nNomor 6 :");
        // No 6 : Method Contains()
        string Kata = "how$are$you";
        bool result_1 = Kata.Contains("$$"); //apakah ada karakter "$$" pada Kata
        bool result_2 = Kata.Contains("$"); //apakah ada karakter "$" pada Kata
        bool result_3 = Kata.Contains("are"); //apakah ada karakter "are" pada Kata
        Console.WriteLine(result_1); //hasilnya false
        Console.WriteLine(result_2); //hasilnya true
        Console.WriteLine(result_3); //hasilnya true

        Console.WriteLine("\nNomor 7 :");
        // No 7 : Mengubah huruf menjadi Kapital dan Non Kapital
        string Kata_Contoh_1 = "Hello World";
        string Kata_Upper = Kata_Contoh_1.ToUpper(); // ubah ke Kapital
        Console.WriteLine(Kata_Upper);

        string Kata_Contoh_2 = "hELLo wORlD";
        string kata_Lower = Kata_Contoh_2.ToLower(); // ubah ke non kapital
        Console.WriteLine(kata_Lower);

    }
}