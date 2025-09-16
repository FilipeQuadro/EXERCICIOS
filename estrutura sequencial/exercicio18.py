tamanho_arquivo = float(input("Digite o tamanho do arquivo (em MB): "))
velocidade_link = float(input("Digite a velocidade do link (em Mbps): "))

tempo_segundos = (tamanho_arquivo * 8) / velocidade_link
tempo_minutos = tempo_segundos / 60

print(f"\nO tempo aproximado de download é {tempo_minutos:.2f} minutos.")
