class Solution(object):

    __RANGE_MIN = 2**31 * -1
    __RANGE_MAX = 2**31 - 1
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        num = x
        if num < 0:
            num *= -1
            
        reversedNum = 0
        
        while num != 0:
            reversedNum = reversedNum * 10 + num % 10
            num /= 10
            
        reversedNum = reversedNum * -1 if x < 0 else reversedNum
        
        if reversedNum < self.__RANGE_MIN or self.__RANGE_MAX < reversedNum:
            return 0
        else:
            return reversedNum


test = Solution()

print(test.reverse(1534236469))
