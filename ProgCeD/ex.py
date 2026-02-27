import psutil
#enquanto a biblioteca não é utilizada, ela permanece sublinhada

def estado_processo(pid):
    try:
        processo = psutil.Process(pid)
        estado = processo.status()
        return estado
    except psutil.NoSuchProcess:
        return "o Processo não foi encontrado!!!"

#Bloco principal

numero = int(input("Digite um número: "))
estado = estado_processo(numero)
print(f"O estado do Processo com PID {numero} é {estado}!")