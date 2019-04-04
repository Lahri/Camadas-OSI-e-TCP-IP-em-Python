

class CamadaFisica():

    def __init__(self, camada):
        if type(camada) == CamadaEnlace:
            self.camada = "[010110110" + camada.camada + "]"
            print("Valor passado para camada Fisica com sucesso!\n")
            print(self.camada + "]\n")
        else:
            pass

    def Funcao(self):
        return "A camada Fisica define os sentidos da transmissão\n"



class CamadaEnlace():

    def __init__(self, camada):
        if type(camada) == CamadaRede:
            self.camada = "[D4-3D-7E-59-13-02" + camada.camada + "]"
            print("Valor passado para camada Enlace com sucesso!\n")
            print(self.camada + "]\n")
        else:
            pass

    def Funcao(self):
        return "A camada Enlace controla o fluxo e estabelece um protocolo de comunicação\n"


class CamadaRede():

    def __init__(self, camada):
        if type(camada) == CamadaTransporte:
            self.camada = "[172.20.25.37" + camada.camada + "]"
            print("Valor passado para camada Rede com sucesso!\n")
            print(self.camada + "]\n")
        else:
            pass

    def Funcao(self):
        return "A camada Rede realiza o roteamento de funções\n"


class CamadaTransporte():

    def __init__(self, camada):
        if type(camada) == CamadaSessao:

            self.x = int(input("1 - TCP | 2 - UDP: "))

            if self.x == 1:
                self.camada = "[TCP" + camada.camada + "]"
            elif self.x == 2:
                self.camada = "[UDP" + camada.camada + "]"

            print("Valor passado para camada Transporte com sucesso!\n")
            print(self.camada + "]\n")
        else:
            pass

    def Funcao(self):
        return "A camada Transporte segmenta os dados recebidos para próxima camada\n"


class CamadaSessao():

    def __init__(self, camada):
        if type(camada) == CamadaApresentacao:
            self.camada = "[Criptografado" + camada.camada + "]"
            print("Valor passado para camada Sessão com sucesso!\n")
            print(self.camada + "]\n")
        else:
            pass

    def Funcao(self):
        return "A camada Sessão realiza a troca de dados e faz a comunicação entre os hosts\n"


class CamadaApresentacao():

    def __init__(self, camada):
        if type(camada) == CamadaAplicacao:
            self.camada = camada.camada.upper() + camada.camada + "]"

            print("Valor passado para camada Apresentacao com sucesso!\n")
            print(self.camada + "]\n")
        else:
            pass

    def Funcao(self):
        return "A camada Apresentação converte os dados recebidos\n"


class CamadaAplicacao():

    def __init__(self, camada):
            self.camada = "[" + camada
            print("Valor passado para camada Aplicacao com sucesso!\n")
            print(self.camada + "]\n")


    def Funcao(self):
        return "A camada Aplicação é corresponde aos programas que fazem a interação entre máquina-usuário\n"



teste = "Oi"
aplicacao = CamadaAplicacao(teste)
apresentacao = CamadaApresentacao(aplicacao)
sessao = CamadaSessao(apresentacao)
transporte = CamadaTransporte(sessao)
rede = CamadaRede(transporte)
enlace = CamadaEnlace(rede)
fisica = CamadaFisica(enlace)





