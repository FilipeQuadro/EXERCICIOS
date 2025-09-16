ganho_hora = float(input('Quanto você ganha por hora? '))
horas_trabalhadas = float(input('Quantas horas você trabalha por mês? '))

salario_bruto = ganho_hora * horas_trabalhadas

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato


print('Salário Bruto: ', salario_bruto)
print('IR (11%): ', ir)
print('INSS (8%): ', inss)
print('Sindicato (5%): ', sindicato)
print('Salário Líquido: ', salario_liquido)