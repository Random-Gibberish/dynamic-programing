import time


def fib(n):
    """ Returns an integer in O(2^n) time """

    if n <= 2:      # Base cases
        return 1

    result = fib(n-1) + fib(n-2)    # Recursive call
    return result


def memo_fib(n, memo={}):
    """ Memoized fib solution. Returns a
        dict value in O(n) time """

    if n in memo:                   # Memoized base cases
        return memo[n]
    if n <= 2:
        return 1

    # Stores values to reduce recursive calls
    memo[n] = memo_fib(n-1, memo) + memo_fib(n-2, memo)
    return memo[n]


def tab_fib(n):
    """ Tabulated fib solution. Returns the
        last list value in O(n) time """

    arr = [0] * (n+1)   # Fixed length solutions list
    arr[1] = 1          # Base case

    for i in range(n+1):
        try:
            arr[i+1] += arr[i]  # Adds current value to the next
            arr[i+2] += arr[i]  # two positions in the list
        except IndexError:      # Catch index out of range errors
            pass

    return arr[n]


if __name__ == '__main__':
    list_n = [6, 7, 8, 40]

    for _ in list_n:

        # Original fib function
        start_time = time.time()
        fib_n = fib(_)              # Too slow for large n
        end_time = time.time()
        fib_time = end_time - start_time

        # Memoized fib function
        start_time = time.time()
        memo_fib_n = memo_fib(_)
        end_time = time.time()
        memo_time = end_time - start_time

        # Tabulated fib function
        start_time = time.time()
        tab_fib_n = tab_fib(_)
        end_time = time.time()
        tab_time = end_time - start_time

        # Results
        print(f'fib({_}) = {fib_n}')
        print('fib_time:  ', fib_time)
        print('memo_time: ', memo_time)
        print('tab_time:  ', tab_time, '\n')
