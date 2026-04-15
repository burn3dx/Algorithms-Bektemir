def huffman_decoding(encoded_text, huffman_codes):
    # создаём обратный словарь
    reverse_codes = {v: k for k, v in huffman_codes.items()}

    current_code = ""
    decoded_text = ""

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""

    return decoded_text
