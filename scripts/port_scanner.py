# A simple TCP port scanner for educational purposes

import socket


def scan_port(target, port):
    """Scan a single port. Returns True if open."""

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    sock.close()

    return result == 0


def main():
    target = input("Enter target IP: ")

    common_ports = [
        21,
        22,
        23,
        25,
        53,
        80,
        110,
        443,
        3306,
        8080
    ]

    print(f"\n🔍 Scanning {target}...\n")

    open_ports = []

    for port in common_ports:

        if scan_port(target, port):
            print(f"  ✅ Port {port}: OPEN")
            open_ports.append(port)

        else:
            print(f"  ❌ Port {port}: closed")

    print(
        f"\n📊 Scan complete. "
        f"{len(open_ports)} ports open: {open_ports}"
    )


if __name__ == "__main__":
    main()
