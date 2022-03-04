vetor = []
qntNum = int(input("Informe a quantidade de numeros da lista: "))
for x in range(qntNum):
    numero = int(input("Digite o Numero: "))
    vetor.append(numero)
num = int(input("Informe o numero para o calculo das diferencas entre os numeros6: "))
pares = 0
for x in range(len(vetor)):
    for y in range(len(vetor)):
        if vetor[x] + num == vetor[y]:
            pares = pares + 1
numStr = str(num)
paresStr = str(pares)
print("a diferenca "+numStr+" aparece "+paresStr+" vezes.")
input("Aperte enter para sair.")