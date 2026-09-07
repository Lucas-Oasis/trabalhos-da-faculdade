import time
inicio = time.time()
for i in range(1, 1001):
    print(i)
fim = time.time()
print(f"Tempo de execução: {(fim - inicio) * 1000:.4f}ms")