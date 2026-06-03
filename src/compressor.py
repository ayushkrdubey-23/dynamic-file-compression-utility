import os


def compress_data(text, codes):

    binary_string = ""

    for char in text:
        binary_string += codes[char]

    return binary_string


def binary_to_bytes(binary_string):

    extra_padding = 8 - len(binary_string) % 8
    binary_string += "0" * extra_padding

    padded_info = "{0:08b}".format(extra_padding)

    binary_string = padded_info + binary_string

    byte_array = bytearray()

    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        byte_array.append(int(byte, 2))

    return bytes(byte_array)


def save_compressed_file(output_path, data):

    with open(output_path, "wb") as f:
        f.write(data)
        