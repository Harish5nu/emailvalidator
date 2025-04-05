import re

email = input("Enter a Email Address: ")

# Regular expression to match a valid Email
email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

if re.match(email_pattern, email):
    print("Valid Email ✅")
else:
    print("Invalid Email ❌ Please enter a valid email")
