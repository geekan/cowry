# NEED MODIFY FOR BETTER ANSWER
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        for i in A:
            if target == i:
                return True
        return False