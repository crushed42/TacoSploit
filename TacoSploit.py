import socket
import time
import sys
import argparse

# Function to simulate typing effect
def type_effect(text, speed=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Function to scan ports on a given IP
def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Timeout after 1 second
        result = s.connect_ex((ip, port))  # Try to connect to the port
        if result == 0:
            open_ports.append(port)
        s.close()
    return open_ports

# Taco-themed port scanning function
def taco_sploit_scan(ip):
    # Display taco intro
    type_effect(f"Scanning IP: {ip}...\n", 0.1)
    time.sleep(1)
    
    # Define common ports to scan
    taco_ports = [21, 22, 23, 80, 443, 8080, 3306, 5432, 5900]

    # Start scanning
    type_effect("TacoSploit is scanning... Getting the taco toppings...\n", 0.1)
    open_ports = scan_ports(ip, taco_ports)

    # Taco report
    if open_ports:
        type_effect(f"\nTaco hack successful! Open taco ports found at {ip}:\n", 0.1)
        for port in open_ports:
            type_effect(f"Port {port} is open, looks like a spicy taco here!\n", 0.1)
    else:
        type_effect(f"\nNo open taco ports found at {ip}. Maybe the taco shell is closed...\n", 0.1)

# Main function to handle user input and the port scanning process
def main():
    # Argument parser for getting the IP from user input
    parser = argparse.ArgumentParser(description='TacoSploit - A Taco-themed Port Scanner!')
    parser.add_argument('ip', help='IP address to scan (e.g., 192.168.1.1)')
    args = parser.parse_args()

    ip = args.ip
    taco_sploit_scan(ip)

if __name__ == "__main__":
    main()