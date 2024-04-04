from pickle import FALSE
from django.db import models

# Create your models here.
# Models da entidade aqui


# A função save em todas as classes substitui o save normal do model, fazendo com que é salvo o dado SE a chave primaria é Nula, eando edições
# em Chaves primarias já existentes


class ResponsavelModel(models.Model):
    nome = models.CharField(max_length=150)
    matricula = models.IntegerField()
    email_funcional = models.CharField(max_length=320)
    cargo = models.CharField(max_length=150, null=FALSE)
    id_unidade = models.IntegerField(default=1)


class VolAtendParticularizado(models.Model):
    total_atend_particularizado_mes = models.IntegerField()
    fam_encami_inclusao_cad_unico_mes = models.IntegerField()
    fam_encami_atuali_cad_unico_mes = models.IntegerField()
    fam_encami_inclusao_atuali_cad_unico_mes = models.IntegerField()
    individuos_encami_bpc = models.IntegerField()
    fam_encami_para_creas = models.IntegerField()
    visitas_domici_reali = models.IntegerField()
    total_aux_natali_concedido = models.IntegerField()
    total_aux_funeral_concedido = models.IntegerField()
    outros_benef_concedidos = models.IntegerField()


class VolumeServicosConvivenciaEFortalecimentoVinculosDeFamiliasPAIFModel(models.Model):
    total_familias_PAIF = models.IntegerField()
    familias_participando_regularmente_de_grupos_no_ambito_PAIF = models.IntegerField()
    criancas_adolescentes_0_6_anos_no_servico = models.IntegerField()
    criancas_adolescente_7_a_14_no_servico = models.IntegerField()
    adolescenete_15_a_17_no_servico = models.IntegerField()
    adultos_18_a_59_servicos = models.IntegerField()
    idosos_servico = models.IntegerField()
    pessoas_que_participaram_de_atividades = models.IntegerField()
    pessoas_com_deficiencia_servico = models.IntegerField()


class DadosPaifModel(models.Model):
    total_fam_em_acompanha_PAIF = models.IntegerField()
    total_novas_fam_PAIF = models.IntegerField()
    novas_fam_em_situa_extre_pobreza = models.IntegerField()
    # Por algum motivo é necessário um valor default pra popular a base
    novas_fam_bolsa_familia = models.IntegerField(default='0')
    # Por algum motivo é necessário um valor default pra popular a base
    novas_familias_membros_bpc = models.IntegerField(default='0')
    novas_familias_bolsa_familia_em_descomprimento = models.IntegerField()
    novas_familias_criancas_adltes_trabalho = models.IntegerField()
    novas_familias_criancas_adltes_acolhimento = models.IntegerField()
    volume_convivencia_e_fortalecimento_de_vinculos = models.ForeignKey(
        VolumeServicosConvivenciaEFortalecimentoVinculosDeFamiliasPAIFModel,
        on_delete=models.CASCADE)


class DadosCrasModel(models.Model):
    DadosPAIF = models.ForeignKey(DadosPaifModel, on_delete=models.CASCADE)
    vol_atend_particularizado = models.ForeignKey(
        VolAtendParticularizado, on_delete=models.CASCADE)

    vol_serv_convive_fortale_vinculos_fam_PAIF = models.ForeignKey(
        VolumeServicosConvivenciaEFortalecimentoVinculosDeFamiliasPAIFModel,
        on_delete=models.CASCADE)
    responsavel_cras = models.ForeignKey(
        ResponsavelModel, on_delete=models.CASCADE)
    nome_cras = models.CharField(max_length=100)
    cod_cras = models.IntegerField()
    mes_ref = models.CharField(max_length=10)

##### Centro Pop #####


class PesSituaRuaAtendServMesRef(models.Model):
    sexo = models.CharField(max_length=9)
    de_0_a_12_anos = models.IntegerField()
    de_13_a_17_anos = models.IntegerField()
    de_18_a_39_anos = models.IntegerField()
    de_40_a_59_anos = models.IntegerField()
    de_60_anos_ou_mais = models.IntegerField()


class CaractEspIdentiPesAtendServMesRef(models.Model):
    pes_usua_drogas = models.IntegerField()
    migrantes = models.IntegerField()
    pes_doenca_transt_mental = models.IntegerField(null=True, blank=True)


class CadastraPesSituaRuaMesRef(models.Model):
    pes_incluidas_cad_unico_mes_ref = models.IntegerField()
    pes_reali_atuali_cad_unico_mes_ref = models.IntegerField(
        null=True, blank=True)


