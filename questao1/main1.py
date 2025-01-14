# Questão 1: Calculando o valor de SOMA

INDICE = 13  # Valor inicial do índice
SOMA = 0     # Variável para armazenar a soma
K = 0        # Variável de controle

# Loop para somar os valores de 1 até o INDICE
while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

# Exibindo o resultado final
print(f"O valor final da variável SOMA é: {SOMA}")  # Resultado: 91

# Valor esperado
# SOMA = 1 + 2 + 3 + ... + 13 = 91