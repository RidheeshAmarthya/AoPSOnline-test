def solve_pyramid(pyramid, target):
    n = len(pyramid)
    result = []

    # Recursive function to perform DFS
    def dfs(row, col, product, path):
        # If we've reached the last row, check if the product matches the target
        if row == n - 1:
            if product == target:
                result.append(path)
            return

        # Move to the next row (left child) if in bounds
        if col < len(pyramid[row + 1]):
            dfs(row + 1, col, product * pyramid[row + 1][col], path + 'L')
        # Move to the next row (right child) if in bounds
        if col + 1 < len(pyramid[row + 1]):
            dfs(row + 1, col + 1, product * pyramid[row + 1][col + 1], path + 'R')

    # Start DFS from the top of the pyramid
    dfs(0, 0, pyramid[0][0], '')

    # Return the first result found, or an indication that no solution exists
    return result[0] if result else "No solution"


# List of sample test cases
test_cases = [
    {
        "pyramid": [
            [1],
            [2, 3],
            [4, 1, 1]
        ],
        "target": 2,
    },
    {
        "pyramid": [
            [2],
            [4, 3],
            [3, 2, 6],
            [2, 9, 5, 2],
            [10, 5, 2, 15, 5]
        ],
        "target": 720,
    },
    {
        "pyramid": [
                [3],
              [1, 2],
             [4, 6, 8],
            [2, 1, 2, 3]
        ],
        "target": 24,
    },
    {
        "pyramid": [
              [5],
             [2, 3],
            [4, 2, 6]
        ],
        "target": 60,
    },
    {
        "pyramid": [
            [7],
            [3, 5],
            [8, 6, 4],
            [5, 9, 2, 7]
        ],
        "target": 1260,
    },
    {
        "pyramid": [
            [4],
            [1, 2],
            [3, 5, 9],
            [7, 8, 2, 4]
        ],
        "target": 84,
    }
]

# Run test cases
for index, test in enumerate(test_cases):
    pyramid = test["pyramid"]
    target = test["target"]
    result = solve_pyramid(pyramid, target)
    print(f"Test Case {index + 1}:")
    print(f"Pyramid: {pyramid}")
    print(f"Target: {target}")
    print(f"Output: {result}")

