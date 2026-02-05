"""

    DAY 34
#Append data to an existing text file.

"""


def append_to_text_file(text_file_name, text_to_append):
    with open(text_file_name, "a", encoding="utf-8") as txt_file:
        txt_file.write(text_to_append)
    return "DONE"


file_name = "testText.txt"
text_input = "A new line, A new line!\n"

append_to_text_file(file_name, text_input)
