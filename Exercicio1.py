
def Main():
    pergunta = int(input("Carregar matriz de adjacencia(1) ou criar nova(2)? "))
    confere = False
    while (confere == False):
        if (pergunta == 1):
            arq = str(input("Digito o nome da matriz: "))
            arquivo = open(arq + ".txt", "r+")
            print(arquivo.readlines())
            confere = True
        elif (pergunta == 2):
            n = int(input("Tamanho da Matriz de adjacencia: "))
            matriz = [0] * n
            for x in range(0, n):
                matriz[x] = [0] * n
            print(matriz)
            for i in range(0, n):
                for j in range(i + 1, n):
                    entrada = "Coluna {} Linha {} possui aresta('S' para sim e 'N' para nao)? ".format(i, j)
                    confere = str(input(entrada))
                    if (i == j):
                        matriz[i][j] = 0
                    else:
                        corrige = False
                        while (corrige == False):
                            if (confere.upper() == "S"):
                                matriz[i][j] = 1
                                corrige = True
                            elif (confere.upper() == "N"):
                                matriz[i][j] = 0
                                corrige = True
                            else:
                                corrige = False
                                confere = str(input(entrada))
                    matriz[j][i] = matriz[i][j]
                    print(matriz)
            nomearq = input("Nome do arquivo: ")
            arquivo = open(nomearq + ".txt", "w")
            for i in range(0, n):
                for j in range(0, n):
                    arquivo.write(str(matriz[i][j]) + " ")
            confere = True
        elif (pergunta > 2):
            print("Entrada inválida")
            pergunta = int(input("Carregar matriz de adjacencia(1) ou criar nova(2)? "))
Main()