class VolTotalAtendRealiMesRef(models.Model):
    qtd_total_atend_reali_mes_ref = models.IntegerField(null=True, blank=True)


class QtdPerfilPesAbordaEquipServMesRef(models.Model):
    sexo = models.CharField(max_length=9)
    de_0_a_12_anos = models.IntegerField()
    de_13_a_17_anos = models.IntegerField()
    de_18_a_59_anos = models.IntegerField()
    de_60_anos_ou_mais = models.IntegerField()


class SituaIdentiServEspAbordaSocMesRef(models.Model):
    criancas_adltes_situa_trab_infantil_ate_15_anos = models.IntegerField()
    criancas_adltes_situa_explor_sexual = models.IntegerField()
    criancas_adltes_usua_drogas = models.IntegerField()
    pes_adultas_usua_drogas = models.IntegerField(null=True, blank=True)


class VolAbordagensRealiCras(models.Model):
    qtd_total_aborda_realizadas = models.IntegerField(null=True, blank=True)


#####  CREAS  #####
class FamiliasAcompanhadasPAIF(models.Model):
    total_casos_acompanha_PAEFI = models.IntegerField(null=True, blank=True)
    novos_casos_acompanha_PAEFI_mes_ref = models.IntegerField(
        null=True, blank=True)


class NovosCasosAcompanhaPAEFImesRef(models.Model):
    fam_benef_bolsa_familia = models.IntegerField()
    fam_membros_benef_BPC = models.IntegerField()
    fam_criancas_adltes_trab_infantil = models.IntegerField()
    fam_criancas_adltes_serv_acolhi = models.IntegerField()
    fam_situa_viol_substan_psicoativas = models.IntegerField()
    fam_adltes_med_soceduca_meio_abert = models.IntegerField(
        null=True, blank=True)


class PesVitimasViolDireitosPAEFImesRef(models.Model):
    sexo = models.CharField(max_length=9)
    de_0_a_12_anos = models.IntegerField()
    de_13_a_17_anos = models.IntegerField()
    de_18_a_59_anos = models.IntegerField()
    de_60_anos_ou_mais = models.IntegerField()


class CrianAdltesViolIngressaPAEFImesRefC1(models.Model):  # C.1
    sexo = models.CharField(max_length=9)
    de_0_a_6_anos = models.IntegerField()
    de_7_a_12_anos = models.IntegerField()
    de_13_a_17_anos = models.IntegerField()


class CrianAdltesViolIngressaPAEFImesRefC2(models.Model):    # C.2
    sexo = models.CharField(max_length=9)
    de_0_a_6_anos = models.IntegerField()
    de_7_a_12_anos = models.IntegerField()
    de_13_a_17_anos = models.IntegerField()


class CrianAdltesViolIngressaPAEFImesRefC3(models.Model):    # C.3
    sexo = models.CharField(max_length=9)
    de_0_a_6_anos = models.IntegerField()
    de_7_a_12_anos = models.IntegerField()
    de_13_a_17_anos = models.IntegerField()


class CrianAdltesViolIngressaPAEFImesRefC4(models.Model):    # C.4
    sexo = models.CharField(max_length=9)
    de_0_a_6_anos = models.IntegerField()
    de_7_a_12_anos = models.IntegerField()
    de_13_a_17_anos = models.IntegerField()


class CrianAdltesTrabInfantilPAEFImesRef(models.Model):
    sexo = models.CharField(max_length=9)
    de_0_a_6_anos = models.IntegerField()
    de_7_a_12_anos = models.IntegerField()


class IdososSituaViolPAEFImesRefD1(models.Model):  # D.1
    sexo = models.CharField(max_length=9)
    de_60_anos_ou_mais = models.IntegerField()


class IdososSituaViolPAEFImesRefD2(models.Model):   # D.2
    sexo = models.CharField(max_length=9)
    de_60_anos_ou_mais = models.IntegerField()


class PesComDeficienciaViolPAEFImesRefE1(models.Model):  # E.1
    sexo = models.CharField(max_length=9)
    de_0_a_12_anos = models.IntegerField()
    de_13_a_17_anos = models.IntegerField()
    de_18_a_59_anos = models.IntegerField()
    de_60_anos_ou_mais = models.IntegerField()


class PesComDeficienciaViolPAEFImesRefE2(models.Model):  # E.2
    sexo = models.CharField(max_length=9)
    de_0_a_12_anos = models.IntegerField()
    de_13_a_17_anos = models.IntegerField()
    de_18_a_59_anos = models.IntegerField()
    de_60_anos_ou_mais = models.IntegerField()


