import heapq


class HuffmanNode:

    def __init__(self, char, freq):

        self.char = char
        self.freq = freq

        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# ---------------------------
# BUILD MIN HEAP
# ---------------------------
def build_min_heap(frequency):

    heap = []

    for char, freq in frequency.items():
        node = HuffmanNode(char, freq)
        heapq.heappush(heap, node)

    return heap


# ---------------------------
# DEBUG: PRINT HEAP
# ---------------------------
def print_min_heap(heap):

    print("\n===== MIN HEAP (DEBUG) =====\n")

    for node in heap:

        if node.char == " ":
            ch = "[SPACE]"
        elif node.char == "\n":
            ch = "[NEWLINE]"
        elif node.char is None:
            ch = "[INTERNAL]"
        else:
            ch = node.char

        print(f"{ch} : {node.freq}")


# ---------------------------
# BUILD HUFFMAN TREE
# ---------------------------
def build_huffman_tree(frequency):

    heap = build_min_heap(frequency)

    print_min_heap(heap)

    while len(heap) > 1:

        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = HuffmanNode(None, left.freq + right.freq)

        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


# ---------------------------
# GENERATE HUFFMAN CODES
# ---------------------------
def generate_codes(root, current_code="", codes=None):

    if codes is None:
        codes = {}

    if root is None:
        return codes

    # If leaf node
    if root.char is not None:
        codes[root.char] = current_code
        return codes

    # Traverse left = 0
    generate_codes(root.left, current_code + "0", codes)

    # Traverse right = 1
    generate_codes(root.right, current_code + "1", codes)

    return codes
