import os

# Show available NMAP options
print("NMAP options:")
print("-p <port ranges>: Scan specified ports")
print("-sS: TCP SYN scan")
print("-sU: UDP scan")
print("-O: OS detection")
print("-sV: Service detection")
print("-sC: Script scan with default scripts")
print("-A: Aggressive scan options")
print("-v: Increase verbosity")
print("-T<0-5>: Set timing template (higher is faster)")
print("-oA <basename>: Output results to files in the given formats")

# Get target IP address from user
target_ip = input("Enter target IP address: ")

# Get NMAP options from user
nmap_options = input("Enter NMAP options: ")

# Run NMAP command with sudo
os.system(f"sudo nmap {target_ip} {nmap_options}")

# Generate file name for output
file_name = f"nmap_scan_output_{target_ip}.txt"
file_num = 1

# Check if file already exists, increment number until unique name is found
while os.path.exists(file_name):
    file_num += 1
    file_name = f"nmap_scan_output_{target_ip}_{file_num}.txt"

# Run NMAP command and save output to file
os.system(f"sudo nmap {nmap_options} -oN {file_name} {target_ip}")

while True:
    # Get user input for target IP and NMAP options
    target_ip = input("Enter the target IP: ")
    nmap_options = input("Enter NMAP options (e.g. -p 80,443): ")

    # Generate file name for output
    file_name = f"nmap_scan_output_{target_ip}.txt"
    file_num = 1

    # Check if file already exists, increment number until unique name is found
    while os.path.exists(file_name):
        file_num += 1
        file_name = f"nmap_scan_output_{target_ip}_{file_num}.txt"

    # Run NMAP command and save output to file
    os.system(f"sudo nmap {nmap_options} -oN {file_name} {target_ip}")

    # Ask if user wants to scan another target
    another_scan = input("Do you want to scan another target? (y/n) ")
    if another_scan.lower() != "y":
        break

