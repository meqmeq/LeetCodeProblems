def removeDuplicates(s: str) -> str:

    # while 1:
    #     strCopy = ''
    #     strLen = len(s)
    #     isDup = False

    #     if len(s) == 1 or len(s) == 0:
    #         break

    #     if s[0] != s[1]:
    #         strCopy += s[0]

    #     for i in range(1, strLen - 1):

    #         if s[i] != s[i-1] and s[i] != s[i+1]:
    #             strCopy += s[i]
    #         else:
    #             isDup = True

    #     if s[strLen-1] != s[strLen - 2]:
    #         strCopy += s[strLen - 1]

    #     s = strCopy

    #     if isDup == False:
    #         break

    # return s

    while 1:
        strLen = len(s)
        removedDup = False

        if len(s) == 1 or len(s) == 0:
            break

        for i in range(0, strLen - 1):
            if s[i] == s[i+1]:
                if len(s) == 3:
                    s = s[2]
                    removedDup = False
                    break
                s = s[:i] + s[i+2:]
                removedDup = True
                break
            else:
                removedDup = False

        if removedDup == True:
            continue

        break

    return s


print(removeDuplicates("abbaca"))
