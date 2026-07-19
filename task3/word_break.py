def word_break_exists(s, word_dict):
    """Returns True if s can be segmented into dictionary words."""
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break  

    return dp[n]


def word_break_count(s, word_dict):
    """Returns the number of ways s can be segmented into dictionary words."""
    n = len(s)
    count = [0] * (n + 1)
    count[0] = 1  

    for i in range(1, n + 1):
        for j in range(i):
            if count[j] > 0 and s[j:i] in word_dict:
                count[i] += count[j]

    return count[n]


def word_break_all_ways(s, word_dict):
    """Returns all possible segmentations (for small strings, for demonstration)."""
    n = len(s)
    if not word_break_exists(s, word_dict):
        return []

    results = []

    def backtrack(start, path):
        if start == n:
            results.append(" ".join(path))
            return
        for end in range(start + 1, n + 1):
            word = s[start:end]
            if word in word_dict:
                path.append(word)
                backtrack(end, path)
                path.pop()

    backtrack(0, [])
    return results


if __name__ == "__main__":
    word_dict = {"cat", "cats", "and", "sand", "dog", "catsand", "catsanddog"}

    test1 = "catsanddog"
    print(f"'{test1}' segmentable? {word_break_exists(test1, word_dict)}")
    print(f"Number of ways: {word_break_count(test1, word_dict)}")
    print(f"All segmentations: {word_break_all_ways(test1, word_dict)}")

    test2 = "catsandog"  # should fail - "og" is not in the dictionary
    print(f"\n'{test2}' segmentable? {word_break_exists(test2, word_dict)}")
    print(f"Number of ways: {word_break_count(test2, word_dict)}")