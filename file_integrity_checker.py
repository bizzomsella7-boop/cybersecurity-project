import hashlib
import os

print("=" * 55)
print("           FILE INTEGRITY CHECKER")
print("=" * 55)

file_path = input("Enter file path to check: ").strip()

if not os.path.isfile(file_path):
    print("\nError: File not found.")
    exit()

sha256 = hashlib.sha256()

with open(file_path, "rb") as file:
    for block in iter(lambda: file.read(4096), b""):
        sha256.update(block)

file_hash = sha256.hexdigest()

print("\nFile:", file_path)
print("SHA-256:", file_hash)
print("\nIntegrity hash generated successfully.")
print("=" * 55)
