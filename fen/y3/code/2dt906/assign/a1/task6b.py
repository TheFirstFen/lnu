from task6a import *
import random
import string
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def read_file(filename):
    """Read lines from a file, stripping newline characters"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def test_uniformity(filename):
    """Test uniformity of hash distribution"""
    lines = read_file(filename)
    if not lines:
        return None

    hash_values = [hash(line) for line in lines]

    # Calculate distribution
    distribution = Counter(hash_values)

    # Calculate chi-square statistic
    expected_freq = len(hash_values) / 256
    chi_square = sum((obs - expected_freq) ** 2 / expected_freq
                     for obs in distribution.values())

    # Create visualization
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
        'total_inputs': len(hash_values)
    }


def test_avalanche(filename):
    """Test avalanche effect by making small changes to input"""
    lines = read_file(filename)
    if not lines:
        return None

    hash_changes = []

    for line in lines:
        if len(line) > 0:  # Ensure line is not empty
            # Get original hash
            original_hash = hash(line)

            # Modify one character and get new hash
            modified = line[:-1] + \
                chr((ord(line[-1]) + 1) % 128)  # Change last char
            modified_hash = hash(modified)

            # Calculate absolute difference in hash values
            hash_diff = abs(modified_hash - original_hash)
            hash_changes.append(hash_diff)

    # Create visualization of hash changes
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


def generate_test_data(num_strings=100000, min_length=5, max_length=50):
    return [''.join(random.choices(string.printable, k=random.randint(min_length, max_length)))
            for _ in range(num_strings)]


def main():
    print("Testing Uniformity...")
    uniformity_results = test_uniformity("./Uniformity_test.txt")
    if uniformity_results:
        print("\nUniformity Test Results:")
        print(f"Total inputs: {uniformity_results['total_inputs']}")
        print(f"Unique hash values: {uniformity_results['unique_values']}")
        print(f"Chi-square statistic: {uniformity_results['chi_square']:.2f}")

    print("\nTesting Avalanche Effect...")
    avalanche_results = test_avalanche("Avalanche_test.txt")
    if avalanche_results:
        print("\nAvalanche Test Results:")
        print(f"Average change in hash: {avalanche_results['avg_change']:.2f}")
        print(f"Standard deviation: {avalanche_results['std_change']:.2f}")
        print(f"Maximum change: {avalanche_results['max_change']}")
        print(f"Minimum change: {avalanche_results['min_change']}")
        print(f"Total tests: {avalanche_results['total_tests']}")


if __name__ == "__main__":
    main()
