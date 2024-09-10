from Class.medico import Medico
from Class.paciente import Paciente
from Class.atendimento import Atendimento

class SistemaAtendimentos:
    def __init__(self):
        self.medicos = []
        self.pacientes = []
        self.atendimentos = []

    def cadastrar_medico(self):
        nome = input("Nome do médico: ")
        crm = input("CRM do médico: ")
        medico = Medico(nome, crm)
        self.medicos.append(medico)
        print(f"Médico {nome} cadastrado com sucesso.")

    def cadastrar_paciente(self):
        nome = input("Nome do paciente: ")
        cpf = input("CPF do paciente: ")
        paciente = Paciente(nome, cpf)
        paciente.cadastar_endereco()
        paciente.cadastar_telefone()
        self.pacientes.append(paciente)
        print(f"Paciente {nome} cadastrado com sucesso.")

    def cadastrar_atendimento(self):
        if not self.medicos:
            print("Nenhum médico cadastrado. Cadastre um médico primeiro.")
            return
        if not self.pacientes:
            print("Nenhum paciente cadastrado. Cadastre um paciente primeiro.")
            return

        print("Escolha o médico para o atendimento:")
        for idx, medico in enumerate(self.medicos):
            print(f"{idx + 1} - {medico.nome} (CRM: {medico.crm})")
        medico_idx = int(input("Número do médico: ")) - 1
        medico = self.medicos[medico_idx]

        print("Escolha o paciente para o atendimento:")
        for idx, paciente in enumerate(self.pacientes):
            print(f"{idx + 1} - {paciente.nome} (CPF: {paciente.cpf})")
        paciente_idx = int(input("Número do paciente: ")) - 1
        paciente = self.pacientes[paciente_idx]

        data = input("Data do atendimento (dd/mm/aaaa): ")
        descricao = input("Descrição do atendimento: ")

        atendimento = Atendimento(medico, paciente, data, descricao)
        self.atendimentos.append(atendimento)
        print(f"Atendimento cadastrado com sucesso.")

    def listar_atendimentos(self):
        if not self.atendimentos:
            print("Nenhum atendimento cadastrado.")
            return

        for idx, atendimento in enumerate(self.atendimentos):
            print(f"\nAtendimento {idx + 1}")
            print(f"Médico: {atendimento.medico.nome} (CRM: {atendimento.medico.crm})")
            print(f"Paciente: {atendimento.paciente.nome} (CPF: {atendimento.paciente.cpf})")
            print(f"Data: {atendimento.data}")
            print(f"Descrição: {atendimento.descricao}")

    def buscar_atendimentos_por_medico(self):
        if not self.medicos:
            print("Nenhum médico cadastrado.")
            return

        print("Escolha o médico para buscar atendimentos:")
        for idx, medico in enumerate(self.medicos):
            print(f"{idx + 1} - {medico.nome} (CRM: {medico.crm})")
        medico_idx = int(input("Número do médico: ")) - 1
        medico = self.medicos[medico_idx]

        atendimentos_medico = [a for a in self.atendimentos if a.medico == medico]

        if not atendimentos_medico:
            print(f"Nenhum atendimento encontrado para o médico {medico.nome}.")
        else:
            print(f"Atendimentos para o médico {medico.nome}:")
            for idx, atendimento in enumerate(atendimentos_medico):
                print(f"\nAtendimento {idx + 1}")
                print(f"Paciente: {atendimento.paciente.nome} (CPF: {atendimento.paciente.cpf})")
                print(f"Data: {atendimento.data}")
                print(f"Descrição: {atendimento.descricao}")

    def menu(self):
        while True:
            print("\nMenu Principal")
            print("1 - Cadastrar Médico")
            print("2 - Cadastrar Paciente")
            print("3 - Cadastrar Atendimento")
            print("4 - Listar Atendimentos")
            print("5 - Buscar Atendimentos por Médico")
            print("-1 - Sair")
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                self.cadastrar_medico()
            elif opcao == 2:
                self.cadastrar_paciente()
            elif opcao == 3:
                self.cadastrar_atendimento()
            elif opcao == 4:
                self.listar_atendimentos()
            elif opcao == 5:
                self.buscar_atendimentos_por_medico()
            elif opcao == -1:
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")


sistema = SistemaAtendimentos()
sistema.menu()