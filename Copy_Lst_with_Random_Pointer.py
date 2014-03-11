# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
            
        hashmap = {}
        newhead = RandomListNode(head.label)
        
        psrc = head
        pdst = newhead
        
        hashmap[psrc] = pdst
        
        while psrc is not None:
            if psrc.next is not None:
                # make or link exist node for psrc.next
                if hashmap.has_key(psrc.next):
                    pnew = hashmap[psrc.next]
                else:
                    pnew = RandomListNode(psrc.next.label)
                # points pdst.next to new node, and add the mapping
                pdst.next = pnew
                hashmap[psrc.next] = pdst.next
            
            if psrc.random is not None:
                # make or link exist node for psrc.random
                if hashmap.has_key(psrc.random):
                    pnew = hashmap[psrc.random]
                else:
                    pnew = RandomListNode(psrc.random.label)
                # points pdst.random to new node, and add the mapping
                pdst.random = pnew
                hashmap[psrc.random] = pdst.random
            
            psrc = psrc.next
            pdst = pdst.next

        return newhead