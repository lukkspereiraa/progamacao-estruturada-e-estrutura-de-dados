import numpy as np

precos_acoes = np.array([
    [150, 200, 180, 220, 170], 
    [155, 205, 185, 225, 175], 
    [160, 210, 190, 230, 180],
    [165, 215, 195, 235, 185], 
    [170, 220, 200, 240, 190], 
    [175, 225, 205, 245, 195], 
    [180, 230, 210, 250, 200]
])

media_diaria = np.mean(precos_acoes, axis=0)
print("Média diária dos preços das ações para cada empresa:")
print(f"Empresa A: {media_diaria[0]:.2f}")
print(f"Empresa B: {media_diaria[1]:.2f}")
print(f"Empresa C: {media_diaria[2]:.2f}")
print(f"Empresa D: {media_diaria[3]:.2f}")
print(f"Empresa E: {media_diaria[4]:.2f}")

variacao_diaria = np.ptp(precos_acoes, axis=0)
print("Variação diária dos preços das ações para cada empresa:")
print(f"Empresa A: {variacao_diaria[0]}")
print(f"Empresa B: {variacao_diaria[1]}")
print(f"Empresa C: {variacao_diaria[2]}")
print(f"Empresa D: {variacao_diaria[3]}")
print(f"Empresa E: {variacao_diaria[4]}")

precos_empresa_B = precos_acoes[:, 1]
dia_maior_preco = np.argmax(precos_empresa_B)
dia_menor_preco = np.argmin(precos_empresa_B)
print("Dia da semana com maior e menor preço para a empresa B:")
print(f"Maior preço: Dia {dia_maior_preco + 1}, Preço: {precos_empresa_B[dia_maior_preco]}")
print(f"Menor preço: Dia {dia_menor_preco + 1}, Preço: {precos_empresa_B[dia_menor_preco]}")

precos_acoes_atualizados = precos_acoes * 1.05
nova_media_diaria = np.mean(precos_acoes_atualizados, axis=0)
print("Nova média diária dos preços das ações após aumento de 5%:")
print(f"Empresa A: {nova_media_diaria[0]:.2f}")
print(f"Empresa B: {nova_media_diaria[1]:.2f}")
print(f"Empresa C: {nova_media_diaria[2]:.2f}")
print(f"Empresa D: {nova_media_diaria[3]:.2f}")
print(f"Empresa E: {nova_media_diaria[4]:.2f}")


