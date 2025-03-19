def make_oxidized_python_distribution(pyoxidizer):
    dist = pyoxidizer.default_python_distribution()
    policy = pyoxidizer.default_resource_policy()

    # Define the executable
    exe = pyoxidizer.add_python_executable(
        name="cli_tool",
        python_distribution=dist,
        policy=policy,
    )

    # Add your script
    exe.add_python_resources(exe.pip_install(["cli_tool.py"]))

    # Enable single binary mode
    exe.packaging_mode = "standalone_exe"

    # Set entry point
    exe.set_entry_point("cli_tool", "main")

    return exe