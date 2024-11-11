package Assignment2;

public class AVLTree {
    AVLNode root;

    public AVLTree() {
        root = null;
    }

    public AVLNode _add(AVLNode n, int key) {
        if (n == null) {
            return new AVLNode(key);
        }
        if (n.key > key) {
            n.left = _add(n.left, key);
        } else if (n.key < key) {
            n.right = _add(n.right, key);
        }
        return _balance(n);
    }
    public void add(int key) {
        root = _add(root, key);
    }

    private AVLNode _balance(AVLNode n) {
        if (n == null) {
            return n;
        }

        if (height(n.left) - height(n.right) > 1) {
            if (height(n.left.left) >= height(n.left.right)) {
                n = rotateLeft(n);
            } else {
                n = doubleLeft(n);
            }
        } else if (height(n.right) - height(n.left) > 1) {
            if (height(n.right.right) >= height(n.right.left)) {
                n = rotateRight(n);
            } else {
                n = doubleRight(n);
            }
        }

        n.height = Math.max(height(n.left), height(n.right)) + 1;
        return n;
    }
    private int height(AVLNode node) {
        if (node == null) {
            return -1;
        }
        return node.height;
    }

    private AVLNode rotateLeft(AVLNode r2) {
        AVLNode r1 = r2.left;
        r2.left = r1.right;
        r1.right = r2;
        r2.height = Math.max(height(r2.left), height(r2.right)) + 1;
        r1.height = Math.max(height(r1.left), r2.height) + 1;

        return r1;
    }
    private AVLNode rotateRight(AVLNode r2) {
        AVLNode r1 = r2.right;
        r2.right = r1.left;
        r1.left = r2;
        r2.height = Math.max(height(r2.left), height(r2.right)) + 1;
        r1.height = Math.max(height(r1.left), r2.height) + 1;

        return r1;
    }
    private AVLNode doubleRight(AVLNode n) {
        n.right = rotateLeft(n.right);
        return rotateRight(n);
    }

    private AVLNode doubleLeft(AVLNode n) {
        n.left = rotateRight(n.left);
        return rotateLeft(n);
    }
    public void delete(int key) {
        root = _delete(root, key);
    }

    private AVLNode _delete(AVLNode root, int key) {
        if (root == null) {
            return root;
        }

        if (key < root.key) {
            root.left = _delete(root.left, key);
        } else if (key > root.key) {
            root.right = _delete(root.right, key);
        } else {
            if (root.left == null) {
                return root.right;
            } else if (root.right == null) {
                return root.left;
            }

            root.key = minValue(root.right);
            root.right = _delete(root.right, root.key);
        }
        root.height = Math.max(height(root.left), height(root.right)) + 1;
        return _balance(root);
    }
        private int minValue(AVLNode root) {
        int minValue = root.key;
        while (root.left != null) {
            minValue = root.left.key;
            root = root.left;
        }
        return minValue;
    }
    public int getTreeheight() {
        return height(root);
    }
}
