"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

    # Dictionary to map original node -> copied node
        mapping = {}

    # First pass: create copies of all nodes but don't link them yet
        curr = head
        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next

    # Second pass: link next and random pointers using the mapping
        curr = head
        while curr:
            mapping[curr].next = mapping[curr.next] if curr.next else None
            mapping[curr].random = mapping[curr.random] if curr.random else None
            curr = curr.next

        return mapping[head]

        