import math

def analise(l):
    menor = math.inf
    maior = -math.inf
    pares = 0

    for n in l:

        if n%2 == 0:
            pares += 1

        if n < menor:
            menor = n

        if n > maior:
            maior = n

    soma = sum(l)
    media = soma/len(l)

    print(f'Média: {media:.2f}\n'
          f'Maior número: {maior}\n'
          f'Menor número: {menor}\n'
          f'Quantidade de números pares: {pares}')