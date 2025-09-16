gb = float(input('Insira o tamanho do arquivo em GBs: '))
mb = gb * 1_024
kb = gb * 1_024 * 1_024
print(f'O arquivo tem {mb}MBs ou {kb} KBs.')