class MulheresAdultVitViolIntrafamiliarPAEFImesRef(models.Model):
    mulheres_adult_vit_viol_intrafamiliar = models.IntegerField(
        null=True, blank=True)


class PesVitTrafHumanoPAEFImesRef(models.Model):  # G
    sexo = models.CharField(max_length=9)
    de_0_a_12_anos = models.IntegerField()
    de_13_a_17_anos = models.IntegerField()
    de_18_a_59_anos = models.IntegerField()
    de_60_anos_ou_mais = models.IntegerField()


class PesVitDiscrimiOrieSexualPAEFImesRef(models.Model):  # H
    pes_discrimi_orie_sexual = models.IntegerField(null=True, blank=True)


class PesSituaRuaPAEFImesRef(models.Model):  # I
    sexo = models.CharField(max_length=9)
    de_0_a_12_anos = models.IntegerField()
    de_13_a_17_anos = models.IntegerField()
    de_18_a_59_anos = models.IntegerField()
    de_60_anos_ou_mais = models.IntegerField()
    pes_situa_rua = models.IntegerField(null=True, blank=True)


class AtendRealizadosMesRef(models.Model):  # M - Bloco II
    total_atendi_indivi_mes_ref = models.IntegerField()
    total_atendi_grupo_mes_ref = models.IntegerField()
    fam_encaminha_cras_mes_ref = models.IntegerField()
    visitas_domici_mes_ref = models.IntegerField(null=True, blank=True)


class VolAdltesMedSoceduca(models.Model):  # J
    total_adltes_med_soceduca = models.IntegerField()
    qtd_adltes_liberdade_assisti = models.IntegerField()
    qtd_adltes_presta_serv_comuni = models.IntegerField(null=True, blank=True)


class QtdNovosAdltesServMesRef(models.Model):  # J.4

    masculino = models.IntegerField()
    feminino = models.IntegerField(null=True, blank=True)


class NovosAdltesLAmesRef(models.Model):    # J.5
    masculino = models.IntegerField()
    feminino = models.IntegerField(null=True, blank=True)


class NovosAdltesPSCmesRef(models.Model):   # J.6
    masculino = models.IntegerField()
    feminino = models.IntegerField(null=True, blank=True)


class QtdPesAbdEquipServMesRef(models.Model):  # K
    sexo = models.CharField(max_length=9)
    de_0_a_12_anos = models.IntegerField()
    de_13_a_17_anos = models.IntegerField()
    de_18_a_59_anos = models.IntegerField()
    de_60_anos_ou_mais = models.IntegerField()


class SituaIdentServEspcAbordaSocialMesRef(models.Model):
    criancas_adltes_trab_infatil_15_anos = models.IntegerField()  # K.02
    criancas_adltes_explo_sexual = models.IntegerField()
    criancas_adltes_usua_drogas = models.IntegerField()
    adultos_usua_drogas = models.IntegerField()
    migrantes = models.IntegerField(null=True, blank=True)


class VolAbordagensReali(models.Model):  # L
    qtd_total_aborda_reali_mes_ref = models.IntegerField(null=True, blank=True)


class Save_dadosCrasModel(models.Model):
    DadosCras = models.ForeignKey(DadosCrasModel, on_delete=models.DO_NOTHING)
    Salvo = models.BooleanField()

    def save(self, *args, **kwargs):
        if self.pk is True:
            super(Save_dadosCrasModel, self).save(*args, **kwargs)
        raise Exception('O model não pode ser modificado.')


# chave pri dadosCras
# boolean salvo ou n



#SUPER MODEL CREAS 


