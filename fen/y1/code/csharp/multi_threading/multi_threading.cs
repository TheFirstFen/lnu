// multi_threading.cs
//
// Author: Samuel Berg
// Date: 10-Sep-2019

using System;
using System.Threading;

namespace MultithreadingApplication
{
    class ThreadCreatoinProgram
    {
        public static void CallToChildThread()
        {
            string name = Thread.CurrentThread.Name;
            Console.WriteLine(name + " started");
            for (int i = 0; i <= 10; i++)
            {
                Console.WriteLine(name + ": " + i);
                Thread.Sleep(500);
            }
        }
        static void Main(string[] args)
        {
            ThreadStart childref1 = new ThreadStart(CallToChildThread);

            ThreadStart childref2 = new ThreadStart(CallToChildThread);

            Thread thread1 = new Thread(childref1);
            thread1.Name = "Thread1";

            Thread thread2 = new Thread(childref2);
            thread1.Name = "Thread2";

            thread1.Start();
            thread2.Start();
        }
    }
}
