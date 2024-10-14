import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

MEU_BANCO = create_engine("sqlite:///meubanco.db")

Session = sessionmaker(bind=MEU_BANCO)
session = Session()

Base = declarative_base()

class Aluno(Base):
    __tablename__ = "alunos"

    ra = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String) 
    sobrenome = Column("email", String) 
    email = Column("email", String) 
    senha = Column("senha", String) 

    def __init__(self, ra:str, nome:str, sobrenome:str, email:str, senha:str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha
        