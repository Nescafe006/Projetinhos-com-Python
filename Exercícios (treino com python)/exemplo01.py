numeros = []
for i in range(10):
    num = int(input('Digite um número: '))
    numeros.append(num)


soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)


print('Soma:', soma)
print('Maior:', maior)
print('Menor:', menor)