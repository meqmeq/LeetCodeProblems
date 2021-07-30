
def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """

    coins = sorted(coins)
    initList = [amount+1] * (amount + 1)

    initList[0] = 0

    for i in range(1, len(initList)):
        for coin in coins[::-1]:
            if (i - coin) >= 0:
                if initList[i-coin] == -1:
                    initList[i] = -1
                else:
                    initList[i] = initList[i-coin] + 1

                    break
            elif coin == coins[0] and i-coin < 0:
                initList[i] = -1

    return initList[amount]


print(coinChange(
    [186, 419, 83, 408], 6249))
