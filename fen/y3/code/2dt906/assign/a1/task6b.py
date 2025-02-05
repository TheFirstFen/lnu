# Author: Samuel Berg
# Date: 2025-01-30
# For: Task 6b in Assignment 1 in course 2DT906 at LNU
# Completion: Done!

from task6a import *
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def read_file(filename: str) -> list:
    """
    Read lines from a file, stripping newline characters
    Args:
        filename (str): The name of the file to read
    Returns:
        list: List of lines from the file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def test_uniformity(filename: str) -> dict:
    """
    Test uniformity of hash distribution
    Args:
        filename (str): The name of the file to read
    Returns:
        dict: Results of the uniformity test
    """
    lines = read_file(filename)
    if not lines:
        return None

    hash_values = [my_hash(line) % 256 for line in lines if line]

    distribution = Counter(hash_values)

    # Computes the chi-square statistic
    expected_freq = len(hash_values) / 256
    chi_square = sum((obs - expected_freq) ** 2 / expected_freq
                     for obs in distribution.values())

    plt.figure(figsize=(15, 5))
    plt.bar(distribution.keys(), distribution.values())
    plt.title('Distribution of Hash Values')
    plt.xlabel('Hash Value')
    plt.ylabel('Frequency')
    plt.show()

    return {
        'chi_square': chi_square,
        'distribution': distribution,
        'unique_values': len(distribution),
        'total_inputs': len(hash_values),
        'avg_distribution': np.mean(list(distribution.values()))
    }


def test_avalanche(filename: str) -> dict:
    """
    Test avalanche effect by making small changes to input
    Args:
        filename (str): The name of the file to read
    Returns:
        dict: Results of the avalanche test
    """
    lines = read_file(filename)
    if not lines:
        return None

    hash_changes = []

    for i, line in enumerate(lines):
        if len(line) > 0 and i + 1 < len(lines):
            original_hash = my_hash(line) % 256
            modified_hash = my_hash(lines[i+1]) % 256

            hash_diff = abs(modified_hash - original_hash)
            hash_changes.append(hash_diff)

    changes_count = Counter(hash_changes)

    plt.figure(figsize=(15, 5))
    x_values = sorted(changes_count.keys())
    y_values = [changes_count[x] for x in x_values]

    plt.bar(x_values, y_values)
    plt.title('Distribution of Changes in Hash Values')
    plt.xlabel('Change in Hash Value')
    plt.ylabel('Number of Strings')
    plt.grid(True, alpha=0.3)
    plt.show()

    return {
        'avg_change': np.mean(hash_changes),
        'std_change': np.std(hash_changes),
        'max_change': max(hash_changes),
        'min_change': min(hash_changes),
        'total_tests': len(hash_changes)
    }


def main():
    print("Testing Uniformity...")
    uniformity_results = test_uniformity("./data/task6/Uniformity_test.txt")
    if uniformity_results:
        print("\nUniformity Test Results:")
        print(f"Total inputs: {uniformity_results['total_inputs']}")
        print(f"Unique hash values: {uniformity_results['unique_values']}")
        print(f"Chi-square statistic: {uniformity_results['chi_square']:.2f}")
        print(f"Average distribution: {
              uniformity_results['avg_distribution']:.2f}")

    print("\nTesting Avalanche Effect...")
    avalanche_results = test_avalanche("./data/task6/Avalanche_test.txt")
    if avalanche_results:
        print("\nAvalanche Test Results:")
        print(f"Average change in hash: {avalanche_results['avg_change']:.2f}")
        print(f"Standard deviation: {avalanche_results['std_change']:.2f}")
        print(f"Maximum change: {avalanche_results['max_change']}")
        print(f"Minimum change: {avalanche_results['min_change']}")
        print(f"Total tests: {avalanche_results['total_tests']}")


if __name__ == "__main__":
    main()
