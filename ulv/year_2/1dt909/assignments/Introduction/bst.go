package main

import (
	"fmt"
)

type Node[T any] struct {
	Value T
	Left, Right *Node[T]
}

type BST[T any] struct {
	Root *Node[T]
	less func(a, b T) bool
}

func NewBST[T any](less func(a, b T) bool) *BST[T] {
	return &BST[T]{less: less}
}

func (bst *BST[T]) Insert(value T) {
	bst.Root = bst.insertRec(bst.Root, value)
}

func (bst *BST[T]) insertRec(root *Node[T], value T) *Node[T] {
	if root == nil {
		return &Node[T]{Value: value}
	}

	if bst.less(value, root.Value) {
		root.Left = bst.insertRec(root.Left, value)
	} else if bst.less(root.Value, value) {
		root.Right = bst.insertRec(root.Right, value)
	}

	return root
}

func (bst *BST[T]) Remove(value T) {
	bst.Root = bst.removeRec(bst.Root, value)
}

func (bst *BST[T]) removeRec(root *Node[T], value T) *Node[T] {
	if root == nil {
		return nil
	}

	if bst.less(value, root.Value) {
		root.Left = bst.removeRec(root.Left, value)
	} else if bst.less(root.Value, value) {
		root.Right = bst.removeRec(root.Right, value)
	} else {
		if root.Left == nil {
			return root.Right
		} else if root.Right == nil {
			return root.Left
		}

		root.Value = minValue(root.Right)
		root.Right = bst.removeRec(root.Right, root.Value)
	}
	return root
}

func minValue[T any](node *Node[T]) T {
	minNode := node
	for minNode.Left != nil {
		minNode = minNode.Left
	}
	return minNode.Value
}

func (bst *BST[T]) Find(value T) *Node[T] {
	return bst.findRec(bst.Root, value, bst.less)
}

func (bst *BST[T]) findRec(root *Node[T], value T, less func(a, b T) bool) *Node[T] {
	if root == nil || !less(root.Value, value) && !less(value, root.Value) {
		return root
	}

	if less(value, root.Value) {
		return bst.findRec(root.Left, value, less)
	}

	return bst.findRec(root.Right, value, less)
}

func (bst *BST[T]) InOrder(root *Node[T], f func(T)) {
	bst.inOrder(bst.Root, f)
}

func (bst *BST[T]) inOrder(root *Node[T], f func(T)) {
	if root != nil {
		bst.inOrder(root.Left, f)
		f(root.Value)
		bst.inOrder(root.Right, f)
	}
}

func main() {
	less := func(a, b int) bool { return a < b }
	bst := NewBST[int](less)

	bst.Insert(5)
	bst.Insert(3)
	bst.Insert(7)
	bst.Insert(2)
	bst.Insert(4)
	bst.Insert(6)
	bst.Insert(8)
	bst.Insert(1)
	//bst.Insert("ac")
	//bst.Insert("ab")
	//bst.Insert("aa")

	searchValue := 4
	foundNode := bst.Find(searchValue)
	if foundNode != nil {
		fmt.Printf("Value %v found in the BST\n", searchValue)
	} else {
		fmt.Printf("Value %v not found in the BST\n", searchValue)
	}

	removeValue := 7
	bst.Remove(removeValue)
	fmt.Println("Removed value", removeValue, "from the BST")

	fmt.Println("In-order walk of the BST:")
	bst.InOrder(bst.Root, func(value int) {
		fmt.Println(value)
	})
}
