class Solution(object):
    def getSumAndCarry(self, a, b, c):
        binMap = {
            "000" : [0, 0],
            "001" : [1, 0],
            "010" : [1, 0],
            "011" : [0, 1],
            "100" : [1, 0],
            "101" : [0, 1],
            "110" : [0, 1],
            "111" : [1, 1]
        }
        return binMap[str(a)+str(b)+str(c)]
    
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        longestLen = max(len(a), len(b))
        carry = 0
        result = ""
        for i in range(-1, -1*longestLen-1, -1):
            aVal = 0
            bVal = 0
            
            try:
                aVal = a[i]
            except:
                pass

            try:
                bVal = b[i]
            except:
                pass
            
            sum, carry = self.getSumAndCarry(aVal, bVal, carry)
            result = str(sum) + result
        
        if carry == 1:
            result = str(carry) + result
        return result