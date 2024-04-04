from abc import ABC, abstractmethod
from ..entities.volume_atendimento_particularizado import VolumeAtendimentoParticularizado

class VolumeAtendimentoParticularizadoRepository(ABC):

    @abstractmethod
    def recuperar_volume_atendimento_particularizado(cras: str) ->  VolumeAtendimentoParticularizado:
        pass

    @abstractmethod
    def salvar_volume_atendimento_particularizado(volume : VolumeAtendimentoParticularizado, cras, mes_referencia) -> bool:
        pass
