import subprocess

def create_user(username):
    """Creates a Linux user and verifies the creation."""
    try:
        # Create the user (Runs `sudo useradd <username>`)
        subprocess.run(["sudo", "useradd", username], check=True)
        print(f"✅ User '{username}' created successfully.")

        # Verify user creation (Runs `id <username>`)
        result = subprocess.run(["id", username], capture_output=True, text=True)

        if result.returncode == 0:
            print(f"🔍 User verification successful:\n{result.stdout}")
        else:
            print(f"❌ User verification failed: {result.stderr}")

    except subprocess.CalledProcessError as e:
        print(f"❌ Error: Failed to create user '{username}'. {e}")

# Ask for username input
username = input("Enter the new username: ")
create_user(username)