from collections import Counter

def huffman_encoding(text):
    freq = Counter(text)
    nodes = [[char, freq[char]] for char in freq]
    codes = {char: "" for char in freq}

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x[1])

        left = nodes.pop(0)
        right = nodes.pop(0)

        for char in left[0]:
            codes[char] = '0' + codes[char]
        for char in right[0]:
            codes[char] = '1' + codes[char]

        nodes.append([left[0] + right[0], left[1] + right[1]])

    encoded = ''.join(codes[char] for char in text)
    return encoded, codes
