class Solution:
    def climbStairs(self, n: int) -> int:
        # one, two = 1, 1

        # for i in range(n-1):
        #     temp = one
        #     one = one + two
        #     two = temp

        # return one

        # True DP (Bottom Up)
        if n <= 2:
            return n
    
        first, second = 1, 2
        for _ in range(3, n+1):
            first, second = second, first + second
        
        return second
        
        