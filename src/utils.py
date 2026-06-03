def read_file(file_path):
    """
    Reads content from a text file
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        print("File not found.")
        return None

    except Exception as e:
        print("Error:", e)
        return None


def calculate_frequency(text):
    """
    Calculates frequency of each character using HashMap
    """

    frequency = {}

    for char in text:

        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency