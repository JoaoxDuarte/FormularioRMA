from dataclasses import dataclass
from ..utils.my_attr import MyAttr, positive_validator


@dataclass
class VolumeServicosConvivenciaEFortalecimentoVinculosDeFamiliasPAIF:
    total_familias_PAIF : int = MyAttr(int, [positive_validator]) # >=0
    familias_participando_regularmente_de_grupos_no_ambito_PAIF : int  = MyAttr(int, [positive_validator])# >=0
    criancas_adolescentes_0_6_anos_no_servico : int = MyAttr(int, [positive_validator]) #>=0
    criancas_adolescente_7_a_14_no_servico : int = MyAttr(int, [positive_validator]) #>=0
    adolescenete_15_a_17_no_servico : int  = MyAttr(int, [positive_validator])# >=0
    adultos_18_a_59_servicos : int  = MyAttr(int, [positive_validator])# >=0
    idosos_servico : int = MyAttr(int, [positive_validator]) # >=0
    pessoas_que_participaram_de_atividades : int = MyAttr(int, [positive_validator]) # >=0
    pessoas_com_deficiencia_servico : int = MyAttr(int, [positive_validator]) # >=0
