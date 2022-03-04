import math
frase = "frase para criptografar aqui"
fraseSemEspacos = frase.replace(" ", "")
passo = int(math.ceil(math.sqrt(len(fraseSemEspacos))))
tamanho = len(fraseSemEspacos)
grid = []
for i in range(passo):
    lista = []
    for j in range(i, len(fraseSemEspacos), passo):
        lista.append(fraseSemEspacos[j])
    grid.append("".join(lista))
print(grid)