class Paciente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.telefone = []
        self.endereco = {"Rua", "Numero" , "Bairro" }

    def cadastar_telefone(self):
        while True:
            print("Cadastar Telefone:")
            continuar = input("1-Cadastar numero de telefone \n 0-sair: ")
            if continuar == "1" :
                numero = ""
                numero = input("Digite o numero do telefone: ")
                self.telefone.append(numero)
            elif continuar == "0":
                break
    
    def cadastar_endereco(self):
        while True:
            print("Cadastar endereco: ")
            while True:
                rua = input("Escreva o nome da rua : ")
                if type(rua) != int :
                    self.endereco.update({"Rua" : rua})
                    break
                else:
                    print("Digite algo valido. EX: Alameda juse quintino ")
            while True:
                numero = input("Digite o numero da casa: ")
                if numero.isnumeric() :
                    self.endereco.update({"Numero" : numero})
                    break
                else:
                    print("Digite algo valido. EX:22")
            while True:
                bairro = input("Digite o nome do bairro por estenco: ")
                if type(bairro) != int:
                    self.endereco.update({"Bairro" : bairro})
                    break
                else:
                    print("Digite algo valido. EX: Vinte nove de julho") 
            break
                





