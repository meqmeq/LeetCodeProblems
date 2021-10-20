def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    L = 0
    R = 0
    ans = []
    while R < len(s):
        if s[R] == ' ' or R == len(s)-1:
            cpy = ''
            if L == 0:
                # ans[:R-1] = s[R-1::-1]
                cpy = s[R::-1]
                print(ans)
            elif R == (len(s)-1):
                # ans[L:] = s[:L-1:-1]
                cpy = s[:L-1:-1]
            else:
                # ans[L:R+1] = s[R:L-1:-1]
                cpy = s[R-1:L-1:-1]
                print(ans)
            ans.append(cpy)
            if R != len(s)-1:
                ans.append(" ")
            print(ans)
            R += 1
            L = R
        elif s[R] != ' ':
            R += 1
    return "".join(ans)

# return " ".join(i[::-1] for i in s.split()) => Easiest answer LMAO


print(reverseWords("Let's take LeetCode contest"))
# print(reverseWords(
#     "hehhhhhhe"))
