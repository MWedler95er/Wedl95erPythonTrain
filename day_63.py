import os

# Build a basic CRUD appication


class Crud:
    def __init__(self, text_file_name):
        self.text_file_name = text_file_name

    def create_file(self):
        with open(self.text_file_name, "w", encoding="utf-8") as t:
            t.write("")
        return "DONE"

    def read_file(self):
        with open(self.text_file_name, "r", encoding="utf-8") as t:
            for x in t:
                print(x)
        return "DONE"

    def update_file(self, text_input):
        with open(self.text_file_name, "w", encoding="utf-8") as t:
            t.writelines(text_input)
        return "DONE"

    def delete_file(self):
        os.remove(self.text_file_name)
        return "DONE"


FILE_NAME = "DasIstDerZweiteTest.txt"
TEXT_INPUT = "Das ist der test für den Update"

crud_app = Crud(FILE_NAME)
crud_app.create_file()
crud_app.update_file(TEXT_INPUT)
crud_app.read_file()
