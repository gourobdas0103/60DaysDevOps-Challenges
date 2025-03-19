from setuptools import setup

setup(
    name="greet-cli",
    version="1.0",
    py_modules=["cli_tool_click"],  # Update for argparse version if needed
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "greet=cli_tool_click:greet",
        ],
    },
)
