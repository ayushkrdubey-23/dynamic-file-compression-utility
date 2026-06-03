import os

from src.utils import read_file, calculate_frequency
from src.huffman import build_huffman_tree, generate_codes
from src.compressor import compress_data, binary_to_bytes, save_compressed_file
from src.decompressor import bytes_to_binary, decompress_data, save_decompressed_file


FILE_PATH = "input_files/sample.txt"

OUTPUT_FREQ = "outputs/frequency_table.txt"
OUTPUT_TREE = "outputs/huffman_tree.txt"
OUTPUT_CODES = "outputs/huffman_codes.txt"

COMPRESSED_FILE = "compressed_files/output.bin"
DECOMPRESSED_FILE = "decompressed_files/output.txt"


def save_text_file(path, content_list):

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(content_list))


def main():

    # -------------------------
    # READ FILE
    # -------------------------
    text = read_file(FILE_PATH)
    if not text:
        return

    # -------------------------
    # FREQUENCY TABLE
    # -------------------------
    frequency = calculate_frequency(text)

    freq_output = ["===== FREQUENCY TABLE =====\n"]

    for char, freq in sorted(frequency.items()):

        if char == " ":
            display = "[SPACE]"
        elif char == "\n":
            display = "[NEWLINE]"
        else:
            display = char

        freq_output.append(f"{display} : {freq}")

    save_text_file(OUTPUT_FREQ, freq_output)

    # -------------------------
    # BUILD TREE
    # -------------------------
    root = build_huffman_tree(frequency)

    # -------------------------
    # GENERATE CODES
    # -------------------------
    codes = generate_codes(root)

    # -------------------------
    # COMPRESS
    # -------------------------
    binary_string = compress_data(text, codes)

    compressed_bytes = binary_to_bytes(binary_string)

    os.makedirs("compressed_files", exist_ok=True)
    os.makedirs("decompressed_files", exist_ok=True)

    save_compressed_file(COMPRESSED_FILE, compressed_bytes)

    print("\n===== COMPRESSION DONE =====")
    print("Compressed File:", COMPRESSED_FILE)

    # -------------------------
    # DECOMPRESSION STEP
    # -------------------------
    print("\n===== DECOMPRESSION STARTED =====")

    binary = bytes_to_binary(COMPRESSED_FILE)

    restored_text = decompress_data(binary, root)

    save_decompressed_file(DECOMPRESSED_FILE, restored_text)

    print("Decompressed File:", DECOMPRESSED_FILE)

    # -------------------------
    # VERIFICATION
    # -------------------------
    if text == restored_text:
        print("\nSUCCESS: Original and Decompressed files match ✅")
    else:
        print("\nERROR: Mismatch ❌")

    # -------------------------
    # SIZE REPORT
    # -------------------------
    original_size = len(text.encode("utf-8"))
    compressed_size = os.path.getsize(COMPRESSED_FILE)

    print("\n===== SIZE REPORT =====")
    print("Original Size  :", original_size, "bytes")
    print("Compressed Size:", compressed_size, "bytes")
    print("Ratio          :", round(compressed_size / original_size, 2))


if __name__ == "__main__":
    main()
    