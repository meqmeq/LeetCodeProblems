def isIsomorphic(s, t):
    """ls
    :type s: str
    :type t: str
    :rtype: bool
    """

    dictionary = dict(zip(list(s),list(t)))

    if len(set(dictionary.values())) != len(dictionary.values()):
        return False
    word = ''
    for i in s:
        word += dictionary[i]

    print(dictionary,word)
    return word == t

print(isIsomorphic("badc","baba"))