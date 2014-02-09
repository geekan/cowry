def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                #nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        plist = []
        for i in all_perms(num):
            plist.append(i)
        return plist

s = Solution()
print s.permute([1,2,3,4])