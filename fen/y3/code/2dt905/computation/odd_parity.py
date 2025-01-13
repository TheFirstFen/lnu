# Function to compute odd parity for each row in the matrix
def compute_odd_parity(matrix):
    row_parity_results = []

    for row in matrix:
        # Count the number of 1s in the binary string
        count_of_ones = row.count('1')

        # Check odd or even parity
        parity = 1 if count_of_ones % 2 == 0 else 0

        # Append parity to the result list
        row_parity_results.append(parity)

    return row_parity_results

# Function to compute odd parity for each column in the matrix
def compute_column_parity(matrix):
    # Transpose the matrix to get columns as rows
    transposed_matrix = ["".join(row[i] for row in matrix) for i in range(len(matrix[0]))]

    column_parity_results = []

    for column in transposed_matrix:
        # Count the number of 1s in the binary string
        count_of_ones = column.count('1')

        # Check odd or even parity
        parity = 1 if count_of_ones % 2 == 0 else 0

        # Append parity to the result list
        column_parity_results.append(parity)

    return column_parity_results

# Example matrix
matrix = ["1001101", "1111010", "0011101", "1010101"]

# Compute odd parity for rows
row_parity_results = compute_odd_parity(matrix)

# Compute odd parity for columns
column_parity_results = compute_column_parity(matrix)

# Output the results
print("Row Parity:")
for row, parity in zip(matrix, row_parity_results):
    print(f"Row: {row}, Odd Parity: {parity}")

print("\nColumn Parity:")
for i, parity in enumerate(column_parity_results):
    print(f"Column {i}: Odd Parity: {parity}")

