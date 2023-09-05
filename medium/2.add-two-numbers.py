
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def buildNewList(self,total):
        head = ListNode(total  % 10)
        total = total/10
        temp = head
        while(total != 0):
            temp.next = ListNode(total % 10)
            total = total / 10
            temp = temp.next
        return head
            
            
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp1 = l1
        temp2 = l2
        size1 = 0
        size2 = 0
        while temp1 != None or temp2 != None:
            if temp1 != None:
                size1 = size1 + 1
                temp1 = temp1.next
            if temp2 != None:
                size2 = size2 + 1
                temp2 = temp2.next
            
        temp1 = l1
        temp2 = l2
        totals = [0, 0]
        exponent1 = 0
        exponent2 = 0
        while size1 > 0 or size2 > 0:
            if size1 > 0:
                sumAndDecrement(temp1.val, totals, exponent1, 0)
                exponent1 = exponent1 + 1
                size1 = size1 - 1
                temp1 = temp1.next
                

            if size2 > 0:
                sumAndDecrement(temp2.val, totals, exponent2, 1)
                exponent2 = exponent2 + 1
                size2 = size2 - 1
                temp2 = temp2.next
        
        total = totals[0] + totals[1]
        return self.buildNewList(total)


        


def sumAndDecrement(val, totals, exponent, index):
    totals[index] = totals[index] + (val * (10**exponent))
