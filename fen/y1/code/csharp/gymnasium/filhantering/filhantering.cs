// Program.cs
//
// Author: Samuel Berg
// Date: 10-Aug-2019

using System;
using System.IO;

namespace Filhantering_Fil_Summa
{
    class Program
    {
        static void Main(string[] args)
        {
            FileStream fs = new FileStream("talfil.tf", FileMode.OpenOrCreate, FileAccess.Read);
            BinaryReader br = new BinaryReader(fs);
            StreamWriter sw = new StreamWriter("talfil.txt");
            StreamWriter sw_sum = new StreamWriter("Summa.txt");

            int sum = 0;
            int fsum = 0;
            string row = "";

            for (int i = 0; i < fs.Length / 4; i++)
            {
                int num = br.ReadInt32();
                sum += num;
                sw.WriteLine(num);
                // Console.WriteLine(num);
            }

            sw.Close();

            StreamReader sr = new StreamReader("talfil.txt");

            for (int i = 0; i < fs.Length / 4; i++)
            {
                row = sr.ReadLine();
                if (row == "5")
                {
                    fsum += 1;
                }
            }

            sr.Close();

            sw_sum.WriteLine("The sum of all the numbers in the file: " + sum);
            sw_sum.WriteLine("The sum of all the singular fives in the file: " + fsum);

            Console.WriteLine("File length: " + fs.Length / 4);
            Console.WriteLine("The sum of all the numbers in the file: " + sum);
            Console.WriteLine("The sum of all the singular fives in the file: " + fsum);

            br.Close();
            sw_sum.Close();

            Console.ReadLine();
        }
    }
}
