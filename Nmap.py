import socket
import sys

def port_scanner():
    default_ip = '127.0.0.1'
    target = input(f"Enter IP address (default {default_ip}): ").strip() or default_ip
    port_input = input("Enter port (e.g. 80) or range (e.g. 20-1024): ").strip()

    try:
        if '-' in port_input:
            start, end = map(int, port_input.split('-', 1))
            ports = range(max(1, start), min(65535, end) + 1)
        else:
            ports = [int(port_input)]
    except ValueError:
        print("Invalid format. Use numbers or 1-65535 range.")
        return

    print(f"\nScanning {target}...")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            status = "OPEN" if result == 0 else "closed"
            print(f"Port {port}: {status}")

if __name__ == "__main__":
    try:
        port_scanner()
    except KeyboardInterrupt:
        print("\nScan stopped by user.")