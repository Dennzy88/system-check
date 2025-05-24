import psutil
import platform
import time

def format_gb(value):
    return round(value / (1024 ** 3), 2)

print("📊 SYSTEM PERFORMANCE REPORT\n")

# OS info
print(f"Operativni sistem: {platform.system()} {platform.release()}")
print(f"Procesor: {platform.processor()}")

# CPU info
print(f"Trenutno CPU opterećenje: {psutil.cpu_percent(interval=1)}%")

# RAM info
ram = psutil.virtual_memory()
print(f"Ukupna RAM memorija: {format_gb(ram.total)} GB")
print(f"Dostupna RAM memorija: {format_gb(ram.available)} GB")
print(f"Korišćena RAM memorija: {format_gb(ram.used)} GB")
print(f"Iskorišćenost RAM-a: {ram.percent}%")

# Disk info
disk = psutil.disk_usage('/')
print(f"Ukupan prostor na disku: {format_gb(disk.total)} GB")
print(f"Slobodan prostor na disku: {format_gb(disk.free)} GB")
print(f"Iskorišćenost diska: {disk.percent}%")

# Aktivni procesi
print("\n🔍 Top 5 procesa po korišćenju memorije:")
for proc in sorted(psutil.process_iter(['pid', 'name', 'memory_info']),
                   key=lambda p: p.info['memory_info'].rss,
                   reverse=True)[:5]:
    print(f"PID {proc.info['pid']}: {proc.info['name']} - {round(proc.info['memory_info'].rss / (1024 ** 2), 2)} MB")
