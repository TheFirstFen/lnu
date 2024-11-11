package Assignment2;

public class BST {
    private btNode root;

    public BST() {
        root = null;
    }
        public void insert(int key) {
        root = insertRec(root, key);
    }

    private btNode insertRec(btNode root, int key) {
        if (root == null) {
            root = new btNode(key);
            return root;
        }
        if (key < root.key) {
            root.left = insertRec(root.left, key);
        } else if (key > root.key) {
            root.right = insertRec(root.right, key);
        }
        return root;
    }
    public int getDepth() {
        return getDepth(root);
    }

    private int getDepth(btNode node) {
        if (node == null) {
            return 0;
        } else {
            int leftDepth = getDepth(node.left);
            int rightDepth = getDepth(node.right);

            return Math.max(leftDepth, rightDepth) + 1;
        }
    }
    public void delete(int key) {
        root = deleteNode(root, key);
    }

    private btNode deleteNode(btNode root, int key) {
        if (root == null) {
            return root;
        }

        if (key < root.key) {
            root.left = deleteNode(root.left, key);
        } else if (key > root.key) {
            root.right = deleteNode(root.right, key);
        } else {
            if (root.left == null) {
                return root.right;
            } else if (root.right == null) {
                return root.left;
            }
            root.key = minValue(root.right);
            root.right = deleteNode(root.right, root.key);
        }

        return root;
    }

    private int minValue(btNode root) {
        int minValue = root.key;
        while (root.left != null) {
            minValue = root.left.key;
            root = root.left;
        }
        return minValue;
    }
}

