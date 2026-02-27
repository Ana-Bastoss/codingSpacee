import psutil

for X in psutil.process_iter(['pid','name']):
    try:
        print(f"{X.info['pid']} \t {X.info['name']}")
    except(psutil.NoSuchProces, psutil.AccessDenied, psutil.ZombieProcess):
        pass
    