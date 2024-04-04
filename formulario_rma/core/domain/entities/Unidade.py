from dataclasses import dataclass


@dataclass
class Unidade:
    id_unidade: str
    nome: str
    tipo: str
    endereco: str

    def __str__(self):
        return f'Unidade {self.nome} do tipo {self.tipo} de id {self.id_unidade} e endereço {self.endereco}'
