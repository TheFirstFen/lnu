package main

import (
	"cmp"
	"fmt"
)

type node[T cmp.Ordered] struct {
	Key        T
	LeftChild  *node[T]
	RightChild *node[T]
}

func Insert[T cmp.Ordered](root *node[T], key T) *node[T] {
	if root == nil {
		return &node[T]{Key: key}
	}
	if key < root.Key {
		root.LeftChild = Insert(root.LeftChild, key)
	} else if key > root.Key {
		root.RightChild = Insert(root.RightChild, key)
	}
	return root
}

func Remove[T cmp.Ordered](root *node[T], key T) *node[T] {
	if root == nil {
		return nil
	}
	if key < root.Key {
		root.LeftChild = Remove(root.LeftChild, key)
	} else if key > root.Key {
		root.RightChild = Remove(root.RightChild, key)
	} else {
		if root.LeftChild == nil {
			return root.RightChild
		} else if root.RightChild == nil {
			return root.LeftChild
		}

		minRight := getMin(root.RightChild)
		root.Key = minRight.Key
		root.RightChild = Remove(root.RightChild, minRight.Key)
	}
	return root
}

func getMin[T cmp.Ordered](root *node[T]) *node[T] {
	for root.LeftChild != nil {
		root = root.LeftChild
	}
	return root
}
func InOrderTraversal[T cmp.Ordered](root *node[T]) {
	if root != nil {
		InOrderTraversal(root.LeftChild)
		fmt.Print(root.Key, " ")
		InOrderTraversal(root.RightChild)
	}
}
func main() {
	var root *node[int]

	root = Insert(root, 5)
	root = Insert(root, 3)
	root = Insert(root, 7)
	root = Insert(root, 2)
	root = Insert(root, 4)

	fmt.Println("Before removal:")
	InOrderTraversal(root)

	root = Remove(root, 3)

	fmt.Println("\nAfter removal:")
	InOrderTraversal(root)
}
