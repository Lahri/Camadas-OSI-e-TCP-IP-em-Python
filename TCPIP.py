class CamadaFisica():

    def __init__(self, camada):
        if type(camada) == CamadaInternet:
            self.camada = camada
            print("Valor passado para camada Fisica com sucesso!")
        else:
            pass

    def Funcao(self):
        return "Trata-se das tecnologias usadas para conexões, como: Ethernet, Wi-fi e Modem"

class CamadaInternet():

    def __init__(self, camada):
        if type(camada) == CamadaTransporte:
            self.camada = camada
            print("Valor passado para camada Internet com sucesso!")
        else:
            pass

    def Funcao(self):
        return "Responsável pelas conexões entre as redes locais"


class CamadaTransporte():

    def __init__(self, camada):
        if type(camada) == CamadaAplicacao:
            self.camada = camada
            print("Valor passado para camada Transporte com sucesso!")
        else:
            pass

    def Funcao(self):
        return "Controla comunicação host-a-host"


class CamadaAplicacao():

    def __init__(self, camada):
            self.camada = camada
            print("Valor passado para camada Aplicacao com sucesso!")


    def Funcao(self):
        return "Contém todos os protocolos para um serviço específico de comunicação de dados em um nível de processo-a-processo"


teste = "Realizando teste"
aplicacao = CamadaAplicacao(teste)
transporte = CamadaTransporte(aplicacao)
internet = CamadaInternet(transporte)
fisica = CamadaFisica(internet)