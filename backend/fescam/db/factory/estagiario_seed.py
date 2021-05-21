from os import path
import sys


sys.path.append(path.abspath('.'))
from faker import Faker
from fescam.components.functions_helpers import cpfNumber_int_to_str
from fescam.schemas.estagiaro import EstagiarioCreated
from fescam.model.Funcionario import Funcionario
from fescam.DAO.EstagiarioDAO import EstagiarioDAO

fake = Faker(['pt_BR'])

def factory():
    estDAO = EstagiarioDAO()
    nome = fake.name()
    senha = fake.password()
    CPF = cpfNumber_int_to_str(fake.pyint(min_value=0, max_value=99999999999, step=1))
    estagiario = EstagiarioCreated(nome = nome, CPF = CPF, senha = senha)
    return estDAO.createBySchema(estagiario)