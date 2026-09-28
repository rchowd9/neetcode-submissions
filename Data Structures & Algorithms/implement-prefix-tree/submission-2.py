class TrieNode:
    """Node structure for the Trie."""
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Flag to mark end of a word


class PrefixTree:
    """Prefix Tree (Trie) implementation."""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.
        """
        if not isinstance(word, str) or not word:
            raise ValueError("Word must be a non-empty string.")

        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Return True if the word exists in the Trie.
        """
        if not isinstance(word, str) or not word:
            return False

        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Return True if there is any word in the Trie that starts with the given prefix.
        """
        if not isinstance(prefix, str) or not prefix:
            return False

        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True