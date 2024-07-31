## code-merger

![Code Merger](https://img.shields.io/badge/language-python-blue) ![version](https://img.shields.io/badge/version-1.0-brightgreen) ![license](https://img.shields.io/badge/license-MIT-blue)

## 🚀 Overview

**code-merger** is a powerful and flexible command-line tool designed to merge files of specified extensions into a single Markdown document. Perfect for pasting your project as a reference to an LLM with a long context (like GPT-4o or Google Gemini) or for generating comprehensive project documentation or combining multiple code files into one easily navigable format.

## 📜 Features

- Support for a wide range of file extensions.
- Automatic generation of project folder structure.
- File contents are seamlessly merged and formatted in Markdown.
- Output can be saved to a file or copied directly to the clipboard.

## 🛠 Installation

### Using pip

You can easily install code-merger from PyPI (Python Package Index):

```sh
pip install code-merger
```

### From Source

Clone this repository, install via pip using the flag -e to customize it.

```sh
git clone https://github.com/your-username/code-merger.git
cd code-merger
pip install -e .
```

## 🚀 Usage

code-merger is simple to use right from your command line.

### Command-Line Interface

```sh
merge [-e EXTENSIONS] [-f FILENAME]
```

### Options

- `-e`, `--extensions`: List of file extensions to merge. Defaults to a comprehensive list of common coding languages. If not specified, scans for all supported exstensions.
- `-f`, `--filename`: Name of the output file. If omitted, the merged content will be copied to the clipboard.

## 📌 Examples

### Merge Specific Extensions

```sh
merge -e py js html
```

### Save Merged Content to File

```sh
merge -e py js html -f merged_documentation.md
```

### Use Default Extensions and Copy to Clipboard

```sh
merge
```

## Supported Extensions

code-merger supports an extensive list of file extensions including but not limited to:

- Python (`.py`)
- JavaScript (`.js`, `.jsx`, `.tsx`, `.ts`)
- HTML (`.html`)
- CSS (`.css`, `.scss`)
- YAML (`.yaml`, `.yml`)
- JSON (`.json`)
- Markdown (`.md`)
- C (`.c`)
- C++ (`.cpp`)
- Java (`.java`)
- Ruby (`.rb`)
- Go (`.go`)
- Rust (`.rs`)
- Shell scripts (`.sh`)
- Perl (`.pl`)
- PHP (`.php`)
- Swift (`.swift`)
- Kotlin (`.kotlin`)
- R (`.r`)
- Objective C (`.m`, `.h`)

## 🛡️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👏 Contributing

We welcome contributions! If you have any ideas, suggestions, or improvements, feel free to open an issue or submit a pull request.

## 📧 Contact

For any questions, feel free to reach out.

<!-- ## 📄 Acknowledgments

Special thanks to all the contributors and users for making this project better. -->

---
<br>
<!-- Elevate your project documentation with **code-merger**! -->

[![GitHub stars](https://img.shields.io/github/stars/your-username/code-merger.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/your-username/code-merger/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/your-username/code-merger.svg?style=social&label=Fork&maxAge=2592000)](https://GitHub.com/your-username/code-merger/fork/)