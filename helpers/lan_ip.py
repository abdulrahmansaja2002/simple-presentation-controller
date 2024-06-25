import socket

def get_local_ip():
    try:
        # Create a dummy socket connection to an external address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        # Doesn't matter if the address is reachable
        s.connect(('10.254.254.254', 1))
        local_ip = s.getsockname()[0]
        s.close()
    except Exception:
        local_ip = '127.0.0.1'
    return local_ip

if __name__ == "__main__":
    local_ip = get_local_ip()
    print(f"My local IP address is: {local_ip}")
