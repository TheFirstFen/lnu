using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
using System.Threading;

namespace InfogandeSortering
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] a = new int[10];  //Arrays for Bubblesort
            int[] b = new int[1000];
            int[] c = new int[100000];

            int[] d = new int[10];  //Arrays for Insertionsort
            int[] e = new int[1000];
            int[] f = new int[100000];

            int[] g = new int[10];  //Arrays for Mergsort
            int[] h = new int[1000];
            int[] j = new int[100000];

            int[] k = new int[10];  //Arrays for Quicksort
            int[] l = new int[1000];
            int[] m = new int[100000];

            Random tal = new Random();  //Number generator

            Stopwatch sw = new Stopwatch();  //Stopwatch

            double frequency = Stopwatch.Frequency; //Making it possible to see amount of nanoseconds it takes
            double nanosecPerTick = (1000 * 1000 * 1000) / frequency;

            double Atime = -1;   //Save location of times
            double Btime = -1;
            double Ctime = -1;
            double Dtime = -1;
            double Etime = -1;
            double Ftime = -1;
            double Gtime = -1;
            double Htime = -1;
            double Jtime = -1;
            double Ktime = -1;
            double Ltime = -1;
            double Mtime = -1;

            double Fastest10;
            double Fastest1000;
            double Fastest100000;

            for (int i = 0; i < 10; i++)    //Adding numbers to the arrays of 10
            {
                a[i] = tal.Next(0, 1000000);
                d[i] = tal.Next(0, 1000000);
                g[i] = tal.Next(0, 1000000);
                k[i] = tal.Next(0, 1000000);
            }

            for (int i = 0; i < 1000; i++)  //Adding numbers to the arrays of 1000
            {
                b[i] = tal.Next(0, 1000000);
                e[i] = tal.Next(0, 1000000);
                h[i] = tal.Next(0, 1000000);
                l[i] = tal.Next(0, 1000000);
            }

            for (int i = 0; i < 100000; i++)    //Adding numbers to the arrays of 100000
            {
                c[i] = tal.Next(0, 1000000);
                f[i] = tal.Next(0, 1000000);
                j[i] = tal.Next(0, 1000000);
                m[i] = tal.Next(0, 1000000);
            }

            Console.WriteLine("Sorting algorithms timed tests");    //Writing out the type of sorting algorithm and the amount of elements inside of that array. First with 10 numbers in each array, then 1000 numbers and at last 100000 numbers.
            Thread.Sleep(2000); //Wait 2 seconds
            Console.WriteLine("Press ENTER to START!");
            Console.ReadLine(); //User has to press enter to start the sorting. Has to do that for all of the other sorting parts aswell.

            //hur man anropar en metod i en class: (classnamn.metodnamn(arraynamn))
            Console.WriteLine("Bubblesort with 10 numbers");
            sw.Start();
            Bubblesort.BubbleSort(a);    //start sorting(Bubblesort)
            sw.Stop();
            Atime = sw.ElapsedTicks * nanosecPerTick;
            Console.WriteLine(sw.ElapsedTicks * nanosecPerTick + " ns");
            sw.Reset();
            Console.ReadLine();

            Console.WriteLine("Insertionsort with 10 numbers");
            sw.Start();
            Insertionsort.InsertionSort(d);    //start sorting(Insertionsort)
            sw.Stop();
            Dtime = sw.ElapsedTicks * nanosecPerTick;
            Console.WriteLine(sw.ElapsedTicks * nanosecPerTick + " ns");
            sw.Reset();
            Console.ReadLine();

            Console.WriteLine("Mergesort with 10 numbers");
            sw.Start();
            Mergsort.MergeSort(g);    //start sorting(Mergsort)
            sw.Stop();
            Gtime = sw.ElapsedTicks * nanosecPerTick;
            Console.WriteLine(sw.ElapsedTicks * nanosecPerTick + " ns");
            sw.Reset();
            Console.ReadLine();

            Console.WriteLine("Quicksort with 10 numbers");
            sw.Start();
            Quicksort.QuickSort(k);    //start sorting(Quicksort)
            sw.Stop();
            Ktime = sw.ElapsedTicks * nanosecPerTick;
            Console.WriteLine(sw.ElapsedTicks * nanosecPerTick + " ns");
            sw.Reset();
            Console.ReadLine();

            Console.WriteLine("Bubblesort with 1000 numbers");
            sw.Start();
            Bubblesort.BubbleSort(b);    //start sorting(Bubblesort)
            sw.Stop();
            Btime = sw.ElapsedTicks * nanosecPerTick;
            Console.WriteLine(sw.ElapsedTicks * nanosecPerTick + " ns");
            sw.Reset();
            Console.ReadLine();

            Console.WriteLine("Insertionsort with 1000 numbers");
            sw.Start();
            Insertionsort.InsertionSort(e);    //start sorting(Insertionsort)
            sw.Stop();
            Etime = sw.ElapsedTicks * nanosecPerTick;
            Console.WriteLine(sw.ElapsedTicks * nanosecPerTick + " ns");
            sw.Reset();
            Console.ReadLine();

            Console.WriteLine("Mergesort with 1000 numbers");
            sw.Start();
            Mergsort.MergeSort(h);    //start sorting(Mergsort)
            sw.Stop();
            Htime = sw.ElapsedTicks * nanosecPerTick;
            Console.WriteLine(sw.ElapsedTicks * nanosecPerTick + " ns");
            sw.Reset();
            Console.ReadLine();

            Console.WriteLine("Quicksort with 1000 numbers");
            sw.Start();
            Quicksort.QuickSort(l);    //start sorting(Quicksort)
            sw.Stop();
            Ltime = sw.ElapsedTicks * nanosecPerTick;
            Console.WriteLine(sw.ElapsedTicks * nanosecPerTick + " ns");
            sw.Reset();
            Console.ReadLine();

            Console.WriteLine("Bubblesort with 100000 numbers");
            sw.Start();
            Bubblesort.BubbleSort(c);    //start sorting(Bubblesort)
            sw.Stop();
            Ctime = sw.ElapsedTicks * nanosecPerTick;
            Console.WriteLine(sw.ElapsedTicks * nanosecPerTick + " ns");
            sw.Reset();
            Console.ReadLine();

            Console.WriteLine("Insertionsort with 100000 numbers");
            sw.Start();
            Insertionsort.InsertionSort(f);    //start sorting(Insertionsort)
            sw.Stop();
            Ftime = sw.ElapsedTicks * nanosecPerTick;
            Console.WriteLine(sw.ElapsedTicks * nanosecPerTick + " ns");
            sw.Reset();
            Console.ReadLine();

            Console.WriteLine("Mergesort with 100000 numbers");
            sw.Start();
            Mergsort.MergeSort(j);    //start sorting(Mergsort)
            sw.Stop();
            Jtime = sw.ElapsedTicks * nanosecPerTick;
            Console.WriteLine(sw.ElapsedTicks * nanosecPerTick + " ns");
            sw.Reset();
            Console.ReadLine();

            Console.WriteLine("Quicksort with 100000 numbers");
            sw.Start();
            Quicksort.QuickSort(m);    //start sorting(Quicksort) ERROR!!!
            sw.Stop();
            Mtime = sw.ElapsedTicks * nanosecPerTick;
            Console.WriteLine(sw.ElapsedTicks * nanosecPerTick + " ns");
            sw.Reset();
            Console.ReadLine();

            //Write out all of the times categorized by type of sorting. Strating from Insertonsort to Quicksort.
            Console.WriteLine("\n");
            Console.WriteLine("Bubblesort:");
            Console.WriteLine("Array with 10 elements took: " + Atime + " ns");
            Console.WriteLine("Array with 1000 elements took: " + Btime + " ns");
            Console.WriteLine("Array with 100000 elements took: " + Ctime + " ns");

            Console.WriteLine("\n");
            Console.WriteLine("Insertionsort:");
            Console.WriteLine("Array with 10 elements took: " + Dtime + " ns");
            Console.WriteLine("Array with 1000 elements took: " + Etime + " ns");
            Console.WriteLine("Array with 100000 elements took: " + Ftime + " ns");

            Console.WriteLine("\n");
            Console.WriteLine("Mergsort:");
            Console.WriteLine("Array with 10 elements took: " + Gtime + " ns");
            Console.WriteLine("Array with 1000 elements took: " + Htime + " ns");
            Console.WriteLine("Array with 100000 elements took: " + Jtime + " ns");

            Console.WriteLine("\n");
            Console.WriteLine("Quicksort:");
            Console.WriteLine("Array with 10 elements took: " + Ktime + " ns");
            Console.WriteLine("Array with 1000 elements took: " + Ltime + " ns");
            Console.WriteLine("Array with 100000 elements took: " + Mtime + " ns");

            if (Atime < Dtime && Atime < Gtime && Atime < Ktime) //Looking for fastest sortingalgorithm for 10 elements
            {
                Fastest10 = Atime;
            }
            else if (Dtime < Atime && Dtime < Gtime && Dtime < Ktime)
            {
                Fastest10 = Dtime;
            }
            else if (Gtime < Atime && Gtime < Dtime && Gtime < Ktime)
            {
                Fastest10 = Gtime;
            }
            else
            {
                Fastest10 = Ktime;
            }

            if (Btime < Etime && Btime < Htime && Btime < Ltime)    //Looking for fastest sortingalgorithm for 1000 elements
            {
                Fastest1000 = Btime;
            }
            else if (Etime < Btime && Etime < Htime && Etime < Ltime)
            {
                Fastest1000 = Etime;
            }
            else if (Htime < Btime && Htime < Etime && Htime < Ltime)
            {
                Fastest1000 = Htime;
            }
            else
            {
                Fastest1000 = Ltime;
            }

            if (Ctime < Ftime && Ctime < Jtime && Ctime < Mtime)    //Looking for fastest sorting algorithm for 100000 elements
            {
                Fastest100000 = Ctime;
            }
            else if (Ftime < Ctime && Ftime < Jtime && Ftime < Mtime)
            {
                Fastest100000 = Ftime;
            }
            else if (Jtime < Ctime && Jtime < Ftime && Jtime < Mtime)
            {
                Fastest100000 = Jtime;
            }
            else
            {
                Fastest100000 = Mtime;
            }

            Console.WriteLine("\n");
            Console.WriteLine("Fastest sorting algorithm for 10 elements: ");
            Console.WriteLine(Fastest10);

            Console.WriteLine("\n");
            Console.WriteLine("Fastest sorting algorithm for 1000 elements: ");
            Console.WriteLine(Fastest1000);

            Console.WriteLine("\n");
            Console.WriteLine("Fastest sorting algorithm for 100000 elements: ");
            Console.WriteLine(Fastest100000);

            Console.ReadLine();
        }
    }
}
