using System;
using System.Collections.Generic;
using System.Text;

namespace Stack
{
    class Queue
    {
        /// <summary>
        /// Själva stacken
        /// </summary>
        private int[] queue;

        /// <summary>
        /// Stackpekaren som också håller reda på hur många element det finns i stacken
        /// </summary>
        private int count = 0;

        public int Count
        { get { return count; }  }

        public int this[int i]
        {
            get { return queue[i]; }
            set { queue[i] = value; }
        }

        public Queue()
        {
            queue = new int[10];
        }

        public Queue(int size)
        {
            queue = new int[size];
        }

        /// <summary>
        /// Lägger till ett element sist i kön
        /// </summary>
        /// <param name="value"></param>
        public void Enqueue(int value)
        {
            if (queue.Length == count)
                ReSize((int)(count * 1.3));

            queue[count] = value;
            count++;
        }

        /// <summary>
        /// Tar bort första värdet i stacken och flyttar alla element ett steg framåt
        /// </summary>
        public int Dequeue()
        {
            int rem = queue[0];

            for (int i = 0; i < count; i++)
            {
                queue[i] = queue[i + 1];
            }

            count--;

            return rem;
        }

        /// <summary>
        /// Retunerar det första värdet i stackens
        /// </summary>
        /// <returns></returns>
        public int Peek()
        {
            return queue[0];
        }

        /// <summary>
        /// Ändrar stoleken på stacken
        /// </summary>
        /// <param name="size">Nya storleken på stacken</param>
        private void ReSize(int size)
        {
            int[] temp = queue;

            queue = new int[size];

            for (int i = 0; i < count; i++)
            {
                queue[i] = temp[i];
            }
        }


        /// <summary>
        /// Rensar stcken
        /// </summary>
        public void Clear()
        {
            count = 0;
            queue = new int[10];
        }
    }
}
