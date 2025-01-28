from task6a import *
import random
import string
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def test_uniformity(input_strings):
    """Test uniformity of hash distribution"""
    hash_values = [hash(s) for s in input_strings]

    # Calculate distribution
    distribution = Counter(hash_values)

    # Calculate chi-square statistic
    expected_freq = len(hash_values) / 256
    chi_square = sum((obs - expected_freq) ** 2 / expected_freq
                     for obs in distribution.values())

    # Degrees of freedom = number of possible values - 1
    df = 255

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


def test_avalanche(base_strings, num_modifications=100):
    """Test avalanche effect by making small changes to input"""
    results = []

    for base in base_strings:
        base_hash = hash(base)

        # Make small modifications and compare
        for _ in range(num_modifications):
            # Modify one random character
            pos = random.randint(0, len(base)-1)
            modified = base[:pos] + \
                random.choice(string.printable) + base[pos+1:]
            mod_hash = hash(modified)

            # Calculate bit difference
            bit_diff = bin(base_hash ^ mod_hash).count('1')
            results.append(bit_diff)

    # Visualize bit differences
    plt.figure(figsize=(10, 5))
    plt.hist(results, bins=range(9), align='left')
    plt.title('Distribution of Bit Changes in Hash Output')
    plt.xlabel('Number of Bits Changed')
    plt.ylabel('Frequency')
    plt.show()

    return {
        'avg_bits_changed': np.mean(results),
        'std_bits_changed': np.std(results),
        'total_tests': len(results)
    }

# Generate test data (since we don't have the actual files)


def generate_test_data(num_strings=100000, min_length=5, max_length=50):
    return [''.join(random.choices(string.printable, k=random.randint(min_length, max_length)))
            for _ in range(num_strings)]


def uniformity_data():
    pass


def avalanche_data():
    pass


# Run tests
print("Running uniformity tests...")
test_strings = generate_test_data()
uniformity_results = test_uniformity(test_strings)

print("\nUniformity Test Results:")
print(f"Total inputs: {uniformity_results['total_inputs']}")
print(f"Unique hash values: {uniformity_results['unique_values']}")
print(f"Chi-square statistic: {uniformity_results['chi_square']:.2f}")

print("\nRunning avalanche tests...")
avalanche_results = test_avalanche(test_strings[:10])

print("\nAvalanche Test Results:")
print(f"Average bits changed: {avalanche_results['avg_bits_changed']:.2f}")
print(f"Standard deviation: {avalanche_results['std_bits_changed']:.2f}")
print(f"Total tests: {avalanche_results['total_tests']}")
