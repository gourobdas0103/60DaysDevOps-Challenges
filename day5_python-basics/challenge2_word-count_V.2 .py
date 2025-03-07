file_name = input("Enter the file name: ")

try:
    word_count = 0
    with open(file_name, "r") as file:
        for line in file:
            word_count += len(line.split())

    print(f"✅ The file '{file_name}' contains {word_count} words.")

except FileNotFoundError:
    print(f"❌ Error: The file '{file_name}' was not found.")
except Exception as e:
    print(f"❌ An error occurred: {e}")