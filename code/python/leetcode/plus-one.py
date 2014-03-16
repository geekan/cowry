class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        n = len(digits)
        csum = 1
        for i in reversed(range(n)):
            digits[i] += csum
            if digits[i] >= 10:
                csum = digits[i] / 10
                digits[i] -= (digits[i] / 10) * 10
            else:
                csum = 0
            if i == 0 and csum > 0:
                digits.insert(0, csum)
        return digits