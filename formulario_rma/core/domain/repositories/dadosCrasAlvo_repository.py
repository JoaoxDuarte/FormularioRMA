from abc import ABC, abstractmethod

from core.domain.entities.dadosCras import DadosCras




class RepositoryDadosCrasAlvo(ABC):

    @abstractmethod
    def enviar_dados_cras(self, dados_cras: DadosCras):
        pass