class Node:
    def __init__(self, char=None, frequency=None):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

def build_huffman_tree(data):
    frequency = {}
    for char in data:
        frequency[char] = frequency.get(char, 0) + 1

    nodes = [Node(char=c, frequency=f) for c, f in frequency.items()]

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.frequency)
        left = nodes.pop(0)
        right = nodes.pop(0)
        merged = Node(frequency=left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        nodes.append(merged)

    return nodes[0]

def build_huffman_codes(node, current_code="", codes=None):
    if codes is None:
        codes = {}
    if node is not None:
        if node.char is not None:
            codes[node.char] = current_code
        build_huffman_codes(node.left, current_code + "0", codes)
        build_huffman_codes(node.right, current_code + "1", codes)
    return codes

def huffman_encode(data):
    root = build_huffman_tree(data)
    codes = build_huffman_codes(root)
    encoded_data = ''.join(codes[char] for char in data)
    return encoded_data, codes

def huffman_decode(encoded_data, codes):
    decoded_data = ""
    current_code = ""
    for bit in encoded_data:
        current_code += bit
        for char, code in codes.items():
            if current_code == code:
                decoded_data += char
                current_code = ""
                break
    return decoded_data

# Example usage:
data = "hello world"
encoded_data, codes = huffman_encode(data)
decoded_data = huffman_decode(encoded_data, codes)

print("Original Data:", data)
print("code:", codes)
print("Encoded Data:", encoded_data)
print("Decoded Data:", decoded_data)
