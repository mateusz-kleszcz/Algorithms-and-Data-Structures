class trieNode:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.isEnd = False


def isDifferent(arr):
    root = trieNode(-1)

    for el in arr:
        curr = root
        for i in range(len(el)):
            char = el[i]
            isNode = False

            for child in curr.children:
                if child.key == char:
                    isNode = True
                    curr = child
                    break

            if not isNode:
                new = trieNode(char)
                curr.children.append(new)
                curr = new

        if curr.isEnd:
            return False

        curr.isEnd = True

    return True


gens = [
    'AAACCCGGGTT',
    'AAACCCGGGAT',
    'AAACCCGGATT',
    'AAACCCGCATT',
]
print(isDifferent(gens))