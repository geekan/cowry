class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        l = [[1],]
        while len(l) < numRows:
            nrow = [1] + [0] * (len(l)-1) + [1]
            for i in range(1, len(nrow) - 1):
                # print i, nrow, l
                nrow[i] += l[-1][i-1] + l[-1][i]
            l.append(nrow)
        return l


print Solution().generate(10)