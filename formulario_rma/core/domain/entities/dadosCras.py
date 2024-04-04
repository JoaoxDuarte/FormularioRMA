
from dataclasses import dataclass

from .DadosPAIF import DadosPAIF
from .VolumeServicosConvivenciaEFortalecimentoVinculos import VolumeServicosConvivenciaEFortalecimentoVinculosDeFamiliasPAIF
from .responsavelCras import ResponsavelCras
from .volume_atendimento_particularizado import VolumeAtendimentoParticularizado


@dataclass
class DadosCras:
    dados_Paif: DadosPAIF
    volume_atendimento_particularizado: VolumeAtendimentoParticularizado
    volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF: VolumeServicosConvivenciaEFortalecimentoVinculosDeFamiliasPAIF
    responsavel_cras: ResponsavelCras
    nome_cras: str
    codigo_cras: int
    mes_referencia: str