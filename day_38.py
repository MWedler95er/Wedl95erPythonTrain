"""

    DAY 38
# Create acustum exception class.

"""


class OwnExceptions(Exception):
    def __init__(self, message):
        self.message = "That ist your own exception: " + message
        super().__init__(self.message)

    def __str__(self):
        return f"OwnExceptions: {self.message}"


try:
    raise OwnExceptions("This is a custom error message.")
except OwnExceptions as e:
    print(e)
    print(e.message)

    # Output:
    # OwnExceptions: That ist your own exception: This is a custom error message.
