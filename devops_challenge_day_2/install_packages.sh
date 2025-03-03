#!/bin/bash

# List of packages to install
PACKAGES=("git" "vim" "curl")

# Function to check and install a package
install_package() {
    if dpkg -l | grep -qw "$1"; then
        echo "✅ $1 is already installed."
    else
        echo "📦 Installing $1..."
        sudo apt-get install -y "$1" && echo "✅ $1 installed successfully!" || echo "❌ Failed to install $1."
    fi
}

# Loop through each package and install if needed
for package in "${PACKAGES[@]}"; do
    install_package "$package"
done
