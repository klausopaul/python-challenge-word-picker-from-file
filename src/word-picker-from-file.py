import os
import random


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    """
    main Reads a list of names from a text file, randomly picks one, and displays it.
    It's perfect for practicing file handling and working with lists in Python.

    Returns:
        Nothing
    """
    file_with_names = "./data/names.txt"

    with open(file_with_names, "r", encoding="utf-8") as f:
        list_with_names = f.readlines()

    print(f"File has {len(list_with_names)} names")

    selected_name = random.choice(list_with_names)

    print(f"Randomly picking: {selected_name}")


if __name__ == "__main__":
    cls()
    main()
