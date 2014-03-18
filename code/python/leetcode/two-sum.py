class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        num_dict = {}
        for i in range(len(num)):
            k = num[i]
            t = target - k
            if t in num_dict and num_dict[t] < i+1:
                return (num_dict[t], i+1)
            else:
                num_dict.update({k:(i+1)})

n1 = [0,4,3,0]
n2 = [1,3,10,100,200]
target = 0
print [Solution().twoSum(num, target) for num in (n1, n2)]