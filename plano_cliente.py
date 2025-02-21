# Desafio
# Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude aos seus clientes a escolherem o plano de internet ideal com base em seu consumo mensal de dados. Para a resolução, você pode solicitar ao usuário que insira o seu consumo, sendo este um valor 'float'. Crie uma função chamada recomendar_plano para receber o consumo médio mensal de dados informado pelo cliente, além de utilizar estruturas condicionais para fazer a verificação e retornar o plano adequado.

# Planos Oferecidos:

# - Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.
# - Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.
# - Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.

# Entrada
# Como entrada solicite o consumo médio mensal de dados em GB (float).

# Saída
# Retorne o plano ideal para o cliente de acordo com o consumo informado na entrada.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada	Saída
# 10

# Plano Essencial Fibra - 50Mbps

# 19

# Plano Prata Fibra - 100Mbps
# 21

# Plano Premium Fibra - 300Mbps

#################################################################################################################

#Escolhendo o plano de consumo ideal

# Define uma função chamada recomendar_plano que recebe um parâmetro 'consumo'
def recomendar_plano(consumo):

    # Se o consumo for menor ou igual a 10 GB, recomenda o Plano Essencial Fibra
    if consumo <= 10:
        print(f'Seu consumo é de {consumo} GB')  # Exibe o consumo do usuário
        print()  # Imprime uma linha em branco para organização da saída
        print('O plano ideal é o Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB')

    # Se o consumo estiver entre 10 e 20 GB, recomenda o Plano Prata Fibra
    elif 10 < consumo <= 20:
        print(f'Seu consumo é de {consumo} GB')  # Exibe o consumo do usuário
        print()  # Linha em branco
        print('O plano ideal é o Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB')

    # Se o consumo for maior que 20 GB, recomenda o Plano Premium Fibra
    elif consumo > 20:
        print(f'Seu consumo é de {consumo} GB')  # Exibe o consumo do usuário
        print()  # Linha em branco
        print('O plano ideal é o Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB')

    # Caso um valor inválido seja digitado (essa condição nunca será ativada nesse código)
    else:
        print('Valor digitado incorreto, tente novamente')

# Exibe uma mensagem de boas-vindas
print('Seja bem-vindo, vamos consultar o seu plano')
print()  # Linha em branco

# Solicita que o usuário insira seu consumo mensal e converte a entrada para um número decimal (float)
consumo = float(input('Informe o seu consumo mensal: '))

print()  # Linha em branco
    
# Chama a função recomendar_plano passando o valor inserido pelo usuário como argumento
recomendar_plano(consumo)

print()  # Linha em branco para organização da saída
