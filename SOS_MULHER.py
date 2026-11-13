#Curso:Técnico em informática
#Ano: 2º ano
#Turma: A
#Disciplina: Programação Orientada a Objetos
#Integrantes: Eduardo Ferreira, Salomão Bottow, Lázaro Henrique, Jonatas Oliveira 

class Usuario: #classe mãe
    def __init__(self, nome, cpf, email, senha):
        self.nome = nome
        self.cpf = cpf
        self. email = email
        self.senha = senha

    def login(self, email, senha):
        if self.email == email and self.senha == senha:
            return True
        return False
    def logout(self):
        print("saída da conta concluída com successo")

    def AtualizarDados(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Vitima(Usuario): #vitima herda de usuário
    def __init__(self,nome,cpf,email,senha,numeroMPU,statusdeportecao,datadecadastro):
        super().__init__(nome, cpf, email, senha)
        self.numeroMPU = numeroMPU
        self.statusdeprotecao = statusdeportecao
        self.datadecadastro = datadecadastro

    def AcionarSOS(self):
        print("SOS acionado!!!")

    def compartilharLocalização(self):
        print("Localização compartilhada para as devidas providências")

    def ConsultarMPU(self):
        return None

    def AtualizarDados(self, nome, cpf, telefone, email):
        self.nome = nome 
        self.cpf = cpf
        self.email = email

class policial(Usuario): # a classe policial herda de usuario
    def __init__(self, nome, cpf, email, senha, batalhao, patente):
        super().__init__(nome, cpf, email, senha)
        self.batalhao = batalhao
        self.patente = patente

    def receberChamado(self):
        print("Chamado recebido")

    def atenderChamado(self):
        print("Chamado rebecido")

    def atualizarStatus(self):
        print("Status atualzados")

class MedidaProtetiva: 
    def __init__(self, numerodoProcesso, dataemissao, status, datadeValidade):
        self.numerodoProcesso = numerodoProcesso
        self.dataemissao = dataemissao
        self.status = status
        self.datadeValidade = datadeValidade

    def veridicarValidade(self):
        return True

    def atualizarstatus(self, novoStatus):
        self.status = novoStatus

class Notificacao:
    def __init__(self, idNotificacao, mensagem, DataHora, lida):
        self.idNotificacao = idNotificacao
        self.mensagem = mensagem
        self.DataHora = DataHora
        self.lida = lida

    def enviar(self):
        print("Notificação enviada para o policial")

    def enviarMensagem(self, mensagem):
        self.mensagem = mensagem
        print("Mensagem enviada")

    def visualizar(self):
        print(self.mensagem)

class Ocorrencia:
    def __init__(self, idOcorrencia, DataHora, status, descricao, tipo):
        self.idOcorrencia = idOcorrencia
        self.DataHora = DataHora
        self.status = status
        self.descricao = descricao
        self.tipo = tipo

    def abrirOcorrencia(self):
        self.status = "Aberta"

    def encerrarOcorencia(self):
        self.status = "Encerrada"

    def atualizarOcorrencia(self, status, descricao):
        self.status = status
        self.descricao = descricao

class Localização:
    def __init__(self, Latitude, DataHora, Longitude, Origem):
        self.Latitude = Latitude
        self.DataHora = DataHora
        self.Longitude = Longitude
        self.Origem = Origem

    def obterLocalização(self):
        return self

    def atualizarLocalização(self):
        print("Localização atualizada")

class Agressor:
    def __init__(self, Nivel_de_risco, nome, cpf, localizacao, FichaCriminal):
        self.Nivel_de_risco = Nivel_de_risco
        self.nome = nome
        self.cpf = cpf
        self.localização = localizacao
        self.FichaCriminal = FichaCriminal

    def EnviarLocalização(self):
        return 0 

    def operation22(self):
        print("Operação realizada com sucesso!")