contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
             'seis', 'sete', 'oito', 'nove', 'dez','onze', 
             'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
               'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre (0 e 20): '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {contagem[num]}')
        break
    else:
        print('Número inválido! Tente novamente.')
        
