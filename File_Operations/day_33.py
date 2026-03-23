"""
    Docstring for Day33
#Write data to a text file.

"""


def write_txt(txt_file_name, text_file_input):
    with open(txt_file_name, "w", encoding="utf-8") as bare_txt:
        bare_txt.writelines(text_file_input)
    return "DONE"


TEXT = "Test text - Day 33 "

write_txt("testText.txt", TEXT)
