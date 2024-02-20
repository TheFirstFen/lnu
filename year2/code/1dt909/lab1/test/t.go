package main

import (
	"math"
	"sync"
	"sync/atomic"
)

type LLNode struct {
	key int
	nxt *LLNode
}

type LL struct {
	head, tail *LLNode
}

func NewLL() LL {
	head := LLNode{key: math.MinInt}
	tail := LLNode{key: math.MaxInt}
	head.nxt = &tail

	return LL{head: &head, tail: &tail}
}

func (lst *LL) find(k int) (pred *LLNode, curr *LLNode) {
	curr = lst.head
	for {
		pred = curr
		curr = curr.nxt
		if curr.key >= k {
			break
		}
	}

	return pred, curr
}

func (lst *LL) contains(k int) bool {
	_, curr := lst.find(k)

	return curr.key == k
}

func (lst *LL) Add(k int) bool {
	pred, curr := lst.find(k)
	if curr.key == k {
		return false
	} else {
		n := LLNode{key: k, nxt: curr}
		pred.nxt = &n
		return true
	}
}

func (lst *LL) Remove(k int) bool {
	pred, curr := lst.find(k)
	if curr.key != k {
		return false
	} else {
		pred.nxt = curr.nxt
		return true
	}
}

type CoarseLL struct {
	head, tail *LLNode
	lock       sync.Mutex
}

func NewCoarseLL() CoarseLL {
	head := LLNode{key: math.MinInt}
	tail := LLNode{key: math.MaxInt}
	head.nxt = &tail

	return CoarseLL{head: &head, tail: &tail}
}

func (lst *CoarseLL) Find(k int) (pred *LLNode, curr *LLNode) {
	curr = lst.head
	for {
		pred = curr
		curr = curr.nxt
		if curr.key >= k {
			break
		}
	}
	return pred, curr
}

func (lst *CoarseLL) Add(k int) bool {
	lst.lock.Lock()
	defer lst.lock.Unlock()

	pred, curr := lst.Find(k)

	if curr.key == k {
		return false
	} else {
		n := LLNode{key: k, nxt: curr}
		pred.nxt = &n
		return true
	}
}

func (lst *CoarseLL) Contains(k int) bool {
	lst.lock.Lock()
	_, curr := lst.Find(k)
	lst.lock.Unlock()

	return curr.key == k
}

func (lst *CoarseLL) Remove(k int) bool {
	lst.lock.Lock()
	defer lst.lock.Unlock()

	pred, curr := lst.Find(k)
	if curr.key != k {
		return false
	} else {
		pred.nxt = curr.nxt
		return true
	}
}

type LLFine struct {
	head, tail *LLLockNode
}

type LLLockNode struct {
	lock sync.Mutex
	key  int
	nxt  *LLLockNode
}

func NewLLFine() LLFine {
	head := LLLockNode{key: math.MinInt}
	tail := LLLockNode{key: math.MaxInt}
	head.nxt = &tail

	return LLFine{head: &head, tail: &tail}
}

func (lst *LLFine) Find(k int) (pred *LLLockNode, curr *LLLockNode) {
	pred = lst.head
	curr = pred.nxt
	pred.lock.Lock()
	curr.lock.Lock()
	for curr.key < k {
		pred.lock.Unlock()
		pred = curr
		curr = curr.nxt
		curr.lock.Lock()
	}

	return pred, curr
}

func (lst *LLFine) Add(k int) bool {
	pred, curr := lst.Find(k)
	defer pred.lock.Unlock()
	defer curr.lock.Unlock()

	if curr.key == k {
		return false
	} else {
		n := LLLockNode{key: k, nxt: curr}
		pred.nxt = &n
		return true
	}
}

func (lst *LLFine) Remove(k int) bool {
	pred, curr := lst.Find(k)
	defer pred.lock.Unlock()
	defer curr.lock.Unlock()

	if curr.key != k {
		return false
	} else {
		pred.nxt = curr.nxt
		return true
	}
}

func (lst *LLFine) Contains(k int) bool {
	pred, curr := lst.Find(k)
	defer pred.lock.Unlock()
	defer curr.lock.Unlock()

	return curr.key == k
}

type LLANode struct {
	lock sync.Mutex
	key  int
	nxt  atomic.Pointer[LLANode]
}

type LLAFine struct {
	head, tail atomic.Pointer[LLANode]
}

func NewLLAFine() LLAFine {
	head := LLANode{key: math.MinInt}
	tail := LLANode{key: math.MaxInt}
	head.nxt.Store(&tail)

	return LLAFine{head: &head, tail: &tail}
}

func (lst *LLAFine) Find(k int) (pred *LLANode, curr *LLANode) {
	pred = lst.head.Load()
	curr = pred.nxt.Load()
	for {
		if curr.key >= k {
			break
		}
		pred = curr
		curr = curr.nxt.Load()
	}
	return pred, curr
}

func (lst *LLAFine) Add(k int) bool {
	for {
		pred, curr = lst.Find(k)
		pred.lock.Lock()
		curr.lock.Lock()

		if lst.valid(pred, curr) {
			n := LLANode{key: k}
			n.nxt.Store(curr)
			pred.nxt.Store(&n)
			pred.lock.Unlock()
			curr.lock.Unlock()
			return true
		}
		pred.lock.Unlock()
		curr.lock.Unlock()
	}
}

func (lst LLAFine) valid(pred, curr *LLANode) bool {
	n := lst.head.Load()
	for n.key <= pred.key {
		if n == pred {
			return pred.nxt.Load() == curr
		}
		n = n.nxt.Load()
	}
	return false
}
