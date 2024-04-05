// Program.cs
//
// Author: Samuel Berg
// Date: 10-Aug-2019

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SLL
{
    class Program
    {
        static void Main(string[] args)
        {
            LinkedList list = new LinkedList();

            list.AddLast(1);
            list.AddLast(2);
            list.Add(1, 3);

            list.PrintList();

            list.Remove(1);

            list.PrintList();

            list.RemoveValue(2);

            list.PrintList();

            list.Clear();

            Console.ReadLine();
        }
    }
}
