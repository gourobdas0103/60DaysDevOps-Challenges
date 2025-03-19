import paramiko

# List of servers
servers = [
    {"host": "192.168.1.100", "user": "ubuntu", "password": None, "key": "/path/to/private/key"},
    {"host": "192.168.1.101", "user": "ubuntu", "password": "yourpassword", "key": None},
]

def run_ssh_command(host, user, password, key, command):
    """Runs an SSH command using Paramiko with support for both key and password authentication."""
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        if key:
            client.connect(hostname=host, username=user, key_filename=key, timeout=10)
        else:
            client.connect(hostname=host, username=user, password=password, timeout=10)

        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()

        print(f"✅ {host} Output:\n{output}\n" if output else f"❌ {host} Error:\n{error}\n")
        client.close()
    except Exception as e:
        print(f"❌ Failed to connect to {host}: {e}")

# Run command on all servers
for server in servers:
    print(f"🔌 Connecting to {server['host']}...")
    run_ssh_command(server["host"], server["user"], server.get("password"), server.get("key"), "uptime")
