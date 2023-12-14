package algorithms.tree;

public class AVL {
    class Node {
        int key, height;
        Node l, r;

        public Node(int item) {
            key = item;
            height = 1;
            l = r = null;
        }
    }

    public class AVLTree {
        private Node root;

        public AVLTree() {
            root = null;
        }

        private int height(Node node) {
            if (node == null)
                return 0;

            return node.height;
        }

        private int balance(Node node) {
            if (node == null)
                return 0;

            return height(node.l) - height(node.r);
        }

        private void updateHeight(Node node) {
            if (node != null)
                node.height = 1 + Math.max(height(node.l), height(node.r));
        }

        private Node rotateR(Node y) {
            Node x = y.l;
            Node T2 = x.r;

            x.r = y;
            y.l = T2;

            updateHeight(y);
            updateHeight(x);

            return x;
        }

        private Node rotateL(Node x) {
            Node y = x.r;
            Node T2 = y.l;

            y.l = x;
            x.r = T2;

            updateHeight(x);
            updateHeight(y);

            return y;
        }

        public void insert(int key) {
            root = insert(root, key);
        }

        private Node insert(Node node, int key) {
            if (node == null)
                return new Node(key);

            if (key < node.key)
                node.l = insert(node.l, key);
            else if (key > node.key)
                node.r = insert(node.r, key);
            else
                return node;

            updateHeight(node);

            int balance = balance(node);

            if (balance > 1) {
                if (key < node.l.key)
                    return rotateR(node);
                else {
                    node.l = rotateL(node.l);
                    return rotateR(node);
                }
            }

            if (balance < -1) {
                if (key > node.r.key)
                    return rotateL(node);
                else {
                    node.r = rotateR(node.r);
                    return rotateL(node);
                }
            }

            return node;
        }

        public void delete(int key) {
            root = delete(root, key);
        }

        private Node delete(Node root, int key) {
            if (root == null)
                return root;

            if (key < root.key)
                root.l = delete(root.l, key);
            else if (key > root.key)
                root.r = delete(root.r, key);
            else {
                if (root.l == null)
                    return root.r;
                else if (root.r == null)
                    return root.l;

                root.key = minValue(root.r);

                root.r = delete(root.r, root.key);
            }

            updateHeight(root);

            int balance = balance(root);

            if (balance > 1) {
                if (balance(root.l) >= 0)
                    return rotateR(root);
                else {
                    root.l = rotateL(root.l);
                    return rotateR(root);
                }
            }

            if (balance < -1) {
                if (balance(root.r) <= 0)
                    return rotateL(root);
                else {
                    root.r = rotateR(root.r);
                    return rotateL(root);
                }
            }

            return root;
        }

        private int minValue(Node node) {
            int minValue = node.key;

            while (node.l != null) {
                minValue = node.l.key;
                node = node.l;
            }

            return minValue;
        }

        public void inOrder() {
            inOrder(root);
        }

        private void inOrder(Node root) {
            if (root != null) {
                inOrder(root.l);
                System.out.print(root.key + " ");
                inOrder(root.r);
            }
        }
    }
}
