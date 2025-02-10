import matplotlib.pyplot as plt
import numpy as np
from T6a import hash
from collections import Counter

def file_reader(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]
    
def uniformity_test(file_name):
    text = file_reader(file_name)

    hash_values = [hash(line) for line in text if line]
    distribution = Counter(hash_values)
    
    plt.figure(figsize=(20, 10))
    plt.bar(distribution.keys(), distribution.values())
    plt.title('Distribution of Hash Values')
    plt.xlabel('Hash Value')
    plt.ylabel('Frequency')
    plt.show()

    return {
        'unique_values': len(distribution),
        'total_inputs': len(hash_values),
        'avg_distribution': np.mean(list(distribution.values()))
    }

def test_avalanche(file_name):
    text = file_reader(file_name)

    hash_changes = []

    for i, line in enumerate(text):
        if len(line) > 0 and i + 1 < len(text):
            original_hash = hash(line)
            modified_hash = hash(text[i + 1])

            hash_diff = abs(modified_hash - original_hash)
            hash_changes.append(hash_diff)
    
    change_count = Counter(hash_changes)

    plt.figure(figsize=(20, 10))
    x_values = sorted(change_count.keys())
    y_values = [change_count[x] for x in x_values]

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
    }

def main():
    print("Testing Uniformity...")
    uniformity_results = uniformity_test("../Data/Uniformity_test.txt")
    if uniformity_results:
        print("\nUniformity Test Results:")
        print(f"Total inputs: {uniformity_results['total_inputs']}")
        print(f"Unique hash values: {uniformity_results['unique_values']}")
        print(f"Average distribution: {uniformity_results['avg_distribution']:.0f}")

    print("\nTesting Avalanche Effect...")
    avalanche_results = test_avalanche("../Data/Avalanche_test.txt")
    if avalanche_results:
        print("\nAvalanche Test Results:")
        print(f"Average change in hash: {avalanche_results['avg_change']:.0f}")
        print(f"Standard deviation: {avalanche_results['std_change']:.0f}")
        print(f"Maximum change: {avalanche_results['max_change']}")
        print(f"Minimum change: {avalanche_results['min_change']}")


if __name__ == "__main__":
    main()