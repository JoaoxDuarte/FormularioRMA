from core.domain.entities.dadosCras import DadosCras
from core.domain.repositories.dadosCrasAlvo_repository import RepositoryDadosCrasAlvo


class EnviarDadosCrasParaAlvo:
    def __init__(self, alvo_dados_cras: RepositoryDadosCrasAlvo):
        self.alvo_dados_cras = alvo_dados_cras

    def run(self, dados_cras: DadosCras):
        return self.alvo_dados_cras.enviar_dados_cras(dados_cras)
        