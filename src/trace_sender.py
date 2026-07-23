import pyshark

capture = pyshark.FileCapture("SMTP.pcap", 
                              display_filter='smtp contains "FROM"')

source = str(capture[0].ip.src)
destination = str(capture[0].ip.dst)

print("Step 1: Analyzing SMTP traffic in the packet capture to identify the sender.")
print(f"The email was sent from IP address {source} to mail server {destination}.")
print(f"Next, we'll check the DHCP log to see which device held {source} at the time of the incident.")
print("#"*80)

with open(r'D:\1.Cybersecurity Learning\1. Codepath Intermediate Cybersecurity\Unit 1\sample_files\DHCP.txt', 'r') as file:
    txt_lines = file.readlines()
    
    print(f"Step 2: Searching DHCP logs for lease activity involving {source}...\n")
    for line in txt_lines:
        if source in line:
            print(f"\t{line}")

print("Step 3: Based on the DHCP lease timeframe.")
host_name = input("Enter the host device name assigned to this IP: ")

print(f"\nStep 3: Cross-referencing {host_name} against the Windows Security log.")
print(f"Pulling logon/logoff events tied to {host_name} to confirm which user account was active during the email timestamp.")
print("#"*80)
with open(r'D:\1.Cybersecurity Learning\1. Codepath Intermediate Cybersecurity\Unit 1\sample_files\security_log.txt', 'r') as file:
    txt_lines = file.readlines()

    for line in txt_lines:
        if host_name in line:
            print(f"\t{line}")
