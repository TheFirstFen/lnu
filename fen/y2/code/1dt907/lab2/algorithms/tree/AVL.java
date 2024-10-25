package algorithms.tree;

public class AVL {
    private AVLNode root;

    public AVL() {
        root = null;
    }

    private static int height(AVLNode node) {
        if (node == null)
            return 0;

        return node.height;
    }

    private int balance(AVLNode node) {
        if (node == null)
            return 0;

        return height(node.l) - height(node.r);
    }

    private static void updateHeight(AVLNode node) {
        if (node != null)
            node.height = 1 + Math.max(height(node.l), height(node.r));
    }

    private AVLNode rotateR(AVLNode y) {
        AVLNode x = y.l;
        AVLNode T2 = x.r;

        x.r = y;
        y.l = T2;

        updateHeight(y);
        updateHeight(x);

        return x;
    }

    private AVLNode rotateL(AVLNode x) {
        AVLNode y = x.r;
        AVLNode T2 = y.l;

        y.l = x;
        x.r = T2;

        updateHeight(x);
        updateHeight(y);

        return y;
    }

    public void insert(int key) {
        root = insert(root, key);
    }

    private AVLNode insert(AVLNode node, int key) {
        if (node == null)
            return new AVLNode(key);

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

    private AVLNode delete(AVLNode root, int key) {
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

    private int minValue(AVLNode node) {
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

    private void inOrder(AVLNode root) {
        if (root != null) {
            inOrder(root.l);
            System.out.print(root.key + " ");
            inOrder(root.r);
        }
    }

    public boolean search(int key) {
        return serachRec(root, key);
    }

    private boolean serachRec(AVLNode root, int key) {
        if (root == null || root.key == key) {
            return root != null;
        }

        if (key < root.key) {
            return serachRec(root.l, key);
        }

        return serachRec(root.r, key);
    }

    public int status() {
        if (root != null)
            return height(root);
        else
            return 0;
    }

    public AVL generateBalancedTree(int[] n) {
        AVL temp = new AVL();
        temp.root = sortedArrToTree(n, 0, n.length - 1);
        return temp;
    }

    private static AVLNode sortedArrToTree(int[] values, int start, int stop) {
        if (start > stop)
            return null;

        int mid = (start + stop) / 2;
        AVLNode node = new AVLNode(values[mid]);

        node.l = sortedArrToTree(values, start, mid - 1);
        node.r = sortedArrToTree(values, mid + 1, stop);

        updateHeight(node);

        return node;
    }
}
