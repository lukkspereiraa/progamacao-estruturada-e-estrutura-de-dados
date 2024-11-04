import random
def bubbleSort(array):
    n = len(array)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux
                

# Gerar um array com 200.000 números desordenados
array = random.sample(range(1, 2001), 2000)
array[:10]  # Mostrar os 10 primeiros números para verificação

print(f'vetor ordernado: {array}')
bubbleSort(array)
print(array)