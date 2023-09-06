class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Cases  0 + 1 = 1, 1 + 1 = 1(carry)0
        lastIndexA = len(a) - 1
        lastIndexB = len(b) - 1
        carry = 0
        mainList = a if lastIndexA > lastIndexB else b
        secondaryList = b if mainList == a else a
        index = len(secondaryList) - 1
        mainIndex = len(mainList) - 1
        rtnString = ''
        while index >= 0:
            bit1 = mainList[mainIndex]
            bit2 = secondaryList[index]
            if carry == 1:
                carry = 1 if bit2 == '1' else 0
                if bit2 == '1':
                    bit2 = '0'
                else:
                    bit2 = '1'
            if (bit2 == '1' and bit1 == '0') or (bit2 == '0' and bit1 == '1'):
               rtnString = '1' + rtnString
            elif bit2 == '1' and bit1 == '1':
                rtnString = '0' + rtnString
                carry = 1
            else:
                rtnString = '0' + rtnString
            index = index - 1
            mainIndex = mainIndex - 1
        
        
        while mainIndex >= 0:
            if carry == 1: 
                if mainList[mainIndex] == '0':
                    rtnString = '1' + rtnString
                    carry = 0
                else:
                    rtnString = '0' + rtnString
            else:
                rtnString = mainList[mainIndex] + rtnString
            mainIndex = mainIndex - 1

        if carry == 0:
            return rtnString
        return '1' + rtnString

            

            

        
