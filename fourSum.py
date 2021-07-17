def fourSum(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

    # Only 188/238 attempts
    # n = len(nums)
    # ans = []
    # for i in range(0, n-3):
    #     for j in range(i+1, n-2):
    #         for k in range(j+1, n-1):
    #             for l in range(k+1, n):
    #                 if nums[i] + nums[j] + nums[k] + nums[l] == target:
    #
    #                     temp = [nums[i], nums[j], nums[k], nums[l]]
    #                     if temp not in ans:
    #                         ans.append(temp)

    # return ans
    """
    Below was my attempt to do 4sum with 1 while loop. After looking at the solution I needed 2 
    """
    # n = len(nums)
    # ans = []
    # nums = sorted(nums)

    # tmpList = []
    # for i in range(len(nums)-3):
    #     tmpList = []
    #     L = i + 1
    #     R = n - 1
    #     while L != R:

    #         if tmpList == []:
    #             tmpList.append(nums[i])
    #             tmpList.append(nums[L])
    #             tmpList.append(nums[R])
    #         elif len(tmpList) < 4:
    #             if sum(tmpList) + nums[R-1] <= target:
    #                 R -= 1
    #                 tmpList.append(nums[R])
    #             elif sum(tmpList) + nums[L+1] <= target:
    #                 L += 1
    #                 tmpList.append(nums[L])
    #             else:
    #                 tmpList = []
    #                 R -= 1
    #         elif len(tmpList) == 4 and sum(tmpList) == target and tmpList not in ans and L != R:

    #             ans.append(tmpList)
    #             tmpList = []
    #             L += 1
    #             R = n - 1
    #         else:

    #             if sum(tmpList) < target:
    #                 L += 1
    #                 R = n-1
    #             else:
    #                 L = i+1
    #                 R -= 1

    #             tmpList = []

    # return ans
    """
    Attemp after looking at the solution
    """
    n = len(nums)
    ans = []
    nums = sorted(nums)

    for i in range(0, n - 3):
        for j in range(i+1, n - 2):
            t = target - nums[j] - nums[i]
            R = n - 1
            L = j + 1

            while (R > L):
                if nums[R] + nums[L] == t:
                    if [nums[i], nums[j], nums[L], nums[R]] not in ans:
                        ans.append([nums[i], nums[j], nums[L], nums[R]])
                    third = nums[L]
                    fourth = nums[R]
                    while L < R and nums[L] == third:
                        L += 1
                    while L < R and nums[R] == fourth:
                        R -= 1
                elif nums[R] + nums[L] > t:
                    R -= 1
                else:
                    L += 1

    return ans


print(fourSum([2, 2, 2, 2, 2], 8))
