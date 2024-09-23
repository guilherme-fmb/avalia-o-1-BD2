from classes import Motorista, Passageiro, Corrida

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com um comando: ")
            if command == "quit":
                print("Até mais!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido! Tente de novo.")

class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        corridas = []
        controle = 1
        while(controle == 1):
            nome = input("Nome do passageiro: ")
            documento = input("Documento do passageiro: ")
            passageiro = Passageiro(nome,documento)

            notaCorrida = int(input("Nota da corrida: "))
            distancia = float(input("Distância da corrida: "))
            valor = float(input("Valor da corrida: "))
            corrida = Corrida(notaCorrida,distancia,valor,passageiro)
            corridas.append(corrida)

            controle = int(input("Digite 1 para continuar adicionando corridas, ou 0 para parar de adicionar."))
        
        notaMotorista = int(input("Nota do motorista: "))
        motorista = Motorista(notaMotorista,corridas)
        self.motorista_model.create_motorista(motorista)

    def read_motorista(self):
        id = input("Digite o Id: ")
        self.motorista_model.read_motorista_by_id(id)
    
    def update_motorista(self):
        id = input("Digite o Id: ")
        
        controle = 1
        corridas = []
        
        while(controle == 1):
            nome = input("Nome do passageiro: ")
            documento = input("Documento do passageiro: ")
            passageiro = Passageiro(nome,documento)

            notaCorrida = int(input("Nota da corrida: "))
            distancia = float(input("Distância da corrida: "))
            valor = float(input("Valor da corrida: "))
            corrida = Corrida(notaCorrida,distancia,valor,passageiro)
            corridas.append(corrida)

            controle = int(input("Digite 1 para continuar adicionando corridas, ou 0 para parar de adicionar."))
        
        notaMotorista = int(input("Nota do motorista: "))
        motorista = Motorista(notaMotorista,corridas)
        self.motorista_model.update_motorista(id, motorista)

    def delete_motorista(self):
        id = input("Entre com o ID: ")
        self.motorista_model.delete_motorista(id)
        
    def run(self):
        print("Comandos disponíveis para manipulação de motoristas: create, read, update, delete, quit")
        super().run()