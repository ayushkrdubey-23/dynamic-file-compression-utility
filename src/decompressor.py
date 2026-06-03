import os


def bytes_to_binary(file_path):

    with open(file_path, "rb") as f:
        byte_data = f.read()

    binary_string = ""

    for byte in byte_data:
        binary_string += format(byte, "08b")

    # First byte contains padding info
    padding = int(binary_string[:8], 2)

    binary_string = binary_string[8:]

    if padding > 0:
        binary_string = binary_string[:-padding]

    return binary_string


def decompress_data(binary_string, root):

    result = ""

    current = root

    for bit in binary_string:

        if bit == "0":
            current = current.left
        else:
            current = current.right

        # Leaf node found
        if current.char is not None:
            result += current.char
            current = root

    return result


def save_decompressed_file(path, text):

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
        