class TrieNode:
    def __init__(self):
        self.child = dict()
        self.isEndOfWord = False

    def __repr__(self):
        char_in_dict = []
        for i in range(97, 123):
            if chr(i) in self.child:
                char_in_dict.append(chr(i))
        return "Children -> " + str(char_in_dict)


"""
addWord()
1) Every character of the input key is inserted as an individual Trie node.
   Note that the child is a dictionary to next-level trie nodes.
2) The key character acts as an key to the dictionary child.
3) If the input key is new or an extension of the existing key,
   construct non-existing nodes of the key, and mark the end of the word for the last node.
4) If the input key is a prefix of the existing key in Trie, Simply mark the last node of
   the key as the end of a word.
"""


def addWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = TrieNode()
        temp = temp.child[ch]
    temp.isEndOfWord = True


def findWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            return False
        temp = temp.child[ch]
    return temp.isEndOfWord


def isWord(node):
    return node.isEndOfWord


def isEmpty(node):
    return len(node.child) == 0


def removeWord(root, s, level, len):
    if root == None:
        return False

    """
    Case 1: The word to be removed is an independent word. Its deletion does not affect any other words in the Trie.
    If level == len, it means that we have successfully traversed to the last character of this word in this Trie, 
    also means that we have found the word to be removed in this Trie, but do not delete it yet, we mark the isEndOfWord
    attribute to False for deleting later.
    
    """
    if level == len:
        if root.isEndOfWord:
            root.isEndOfWord = False
            return True
        return False

    ch = s[level]

    """
    If we cannot find the next char in Trie, then stop traverse.
    """
    if ch not in root.child:
        return False

    """
    This flag is attached with a node, it indicates if a node is in the word to be deleted or not.
    """
    flag = removeWord(root.child[ch], s, level + 1, len)

    if (
        flag == True
        and isWord(root.child[ch]) == False
        and isEmpty(root.child[ch]) == True
    ):
        del root.child[ch]

    return flag


def printWord(root, s):
    if isWord(root):
        print(s)
    for ch in root.child:
        printWord(root.child[ch], s + ch)


root = TrieNode()
addWord(root, "bigo")
addWord(root, "then")
addWord(root, "big")
addWord(root, "the")
addWord(root, "github")
printWord(root, "")
removeWord(root, "githubbg", 0, 6)
print("\nAfter remove:")
printWord(root, "")
