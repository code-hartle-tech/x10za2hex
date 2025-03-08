# 🚧 x10za2hex 🧮

## 📜 Overview

The [x10za2hex](): **Xtensa To Hex Converter** is a command-line tool designed to translate Xtensa assembly instructions into their corresponding machine code (hex representation). This utility is particularly useful for low-level debugging, reverse engineering, and verifying instruction encoding.

## 🎯 Key Features

- ✅ Converts **Xtensa assembly instructions** into **hex encoding**.
- ✅ Displays output in a **colorized table** using Rich.
- ✅ Supports **both optimized and unoptimized** instruction formats (e.g., `movi.n`, `_movi`).
- ✅ Handles **various instruction types**, including register operations, memory loads/stores, and jumps.
- ✅ Works seamlessly with **l32i** and its compressed counterpart **l32i.n**.

## 📦 Prerequisites

Before using this tool, ensure that your system meets the following requirements:

- 🔹 **ESP-IDF Environment**
- 🔹 **Python 3.x**
- 🔹 **Xtensa Toolchain**
- 🔹 **'Rich' Python library**

### ⚙️ Installing Dependencies

To install the required dependencies, follow these steps:

#### 🔹 Python Dependencies
```sh
pip install rich
```

Alternatively, you can install Python dependencies using Pipenv:
```sh
pipenv install
pipenv shell
```

#### 🔹 Xtensa Toolchain Installation
🧾 Refer to the official ESP-IDF installation guide for proper setup: [ESP-IDF Installation Documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html)

## 🚀 Usage Guide

To convert a single instruction, use the following command:
```sh
python x10za2hex.py "movi a3, 10"
```

### 📌 Example Output

| **📜 Instruction** | **🟩 Hex Code** |
|--------------------|---------------|
| `movi.n a3, 10`    | `A30C`      |

### ✋🏻 Preventing Optimization

To prevent automatic assembler optimizations, use an underscore (`_`) before an instruction:
```sh
python x10za2hex.py "_movi a3, 10"
```

### 📌 Example Output

| **📜 Instruction** | **🟩 Hex Code** |
|--------------------|---------------|
| `movi a3, 10`    | `0AA032`      |

## 🛠️ Supported Instructions

This tool supports a wide range of Xtensa instructions, including:

- 🧮 **Arithmetic Operations**:
  - `add`, `sub`, `xor`, etc.
- 📦 **Memory Access**:
  - `l32i`, `s32i`, `l8ui`
- 🔀 **Branch and Jump**:
  - `j`, `beq`, `bne`
- 🔧 **Shift and Bitwise Operations**:
  - `slli`, `srli`, `srai`
- 🔁 **Call and Return**:
  - `call8`, `ret`

## 🛠️ Troubleshooting

If you encounter any issues, check the following:

- ❌ **Xtensa Assembler Not Found**:
  - Ensure **ESP-IDF Environment** is loaded in the terminal session and is available in your system `PATH` before running this tool. This ensures the Xtensa toolchain functions correctly.
- ❌ **Syntax Errors**:
  - Verify that the instruction format follows Xtensa’s ISA documentation.
- ❌ **Unexpected Output**:
  - Refer to the [Xtensa®️ Instruction Set Architecture (ISA) Summary](https://www.cadence.com/content/dam/cadence-www/global/en_US/documents/tools/silicon-solutions/compute-ip/isa-summary.pdf).

## 📜 License

This project is open-source and licensed under the MIT License.

## 👨‍💻 Author

Developed by **HARTLE.TECH**.
