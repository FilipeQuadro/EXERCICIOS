import math  # pesquisei e descobrir sobre o ceil para arredondar pra cima o valor

area = float(input("Digite qual o tamanho em metros quadrados da área que será pintada: "))

litros_necessarios = area / 3

latasreais = litros_necessarios / 18

latas_comprar = math.ceil(latasreais)

preco_total = latas_comprar * 80

print("\n   Resultado    ")
print("Área a ser pintada:", area, "m²")
print("Litros necessários:", round(litros_necessarios, 2))
print("Quantidade de latas necessárias:", latas_comprar)
print("Preço total: R$", preco_total)
