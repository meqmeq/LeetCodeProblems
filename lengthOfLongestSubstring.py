def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    L = 0
    R = 1
    maxSub = 0
    while R != len(s):
        d = s[L:R]
        if s[R] not in d:
            l = len(d)
            if maxSub < l:
                maxSub = l
            R += 1
        else:
            L += 1
    return maxSub


print(lengthOfLongestSubstring("abcabcbb"))
