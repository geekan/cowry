class Solution:
    roman_dict = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    def intToRoman(self, num):
        for kv in self.roman_dict:
            if kv[0] <= num:
                return kv[1] + self.intToRoman(num - kv[0])
        return ''

# 1884
s = [1, 90, 99, 3999]
print [Solution().intToRoman(i) for i in s]