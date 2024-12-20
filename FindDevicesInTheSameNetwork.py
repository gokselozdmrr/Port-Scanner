import os
import platform
from concurrent.futures import ThreadPoolExecutor

# Ping atılacak IP aralığını belirle
network = "192.168.18."
start_ip = 3
end_ip = 254

# Ping fonksiyonu
def ping(ip):
    command = f"ping -c 1 {ip}" if platform.system().lower() != "windows" else f"ping -n 1 {ip}"
    response = os.system(command)
    if response == 0:
        print(f"[+] Cihaz bulundu: {ip}")

# Thread kullanarak tarama yap
print("Ağ taraması başlıyor...\n")
with ThreadPoolExecutor(max_workers=10) as executor:
    for i in range(start_ip, end_ip + 1):
        ip = f"{network}{i}"
        executor.submit(ping, ip)

print("\nTarama tamamlandı!")
