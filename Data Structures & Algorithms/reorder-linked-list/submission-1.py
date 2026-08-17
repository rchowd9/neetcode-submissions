# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow_pointer = fast_pointer = head
        while fast_pointer.next and fast_pointer.next.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
      
        # Step 2: Split the list into two halves
        # slow_pointer now points to the middle node
        second_half_head = slow_pointer.next
        slow_pointer.next = None  # Disconnect first half from second half
      
        # Step 3: Reverse the second half of the list
        previous_node = None
        current_node = second_half_head
        while current_node:
            next_temp = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_temp
      
        # previous_node now points to the head of reversed second half
        reversed_second_half = previous_node
        first_half = head
      
        # Step 4: Merge the two halves by alternating nodes
        # Take one node from first half, then one from reversed second half
        while reversed_second_half:
            # Save next nodes
            first_half_next = first_half.next
            second_half_next = reversed_second_half.next
          
            # Connect nodes alternately
            first_half.next = reversed_second_half
            reversed_second_half.next = first_half_next
          
            # Move pointers forward
            first_half = first_half_next
            reversed_second_half = second_half_next

        
        