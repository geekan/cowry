class Solution:
    # @return a list of lists of integers
    def comb(self, lists, int_list, n, k, start):
        # print int_list
        if len(int_list) == k:
            lists.append(int_list[:])
            return
        for i in range(start, n):
            int_list += [i]
            self.comb(lists, int_list, n, k, i+1)
            int_list.pop()

    def combine(self, n, k):
        lists = []
        if k == 0:
            return []
        self.comb(lists, [], n+1, k, 1)
        return lists

print Solution().combine(0, 0)