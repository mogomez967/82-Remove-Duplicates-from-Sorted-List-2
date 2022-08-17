# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TODO: case of [1, 1, 1, 2, 3] is outputting incorrectly
#       output = [1, 2, 3] when it should be [2, 3]
#       it seems to be solely keeping in the first node regardless

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        prev = None

        count = 0
        STALL = False
        stall_count = 0
        num = 2
        if head is not None:
            HEAD_VAL = head.val
        while(curr is not None and curr.next is not None):
            # print("head: ", head.val)
            count += 1
            if count < 3:
                prev = head
            else:
                if STALL:
                    stall_count += 1
                    if stall_count > 1:
                        STALL = False
                        stall_count = 0
                else:
                    prev = prev.next

            print(count, "curr =  ", curr.val, " prev = ", prev.val, " next = ", curr.next.val)
            if curr.val == curr.next.val:
                curr.next = curr.next.next
                prev.next = curr.next
                STALL = True
                if count < num:
                    temp = head
                    if head.next is not None:
                        head.val = head.next.val
                    mod_HEAD_VAL = head.val
                    temp = None
                    if HEAD_VAL == mod_HEAD_VAL:
                        num += 1
            else:
                curr = curr.next
        return head

one = ListNode()
two = ListNode()
three = ListNode()
four = ListNode()
five = ListNode()
six = ListNode()
sev = ListNode()

one.val = 1
one.next = two

two.val = 1
two.next = three

three.val = 2
three.next = four

four.val = 3
four.next = five

five.val = 4
five.next = six

six.val = 4
six.next = sev

sev.val = 5
sev.next = None

curr = one

while(curr is not None):
    print(curr.val, end=" ")
    curr = curr.next

print()
curr = one

Solution.deleteDuplicates(Solution.deleteDuplicates, one)

while(curr is not None):
    print(curr.val, end=" ")
    curr = curr.next