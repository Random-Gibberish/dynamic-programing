
def memo_how_sum(target_sum, numbers, memo={}):
    """ Returns the first list that sums up
        to 'target_sum' in O(m^2 * n) time """

    if target_sum in memo:      # Memoized base cases
        return memo[target_sum]
    if target_sum == 0:         # Base case
        return []
    if target_sum < 0:
        print('target_sum must be positive')
        return None

    # For each number subtract it from the target and
    # call recursively with the remainder as target_sum
    for num in numbers:
        remainder = target_sum - num
        remainder_result = memo_how_sum(remainder, numbers, memo)

        if remainder_result is not None:                 # If reachable, add
            memo[target_sum] = [*remainder_result, num]  # it to the memo
            return memo[target_sum]

    memo[target_sum] = None
    return None


def tab_how_sum(target_sum, numbers):
    """ Returns the first list that sums up
        to 'target_sum' in O(m^2 * n) time """

    arr = [None for _ in range(target_sum+1)]   # Default list of None
    arr[0] = []                                 # Empty list base case

    # For each index that isn't None move the current
    # list to the positions 'num' ahead for each number
    # and append 'num', the number used to reach that position
    for i in range(target_sum):
        if arr[i] is not None:
            for num in numbers:
                if i+num < len(arr):
                    arr[i+num] = [*arr[i]]
                    arr[i+num].append(num)

    return arr[target_sum]


if __name__ == '__main__':
    target_sums = 7, 7, 7, 8, 300
    all_numbers = [[2, 3],
                   [5, 3, 4, 7],
                   [2, 4],
                   [2, 3, 5],
                   [7, 14]]

    all_cases = list(zip(target_sums, all_numbers))

    for a_case in all_cases:
        memo_how = memo_how_sum(a_case[0], a_case[1], {})
        print(memo_how)

        tab_how = tab_how_sum(a_case[0], a_case[1])
        print(tab_how)
