import os

cwd = os.getcwd()
creds = cwd + r"\credentials.json"
print(creds)

# Open the file in read-only mode ('r')
with open(creds, 'r') as file:
    # Read the entire file into a string
    file_contents = file.read()

# Print the file contents
print(file_contents)

# Method 1: Using the `os.path.exists()` function
file_path = creds
