import os

# Define the directory containing files
directory = "test_files"

try:
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"❌ Error: The directory '{directory}' does not exist.")
        exit()

    # Loop through files in the directory
    for count, filename in enumerate(os.listdir(directory), start=1):
        old_path = os.path.join(directory, filename)  # Get full file path

        # Define the new file name format
        new_filename = f"renamed_file_{count}.txt"
        new_path = os.path.join(directory, new_filename)

        # Rename the file
        os.rename(old_path, new_path)

        print(f"✅ Renamed '{filename}' → '{new_filename}'")

except Exception as e:
    print(f"❌ An error occurred: {e}")