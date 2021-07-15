def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    # Recursion inneficient
    if len(s) == 0:
        return True
    elif len(s) % 2 == 0:
        for i in range(len(s)-1):
            if (s[i] == '{' and s[i+1] == '}') or (s[i] == '[' and s[i+1] == ']') or (s[i] == '(' and s[i+1] == ')'):
                s = s[:i] + s[i+2:]
                return isValid(s)

    else:
        return False


print(isValid("{[]}"))
