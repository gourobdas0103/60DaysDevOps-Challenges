import psutil
import time

def monitor_system():
    """Continuously monitor CPU and memory usage every 5 seconds."""
    try:
        while True:
            # Get CPU and memory usage
            cpu_usage = psutil.cpu_percent(interval=1)  # CPU usage in percentage
            memory_info = psutil.virtual_memory()  # Memory usage details

            # Print system usage statistics
            print(f"🔲 CPU Usage: {cpu_usage}% | ⛁ Memory Usage: {memory_info.percent}%")

            # Wait for 5 seconds before the next check
            time.sleep(5)

    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user.")

# Run the monitoring function
monitor_system()
