class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Marks the end of a valid word


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """Adds a word into the data structure."""
        if not isinstance(word, str) or not word.isalpha():
            raise ValueError("Word must be a non-empty string of letters.")

        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Searches for a word in the data structure.
        '.' can match any letter.
        """
        if not isinstance(word, str) or not word:
            return False

        def dfs(node: TrieNode, index: int) -> bool:
            if index == len(word):
                return node.is_end_of_word

            char = word[index]
            if char == '.':
                # Try all possible children
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], index + 1)

        return dfs(self.root, 0)
