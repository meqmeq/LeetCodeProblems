class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.data.append(num)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.data) == 1:
            return self.data[0]
        elif sum(self.data) % 2 != 0:
            return sum(self.data)/2.0
        else:
            return self.data[len(self.data)/2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
