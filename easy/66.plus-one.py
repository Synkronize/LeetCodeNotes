class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        exponent = len(digits) - 1
        number = 0
        for digit in digits:
            number = number + (digit * (10**exponent))
            exponent = exponent - 1
        
        newNumber = number + 1
        
        newExp = 0
        while newNumber != 0:
            if newExp > len(digits) - 1:
                digits.insert(0, newNumber % 10)
            else:    
                digits[(len(digits) - 1) - newExp] = newNumber % 10
            newNumber = newNumber / 10
            newExp = newExp + 1
        return digits

