# http://jane4532.blogspot.com/2013/07/generate-parenthesisleetcode.html
# µ›πÈ£¨œ»top down£¨‘Ÿbottom up
class Solution:
    # @param an integer
    # @return a list of string

    def gen(self, n, left, right, brackets):
        # print n, left, right, "".join(brackets)
        if left == right == n:
            self.lstr.append("".join(brackets))
            return
        if left < n:
            brackets[left+right] = '('
            self.gen(n, left+1, right, brackets)
        if left > right:
            brackets[left+right] = ')'
            self.gen(n, left, right+1, brackets)
    
    def generateParenthesis(self, n):
        self.lstr = []
        self.gen(n, 0, 0, ['']*2*n)
        return self.lstr

print Solution().generateParenthesis(3)