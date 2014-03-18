class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if not s:
            return 0
        count = 0
        last = 0
        for i in range(len(s)):
            if s[i] == ' ':
                if count != 0:
                    last = count
                count = 0
            else:
                count += 1
        return count if s[-1] != ' ' else last

print Solution().lengthOfLastWord('b   a    ')