import psutil

Processo = psutil.Process(0)

MI = Processo.memory_info()

MemoriaFisica = MI.rss / (1024 * 1024) #real,fisica(RAM)
MemoriaVirtual = MI.vms / (1024 * 1024) #virtual

print(f"{MemoriaFisica} \t {MemoriaVirtual}")