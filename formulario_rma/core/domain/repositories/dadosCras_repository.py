from abc import ABC, abstractmethod

from ..entities.dadosCras import DadosCras


class DadosCrasRepository(ABC):

    @abstractmethod
    def enviar_dados_cras(self, dados_cras: DadosCras):
        pass
    @abstractmethod
    def recuperar_dados_cras_por_id_cras(id_cras: int, mes_referencia: str):
        pass