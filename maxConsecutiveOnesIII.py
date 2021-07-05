def longestOnes(nums: list[int], k: int) -> int:
    # maxConsecs = 0

    # for i in range(0, len(nums)):

    #     numZeros = 0
    #     numConsecs = 0

    #     for j in range(i, len(nums)):
    #         if nums[j] == 0 and numZeros < k:
    #             numZeros += 1
    #             numConsecs += 1
    #         elif nums[j] == 1:
    #             numConsecs += 1
    #         else:
    #             break

    #         if numConsecs > maxConsecs:
    #             maxConsecs = numConsecs

    # return maxConsecs

    maxConsecs, numZeros, windowStart = 0, 0, 0

    for i in range(0, len(nums)):

        if nums[i] == 0 and numZeros <= k:
            numZeros += 1
        if numZeros > k:
            while numZeros > k:
                if nums[windowStart] == 0:
                    numZeros -= 1

                windowStart += 1

        maxConsecs = max(len(nums[windowStart: i+1]), maxConsecs)

    return maxConsecs


ans = longestOnes([0, 0, 1, 1, 0, 0, 1, 1,
                   1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3)

print(f"The answer is {ans}")