class FormCreasModel(models.Model): 
    A1          = models.IntegerField()
    A2          = models.IntegerField()
    B1          = models.IntegerField()
    B2          = models.IntegerField()
    B3          = models.IntegerField()
    B4          = models.IntegerField()
    B5          = models.IntegerField()
    B7          = models.IntegerField()
    
    B6_T        = models.IntegerField()
    B6_M_1      = models.IntegerField()
    B6_M_2      = models.IntegerField()
    B6_M_3      = models.IntegerField()
    B6_M_4      = models.IntegerField()
    B6_F_1      = models.IntegerField()
    B6_F_2      = models.IntegerField()
    B6_F_3      = models.IntegerField()
    B6_F_4      = models.IntegerField()


    C1_T        = models.IntegerField()
    C1_M_1      = models.IntegerField()
    C1_M_2      = models.IntegerField()
    C1_M_3      = models.IntegerField()
    C1_F_1      = models.IntegerField()
    C1_F_2      = models.IntegerField()
    C1_F_3      = models.IntegerField()

    C2_T        = models.IntegerField()
    C2_M_1      = models.IntegerField()
    C2_M_2      = models.IntegerField()
    C2_M_3      = models.IntegerField()
    C2_F_1      = models.IntegerField()
    C2_F_2      = models.IntegerField()
    C2_F_3      = models.IntegerField()

    C3_T        = models.IntegerField()
    C3_M_1      = models.IntegerField()
    C3_M_2      = models.IntegerField()
    C3_M_3      = models.IntegerField()
    C3_F_1      = models.IntegerField()
    C3_F_2      = models.IntegerField()
    C3_F_3      = models.IntegerField()

    C4_T        = models.IntegerField()
    C4_M_1      = models.IntegerField()
    C4_M_2      = models.IntegerField()
    C4_M_3      = models.IntegerField()
    C4_F_1      = models.IntegerField()
    C4_F_2      = models.IntegerField()
    C4_F_3      = models.IntegerField()

    C5_T        = models.IntegerField()
    C5_M_1      = models.IntegerField()
    C5_M_2      = models.IntegerField()
    C5_F_1      = models.IntegerField()
    C5_F_2      = models.IntegerField()

    D1_T        = models.IntegerField()
    D1_M_1      = models.IntegerField()
    D1_F_1      = models.IntegerField()

    D2_T        = models.IntegerField()
    D2_M_1      = models.IntegerField()
    D2_F_1      = models.IntegerField()
    

    E1_T        = models.IntegerField()
    E1_M_1      = models.IntegerField()
    E1_M_2      = models.IntegerField()
    E1_M_3      = models.IntegerField()
    E1_M_4      = models.IntegerField()
    E1_F_1      = models.IntegerField()
    E1_F_2      = models.IntegerField()
    E1_F_3      = models.IntegerField()
    E1_F_4      = models.IntegerField()

    E2_T        = models.IntegerField()
    E2_M_1      = models.IntegerField()
    E2_M_2      = models.IntegerField()
    E2_M_3      = models.IntegerField()
    E2_M_4      = models.IntegerField()
    E2_F_1      = models.IntegerField()
    E2_F_2      = models.IntegerField()
    E2_F_3      = models.IntegerField()
    E2_F_4      = models.IntegerField()

    F1          = models.IntegerField()
    G1_T        = models.IntegerField()
    G1_M_1      = models.IntegerField()
    G1_M_2      = models.IntegerField()
    G1_M_3      = models.IntegerField()
    G1_M_4      = models.IntegerField()
    G1_F_1      = models.IntegerField()
    G1_F_2      = models.IntegerField()
    G1_F_3      = models.IntegerField()
    G1_F_4      = models.IntegerField()
    
    H1          = models.IntegerField()
    
    I1_T        = models.IntegerField()
    I1_M_1      = models.IntegerField()
    I1_M_2      = models.IntegerField()
    I1_M_3      = models.IntegerField()
    I1_M_4      = models.IntegerField()
    I1_F_1      = models.IntegerField()
    I1_F_2      = models.IntegerField()
    I1_F_3      = models.IntegerField()
    I1_F_4      = models.IntegerField()

    M1          = models.IntegerField()
    M2          = models.IntegerField()
    M3          = models.IntegerField()
    M4          = models.IntegerField()
    J1          = models.IntegerField()
    J2          = models.IntegerField()
    J3          = models.IntegerField()

    J4_T        = models.IntegerField()
    J4_M_1      = models.IntegerField()
    J4_F_1      = models.IntegerField()

    J5_T        = models.IntegerField()
    J5_M_1      = models.IntegerField()
    J5_F_1      = models.IntegerField()
    J6_T        = models.IntegerField()
    J6_M_1      = models.IntegerField()
    J6_F_1      = models.IntegerField()

    
    K1_T        = models.IntegerField()
    K1_M_1      = models.IntegerField()
    K1_M_2      = models.IntegerField()
    K1_M_3      = models.IntegerField()
    K1_M_4      = models.IntegerField()
    K1_F_1      = models.IntegerField()
    K1_F_2      = models.IntegerField()
    K1_F_3      = models.IntegerField()
    K1_F_4      = models.IntegerField()

    K2          = models.IntegerField()
    K3          = models.IntegerField()
    K4          = models.IntegerField()
    K5          = models.IntegerField()
    K6          = models.IntegerField()
    L1          = models.IntegerField()

    responsavel_creas = models.ForeignKey(
        ResponsavelModel, on_delete=models.CASCADE)
    nome_creas = models.CharField(max_length=100)
    cod_creas = models.IntegerField()
    mes_ref = models.CharField(max_length=10)
