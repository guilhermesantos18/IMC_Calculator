from time import sleep
print('-' * 55)
print(f'Calculadora IMC'.center(55))
print('-' * 55)
print('Digite as seguintes informações para calcular o seu imc.')
peso = float(input('Qual é o seu peso: '))
altura = float(input('Qual é a sua altura: '))
imc = peso / altura**2
print('-' * 55)
print('Calculando...')
sleep(1)
if imc < 17:
    print(f'De acordo com o seu imc de {imc:.2f} você está, Abaixo do peso grave.')
elif 17 >= imc < 18.50:
    print(f'De acordo com o seu imc de {imc:.2f} você está, Abaixo do peso.')
elif 18.50 >= imc < 25:
    print(f'De acordo com o seu imc de {imc:.2f} você está com, Peso normal.')
elif 25 >= imc < 30:
    print(f'De acordo com o seu imc de {imc:.2f} você está com, Sobrepeso.')
elif 30 >= imc < 35:
    print(f'De acordo com o seu imc de {imc:.2f} você está com, Obesidade grau 1.')
elif 35 >= imc < 40:
    print(f'De acordo com o seu imc de {imc:.2f} você está com, Obesidade grau 2.') 
else:
    print(f'De acordo com o seu imc de {imc:.2f} você está com, Obesidade grau 3 .')  
