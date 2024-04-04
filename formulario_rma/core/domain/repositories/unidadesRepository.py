from abc import ABC, abstractmethod
from ..entities.responsavelCras import ResponsavelCras
from ..entities.Unidade import Unidade

class UnidadesRepository(ABC):
    @abstractmethod
    def recuperar_dados_unidades(responsavelCras: ResponsavelCras) -> Unidade:
        pass
