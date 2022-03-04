arr = []
qntNum = int(input("Informe a quantidade de numeros do array: "))
for x in range(qntNum):
    numero = int(input("Digite o Numero: "))
    arr.append(numero)
print(arr)
mediana = len(arr) // 2
arr.sort()
print("A mediana e: ")
if not len(arr) % 2:
    print((arr[mediana-1]+arr[mediana])/2)
print(arr[mediana])