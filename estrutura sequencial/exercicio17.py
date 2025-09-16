#fiz esse exercicio mas como um teste para entender melhor o uso do math.ceil e math.floor
#porque eu podia fazer igual o exercicio16.py
import math # para usar o ceil e floor


area = float(input("Digite qual o tamanho em metros quadrados da área que será pintada: "))

# Cálculo de litros com 10% de folga
litros = (area / 6) * 1.1

#opção do usuário
print("\nEscolha a forma de compra:")
print("1 - Apenas latas de 18L")
print("2 - Apenas galões de 3,6L")
print("3 - Misturar latas e galões")

opcao = int(input("Digite 1, 2 ou 3: "))


if opcao == 1:
    latas = math.ceil(litros / 18)
    preco = latas * 80
    print(f"\nLatas: {latas} → Preço: R$ {preco}")

elif opcao == 2:
    galoes = math.ceil(litros / 3.6)
    preco = galoes * 25
    print(f"\nGalões: {galoes} → Preço: R$ {preco}")

elif opcao == 3:
    latas_mix = math.floor(litros / 18)
    resto = litros - (latas_mix * 18)
    galoes_mix = math.ceil(resto / 3.6)

    if galoes_mix == 0:
        preco = latas_mix * 80
        print(f"\nLatas: {latas_mix} → Preço: R$ {preco}")

    if latas_mix == 0:
        preco = galoes_mix * 25
        print(f"\nGalões: {galoes_mix} → Preço: R$ {preco}")
 
    else:
        preco = (latas_mix * 80) + (galoes_mix * 25)
        print(f"\nLatas: {latas_mix} e Galões: {galoes_mix} → Preço: R$ {preco}")
    
else:
    print("Opção inválida! Digite 1, 2 ou 3.")
