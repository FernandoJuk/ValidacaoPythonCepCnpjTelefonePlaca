# from validate_docbr import CPF
# from validate_docbr import CNPJ
from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos incorreta!")

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf inválido!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
      mascara = CPF()
      return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cnpj inválido!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        mascara = CNPJ()
        return mascara.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
# class CpfCnpj():
#     def __init__(self,documento, tipo_doc):
#         self.tipo_doc = tipo_doc
#         documento = str(documento)
#         if self.tipo_doc == 'cpf':
#             if self.cpf_eh_Valido(documento):
#                 self.cpf = documento
#             else:
#                raise ValueError ('CPF Invalido !!')
#         elif self.tipo_doc == 'cnpj':
#             if self.cnpj_eh_Valido(documento):
#                 self.cnpj = documento
#             else:
#                 raise ValueError ('CNPJ Invalido !!')
#         else:
#             raise ValueError('Documento Invalido !!')
#
#
#     def __str__(self):
#         return self.formata_documento(self.tipo_doc)
#
#     def cpf_eh_Valido(self,documento):
#         #cpf = CPF()
#        # if len(documento) == 11 and cpf.validate(documento):
#         if len(documento) == 11:
#             validador = CPF()
#             return validador.validate(documento)
#         else:
#            raise ValueError ('Quantidade de digitos Invalido !!')
#
#     def cnpj_eh_Valido(self,cnpj):
#         if len(cnpj) == 14:
#             validador = CNPJ()
#             return validador.validate(cnpj)
#         else:
#             raise ValueError ('Quantidade de digitos Invalido !!')
#     def formata_documento(self,tipo):
#         # part1 = self.cpf[:3]
#         # part2 = self.cpf[3:6]
#         # part3 = self.cpf[6:9]
#         # part4 = self.cpf[9:]
#         # return ("{}.{}.{}-{}".format(part1,part2,part3,part4))
#         if tipo == 'cpf':
#             cpf = CPF()
#             return cpf.mask(self.cpf)
#         else:
#             cnpj = CNPJ()
#             return cnpj.mask(self.cnpj)