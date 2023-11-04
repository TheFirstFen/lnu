using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SLL
{
    public class LinkedList
    {
        private Node head;
        private int count;

        public LinkedList()
        {
            this.head = null;
            this.count = 0;
        }

        public bool Empty
        {
            get { return this.count == 0; }
        }

        public int Count
        {
            get { return this.count; }
        }

        public object this[int idx]
        {
            get { return this.Get(idx); }
        }

        public object Add(int idx, object obj)
        {
            if (idx < 0)
            {
                throw new ArgumentOutOfRangeException("Index: " + idx);
            }

            if (idx > count)
            {
                idx = count;
            }

            Node cur = this.head;

            if(this.Empty || idx == 0)
            {
                this.head = new Node(obj, this.head);
            }
            else
            {
                for(int i = 0; i < idx - 1; i++)
                {
                    cur = cur.Next;
                }
                
                cur.Next = new Node(obj, cur.Next);
            }

            count++;

            return obj;
        }

        public object AddFirst(object obj)
        {
            return this.Add(0, obj);
        }

        public object AddLast(object obj)
        {
            return this.Add(count, obj);
        }

        public object Remove(int idx)
        {
            if (idx < 0)
            {
                throw new ArgumentOutOfRangeException("Index: " + idx);
            }

            if (this.Empty) 
            { 
                return null; 
            }

            if(idx >= this.count)
            {
                idx = count - 1;
            }

            Node cur = this.head;
            object result = null;

            if (idx == 0)
            {
                result = cur.Data;
                this.head = cur.Next;
            }
            else
            {
                for (int i = 0; i < idx - 1; i++)
                {
                    cur = cur.Next;
                }

                result = cur.Next.Data;

                cur.Next = cur.Next.Next;
            }

            count--;

            return result;
        }

        public object RemoveFirst()
        {
            return this.Remove(0);
        }

        public object RemoveLast()
        {
            return this.Remove(count - 1);
        }

        public object RemoveValue(object obj)   // Error??
        {
            Node prev = null;
            Node cur = head;

            if(cur != null && cur.Data == obj)
            {
                head = cur.Next;
                return head;
            }

            while(cur != null && cur.Data != obj)
            {
                prev = cur;
                cur = cur.Next;
            }

            if (cur == null)
            {
                return null;
            }

            if (prev == null)
            {
                if (cur.Next == null)
                {
                    Clear();
                }
                else
                {
                    head = cur.Next;
                }

                return head;
            }

            if(cur.Next == null)
            {
                prev.Next = null;

                return this.Empty;
            }

            if(prev != null && cur.Next != null)
            {
                prev.Next = cur.Next;

                return prev.Next;
            }

            prev.Next = cur.Next;

            count--;

            return head;
        }

        public void Clear()
        {
            this.head = null;
            this.count = 0;
        }

        public int FindValue(object obj)
        {
            Node cur = this.head;

            for (int i = 0; i < this.count; i++)
            {
                if (cur.Data.Equals(obj))
                {
                    return i;
                }

                cur = cur.Next;
            }

            return -1;
        }

        public bool Contains(object obj)
        {
            return this.FindValue(obj) > -1;
        }

        public object Get(int idx)
        {
            if (idx < 0)
            {
                throw new ArgumentOutOfRangeException("Index: " + idx);
            }

            if (this.Empty)
            {
                return null;
            }

            if (idx >= this.count)
            {
                idx = this.count - 1;
            }

            Node cur = this.head;

            for (int i = 0; i < idx; i++)
            {
                cur = cur.Next;
            }

            return cur.Data;
        }

        public void PrintList()
        {
            Node cur = head;

            while(cur != null)
            {
                Console.WriteLine(cur.Data + "\n");
                cur = cur.Next;
            }
        }
    }
}
