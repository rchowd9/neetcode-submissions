from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = None  # stores the word if this node is end of a word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        m, n = len(board), len(board[0])

        # Build Trie from all words
        for word in words:
            node = root
            for ch in word:
                idx = ord(ch) - ord('a')
                if not node.children[idx]:
                    node.children[idx] = TrieNode()
                node = node.children[idx]
            node.word = word

        res = []

        # DFS from each cell
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, root, res)

        return res

    def dfs(self, board, i, j, node, res):
        m, n = len(board), len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if board[i][j] == '#':
            return
        ch = board[i][j]
        idx = ord(ch) - ord('a')
        child = node.children[idx]
        if not child:
            return

        # If this node marks the end of a word, add it to results
        if child.word:
            res.append(child.word)
            child.word = None  # mark as found to avoid duplicates

        # Mark visited
        board[i][j] = '#'

        # Explore neighbors
        self.dfs(board, i+1, j, child, res)
        self.dfs(board, i-1, j, child, res)
        self.dfs(board, i, j+1, child, res)
        self.dfs(board, i, j-1, child, res)

        # Backtrack
        board[i][j] = ch
