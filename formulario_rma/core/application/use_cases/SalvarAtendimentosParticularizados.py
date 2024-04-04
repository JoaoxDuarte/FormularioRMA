from formulario_rma.core.domain.entities.volume_atendimento_particularizado import VolumeAtendimentoParticularizado
from formulario_rma.core.domain.repositories.volume_atendimento_particularizado_repository import VolumeAtendimentoParticularizadoRepository


class SalvarAtendimentosParticularizados:
    def __init__(self, salvar_atendimentos: VolumeAtendimentoParticularizadoRepository):
        self.salvar_atendimentos = salvar_atendimentos

    def run(self, volume_atendimento: VolumeAtendimentoParticularizado):
        return self.salvar_atendimentos.salvar_volume_atendimento_particularizado(volume_atendimento)
        