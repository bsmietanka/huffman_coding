class Queue:
    def __init__(self, source=[]):
        self.q = source
        self.size = len(self.q)

    def empty(self):
        return self.size == 0

    def enqueue(self, item):
        self.size += 1
        self.q.insert(0, item)

    def dequeue(self):
        self.size -= 1
        return self.q.pop()

    def peek(self):
        return self.q[-1]

class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        res = str(self.data)
        if self.left:
            res += "\nLeft: " + str(self.left)
        if self.right:
            res += "\nRight: " + str(self.right)
        return res

    def __repr__(self):
        res = str(self.data)
        if self.left:
            res += "\nLeft: " + str(self.left)
        if self.right:
            res += "\nRight: " + str(self.right)
        return res

def count_letters(text):
    freq = dict()
    for l in text:
        if l in freq:
            freq[l].data[1] += 1
        else:
            freq[l] = Node(data=[l, 1])
    return freq

'''Takes list of Nodes containing mutable pairs (char, int) sorted by second
element in descending order. Each pair represents number of letter occurances in a text'''
def huffman_tree(letter_frequency):
    leafs = Queue(letter_frequency)
    nodes = Queue()
    while leafs.size + nodes.size > 1:
        if nodes.empty():
            first = leafs.dequeue()
            second = leafs.dequeue()
        elif leafs.empty():
            first = nodes.dequeue()
            second = nodes.dequeue()
        else:
            first = leafs.dequeue() if leafs.peek().data[1] < nodes.peek().data[1] else nodes.dequeue()
            if nodes.empty():
                second = leafs.dequeue()
            elif leafs.empty():
                second = nodes.dequeue()
            else:
                second = leafs.dequeue() if leafs.peek().data[1] < nodes.peek().data[1] else nodes.dequeue()
        node = Node(data=[None, first.data[1] + second.data[1]])
        node.left = first
        node.right = second
        nodes.enqueue(node)
    if nodes.empty():
        res = Node(data=[None, leafs.peek().data[1]])
        res.left = leafs.dequeue()
    else:
        return nodes.dequeue()

def char_codes(root_node, codebook={}, code=""):
    if root_node.data[0]:
        codebook[root_node.data[0]] = code
    else:
        codebook = char_codes(root_node.left, codebook, code + "0")
        codebook = char_codes(root_node.right, codebook, code + "1")
    return codebook

def encode(text):
    coding_tree = huffman_tree(sorted(count_letters(
        text).values(), key=lambda item: item.data[1], reverse=True))
    codebook = char_codes(coding_tree)
    encoded = ""
    for l in text:
        encoded += codebook[l]
    return encoded

def main():
    text = "abaabaaabc"
    encoded = encode(text)
    print("Plain text: {} bits".format(len(text) * 8))
    print("Endoded text: {} bits".format(len(encoded)))

if __name__ == "__main__":
    main()