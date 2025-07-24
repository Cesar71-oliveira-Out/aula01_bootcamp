CONSTANT_BONUS = 1000

# Digite o nome
# Digite o salário
# Digite percentual do Bônus
# Cálcule o valor do Bônus

nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
bonus = float(input("Digite o percentual do Bônus: "))
valor_do_bonus = CONSTANT_BONUS + salario * bonus

# Para print de variáveis deve-se usar o f print(f...)
print(f"Você {nome} possui o bônus no valor de {valor_do_bonus}")