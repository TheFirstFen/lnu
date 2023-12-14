package algorithms.tree;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class Huffman {
    class Node implements Comparable<Node> {
        char data;
        int freq;
        Node l, r;

        public Node(char data, int freq) {
            this.data = data;
            this.freq = freq;
            l = r = null;
        }

        @Override
        public int compareTo(Node other) {
            return this.freq - other.freq;
        }
    }

    private static Map<Character, String> huffmanCodes = new HashMap<>();

    public void run(Huffman huffman, String filePath) {
        try {
            String text = huffman.readFile(filePath);
            Map<Character, Integer> freqMap = huffman.calculateFrequency(text);
            Node root = huffman.buildHuffmanTree(freqMap);
            huffman.generateHuffmanCodes(root, "");
            huffman.displayHuffmanCodes();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private String readFile(String filePath) throws IOException {
        StringBuilder c = new StringBuilder();

        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                c.append(line).append("\n");
            }
        }

        return c.toString();
    }

    private Map<Character, Integer> calculateFrequency(String text) {
        Map<Character, Integer> freqMap = new HashMap<>();

        for (char c : text.toCharArray()) {
            freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);
        }

        return freqMap;
    }

    private Node buildHuffmanTree(Map<Character, Integer> freqMap) {
        PriorityQueue<Node> pQueue = new PriorityQueue<>();

        for (Map.Entry<Character, Integer> entry : freqMap.entrySet()) {
            pQueue.add(new Node(entry.getKey(), entry.getValue()));
        }

        while (pQueue.size() > 1) {
            Node l = pQueue.poll();
            Node r = pQueue.poll();
            Node internalNode = new Node('\0', l.freq + r.freq);
            internalNode.l = l;
            internalNode.r = r;
            pQueue.add(internalNode);
        }

        return pQueue.poll();
    }

    private void generateHuffmanCodes(Node root, String code) {
        if (root == null) {
            return;
        }

        if (root.data != '\0') {
            huffmanCodes.put(root.data, code);
        }

        generateHuffmanCodes(root.l, code + "0");
        generateHuffmanCodes(root.r, code + "1");
    }

    private void displayHuffmanCodes() {
        System.out.println("Huffman Codes:");

        for (Map.Entry<Character, String> entry : huffmanCodes.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
