import psutil
import logging
import time

# Define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
PROCESS_THRESHOLD = 100

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# Function to check CPU usage
def check_cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > CPU_THRESHOLD:
        logging.warning(f"CPU usage is high - {cpu_percent}%")

# Function to check memory usage
def check_memory():
    memory_percent = psutil.virtual_memory().percent
    if memory_percent > MEMORY_THRESHOLD:
        logging.warning(f"Memory usage is high - {memory_percent}%")

# Function to check disk usage
def check_disk():
    disk_percent = psutil.disk_usage('/').percent
    if disk_percent > DISK_THRESHOLD:
        logging.warning(f"Disk usage is high - {disk_percent}%")

# Function to check running processes
def check_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        logging.warning(f"Number of running processes is high - {process_count}")

# Main function
def main():
    logging.info("System Health Check started")
    while True:
        check_cpu()
        check_memory()
        check_disk()
        check_processes()
        time.sleep(5)  # Adjust the sleep time as needed

# Run the main function
if __name__ == "__main__":
    main()
