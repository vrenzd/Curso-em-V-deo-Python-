matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('\nMatriz 3x3:')
for linha in matriz:
    for elemento in linha:
        print(f'{elemento:^5}', end='')
    print()
    