
from core.domain.entities.volume_atendimento_particularizado import VolumeAtendimentoParticularizado
from core.domain.repositories.volume_atendimento_particularizado_repository import VolumeAtendimentoParticularizadoRepository
from main_app.models import DadosCrasModel, VolumeAtendimentoParticularizadoModel


class VolumeAtendimentoParticRepositoryImpl (VolumeAtendimentoParticularizadoRepository):
    def recuperar_volume_atendimento_particularizado(self, cras: str) -> VolumeAtendimentoParticularizado:

        model_cras = DadosCrasModel.objects.filter(
            nome_cras=cras).first()  # .first() faz a mesma coisa que [0]
        model_volume = model_cras.volume_atendimento_particularizado
        return VolumeAtendimentoParticularizado(model_volume.total_atendimento_particularizado_mes,
                                                model_volume.familias_encaminhadas_inclusao_cadunico_mes,
                                                model_volume.familias_encaminhadas_atualizacao_cadunico_mes,
                                                model_volume.familias_encaminhadas_inclusao_atualizacao_cadunico_mes,
                                                model_volume.individuos_encaminhados_para_bpc,
                                                model_volume.familias_encaminhadas_para_creas,
                                                model_volume.visitas_domiciliares_realizadas,
                                                model_volume.total_auxilio_natalidade_concedido,
                                                model_volume.total_auxilio_funeral_concedido,
                                                model_volume.outros_beneficios_concedidos)

    def salvar_volume_atendimento_particularizado(self, volume: VolumeAtendimentoParticularizado, cras, mes_referencia_arg) -> bool:
        dados_cras_model = DadosCrasModel.objects.filter(
            nome_cras=cras, mes_referencia=mes_referencia_arg).first()
        volume_model = VolumeAtendimentoParticularizadoModel(total_atendimento_particularizado_mes=volume._total_atendimento_particularizado_mes,
                                                             familias_encaminhadas_inclusao_cadunico_mes=volume._familias_encaminhadas_inclusao_cadunico_mes,
                                                             familias_encaminhadas_atualizacao_cadunico_mes=volume._familias_encaminhadas_atualizacao_cadunico_mes,
                                                             individuos_encaminhados_para_bpc=volume._individuos_encaminhados_para_bpc,
                                                             familias_encaminhadas_para_creas=volume._familias_encaminhadas_para_creas,
                                                             visitas_domiciliares_realizadas=volume._visitas_domiciliares_realizadas,
                                                             total_auxilio_natalidade_concedido=volume._total_auxilio_natalidade_concedido,
                                                             total_auxilio_funeral_concedido=volume._total_auxilio_funeral_concedido,
                                                             outros_beneficios_concedidos=volume._outros_beneficios_concedidos)

        dados_cras_model = DadosCrasModel(
            volume_atendimento_particularizado=volume_model)

        try:
            volume_model.save()
            dados_cras_model.save()
            return True
        except:
            return False
