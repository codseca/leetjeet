# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()  # starting dummy node
        tail = dummy        # tail will build the new list
        
        # Traverse both lists while nodes exist
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # move tail forward

        # Attach the remaining nodes (if any)
        tail.next = list1 if list1 else list2

        return dummy.next  # return head of merged list
