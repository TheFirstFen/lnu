package algorithms;

public class Percolation {
    private boolean[][] grid;
    private PCWQUnionFind uf;
    private int gridSize;
    public int openSites;

    public Percolation(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException("Grid can not be less then 0");
        }

        gridSize = n;
        grid = new boolean[n][n];
        uf = new PCWQUnionFind(n * n + 2);
        openSites = 0;
    }

    public void open(int row, int col) {
        validateIndices(row, col);

        if (!grid[row - 1][col - 1]) {
            grid[row - 1][col - 1] = true;
            openSites++;

            connectWithNeighbors(row, col);
        }
    }

    public boolean isOpen(int row, int col) {
        validateIndices(row, col);
        return grid[row - 1][col - 1];
    }

    public boolean isFull(int row, int col) {
        validateIndices(row, col);
        return isOpen(row, col) && uf.find(getIndex(row, col)) == uf.find(0);
    }

    public boolean percolates() {
        return uf.find(0) == uf.find(gridSize * gridSize + 1);
    }

    private void connectWithNeighbors(int row, int col) {
        int index = getIndex(row, col);

        if (row > 1 && isOpen(row - 1, col)) {
            uf.union(index, getIndex(row - 1, col));
        }

        if (row < gridSize && isOpen(row + 1, col)) {
            uf.union(index, getIndex(row + 1, col));
        }

        if (col > 1 && isOpen(row, col - 1)) {
            uf.union(index, getIndex(row, col - 1));
        }

        if (col < gridSize && isOpen(row, col + 1)) {
            uf.union(index, getIndex(row, col + 1));
        }

        if (row == 1) {
            uf.union(index, 0);
        }

        if (row == gridSize) {
            uf.union(index, gridSize * gridSize + 1);
        }
    }

    private int getIndex(int row, int col) {
        return (row - 1) * gridSize + col;
    }

    private void validateIndices(int row, int col) {
        if (row < 1 || row > gridSize || col < 1 || col > gridSize) {
            throw new IllegalArgumentException("Invalid row or column");
        }
    }
}
