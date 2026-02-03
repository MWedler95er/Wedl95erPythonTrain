'''
            Day32
        
        # Read an display the contents of a text file.

'''

def read_text(txt):
    with open(txt,"r") as f:
        for x in f:
            print(x)
    
read_text("README.md")


# Pythonic Way
def read_text_2(txt_name):
    with open(txt_name,"r",encoding="utf-8") as bare_text:
        for line in bare_text:
            print(line.strip())

print("________________________________________")
read_text_2("README.md")