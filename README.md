# Dynamic File Compression Utility

## 📌 Project Overview

This project is a **Huffman Coding-based Lossless File Compression System** that dynamically compresses and decompresses files using Data Structures and Algorithms.

It demonstrates real-world use of:
- Greedy Algorithm
- Min Heap (Priority Queue)
- Binary Tree (Huffman Tree)
- HashMap (Frequency Table)

---

## 🚀 Features

- File compression using Huffman Encoding
- Lossless decompression
- Frequency table generation
- Huffman tree visualization
- Binary encoding conversion
- Compression ratio calculation
- CLI-based execution

---

## 🧠 DSA Concepts Used

- HashMap (Character Frequency)
- Min Heap (Priority Queue)
- Binary Tree (Huffman Tree)
- Greedy Algorithm
- Recursion (Tree traversal)

---

## ⚙️ Workflow

Input File
↓
Frequency Calculation
↓
Min Heap Creation
↓
Huffman Tree Construction
↓
Code Generation
↓
Binary Encoding
↓
Compressed File (.bin)
↓
Decompression
↓
Original File Restored

Input File
↓
Frequency Calculation
↓
Min Heap Creation
↓
Huffman Tree Construction
↓
Code Generation
↓
Binary Encoding
↓
Compressed File (.bin)
↓
Decompression
↓
Original File Restored


---

## 📁 Project Structure

Dynamic-File-Compression-Utility/
│
├── input_files/
├── compressed_files/
├── decompressed_files/
├── outputs/
├── src/
│ ├── huffman.py
│ ├── compressor.py
│ ├── decompressor.py
│ └── utils.py
│
├── main.py
├── README.md


---


---

## ▶️ How to Run

### Step 1: Install Python
Make sure Python 3.x is installed on your system.

### Step 2: Run the Project

```bash
python main.py


# 📦 Generated Files

After running the project, you will get:

- Frequency Table → `outputs/frequency_table.txt`  
- Huffman Tree → `outputs/huffman_tree.txt`  
- Huffman Codes → `outputs/huffman_codes.txt`  
- Compressed File → `compressed_files/output.bin`  
- Decompressed File → `decompressed_files/output.txt`  

---

## 🎯 Learning Outcomes

- Implemented Huffman Coding from scratch  
- Understood greedy optimization techniques  
- Learned Min Heap usage in real applications  
- Built full compression-decompression pipeline  
- Improved understanding of system-level programming  
- Gained experience in modular Python project structure  

---

## 🔮 Future Improvements

- Add GUI interface (Tkinter / Web)  
- Support folder compression (ZIP-like system)  
- Add multiple compression algorithms (gzip, lzma, zstd)  
- Add performance benchmarking dashboard  
- Add real-time file compression API  

---

## 👨‍💻 Author

  This project is developed as a **DSA + System Design Portfolio Project** to demonstrate strong fundamentals in algorithms, backend logic, and file processing systems.

---

## ⭐ Note

This is a **lossless compression system**, meaning:

- ✔ Original file is perfectly restored after decompression  
- ✔ No data loss occurs during compression process  