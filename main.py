# #from validate_docbr import CPF
# from cpf_cnpj import CpfCnpj
#
# cpf = "04235921908"
# objeto_cpf = CpfCnpj(cpf,"cpf")
#
# print(objeto_cpf)
#
# cnpj = "29598317000153"
# objeto_cnpj = CpfCnpj(cnpj,"cnpj")
#
# print(objeto_cnpj)

from cpf_cnpj import Documento
from validate_docbr import CNPJ

#cpf_um = Cpf("15316264754")
#print(cpf_um)

exemplo_cnpj = "35379838000112"
#exemplo_cpf = "11111111112"

#cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)

from cpf_cnpj import Documento
from validate_docbr import CNPJ

cpf_um = "15316264754"
#print(cpf_um)

#exemplo_cnpj = "35379838000112"
#exemplo_cpf = "11111111112"

#cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))
documento = Documento.cria_documento(cpf_um)
print(documento)

import re

padrao = "\w{5,50}@[a-z]{3,10}.com.br"
texto = "aaabbbcc rodrigo123@gmail.com.br ccbbbaaa"
resposta = re.search(padrao, texto)

print(resposta.group)

# from telefonesBr import TelefonesBr
# import re
#
# telefone = "2126481234"
#
# telefone_objeto = TelefonesBr(telefone)
# print(telefone_objeto)

from telefonesBr import TelefonesBr
import re

telefone = "552126481234"

telefone_objeto = TelefonesBr(telefone)

#padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.search(padrao,telefone)
#print(resposta.group())

# print(telefone_objeto.format_numero())
#
# from datetime import datetime, timedelta
#
# print(datetime.today())

from datetime import datetime, timedelta
from datas_br import DatasBr

cadastro = DatasBr()
print(cadastro.momento_cadastro)
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
print(cadastro)

print(cadastro.tempo_cadastro())

agora = datetime.now()
agora_formatado = agora.strftime("%Y/%m/%d-%H:%M:%S")
print(agora_formatado)

# agora = datetime.today() + timedelta(days=15, minutes=20,seconds=30)
#     return agora - self.tempo_cadastro


from acesso_cep import BuscaEndereco

cep = 25870145
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)





# from acesso_cep import BuscaEndereco
# cep = "81010190"
# objeto_cep = BuscaEndereco(cep)
#
# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(r.text)

import requests

from acesso_cep import BuscaEndereco
cep = "81010190"
objeto_cep = BuscaEndereco(cep)

#r = requests.get("https://viacep.com.br/ws/01001000/json/")
#print(r.text)

a = objeto_cep.acessa_via_cep()
#print(type(a))
#print(dir(a))#  traz todos os metodos
#print(a.text)  # type STR
#print(a.json()["logradouro"]) #type Dicionario

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)

from busca_placa import BuscaPlaca
placa = input("Digite a placa: ")
objeto_placa = BuscaPlaca(placa)

ano,anoModelo,chassi,cor,modelo,placa,situacao = objeto_placa.acessa_via_placa()

print(
    "\nModelo: ",modelo,
    "\nAno: ",ano,"/",anoModelo,
    "\nChassi: ",chassi,
    "\nCor: ",cor,
    "\nPlaca: ",placa,
    "\nsituacao: ",situacao
    )
