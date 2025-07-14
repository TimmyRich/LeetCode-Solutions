from Testing import test

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def toList(self):
        vals = []
        curr = self
        while curr != None:
            vals.append(curr.val)
            curr = curr.next
        return vals

    def __str__(self):
        vals = self.toList()
        return str(vals)
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.toList() == other.toList()

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode(0)
        curr = l1
        carry = 0
        while curr != None:
            sum = curr.val + l2.val + carry
            carry = sum // 10
            curr.val = sum % 10
            curr = curr.next
            l2 = l2.next

        return result

input = (ListNode(2, ListNode(4)), ListNode(5, ListNode(6 ,ListNode(4))))
expectedOutput = ListNode(6, ListNode(9, ListNode(6)))
sol = Solution()
print(sol.addTwoNumbers(*input))