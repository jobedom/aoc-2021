import os

folder = ""


def set_folder(new_folder):
    global folder
    folder = new_folder
    print(f"\n{new_folder}\n----------------------------------------")


def read_lines_from_file(filename):
    file_path = os.path.join(folder, filename)
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]


def read_number_from_file(filename):
    return [int(line) for line in read_lines_from_file(filename)]
