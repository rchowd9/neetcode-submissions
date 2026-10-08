from collections import defaultdict, deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        Given a sorted list of words in an alien language, return a string
        representing the characters in the correct order. If no valid order exists,
        return an empty string.
        """
        # Step 1: Initialize graph and indegree map
        adj = defaultdict(set)  # adjacency list
        indegree = {c: 0 for word in words for c in word}  # all unique chars

        # Step 2: Build the graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # Invalid case: prefix issue (e.g., "abc" before "ab")
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break  # Only first difference matters

        # Step 3: Topological sort using BFS (Kahn's Algorithm)
        queue = deque([c for c in indegree if indegree[c] == 0])
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)
            for nei in adj[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        # Step 4: Check for cycle (if not all chars are in order)
        if len(order) < len(indegree):
            return ""  # Cycle detected

        return "".join(order)
