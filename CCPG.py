#----------------------------------------
# ✝JMJ✝
#
# C++ Project Generator (CCPG.py)
#
# Description:
#
# A simple script to generate a C++ project structure with CMake support.
# It creates a folder structure, a main.cpp file, CMakeLists.txt, .gitignore, and README.md.
#
#----------------------------------------

import os
import subprocess
from colorama import init, Fore, Style

# setup colorama
init(autoreset=True)

#-----------------------------------------
# Functions
#-----------------------------------------

def print_banner():
    width = 33
    print(Fore.BLUE + "╔" + "═" * width + "╗")
    print(Fore.BLUE + "║" + Fore.YELLOW + "   CPP-CMAKE Project Generator  " + Fore.BLUE + " ║")
    print(Fore.BLUE + "║" + Fore.YELLOW + "           (CCPG.py)             " + Fore.BLUE + "║")
    print(Fore.BLUE + "╚" + "═" * width + "╝")
    print(Style.RESET_ALL)


def enter_project_name():
    while True:
        project_name = input("Enter project name or press 'q' to exit: ").strip()
        if project_name == "q":
            print("Goodbye!")
            exit()  
        elif not project_name:
            print("Project name cannot be empty.")
        elif os.path.exists(project_name):
            print(f"Error: Project '{project_name}' already exists!")
        else:
            break
    return project_name

def create_folder_structure(project_name):
    # Structure
    folders = [
        project_name,
        f"{project_name}/src",
        f"{project_name}/include",
        f"{project_name}/vendor",
        f"{project_name}/docs",
        f"{project_name}/res"
    ]

    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

def create_main_cpp(project_name):
    main_cpp = f"""\
    // main.cpp
    #include <iostream>

    int main() {{
        std::cout << "Hello from {project_name}!" << std::endl;
        return 0;
    }}
    """
    with open(f"{project_name}/src/main.cpp", "w") as f:
        f.write(main_cpp)
                
def create_cmake_content(project_name):
    cmake_content = """cmake_minimum_required(VERSION 3.10)
    project(%s)

    set(CMAKE_CXX_STANDARD 17)
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

    file(GLOB SOURCES "src/*.cpp")

    add_executable(${PROJECT_NAME} ${SOURCES})

    target_include_directories(${PROJECT_NAME}
        PUBLIC
            include
            vendor
    )
    """ % project_name

    with open(f"{project_name}/CMakeLists.txt", "w") as f:
        f.write(cmake_content)

def create_gitignore(project_name):
    gitignore_content = """
    # Build
    build/
    CMakeFiles/
    CMakeCache.txt
    cmake_install.cmake
    Makefile

    # Executables and binary files
    *.exe
    *.out
    *.app
    *.dll
    *.so
    *.dylib
    *.obj
    *.o
    *.a

    # IDE specific
    .vscode/
    *.code-workspace
    .idea/
    *.sublime-workspace
    *.sublime-project

    # Visual Studio files
    *.vcxproj*
    *.sln
    *.user
    *.suo
    *.vcxproj.filters
    *.pdb
    *.idb
    *.ipch
    *.tlog
    *.log
    *.ncb
    *.opensdf
    *.sdf
    *.cachefile

    # MacOS
    .DS_Store

    # General
    *.log
    *.tmp
    *.swp
    *.bak
    *~

    # CTest stuff
    Testing/
    CTestTestfile.cmake
    test_detail.xml
    """

    with open(f"{project_name}/.gitignore", "w") as f:
        f.write(gitignore_content.strip())

def create_readme(project_name):
    # Ask for README.md
    while True:
        create_readme = input("Do you want to create a README.md? (y/n): ").strip().lower()
        if create_readme in ["", "y", "yes"]:
            readme_content = f"# {project_name}\n\nThis `{project_name}` C++ project generated with CCPG.py.\n"
            with open(f"{project_name}/README.md", "w") as f:
                f.write(readme_content)
            print("README.md created.")
            break
        elif create_readme in ["n", "no"]:
            break
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def find_visual_studio():
    common_paths = [
        r"C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe",
        r"C:\Program Files\Microsoft Visual Studio\2022\Professional\Common7\IDE\devenv.exe",
        r"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\devenv.exe",
        r"C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\devenv.exe",
        r"D:\VisualStudio\Common7\IDE\devenv.exe",  
    ]
    
    for path in common_paths:
        if os.path.exists(path):
            return path
    
    return None

def ask_open_in_vs(project_name):
    while True:
        open_vs = input("Do you want to open the project in Visual Studio? (y/n): ").strip().lower()
        if open_vs in ["", "y", "yes"]:
            project_path = os.path.abspath(project_name)
            
            devenv_path = find_visual_studio()
            if devenv_path:
                print(f"Opening {project_path} in Visual Studio...")
                subprocess.Popen([devenv_path, project_path])
            else:
                print("Visual Studio not found automatically.")
                devenv_path = input("Please enter the path to devenv.exe manually: ").strip('"')
                if os.path.exists(devenv_path):
                    subprocess.Popen([devenv_path, project_path])
                else:
                    print("The provided path is invalid.")
            break
        elif open_vs in ["n", "no"]:
            break
        else:
            print("Invalid input.")

#-----------------------------------------
# Main Function
#-----------------------------------------

def main():
    print_banner()
    project_name = enter_project_name()
    create_folder_structure(project_name)
    create_main_cpp(project_name)
    create_cmake_content(project_name)
    create_gitignore(project_name)
    create_readme(project_name)
    print(f"\nProject '{project_name}' created successfully!")
    ask_open_in_vs(project_name)

#-----------------------------------------
# Entry Point
#-----------------------------------------
if __name__ == "__main__":
    main()