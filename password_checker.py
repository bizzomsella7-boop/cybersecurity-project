
import getpass
import re

print("=" * 50)
print("       PASSWORD STRENGTH CHECKER")
print("=" * 50)

password = getpass.getpass("Enter password to check: ")

score = 0
feedback = []

if len(password) >= 8:
    score += 1
else:
    feedback.append("Use at least 8 characters.")

if len(password) >= 12:
    score += 1

if re.search(r"[A-Z]", password):
    score += 1
else:
    feedback.append("Add an uppercase letter.")

if re.search(r"[a-z]", password):
    score += 1
else:
    feedback.append("Add a lowercase letter.")

if re.search(r"\d", password):
    score += 1
else:
    feedback.append("Add a number.")

if re.search(r"[^A-Za-z0-9]", password):
    score += 1
else:
    feedback.append("Add a special character.")

print("\n" + "-" * 50)

if score <= 2:
    strength = "WEAK"
elif score <= 4:
    strength = "MEDIUM"
else:
    strength = "STRONG"

print(f"Strength: {strength}")
print(f"Score: {score}/6")

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print(f"- {item}")
else:
    print("\nGood password characteristics detected.")

print("-" * 50)
