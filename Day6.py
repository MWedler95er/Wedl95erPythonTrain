def greet_user(name):
    print(f"Hello, {name}")


def greet_user(name="Guest"):
    print(f"Hello, {name}")


greet_user()
greet_user("Michael")


def calculation_rectangle(length, breadth):
    return print(length * breadth)


calculation_rectangle(10, 2)


coder_name = "MiKZ"


def name_the_coder(coder_name="Michael"):
    print(coder_name)


name_the_coder()
print(coder_name)


def rename_the_coder():
    global coder_name
    coder_name = "michi"
    print(coder_name)


rename_the_coder()
print(coder_name)
