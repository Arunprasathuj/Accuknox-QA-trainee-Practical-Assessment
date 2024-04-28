import re
from collections import Counter

def analyze_log(log_file):
    # Regular expressions to extract relevant information from log lines
    ip_regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    status_code_regex = r'\s(\d{3})\s'
    requested_page_regex = r'\"(GET|POST) ([^\s]+)'

    # Initialize counters
    total_requests = 0
    status_code_counts = Counter()
    requested_pages = Counter()
    ip_address_counts = Counter()

    # Read and process each line of the log file
    with open(log_file, 'r') as file:
        for line in file:
            total_requests += 1
            ip_address_match = re.search(ip_regex, line)
            status_code_match = re.search(status_code_regex, line)
            requested_page_match = re.search(requested_page_regex, line)
            
            if ip_address_match and status_code_match and requested_page_match:
                ip_address = ip_address_match.group()
                status_code = status_code_match.group(1)
                requested_url = requested_page_match.group(2)
                requested_page = requested_url.split('?')[0]  # Extract the page name from the URL
                status_code_counts[status_code] += 1
                requested_pages[requested_url] += 1
                ip_address_counts[ip_address] += 1
            else:
                print(f"Warning: Failed to extract information from line: {line.strip()}")

    # Generate the summarized report
    report = []
    report.append("Log Analysis Report:")
    report.append("---------------------")
    report.append(f"Total Requests: {total_requests}\n")
    report.append("Status Code Counts:")
    for status_code, count in status_code_counts.items():
        report.append(f"{status_code}: {count}")
    report.append("\nTop 10 Most Requested Pages:")
    for page, count in requested_pages.most_common(10):
        report.append(f"{page}: {count}")
    report.append("\nTop 10 IP Addresses with Most Requests:")
    for ip_address, count in ip_address_counts.most_common(10):
        report.append(f"{ip_address}: {count}")

    # Print the summarized report
    print('\n'.join(report))

# Example usage:
analyze_log("access.log")
