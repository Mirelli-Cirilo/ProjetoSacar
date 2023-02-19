valores = (int(input('Digite um valor:')),
           int(input('Digite outro valor:')),
           int(input('Digite mais um valor:')),
           int(input('Digite último valor:')))

for valor in valores:
    print(f'{valor},', end=' ')
print('Foram os valores digitados!', end=' ')
print(f'\nO número 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O número 3 aparece em {valores.index(3)+1}° posição')
else:
    print('O número três não foi digitado!')
print('Os valores pares digitados foram', end=' ')
for valor in valores:
    if valor % 2 == 0:
        print(valor, end=' ')
