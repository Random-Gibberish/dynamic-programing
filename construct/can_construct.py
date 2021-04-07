
def memo_can_construct(target, word_bank, memo={}):
    """ Returns a boolean value depending on whether 'target'
        'word' can be formed from the 'word_bank' in O(m^2 * n) time """

    if target in memo:                  # Memoized base cases
        return memo[target]
    if target == '':                    # Base case
        return True

    for word in word_bank:
        if target.startswith(word):             # If target starts with 'word'
            suffix = target.removeprefix(word)  # slice out 'word'

            # Call recursively with 'suffix' as the new 'target'
            if memo_can_construct(suffix, word_bank, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False


def tabulated_can_construct(target, word_bank):
    """ Returns a boolean value depending on whether target
        'word' can be formed from the word_bank in O(m^2 * n) time """

    arr = [False for _ in range(len(target)+1)]     # Default False list
    arr[0] = True                                   # Set base case to True

    # From each True (i.e. reachable) word determine the
    # next True words. Continue until list is full
    for i in range(len(target)+1):
        if arr[i]:
            for word in word_bank:

                # If the word matches the characters starting at index i
                if target[i:i+len(word)] == word:
                    arr[i+len(word)] = True

    return arr[len(target)]


if __name__ == '__main__':
    targets = ('abcdef', 'skateboard', 'enterapotentpot',
               'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef')

    word_banks = [['ab', 'abc', 'cd', 'def', 'abcd'],
                  ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'],
                  ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'],
                  ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']]

    all_constructs = list(zip(targets, word_banks))

    for construct in all_constructs:
        memo_can = memo_can_construct(construct[0], construct[1])
        print(memo_can)

        tab_can = tabulated_can_construct(construct[0], construct[1])
        print(tab_can)
