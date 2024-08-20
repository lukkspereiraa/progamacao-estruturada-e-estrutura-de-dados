def processar_dados_sensores(dados_sensores):

    contagem_T, contagem_P, contagem_U = 0, 0, 0
    soma_T, soma_P, soma_U = 0, 0, 0

    tipo = None
    valor = ""
    

    for char in dados_sensores:
        if char == 'T' or char == 'P' or char == 'U':
            if tipo is not None:
                if tipo == 'T':
                    contagem_T += 1
                    soma_T += int(valor)
                elif tipo == 'P':
                    contagem_P += 1
                    soma_P += int(valor)
                elif tipo == 'U':
                    contagem_U += 1
                    soma_U += int(valor)
            
            tipo = char
            valor = ""
        elif char == '|':

            if tipo == 'T':
                contagem_T += 1
                soma_T += int(valor)
            elif tipo == 'P':
                contagem_P += 1
                soma_P += int(valor)
            elif tipo == 'U':
                contagem_U += 1
                soma_U += int(valor)

            tipo = None
            valor = ""
        else:

            valor += char

    media_T = soma_T / contagem_T if contagem_T > 0 else 0
    media_P = soma_P / contagem_P if contagem_P > 0 else 0
    media_U = soma_U / contagem_U if contagem_U > 0 else 0

    return { 
        "T": {"count": contagem_T, "sum": soma_T, "avg": media_T}, 
        "P": {"count": contagem_P, "sum": soma_P, "avg": media_P}, 
        "U": {"count": contagem_U, "sum": soma_U, "avg": media_U}
    }

dados_sensores = "T25|P1013|U60|T24|T26|P1012|U65|U64|P1011|"
resultado = processar_dados_sensores(dados_sensores)
print(resultado)
