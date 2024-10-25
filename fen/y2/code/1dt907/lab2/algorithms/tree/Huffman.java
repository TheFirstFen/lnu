package algorithms.tree;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class HuffmanNode implements Comparable<HuffmanNode> {
    char data;
    int freq;
    HuffmanNode l, r;

    public HuffmanNode(char data, int freq) {
        this.data = data;
        this.freq = freq;
        l = r = null;
    }

    @Override
    public int compareTo(HuffmanNode other) {
        return this.freq - other.freq;
    }
}

public class Huffman {
    private static Map<Character, String> huffmanCodes = new HashMap<>();

    public void run(Huffman huffman, String filePath) {
        try {
            String text = huffman.readFile(filePath);
            Map<Character, Integer> frequencyMap = huffman.calculateFrequency(text);
            HuffmanNode root = huffman.buildHuffmanTree(frequencyMap);
            huffman.generateHuffmanCodes(root, ""); // ! Not working properly
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
        Map<Character, Integer> frequencyMap = new HashMap<>();

        for (char c : text.toCharArray()) {
            frequencyMap.put(c, frequencyMap.getOrDefault(c, 0) + 1);
        }

        return frequencyMap;
    }

    private HuffmanNode buildHuffmanTree(Map<Character, Integer> frequencyMap) {
        PriorityQueue<HuffmanNode> pQueue = new PriorityQueue<>();

        for (Map.Entry<Character, Integer> entry : frequencyMap.entrySet()) {
            pQueue.add(new HuffmanNode(entry.getKey(), entry.getValue()));
        }

        while (pQueue.size() > 1) {
            HuffmanNode l = pQueue.poll();
            HuffmanNode r = pQueue.poll();
            HuffmanNode internalNode = new HuffmanNode('\0', l.freq + r.freq);
            internalNode.l = l;
            internalNode.r = r;
            pQueue.add(internalNode);
        }

        return pQueue.poll();
    }

    private void generateHuffmanCodes(HuffmanNode root, String code) {
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
