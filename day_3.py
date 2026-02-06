"""
Created different data types and initialized variables with inputs.
"""

FIRST_NAME = input("Enter your first name: ")
LAST_NAME = input("Enter your last name: ")
AGE = float(input("Enter your age: "))
PLZ = int(input("Enter your postal code: "))
ADRESSE = str(input("Enter your address: "))
SMOKING_INPUT = input("Do you smoke? (yes/no): ").strip().lower()
SMOKING = SMOKING_INPUT == "yes"
DRIVER_LICENSE_INPUT = (
    input("Do you have a driver's license? (yes/no): ").strip().lower()
)
DRIVER_LICENSE = DRIVER_LICENSE_INPUT == "yes"

print("First Name:", FIRST_NAME)
print("Last Name:", LAST_NAME)
print("Age:", AGE)
print("Postal Code:", PLZ)
print("Address:", ADRESSE)
print("Smoking:", SMOKING)
print("Driver's License:", DRIVER_LICENSE)
