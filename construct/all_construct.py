
def memo_all_construct(target, word_bank, memo={}):
    """ Returns all possible ways of forming 'target' from
        the 'word_bank' as a 2D list in O(n^m) time """

    if target in memo:              # Memoized base cases
        return memo[target]
    if target == '':                # Base case
        return [[]]

    result = []

    for word in word_bank:
        if target.startswith(word):             # If target starts with 'word'
            suffix = target.removeprefix(word)  # slice out 'word

            # Call recursively with 'suffix' as the new 'target'
            suffix_ways = memo_all_construct(suffix, word_bank, memo)
            # Unpack to avoid nesting and concatenate
            target_ways = [[word] + _ for _ in suffix_ways]
            result += target_ways   # Add combination to results

    memo[target] = result
    return result


def tab_all_construct(target, word_bank):
    """ Returns all possible ways of forming 'target' from
        the 'word_bank' as a 2D list in O(n^m) time """

    arr = [[] for _ in range(len(target)+1)]    # Default empty lists
    # Base case, a list containing the single
    # way [None] of forming the empty string ''
    arr[0] = [[]]

    for i in range(len(target)):
        for word in word_bank:

            # If the word matches the characters starting at index i
            # unpack the words used to reach the slice of 'target'
            # and add the next word
            if target[i:i+len(word)] == word:
                combs = [[*way, word] for way in arr[i]]
                arr[i+len(word)] += combs   # Move combs to its index in arr

    return arr[len(target)]


if __name__ == '__main__':
    targets = 'purple', 'abcdef', 'skateboard'
    word_banks = [['purp', 'p', 'ur', 'le', 'purpl'],
                  ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'],
                  ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'],
                  ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']]

    all_constructs = list(zip(targets, word_banks))

    for construct in all_constructs:
        memo_all = memo_all_construct(construct[0], construct[1])
        print(memo_all)

        tab_all = tab_all_construct(construct[0], construct[1])
        print(tab_all)
