package main

import (
	"cmp"
	"fmt"
)

type Node[T cmp.Ordered] struct {
	Val	T
	L, R  *Node[T]
}

type BST[T cmp.Ordered] struct {
	Root *Node[T]
}

func newBST[T cmp.Ordered]() *BST[T] {
	return &BST[T]{}
}

func (bst *BST[T]) Insert(val T) {
	bst.Root = insertRec(bst.Root, val)
}

func insertRec[T cmp.Ordered](root *Node[T], val T) *Node[T] {
	if root == nil {
		return &Node[T]{Val: val}
	}

	if val < root.Val {
		root.L = insertRec(root.L, val)
	} else if val > root.Val {
		root.R = insertRec(root.R, val)
	}

	return root
}

func (bst *BST[T]) Remove(val T) {
	bst.Root = removeRec(bst.Root, val)
}

func removeRec[T cmp.Ordered](root *Node[T], val T) *Node[T] {
	if root == nil {
		return nil
	}

	if val < root.Val {
		root.L = removeRec(root.L, val)
	} else if val > root.Val {
		root.R = removeRec(root.R, val)
	} else {
		if root.L == nil {
			return root.R
		} else if root.R == nil {
			return root.L
		}

		min := findMin(root.R)
		root.Val = min.Val
		root.R = removeRec(root.R, min.Val)
	}

	return root
}

func findMin[T cmp.Ordered](node *Node[T]) *Node[T, ] {
	cur := node
	for cur.L != nil {
		cur = cur.L
	}

	return cur
}

func (bst *BST[T]) Find(val T) bool {
	return findRec(bst.Root, val)
}

func findRec[T cmp.Ordered](root *Node[T], val T) bool {
	if root == nil {
		return false
	}

	if val < root.Val {
		return findRec(root.L, val)
	} else if val > root.Val {
		return findRec(root.R, val)
	} else {
		return true
	}
}

func (bst *BST[T]) Walk(f func(T)) {
	walkRec(bst.Root, f)
}

func walkRec[T cmp.Ordered](root *Node[T], f func(T)) {
	if root != nil {
		walkRec(root.L, f)
		f(root.Val)
		walkRec(root.R, f)
	}
}

func main() {
	testInt()
	testString()
}

func testInt() {
	fmt.Print("Int Version BST\n\n\n")

	bstI := newBST[int]()

	bstI.Insert(5)
	bstI.Insert(3)
	bstI.Insert(7)
	bstI.Insert(2)
	bstI.Insert(4)
	bstI.Insert(6)
	bstI.Insert(8)

	fmt.Println("Find 3:", bstI.Find(3))
	fmt.Println("Find 9:", bstI.Find(9))

	fmt.Println("Removing 3")
	bstI.Remove(3)

	fmt.Println("Find 3:", bstI.Find(3))

	fmt.Println("\nWalking tree:")
	bstI.Walk(func (val int) {
		fmt.Println(val)
	})
}

func testString() {
	fmt.Print("\n\nString Version BST\n\n\n")

	bstS := newBST[string]()

	bstS.Insert("5")
	bstS.Insert("3")
	bstS.Insert("7")
	bstS.Insert("2")
	bstS.Insert("4")
	bstS.Insert("6")
	bstS.Insert("8")
	bstS.Insert("abc")
	bstS.Insert("def")

	fmt.Println("Find \"abc\":", bstS.Find("abc"))
	fmt.Println("Find \"ef\":", bstS.Find("ef"))

	fmt.Println("Removing \"abc\"")
	bstS.Remove("abc")

	fmt.Println("Find \"abc\":", bstS.Find("abc"))

	fmt.Println("\nWalking tree:")
	bstS.Walk(func (val string) {
		fmt.Println(val)
	})
}


