import re

email = input("Enter an email address: ")

# Regular expression to match a valid email
email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

if re.match(email_pattern, email):
    print("Valid Email ✅")
else:
    print("Invalid Email ❌")
