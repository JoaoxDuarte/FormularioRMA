from abc import ABC, abstractmethod

from sids_app.models import USUARIOS_SISTEMA
from ...domain.entities.Unidade import Unidade
from ...domain.entities.responsavelCras import ResponsavelCras
from ...domain.repositories.unidadesRepository import UnidadesRepository
class UnidadesRepository(UnidadesRepository):
    def recuperar_dados_unidades(id_unidade: int) -> Unidade:
        pass

