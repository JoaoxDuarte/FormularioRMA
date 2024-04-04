from abc import ABC, abstractmethod

from ...domain.entities.responsavelCras import ResponsavelCras


class ResponsavelCrasRepository(ABC):

    @abstractmethod
    def recuperar_responsavel_cras(self, login: str) -> ResponsavelCras:
        pass
