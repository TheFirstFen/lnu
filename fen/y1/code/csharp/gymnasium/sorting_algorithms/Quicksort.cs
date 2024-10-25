using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace InfogandeSortering
{
    class Quicksort
    {
        public static void QuickSort(int[] a)
        {
            QuickSort(a, 0, a.Length - 1);
        }

        private static void QuickSort(int[] a, int left, int right)
        {
            if (left < right)
            {
                int pivot = Partition(a, left, right);

                if (pivot > 1)
                {
                    QuickSort(a, left, pivot - 1);
                }
                if (pivot + 1 < right)
                {
                    QuickSort(a, pivot + 1, right);
                }
            }
        }

        private static int Partition(int[] a, int left, int right)
        {
            int pivot = a[left];
            while (true)
            {
                while (a[left] < pivot)
                {
                    left++;
                }

                while (a[right] > pivot)
                {
                    right--;
                }

                if (left < right)
                {
                    if (a[left] == a[right]) return right;

                    int temp = a[left];
                    a[left] = a[right];
                    a[right] = temp;
                }
                else
                {
                    return right;
                }
            }
        }
    }
}
