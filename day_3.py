"""
Created different data types and initialized variables with inputs.
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = float(input("Enter your age: "))
plz = int(input("Enter your postal code: "))
adress = str(input("Enter your address: "))
smoking_input = input("Do you smoke? (yes/no): ").strip().lower()
smoking = True if smoking_input == "yes" else False
driver_license_input = (
    input("Do you have a driver's license? (yes/no): ").strip().lower()
)
driver_license = True if driver_license_input == "yes" else None

print("First Name:", first_name)
print("Last Name:", last_name)
print("Age:", age)
print("Postal Code:", plz)
print("Address:", adress)
print("Smoking:", smoking)
print("Driver's License:", driver_license)
