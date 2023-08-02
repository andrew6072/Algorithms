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
    Case 2: The word to be removed is a prefix of another word. Ex: we wan to remove 'abc' from a Trie that has 'abcd'
    Case 3: The word to be removed contains another word. Ex: remove 'abcd' from a Trie that has 'abc'
    
    If level == len, it means that we have successfully traversed to the last character of this word in this Trie, 
    also means that we have found the word to be removed in this Trie, but do not delete it yet, we mark the 
    attribute 'isEndOfWord' to False for deleting later.
    """
    if level == len:
        if root.isEndOfWord:
            root.isEndOfWord = False
            return True
        return False

    ch = s[level]

    """
    If we cannot find the next char in Trie (which means this word to be removed is not in the Trie), 
    then stop traverse.
    """
    if ch not in root.child:
        return False

    """
    This flag is attached with a node, it indicates if a node is in the word to be removed or not.
    """
    flag = removeWord(root.child[ch], s, level + 1, len)

    """
    If this char is supposed to be removed (flag == True);
    
    and this char is not the ending of any word (we dont want to remove the words that is prefix 
    of the word that we want to be removed -> Case2);
    
    and this char has no child (which means this word is not prefix of any word -> Case3 & Case1), 
    then OK, we can remove this char.
    """
    if (
        flag == True
        and root.child[ch].isEndOfWord == False
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

word_to_remove = "the"
removeWord(root, word_to_remove, 0, len(word_to_remove))

print("\nAfter remove:")
printWord(root, "")
