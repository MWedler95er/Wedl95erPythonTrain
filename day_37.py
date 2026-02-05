"""

    DAY 37
#handle exceptions fo file not found.

"""


def open_file(file_root):
    try:
        with open(file_root, "r", encoding="utf-8") as f:
            return f
    except FileNotFoundError:
        return "ERORR: File not found."


file = "testText_fehler.txt"

print(open_file(file))
