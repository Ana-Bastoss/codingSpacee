import psutil

for X in psutil.process_iter(['pid','name','status']):
    try:
        if X.info['status'] == psutil.STATUS_RUNNING:
            print(f"{X.info['pid']} \t {X.info['name']}")
    except(psutil.NoSuchProces, psutil.AccessDenied, psutil.ZombieProcess):
        pass


# == é para verificar se é igual
# != é para verificar se é DIFERENTE