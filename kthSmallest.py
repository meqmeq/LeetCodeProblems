import bisect


def kthSmallest(matrix, k):
    """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
    # oneD = []
    # for arr in matrix:
    #     oneD += arr

    # oneD = sorted(oneD)

    # return oneD[k-1]
    n = len(matrix)
    high, low = matrix[n-1][n-1], matrix[0][0]
    while low < high:
        cnt = 0
        mid = low + (high-low)//2
        for i in range(0, n):
            # cnt += bisect_right(matrix[i], mid)
            if cnt < k:
                low = mid+1
            else:
                high = mid
    return low


print(kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
