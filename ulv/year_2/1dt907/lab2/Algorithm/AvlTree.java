package Algorithm;

public class AvlTree {
    private AVLNode root;

    private int height(AVLNode node) {
        if (node == null) {
            return 0;
        }
        return node.height;
    }

    private int getBalance(AVLNode node) {
        if (node == null) {
            return 0;
        }
        return height(node.left) - height(node.right);
    }

    private AVLNode rightRotate(AVLNode y) {
        AVLNode x = y.left;
        AVLNode T2 = x.right;

        x.right = y;
        y.left = T2;

        y.height = Math.max(height(y.left), height(y.right)) + 1;
        x.height = Math.max(height(x.left), height(x.right)) + 1;
        return x;
        
    }

    private AVLNode leftRotate(AVLNode x) {
        AVLNode y = x.right;
        AVLNode T2 = y.left;

        y.left = x;
        x.right = T2;

        x.height = Math.max(height(x.left), height(x.right)) + 1;
        y.height = Math.max(height(y.left), height(y.right)) + 1;

        return y;
    }

    public void insert(int key) {
        root = insertRec(root, key);
    }

    private AVLNode insertRec(AVLNode root, int key) {
        if (root == null) {
            return new AVLNode(key);
        }

        if (key < root.key) {
            root.left = insertRec(root.left, key);
        }
        else if (key > root.key) {
            root.right = insertRec(root.right, key);
        }
        else {
            return root;
        }
        root.height = 1 + Math.max(height(root.left), height(root.right));

        int balance = getBalance(root);

        if (balance > 1 && key < root.left.key) {
            return rightRotate(root);
        }
        if (balance < -1 && key > root.right.key) {
            return leftRotate(root);
        }
        if (balance > 1 && key > root.left.key) {
            root.left = leftRotate(root.left);
            return rightRotate(root);
        }
        if (balance < -1 && key < root.right.key) {
            root.right = rightRotate(root.right);
            return leftRotate(root);
        }
        return root;
    }

    public void delete(int key) {
        root = deleteRec(root, key);
    }

    private AVLNode deleteRec(AVLNode root, int key) {
        if (root == null) {
            return root;
        }
        if (key < root.key) {
            root.left = deleteRec(root.left, key);
        }
        else if (key > root.key) {
            root.right = deleteRec(root.right, key);
        }
        else {
            if ((root.left == null) || (root.right == null)) {
                AVLNode temp = null;
                if (temp == root.left) {
                    temp = root.right;
                }
                else {
                    temp = root.left;
                }

                if (temp == null) {
                    temp = root;
                    root = null;
                }
                else {
                    root = temp;
                }
            }
            else {
                AVLNode temp = minValue(root.right);
                root.key = temp.key;
                root.right = deleteRec(root.right, temp.key);
            }
        }

        if (root == null) {
            return root;
        }

        root.height = Math.max(height(root.left), height(root.right)) + 1;

        int balance = getBalance(root);

        if (balance > 1 && getBalance(root.left) >= 0) {
            return rightRotate(root);
        }
        if (balance > 1 && getBalance(root.left) < 0) {
            root.left = leftRotate(root.left);
            return rightRotate(root);
        }
        if (balance < -1 && getBalance(root.right) <= 0) {
            return leftRotate(root);
        }
        if (balance < -1 && getBalance(root.right) > 0) {
            root.right = rightRotate(root.right);
            return leftRotate(root);
        }
        return root;
    }

    private AVLNode minValue(AVLNode root) {
        AVLNode current = root;
        while (current.left != null) {
            current = current.left;
        }
        return current;
    }

    public void inorderTraversal() {
        inorderTraversal(root);
    }

    private void inorderTraversal(AVLNode root) {
        if (root != null) {
            inorderTraversal(root.left);
            System.out.print(root.key + " ");
            inorderTraversal(root.right);
        }
    }

    public boolean search(int key) {
        return searchRec(root, key);
    }

    private boolean searchRec(AVLNode root, int key) {
        if (root == null) {
            return false;
        }

        if (key == root.key) {
            return true;
        }
        else if (key < root.key) {
            return searchRec(root.left, key);
        }
        else {
            return searchRec(root.right, key);
        }
    }

    public static void main(String[] args) {
        AvlTree avlTree = new AvlTree();

        // Inserting elements
        avlTree.insert(10);
        avlTree.insert(20);
        avlTree.insert(30);
        avlTree.insert(40);
        avlTree.insert(50);
        avlTree.insert(25);

        // Displaying the inorder traversal of the AVL tree
        System.out.println("Inorder Traversal:");
        avlTree.inorderTraversal();

        avlTree.delete(10);
        System.out.println("Inorder Traversal:");
        avlTree.inorderTraversal();
    }

    public int treeheight() {
        return root.height;
    }
}

class AVLNode {
    int key, height;
    AVLNode left, right;

    AVLNode(int key) {
        this.key = key;
        this.height = 1;
    }
}