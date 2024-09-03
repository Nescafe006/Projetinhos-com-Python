def coletar_numeros(qtd):
    numeros = []
    for i in range(qtd):
        while True:
            try:
                num = int(input(f'Digite o número {i + 1} de {qtd}: '))
                numeros.append(num)
                break  # Sai do loop se a entrada for válida
            except ValueError:
                print("Entrada inválida! Por favor, digite um número inteiro.")
    return numeros

# Função principal
def main():
    qtd_numeros = 10
    numeros = coletar_numeros(qtd_numeros)

    if numeros:  # Verifica se a lista não está vazia
        soma = sum(numeros)
        maior = max(numeros)
        menor = min(numeros)

        print('Soma:', soma)
        print('Maior:', maior)
        print('Menor:', menor)
    else:
        print("Nenhum número foi inserido.")

# Executa a função principal
main()
