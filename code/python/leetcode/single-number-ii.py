class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones = twos = threes = 0
        for i in A:
            twos |= (ones & i)
            ones ^= i
            threes = ~(ones & twos)
            ones &= threes
            twos &= threes
        return ones

print Solution().singleNumber([1,1,1,2,2,2,3,4,4,4])