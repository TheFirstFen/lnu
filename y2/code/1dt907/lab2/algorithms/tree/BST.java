package algorithms.tree;

public class BST {
    private BSTNode root;

    public BST() {
        root = null;
    }

    public void insert(int key) {
        root = insertRec(root, key);
    }

    private BSTNode insertRec(BSTNode root, int key) {
        if (root == null) {
            root = new BSTNode(key);
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

    private BSTNode deleteRec(BSTNode root, int key) {
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

    private int minValue(BSTNode root) {
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

    private boolean searchRec(BSTNode root, int key) {
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

    private void inOrder(BSTNode root) {
        if (root != null) {
            inOrder(root.l);
            System.out.print(root.key + " ");
            inOrder(root.r);
        }
    }

    private int height(BSTNode node) {
        int l = 0;
        int r = 0;

        if (node.l != null)
            l = height(node.l);
        if (node.r != null)
            r = height(node.r);

        return Math.max(l, r) + 1;
    }

    public int status() {
        if (root != null)
            return height(root);
        else
            return 0;
    }

    public BST generateBalancedTree(int[] n) {
        BST temp = new BST();
        temp.root = sortedArrToTree(n, 0, n.length - 1);
        return temp;
    }

    private static BSTNode sortedArrToTree(int[] values, int start, int stop) {
        if (start > stop)
            return null;

        int mid = (start + stop) / 2;
        BSTNode root = new BSTNode(values[mid]);

        root.l = sortedArrToTree(values, start, mid - 1);
        root.r = sortedArrToTree(values, mid + 1, stop);

        return root;
    }
}