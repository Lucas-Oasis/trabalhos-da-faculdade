import time
inicio = time.time()

print('Olá, mundo!')

fim = time.time()
print(f"Tempo de execução: {(fim - inicio) * 1000:.4f}ms")