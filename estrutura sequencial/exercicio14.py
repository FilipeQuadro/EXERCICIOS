peso_peixe = float(input("Digite o peso do peixe em quilos: "))
multa = 50

if peso_peixe > 50:
    excesso = peso_peixe - 50
    valor_multa = excesso * 4
    print(f"O peso do peixe passou em {excesso:.2f} kg do limite permitido. A multa é de R$ {valor_multa:.2f}.")
elif peso_peixe <= 50:
    print("O peso do peixe está dentro do limite permitido. Não há multa.")