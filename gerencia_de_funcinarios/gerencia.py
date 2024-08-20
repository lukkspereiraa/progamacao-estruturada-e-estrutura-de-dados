funcionarios = []

funcionarios.append({
    "nome": "Ana",
    "idade": 30,
    "salario": 3000.00,
    "cargo": {"descricao": "Analista de Sistemas"}
})

funcionarios.append({
    "nome": "Bruno",
    "idade": 40,
    "salario": 5000.00,
    "cargo": {"descricao": "Gerente de Projetos"}
})

funcionarios.append({
    "nome": "Carla",
    "idade": 28,
    "salario": 2500.00,
    "cargo": {"descricao": "Desenvolvedora"}
})

funcionarios.append({
    "nome": "Diego",
    "idade": 35,
    "salario": 4500.00,
    "cargo": {"descricao": "Coordenador de TI"}
})

funcionarios.append({
    "nome": "Eduarda",
    "idade": 32,
    "salario": 3200.00,
    "cargo": {"descricao": "Analista de Marketing"}
})


soma_salarios = 0
maior_salario = funcionarios[0]["salario"]
menor_salario = funcionarios[0]["salario"]
funcionario_maior_salario = funcionarios[0]
funcionario_menor_salario = funcionarios[0]

for func in funcionarios:
    salario = func["salario"]
    soma_salarios += salario
    
    if salario > maior_salario:
        maior_salario = salario
        funcionario_maior_salario = func
    
    if salario < menor_salario:
        menor_salario = salario
        funcionario_menor_salario = func

media_salarios = soma_salarios / len(funcionarios)

print(f"Média dos salários: R$ {media_salarios:.2f}")
print(f"Funcionário com maior salário: {funcionario_maior_salario['nome']} - Cargo: {funcionario_maior_salario['cargo']['descricao']} - Salário: R$ {funcionario_maior_salario['salario']:.2f}")
print(f"Funcionário com menor salário: {funcionario_menor_salario['nome']} - Cargo: {funcionario_menor_salario['cargo']['descricao']} - Salário: R$ {funcionario_menor_salario['salario']:.2f}")
