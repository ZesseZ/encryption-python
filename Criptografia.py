"""_______________________________________________________________________________________________"""
"""COMO USAR O PROGRAMA: """
"""1 - Selecione a opção de criptografar uma mensagem (digite 1)"""
"""em seguida, digite uma sequência de números para ser usado como chave (ex: 5 4 8 3),"""
"""(Lembre-se da chave escolhida!!! Se puder, anote ela.)"""
"""Após isso, você poderá digitar algo de seu interesse, como plavras e letras"""
"""(Por favor, use # como espaço)"""
"""Depois de realizar essas etapas, o programa irá de devolver uma matriz com diversos números,"""
"""você precisa anotar esses números para a descriptografia, então por favor,"""
"""copie e cole eles em um bloco de notas ou algo parecido."""

"""2 - Após isso, reinicie o programa e dessa vez digite 2 para a descriptografia."""
"""Ele irá solicitar a mesma chave que foi usada para a criptografia"""
"""Insira essa chave para que em seguida você possa inserir os números da matriz obtida."""
"""Dê preferência para digitar esses números um a um para evitar erros!!!"""
"""Após isso o programa irá retornar aquilo que você criptografou..."""
"""________________________________________________________________________________________________"""
import numpy as np

# Inicialização
print(" _ __ _   _ _  _ _  _ _ ")
print("/  || _ \\ \ / //  _ \\|  _  ||  _  \\|  _|| _ \\")
print("\\ `--. | |/ / \\ V /| /  \\/| | | || | | || |_  | |_/ /")
print(" `--. \\|  _/   \\ / | |    | | | || | | ||  _| |    / ")
print("/\\/ /| |      | |  | \\/\\ \\/ /| |/ / | | | |\\ \\ ")
print("\\/ \\|      \\/   \\/ \\/ |/  \\/ \\| \\|")
print("\n\n1- Criptografia")
print("2- Descriptografia")
print("0- Sair")

seletor = input("VAMOS JOGAR? ")



#criptografia
if seletor == "1":
   
    # Solicita a matriz-chave
    chave_input = input("Digite os 4 números da matriz-chave 2x2 (ex.: 5 4 8 3): ").split()
    matriz_bheta = np.array([float(chave_input[0]), float(chave_input[1]), float(chave_input[2]), float(chave_input[3])]).reshape(2, 2)
    
    alpha = input("Digite algo(utilize # como espaço): ").upper()  # Entrada sofre conversão para maiúsculo
    matriz_alpha = []
    numeros = []
    

    for i in range(len(alpha)):
        char = alpha[i]
        if 'A' <= char <= 'Z':
           
            num = ord(char) - ord('A')  # Mapeia A=0, B=1, ..., Z=25
            numeros.append(num)
            #print(f"'{char}' {num}")  # Comentado para depuração opcional
        elif char == '#':
           
            num = 26  # Mapeia "#" como 26
            numeros.append(num)
            #print(f"'{char}' {num}")  # Comentado para depuração opcional
        else:
            print(f"'{char}' não é uma letra ou # válido (ignorado).")

    
    if len(numeros) % 2 != 0:
       
        numeros.append(26)  # Adiciona # se o total for ímpar
    n_linhas = len(numeros) // 2  # Número de linhas (pares)
    matriz_alpha = [numeros[i:i + 2] for i in range(0, len(numeros), 2)]  # Cria pares diretamente

    # Converte para array NumPy
    matriz_alpha_np = np.array(matriz_alpha) 

    # Multiplicação
    result = np.dot(matriz_alpha_np, matriz_bheta)

    #print("alpha\n", matriz_alpha_np)
    #print("bheta\n", matriz_bheta)
    print("Criptografia:\n", result)


elif seletor == "2":
    # Solicita a matriz-chave
    chave_input = input("Digite os 4 números da matriz-chave 2x2 (ex.: 5 4 8 3): ").split()
    matriz_bheta = np.array([float(chave_input[0]), float(chave_input[1]), float(chave_input[2]), float(chave_input[3])]).reshape(2, 2)
    
    
    alpha = input("Digite os numeros da matriz: ").split() #separa os numeros
   
    numeros = [float(x) for x in alpha] #faz a conversão para float
   
    n_linhas = len(numeros) // 2
    
    if len(numeros) % 2 != 0: #checa se forma pares para formar matriz
        print("ERRO!: valor errado para matriz")
   
    else:
       
        matriz_alpha_np = np.array(numeros).reshape(n_linhas, 2) # converte tudo para matriz
        reverse_bheta = np.linalg.inv(matriz_bheta) # inverte matriz chave
        descrip = np.dot(matriz_alpha_np, reverse_bheta) # faz a descriptografia
       
        # Ajuste de padding
        if n_linhas > 1 and (descrip[-1, 0] > 25 or descrip[-1, 1] > 25):
            n_linhas -= 1
        
        # Transforma a matriz resultante em letras
        texto = ""
        for i in range(n_linhas):
            for j in range(2):
                valor = round(descrip[i, j])
                if 0 <= valor <= 25:
                    texto += chr(int(valor) + ord('A'))
                elif valor == 26:
                    texto += " "
        print("Texto descriptografado:", texto)

elif seletor == "0":
    print("SHUTDONW")