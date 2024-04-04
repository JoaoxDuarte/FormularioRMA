from abc import ABC, abstractmethod
from ..entities.DadosPAIF import DadosPAIF

class DadosPAIFRepository(ABC):

    @abstractmethod
    def recuperar_dados_familia_PAIF(cras: str, mes_referencia: str) ->  DadosPAIF:
        pass

    @abstractmethod
    def criar_dados_familia_PAIF(cras: str, mes_referencia: str) ->  DadosPAIF:
        pass 