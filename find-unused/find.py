"""
Find the unused n-letter combination inside the search string

This is slow (can exceed time limit), but works (until it exceeds time limit)
"""

def main():
    letters = set(input())
    combination_len = int(input())
    search_str = input()

    combinations = []
    genCombinations(letters, "", combinations, combination_len)

    for i in range(len(search_str) - combination_len + 1):
        combination = search_str[i:i + combination_len]
        if combination in combinations:
            combinations.remove(combination)

    print(min(combinations))

def genCombinations(letters, combination, combination_store, target_len):
    if len(combination) == target_len:
        combination_store.append(combination)
        return

    for l in letters:
        genCombinations(letters, combination + l, combination_store, target_len)

if __name__ == "__main__":
    main()
