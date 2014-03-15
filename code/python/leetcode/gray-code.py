# http://en.wikipedia.org/wiki/Gray_code
class Solution:
    # @return a list of integers
    def grayCode(self, n):
        li = []
        size = 1 << n
        for i in range(size):
            li.append((i >> 1) ^ i)
        return li

'''
00 - 0
01 - 1
11 - 3
10 - 2

000 - 0 000 0
001 - 1 001 1
011 - 3 010 2
010 - 2 011 3
110 - 6 100 4
111 - 7 101 5
101 - 5 110 6
100 - 4 111 7
'''

print Solution().grayCode(2)
print Solution().grayCode(3)