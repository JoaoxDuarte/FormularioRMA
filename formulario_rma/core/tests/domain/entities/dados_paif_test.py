import pytest
from ....domain.entities.DadosPAIF import DadosPAIF

def test_total_de_novas_familias_PAIF_need_to_be_smaller_or_equal_than_total_de_familias_em_acompanhamento_PAIF():
    with pytest.raises(Exception):
        DadosPAIF(10,11,1,1,1,1,1,1,1)

def test_novas_familias_em_situacao_de_extrema_pobreza_need_to_be_smaller_or_equal_than_total_de_novas_familias_PAIF():
    with pytest.raises(Exception):
        DadosPAIF(10,2,3,1,1,1,1,1,1)

def test_novas_familias_bolsa_familia_need_to_be_smaller_or_equal_than_total_de_novas_familias_PAIF():
    with pytest.raises(Exception):
        DadosPAIF(10,5,1,6,1,1,1,1,1)

def test_novas_familias_bolsa_familia_em_descomprimento_need_to_be_smaller_or_equal_than_novas_familias_bolsa_familia():
    with pytest.raises(Exception):
        DadosPAIF(10,5,1,6,7,1,1,1,1)

def test_novas_familias_membros_bpc_need_to_be_smaller_or_equal_than_total_de_novas_familias_PAIF():
    with pytest.raises(Exception):
        DadosPAIF(10,5,1,1,1,8,1,1,1)

def test_novas_familias_criancas_adolescentes_trabalho_need_to_be_smaller_or_equal_than_total_de_novas_familias_PAIF():
    with pytest.raises(Exception):
        DadosPAIF(10,5,1,1,1,1,6,1,1)

def test_novas_familias_criancas_adolescentes_acolhimento_need_to_be_smaller_or_equal_than_total_de_novas_familias_PAIF():
    with pytest.raises(Exception):
        DadosPAIF(10,5,1,1,1,1,1,6,1)
 