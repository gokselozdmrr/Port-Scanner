import socket
import threading

# Hedef IP ve port aralığının kullanıcıdan alınması

target_ip = input("Enter Target IP: ")
start_port = int(input("Enter Start Port: "))
end_port = int(input("Enter End Port: "))

def scan_port(ip, port):
    # Bağlantı denemesi
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"[+] Port {port} is open")

        sock.close()
    except:
        pass

# Çoklu Thread ile kullanarak tarama

print("\nScanning is starting")

threads = []

for port in range(start_port, end_port+1):
    t = threading.Thread(target=scan_port, args=(target_ip, port))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("\nScanning is finished")
