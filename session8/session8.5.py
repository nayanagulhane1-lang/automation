#Use ChatGPT or Copilot to generate a Python function that checks if a given string is a valid 
# Indian phone number (should be 10 digits, start with 6-9, and contain only numbers). 
# Test the generated function with three sample inputs and write down if it worked as expected.

def validate_phone(phone):
  if len(phone) == 10 and phone[0] in "6789" and phone.isdigit():
    return True
  else:
     return False

print(validate_phone("9876543210"))
print(validate_phone("5123456789"))
print(validate_phone("98765432"))