# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res

        queue = deque([root])

        while queue:
            currLevel = []
            levelSize = len(queue)

            for _ in range(levelSize):
                # Remove node from front of queue
                node = queue.popleft()
              
                # Add node value to current level list
                currLevel.append(node.val)
              
                # Add children to queue for next level processing
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
          
            # Add current level to result
            res.append(currLevel)
      
        return res
        