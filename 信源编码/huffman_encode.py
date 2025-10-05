import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq):
    heap = [HuffmanNode(freq=fr, char=ch) for ch, fr in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)
    
    return heap[0]

def build_huffman_codes(node, prefix="", codebook={}):
    if node.char is not None:
        codebook[node.char] = prefix
    else:
        build_huffman_codes(node.left, prefix + "0", codebook)
        build_huffman_codes(node.right, prefix + "1", codebook)
    return codebook

def huffman_encode(data, codebook):
    return ''.join(codebook[ch] for ch in data)

# Example usage
data = "example text to encode"
freq = Counter(data)
huffman_tree = build_huffman_tree(freq)
huffman_codes = build_huffman_codes(huffman_tree)
encoded_data = huffman_encode(data, huffman_codes)
print("Huffman Encoded Data:", encoded_data)