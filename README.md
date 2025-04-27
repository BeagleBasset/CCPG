# CCPG - C++ Cmake Project Generator

## Overview
**CCPG.py** is a lightweight command-line utility designed to scaffold a modern C++ project with CMake build support in seconds.
After generating the project, it can optionally open it in Visual Studio for you.


![image](https://github.com/user-attachments/assets/167cdfd6-f238-4acb-b53a-196e360eb759)


This tool was primarily created to fit **my personal C++ workflow**, but it can be easily adapted for other styles of development as well.
It will continue to evolve as I gain more experience in complex, structured software development.
You can think of it as a starting skeleton for your own projects.

It automates the creation of:
- Standard project folder structure (`src/`, `include/`, `vendor/`, `docs/`, `res/`)
- Starter `main.cpp` with a minimal "Hello, World!" program
- A ready-to-use `CMakeLists.txt`
- `.gitignore` tuned for C++ and Visual Studio workflows
- Optional `README.md` generation

## Features
- Clean and organized project layout
- Minimal but extensible CMake configuration
- Quick start for professional C++ development
- Colored CLI output for better UX (via `colorama`)
- Simple, user-friendly interaction

## Installation
Clone this repository or download the `CCPG.py` script manually.

Install required Python packages:
```bash
pip install colorama
```

## Usage
Place the `CCPG.py` file where you want to create your project folder.

Run the generator script:

```bash
Python CCPG.py
```

Follow the prompts to:

  - Enter a project name

  - Choose whether to create a README.md
  
  - Decide if you want to open the project in Visual Studio

The tool will automatically generate and organize your project files into a new folder.

## Note

You can create a batch file if you want to run it by double-clicking a `.bat` file:

```bash
@echo off
:: Run the Python script
python CCPG.py
pause
```

## License


This script is free to use for personal or commercial projects.

Feel free to modify it to fit your needs.

All contributions are welcome!

