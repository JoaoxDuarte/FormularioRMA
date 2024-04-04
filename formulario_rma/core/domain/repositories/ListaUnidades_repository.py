from ast import List
from ..entities.Unidade import Unidade
from abc import ABC, abstractmethod


class ListaUnidadesRepository(ABC):

    @abstractmethod
    def recuperar_unidades_cras(self) -> List(Unidade):
        pass

    @abstractmethod
    def recuperar_unidades_centro_pop(self) -> List(Unidade):
        pass

    @abstractmethod
    def recuperar_unidades_creas(self) -> List(Unidade):
        pass
