import requests

class BuscaPlaca:

    def __init__(self, placa):
        placa = str(placa)
        if self.placa_e_Valido(placa):
            self.placa = placa
        else:
            raise ValueError("Placa inválido!")

    def __str__(self):
        return self.format_placa()

    def placa_e_Valido(self, placa):
        if len(placa) == 7:
            return True
        else:
            return False

    def format_placa(self):
        return "{}-{}".format(self.placa[:3],self.placa[3:])

    def acessa_via_placa(self):
        placa = "https://apicarros.com/v1/consulta/{}/json".format(self.placa)
        r = requests.get(placa)
        dados = r.json()
        return (
            dados['ano'],
            dados['anoModelo'],
            dados['chassi'],
            dados['cor'],
            dados['modelo'],
            dados['placa'],
            dados['situacao']
        )




