using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace InfogandeSortering
{
    class Insertionsort
    {
        public static void InsertionSort(int[] lista)
        {
            int i, n;
            int length = lista.Length;
            int temp;

            if (length < 2)
                return;

            for (n = 1; n < length; n++)
            {
                temp = lista[n];
                i = n - 1;

                while (i >= 0 && lista[i] > temp)
                {
                    lista[i + 1] = lista[i];
                    i--;
                }

                lista[i + 1] = temp;
            }
        }
    }
}
