
class Solution:
    # @return an integer
    def reverse(self, x):
        if len(str(x)) == 1:
            return x
        if x < 0:
            return -int(str(-x)[::-1])
        else:
            return int(str(x)[::-1])

x = 123
# print Solution().reverse(x)
print Solution().reverse(-x)
