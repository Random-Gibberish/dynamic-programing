import time


def memo_count_construct(target, word_bank, memo={}):
    """ Returns the numbers of ways 'target' can be
        formed from the 'word_bank' in O(m^2 * n) time """

    if target in memo:          # Memoized based cases
        return memo[target]
    if target == '':            # Base case
        return 1

    total_count = 0

    for word in word_bank:
        if target.startswith(word):             # If target starts with 'word'
            suffix = target.removeprefix(word)  # slice out 'word'

            # Call recursively with 'suffix' as the new 'target'
            num_ways_for_rest = memo_count_construct(suffix, word_bank, memo)
            total_count += num_ways_for_rest

    memo[target] = total_count
    return total_count


def tab_count_construct(target, word_bank):
    """ Returns the numbers of ways 'target' can be
        formed from the 'word_bank' in O(m^2 * n) time """

    arr = [0 for _ in range(len(target)+1)]     # Default 0 ways
    arr[0] = 1                                  # Base case

    for i in range(len(target)):
        for word in word_bank:

            # If the word matches the characters starting at index i
            # add the number of ways to reach arr[i] to arr[i+len(word)]
            if target[i:i+len(word)] == word:
                arr[i+len(word)] += arr[i]

    return arr[len(target)]


if __name__ == '__main__':
    targets = ('purple', 'abcdef', 'skateboard',
               'enterapotentpot', 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef')

    word_banks = [['purp', 'p', 'ur', 'le', 'purpl'],
                  ['ab', 'abc', 'cd', 'def', 'abcd'],
                  ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'],
                  ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'],
                  ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']]

    all_constructs = list(zip(targets, word_banks))

    for construct in all_constructs:

        # Memoized can_construct
        start_time = time.time()
        memo_count = memo_count_construct(construct[0], construct[1])
        end_time = time.time()
        memo_time = end_time - start_time

        # Tabulated can_construct
        start_time = time.time()
        tab_count = tab_count_construct(construct[0], construct[1])
        end_time = time.time()
        tab_time = end_time - start_time

        # Results
        print(f'How many ways can you form {construct[0]} using {construct[1]}?')
        print(memo_count)
        print('memo_count: ', memo_time)
        print('tab_count:  ', tab_time, '\n')
