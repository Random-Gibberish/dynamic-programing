import time


def memo_best_sum(target_sum, numbers, memo={}):
    """ Returns a 2D list of all possible ways to
        sum up to 'target_sum' in O(m^2 * n) time """

    if target_sum in memo:              # Memoized base cases
        return memo[target_sum]
    if target_sum == 0:                 # Base case
        return []
    if target_sum < 0:
        return None

    short_comb = None                   # Shortest combination

    # For each number subtract it from the target and
    # call recursively with the remainder as target_sum
    for num in numbers:
        remainder = target_sum - num
        remain_comb = memo_best_sum(remainder, numbers, memo)

        # Unpack remain_comb into a list to avoid nesting
        if remain_comb is not None:
            comb = [*remain_comb, num]
            if short_comb is None or len(comb) < len(short_comb):
                short_comb = comb       # Update shortest combination

    memo[target_sum] = short_comb
    return short_comb


def tab_best_sum(target_sum, numbers):
    """ Returns a 2D list of all possible ways to
        sum up to 'target_sum' in O(m^2 * n) time """

    arr = [None for _ in range(target_sum+1)]   # Default list of None
    arr[0] = []                                 # Empty list base case

    # For each index that isn't None move the current
    # list to the positions 'num' ahead for each number
    # and append 'num', the number used to reach that position
    for i in range(target_sum):
        if arr[i] is not None:
            for num in numbers:
                comb = [*arr[i], num]   # Unpack each path to avoid nesting
                try:                    # and add 'num' each to combination
                    if arr[i+num] is None or len(arr[i+num]) > len(comb):
                        arr[i+num] = comb   # Move comb to reachable indices
                except IndexError:
                    pass

    return arr[target_sum]


if __name__ == '__main__':
    target_sums = 7, 8, 8, 100
    all_numbers = [[5, 3, 4, 7],
                   [2, 3, 5],
                   [1, 4, 5],
                   [1, 2, 5, 25]]

    all_cases = list(zip(target_sums, all_numbers))

    for a_case in all_cases:

        # Memoized best_sum
        start_time = time.time()
        memo_best = memo_best_sum(a_case[0], a_case[1], {})
        end_time = time.time()
        memo_time = end_time - start_time

        # Tabulated best_sum
        start_time = time.time()
        tab_best = tab_best_sum(a_case[0], a_case[1])
        end_time = time.time()
        tab_time = end_time - start_time

        # Results
        print(f'What is the best way to sum up to {a_case[0]} using {a_case[1]}?')
        print(memo_best)
        print('memo_can: ', memo_time)
        print('tab_can:  ', tab_time, '\n')
