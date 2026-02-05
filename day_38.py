"""

    DAY 38
# Create acustum exception class.

"""


class OwnExceptions(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"OwnExceptions: {self.message}"