
def memo_can_sum(target_sum, numbers, memo={}):
    """ Returns a boolean value depending on whether
        or not it is possible to sum up to the target
        value in O(mn) time """

    if target_sum in memo:              # Memoized base cases
        return memo[target_sum]
    if target_sum == 0:                 # Base case
        return True
    if target_sum < 0:
        print('target_sum must be positive')
        return False

    for num in numbers:                 # For each number subtract it
        remainder = target_sum - num    # from 'target_sum'

        # Repeat for each remainder and if true return True
        if memo_can_sum(remainder, numbers, memo):
            memo[target_sum] = True
            return True

    memo[target_sum] = False    # Store False in memo and continue until True
    return False


def tab_can_sum(remainder, numbers):
    """ Returns the boolean value at the final
        position of the list in O(mn) time """

    arr = [False] * (remainder+1)       # Create default False list
    arr[0] = True                       # Set base case to True

    # From each True (i.e. reachable) value determine the
    # next True values. Continue until list is full
    for i in range(remainder):
        if arr[i]:
            for num in numbers:
                if i+num < len(arr):
                    arr[i+num] = True

    return arr[remainder]


if __name__ == '__main__':
    target_sums = 7, 7, 7, 8, 300
    all_numbers = [[2, 3],
                   [5, 3, 4, 7],
                   [2, 4],
                   [2, 3, 5],
                   [7, 14]]

    all_cases = list(zip(target_sums, all_numbers))

    for a_case in all_cases:
        memo_can = memo_can_sum(a_case[0], a_case[1], {})
        print(memo_can)

        tab_can = tab_can_sum(a_case[0], a_case[1])
        print(tab_can)
