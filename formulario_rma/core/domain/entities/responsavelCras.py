from dataclasses import dataclass
import re


@dataclass
class ResponsavelCras:
    def __init__(self, nome: str,  matricula: str, cargo: str, email_funcional: str, id_unidade: int):
        self.nome = nome
        self.matricula = matricula
        self.cargo = cargo
        self.email_funcional = email_funcional
        self.id_unidade = id_unidade

    def __str__(self) -> str:
        return f'Servidor {self.nome}, de matricula {self.matricula} e apresenta o cargo de {self.cargo}. Lotado em {self.id_unidade}.'

  # Nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str) and not len(nome) == 0:
            self._nome = nome
            return self._nome
        raise ValueError("O nome está errado!")

# Matricula
    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, matricula):
        if isinstance(matricula, str):
            self._matricula = matricula
            return self._matricula
        raise ValueError("A matricula está errada!")

  # Cargo
    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        if isinstance(cargo, str) and not len(cargo) == 0:
            self._cargo = cargo
            return self._cargo
        raise ValueError("O cargo está incorreto!")

  # Email
    @property
    def email_funcional(self):
        return self._email_funcional

    @email_funcional.setter
    def email_funcional(self, email_funcional: str):

        # Verifica se o email_funcional tem @
        EMAIL_REGEX = re.compile(r"[^@]+@sedes\.df\.gov\.br")
        if not isinstance(email_funcional, str) or not EMAIL_REGEX.match(email_funcional):
            raise ValueError("O email está incorreto!")
        self._email_funcional = email_funcional
        return self._email_funcional
