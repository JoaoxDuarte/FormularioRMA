import pytest
from ....domain.entities.volume_atendimento_particularizado import VolumeAtendimentoParticularizado


def test_individuos_encaminhados_para_bpc_need_to_be_smaller_than_total_atendimento_particularizado_mes():
    with pytest.raises(ValueError):
        VolumeAtendimentoParticularizado(10, 1, 1, 11, 1, 1, 1, 1, 1)


def test_familias_encaminhadas_para_creas_need_to_be_smaller_than_total_atendimento_particularizado_mes():
    with pytest.raises(ValueError):
        VolumeAtendimentoParticularizado(10, 1, 1, 1, 11, 1, 1, 1, 1)


def test_visitas_domiciliares_realizadas_need_to_be_smaller_than_total_atendimento_particularizado_mes():
    with pytest.raises(ValueError):
        VolumeAtendimentoParticularizado(10, 1, 1, 1, 1, 11, 1, 1, 1)


def test_total_auxilio_natalidade_concedido_need_to_be_smaller_than_total_atendimento_particularizado_mes():
    with pytest.raises(ValueError):
        VolumeAtendimentoParticularizado(10, 1, 1, 1, 1, 1, 11, 1, 1)


def test_total_auxilio_funeral_concedido_need_to_be_smaller_than_total_atendimento_particularizado_mes():
    with pytest.raises(ValueError):
        VolumeAtendimentoParticularizado(10, 1, 1, 1, 1, 1, 1, 11, 1)


def test_outros_beneficios_concedidos_need_to_be_smaller_than_total_atendimento_particularizado_mes():
    with pytest.raises(ValueError):
        VolumeAtendimentoParticularizado(10, 1, 1, 1, 1, 1, 1, 1, 11)
