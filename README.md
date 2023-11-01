# DirectoryWalker 📂

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A simple Python script to walk through a directory and list its contents, with recursive scanning capabilities.

## 🚀 Quick Start

1. Clone the repository:

   ```bash
   git clone https://github.com/bcostaaa01/directory_forensics.git
   ```

2. Change to the project directory:

   ```bash
   cd directory_forensics
   ```

3. Run the script:

   ```bash
   python main.py
   ```

## 📜 Description

DirectoryWalker is a Python script that allows you to scan and list the contents of a directory, providing both non-recursive and recursive scanning options. It's a handy tool for quickly exploring the files and subdirectories within a folder.

## 🧰 Usage

- **Non-Recursive Scanning**:
  Run the script with the `-p` or `--path` argument to specify the directory you want to scan non-recursively:

  ```bash
  python main.py -p /path/to/your/directory
  ```

- **Recursive Scanning**:
  To scan the directory and its subdirectories recursively, use the `RecursiveWalk` class:

  ```bash
  python main.py -p /path/to/your/directory -r
  ```

  By default, the script will scan the folder where the project code is located if no path is provided.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.
