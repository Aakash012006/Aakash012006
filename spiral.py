# i. Function to filter dictionary based on given keys
def filter_dict(input_dict, keys):
    return {key: input_dict[key] for key in keys if key in input_dict}

# ii. Function to print n x n matrix in spiral order
def print_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1

    while num <= n * n:
        # Traverse from left to right
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Traverse from right to left
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # Traverse from bottom to top
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    # Print the matrix
    for row in matrix:
        print(" ".join(map(str, row)))

# Test the functions
input_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
keys = ['a', 'c', 'e']
filtered_dict = filter_dict(input_dict, keys)
print(filtered_dict)

print("\nSpiral Matrix:")
n = 5
print_spiral_matrix(n)
