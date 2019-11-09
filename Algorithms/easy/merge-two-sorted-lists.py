# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


    def list(self) -> list:
        res = []
        ptr = self
        while True:
            res.append(ptr.val)
            if not ptr.next: break
            ptr = ptr.next
        return res


    def __str__(self):
        res = ''
        ptr = self
        while True:
            if res: res += ', '
            res += str(ptr.val)
            if not ptr.next: break
            ptr = ptr.next

        return res


def listToNodes(alist: list) -> ListNode:
    ptr = ListNode(alist[0])
    head = ptr
    for item in alist[1:]:
        ptr.next = ListNode(item)
        ptr = ptr.next
    return head

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        cur1 = l1
        cur2 = l2
        ptr = None
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        while True:
            if cur1.val < cur2.val:
                if ptr is not None:
                    ptr.next = cur1
                ptr = cur1
                cur1 = cur1.next
            else:
                 if ptr is not None:
                     ptr.next = cur2
                 ptr = cur2
                 cur2 = cur2.next

            if head == None:
                head = ptr
            if not cur1 or not cur2:
                break

        if cur2:
            ptr.next = cur2
        if cur1:
            ptr.next = cur1

        return head

if __name__ == "__main__":
    home = ListNode(1)
    home.next = ListNode(2)
    print(home.list())
    print(home)

    sol = Solution()
    one = listToNodes([1])
    two = listToNodes([2])
    print(sol.mergeTwoLists(one, two))
    one = listToNodes([1,3])
    two = listToNodes([2])
    print(sol.mergeTwoLists(one, two))
    one = listToNodes([1,2,3])
    two = listToNodes([2])
    print(sol.mergeTwoLists(one, two))
    one = listToNodes([1,2,3])
    two = listToNodes([2,5,6])
    print(sol.mergeTwoLists(one, two))
    one = None
    two = listToNodes([2,5,6])
    print(sol.mergeTwoLists(one, two))

