altura = float(input('Qual sua altura em cm: '))
peso = float(input('Qual o seu peso em kg: '))

IMC = peso / (altura / 100) ** 2

if IMC < 18.5:
    print(f'Seu imc é de: {IMC} ,e é considerado magreza.Vai comer.')

elif IMC >= 18.5 and IMC < 24.9:
    print(f'Seu imc é de: {IMC} ,e é considerado normal.Não se preocupe.')

elif IMC >= 25.0 and IMC < 29.9:
    print(f'Seu imc é de: {IMC} ,e é considerado sobrepeso.Melhore sua dieta.')

elif IMC >= 30.0 and IMC < 39.0:
    print(f'Seu imc é de: {IMC} ,e é considerado obesidade.Suas veias estão entupindo.')

else:
    print('PARE DE COMER IMEDIATAMENTE')