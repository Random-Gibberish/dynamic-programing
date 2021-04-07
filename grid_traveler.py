
def grid_traveler(m, n):
    """ A slow grid traveler solution which returns
        an integer in O(2^(n+m)) time """

    if m == 1 or n == 1:        # Base cases
        return 1

    # Recursive calls
    result = grid_traveler(m-1, n) + grid_traveler(m, n-1)
    return result


def memo_grid_traveler(m, n, memo={}):
    """ A memoized solution which returns
        a dict value in O(mn) time """

    key = str(m) + ',' + str(n)  # dict keys
    if key in memo:              # Memoized base cases
        return memo[key]

    if m == 1 or n == 1:
        return 1

    # Store values to reduce recursive calls
    memo[key] = memo_grid_traveler(m-1, n) + memo_grid_traveler(m, n-1)
    return memo[key]


def tabd_grid_traveler(m, n):
    """ A tabulated solution which returns the
        value at arr[m][n] in O(mn) time """

    arr = [[0] * (n+1) for _ in range(m+1)]  # Initiate fixed solutions list
    arr[1][1] = 1                            # Base case

    for row in range(m+1):                # Adds 'current' value to neighbours
        for col in range(n+1):            # that have not yet been visited
            current = arr[row][col]
            if col < n:                   # Right-hand neighbour
                arr[row][col+1] += current
            if row < m:                   # Bottom neighbour
                arr[row+1][col] += current

    return arr[m][n]


if __name__ == '__main__':
    grids = [(1, 1), (2, 3), (3, 2), (3, 3), (18, 18)]

    for grid in grids:
        grid_row = int(grid[0])
        grid_col = int(grid[1])

        slow = grid_traveler(grid_row, grid_col)  # Too slow for large [m, n]
        print(slow)

        memo_grid = memo_grid_traveler(grid_row, grid_col, {})
        print(memo_grid)

        tab_grid = tabd_grid_traveler(grid_row, grid_col)
        print(tab_grid)
