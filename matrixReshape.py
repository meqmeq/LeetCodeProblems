def matrixReshape(mat, r, c):
    """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
    oneDMat = []
    answer = []
    for i in mat:
        for j in i:
            oneDMat.append(j)

    if len(oneDMat) % r == 0 and len(oneDMat) % r % c == 0:
        sizeOfRow = len(oneDMat) / r
        tempList = []
        for i in range(len(oneDMat)):
            tempList.append(oneDMat[i])
            if len(tempList) == sizeOfRow and len(tempList) != 0:
                answer.append(tempList)
                tempList = []

        return answer
    else:
        return mat


print(matrixReshape([[1, 2], [3, 4]], 1, 4))
