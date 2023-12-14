package algorithms.tree;

public class BST {
    class Node {
        int key;
        Node l, r;

        public Node(int item) {
            key = item;
            l = r = null;
        }
    }

    class BSTree {
        private Node root;

        public BSTree() {
            root = null;
        }

        public void insert(int key) {
            root = insertRec(root, key);
        }

        private Node insertRec(Node root, int key) {
            if (root == null) {
                root = new Node(key);
                return root;
            }

            if (key < root.key) {
                root.l = insertRec(root.l, key);
            } else if (key > root.key) {
                root.r = insertRec(root.r, key);
            }

            return root;
        }

        public void delete(int key) {
            root = deleteRec(root, key);
        }

        private Node deleteRec(Node root, int key) {
            if (root == null) {
                return root;
            }

            if (key < root.key) {
                root.l = deleteRec(root.l, key);
            } else if (key > root.key) {
                root.r = deleteRec(root.r, key);
            } else {
                if (root.l == null) {
                    return root.r;
                } else if (root.r == null) {
                    return root.l;
                }

                root.key = minValue(root.r);

                root.r = deleteRec(root.r, root.key);
            }

            return root;
        }

        private int minValue(Node root) {
            int minValue = root.key;

            while (root.l != null) {
                minValue = root.l.key;
                root = root.l;
            }

            return minValue;
        }

        public boolean search(int key) {
            return searchRec(root, key);
        }

        private boolean searchRec(Node root, int key) {
            if (root == null || root.key == key) {
                return root != null;
            }

            if (key < root.key) {
                return searchRec(root.l, key);
            }

            return searchRec(root.r, key);
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
