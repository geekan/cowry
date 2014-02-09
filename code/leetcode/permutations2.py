def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

def unique(iter):
    s = set()
    for i in iter:
        if i in s:
            continue
        else:
            s.add(i)
    return list(s)

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        return unique(all_perms(num))

s = Solution()
print s.permute([1,2,3,4])