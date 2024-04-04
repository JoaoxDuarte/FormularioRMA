from abc import ABC, abstractmethod

from core.domain.entities.VolumeServicosConvivenciaEFortalecimentoVinculos import VolumeServicosConvivenciaEFortalecimentoVinculosDeFamiliasPAIF



class RepositoryVolumeServicosConvivenciaEFortalecimentoVinculos(ABC):

    @abstractmethod
    def recuperar_volume_servico_convivencia_e_fortalecimento_vinculos(cras: str) -> VolumeServicosConvivenciaEFortalecimentoVinculosDeFamiliasPAIF:
        pass