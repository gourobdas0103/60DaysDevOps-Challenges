import os
import sys

# Get the current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# List files in the current directory
files = os.listdir()
print("Files in Directory:", files)

# Get the Python version
print("Python Version:", sys.version)

# Get the script name
print("Script Name:", sys.argv[0])