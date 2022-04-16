class Trie(object):
    def __init__(self):
        self.root_node = {}

    def add_word(self, word):
        current_node = self.root_node
        is_new_word = False

        # Work downwards through the trie, adding nodes as needed,
        # and keeping track of whether we add any nodes

        for char in word:
            if char not in current_node:
                is_new_word = True
                current_node[char] = {}
            current_node = current_node[char]


            # Explicityl mark the end of a word
            # Otherwise, we might say a word is present if its prefix of a different
            # longer word that was added earlier

            if "End Of Word" not in current_node:
                is_new_word = True
                current_node["End of Word"] = {}

            return is_new_word
