import psutil

Processo = psutil.Popen(0)

MI = Procsso.memory_info()

MemoriaFisica = MI.rss / (1024 * 1024)
Memoria