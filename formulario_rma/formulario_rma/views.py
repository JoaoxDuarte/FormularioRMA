from django.db import transaction
import datetime
from main_app.models import FormCreasModel, QtdPesAbdEquipServMesRef, ResponsavelModel
from main_app.models import SituaIdentServEspcAbordaSocialMesRef
from main_app.models import PesSituaRuaPAEFImesRef
from main_app.models import AtendRealizadosMesRef
from main_app.models import VolAdltesMedSoceduca
from main_app.models import QtdNovosAdltesServMesRef
from main_app.models import NovosAdltesLAmesRef
from main_app.models import NovosAdltesPSCmesRef
from main_app.models import MulheresAdultVitViolIntrafamiliarPAEFImesRef
from main_app.models import PesVitTrafHumanoPAEFImesRef
from main_app.models import PesVitDiscrimiOrieSexualPAEFImesRef
from main_app.models import IdososSituaViolPAEFImesRefD2
from main_app.models import IdososSituaViolPAEFImesRefD1
from main_app.models import CrianAdltesTrabInfantilPAEFImesRef
from main_app.models import PesComDeficienciaViolPAEFImesRefE1
from main_app.models import PesComDeficienciaViolPAEFImesRefE2
from main_app.models import CrianAdltesViolIngressaPAEFImesRefC4
from main_app.models import CrianAdltesViolIngressaPAEFImesRefC3
from main_app.models import CrianAdltesViolIngressaPAEFImesRefC2
from main_app.models import CrianAdltesViolIngressaPAEFImesRefC1
from main_app.models import PesVitimasViolDireitosPAEFImesRef
from main_app.models import NovosCasosAcompanhaPAEFImesRef
from main_app.models import FamiliasAcompanhadasPAIF
from core.infrastructure.repository_implementation.ListaUnidadesSidsRepositoryImpl import ListaUnidadesRepositoryImpl
from datetime import date
from django.shortcuts import render
import json
import copy

# Create your views here.

from django.http import HttpResponse
from core.application.use_cases.enviarDadosCrasAlvo import EnviarDadosCrasParaAlvo

from django.contrib.auth.decorators import login_required


from core.domain.entities.DadosPAIF import DadosPAIF
from core.domain.entities.VolumeServicosConvivenciaEFortalecimentoVinculos import VolumeServicosConvivenciaEFortalecimentoVinculosDeFamiliasPAIF
from core.domain.entities.dadosCras import DadosCras
from core.domain.entities.responsavelCras import ResponsavelCras
from core.domain.entities.volume_atendimento_particularizado import VolumeAtendimentoParticularizado
from core.infrastructure.repository_implementation.DadosCrasRepositoryImpl import DadosCrasRepositoryImpl
from core.infrastructure.repository_implementation.responsavelCrasSidsRepositoryImpl import ResponsavelCrasSidsRepositoryImpl
from core.infrastructure.repository_implementation.ResponsavelCrasRepositoryImpl import ResponsavelCrasRepositoryImpl
from core.application.use_cases.CasodeUso_RecuperarDadosCras import RecuperarDadosCras
from core.domain.utils.data_transform import data_transform
import logging
import dataclasses
import json
from json2xml import json2xml
from json2xml.utils import readfromstring
from datetime import datetime


from main_app.models import PesSituaRuaAtendServMesRef
from main_app.models import CaractEspIdentiPesAtendServMesRef
from main_app.models import CadastraPesSituaRuaMesRef
from main_app.models import VolTotalAtendRealiMesRef
from main_app.models import SituaIdentiServEspAbordaSocMesRef
from main_app.models import QtdPerfilPesAbordaEquipServMesRef
from main_app.models import VolAbordagensRealiCras

logger = logging.getLogger(__name__)


#####Centro Pop#####
def extract_pes_situa_rua_atend_serv_mes_Ref(post_dict):
    de_0_a_12_M = post_dict['A1_M_1']
    de_13_a_17_M = post_dict['A1_M_2']
    de_18_a_39_M = post_dict['A1_M_3']
    de_40_a_59_M = post_dict['A1_M_4']
    de_60_M = post_dict['A1_M_5']

    de_0_a_12_F = post_dict['A1_F_1']
    de_13_a_17_F = post_dict['A1_F_2']
    de_18_a_39_F = post_dict['A1_F_3']
    de_40_a_59_F = post_dict['A1_F_4']
    de_60_F = post_dict['A1_F_5']

    return (PesSituaRuaAtendServMesRef(
        sexo="MASCULINO",
        de_0_a_12_anos=de_0_a_12_M,
        de_13_a_17_anos=de_13_a_17_M,
        de_18_a_39_anos=de_18_a_39_M,
        de_40_a_59_anos=de_40_a_59_M,
        de_60_anos_ou_mais=de_60_M
    ), PesSituaRuaAtendServMesRef(
        sexo="FEMININO",
        de_0_a_12_anos=de_0_a_12_F,
        de_13_a_17_anos=de_13_a_17_F,
        de_18_a_39_anos=de_18_a_39_F,
        de_40_a_59_anos=de_40_a_59_F,
        de_60_anos_ou_mais=de_60_F
    ))


def extract_caract_esp_identi_pes_atend_serv_mes_ref(post_dict):
    pes_usua_drogas = post_dict['B1']
    migrantes = post_dict['B2']
    pes_doenca_transt_mental = post_dict['B3']

    return (CaractEspIdentiPesAtendServMesRef(
        pes_usua_drogas,
        migrantes,
        pes_doenca_transt_mental
    ))


def extract_cadastra_pes_situa_rua_mes_ref(post_dict):
    pes_incluidas_cad_unico_mes_ref = post_dict['C1']
    pes_reali_atuali_cad_unico_mes_ref = post_dict['C2']

    return (CadastraPesSituaRuaMesRef(
        pes_incluidas_cad_unico_mes_ref,
        pes_reali_atuali_cad_unico_mes_ref
    ))


def extract_vol_total_atend_reali_mes_ref(post_dict):
    qtd_total_atend_reali_mes_ref = post_dict['D1']

    return (VolTotalAtendRealiMesRef(
        qtd_total_atend_reali_mes_ref
    ))


def extract_pes_situa_rua_atend_serv_mes_ref(post_dict):
    de_0_a_12_M = post_dict['E1_M_1']
    de_13_a_17_M = post_dict['E1_M_2']
    de_18_a_59_M = post_dict['E1_M_3']
    de_60_M = post_dict['E1_M_4']

    de_0_a_12_F = post_dict['E1_F_1']
    de_13_a_17_F = post_dict['E1_F_2']
    de_18_a_59_F = post_dict['E1_F_3']
    de_60_F = post_dict['E1_F_4']

    return (QtdPerfilPesAbordaEquipServMesRef(
        sexo="MASCULINO",
        de_0_a_12_anos=de_0_a_12_M,
        de_13_a_17_anos=de_13_a_17_M,
        de_18_a_59_anos=de_18_a_59_M,
        de_60_anos_ou_mais=de_60_M
    ), QtdPerfilPesAbordaEquipServMesRef(
        sexo="FEMININO",
        de_0_a_12_anos=de_0_a_12_F,
        de_13_a_17_anos=de_13_a_17_F,
        de_18_a_59_anos=de_18_a_59_F,
        de_60_anos_ou_mais=de_60_F
    ))


def extract_situa_identi_serv_esp_aborda_soc_mes_ref(post_dict):
    criancas_adltes_situa_trab_infantil_ate_15_anos = post_dict['E2']
    criancas_adltes_situa_explor_sexual = post_dict['E3']
    criancas_adltes_usua_drogas = post_dict['E4']
    pes_adultas_usua_drogas = post_dict['E5']
    migrantes = post_dict['E6']

    return (SituaIdentiServEspAbordaSocMesRef(
        criancas_adltes_situa_trab_infantil_ate_15_anos,
        criancas_adltes_situa_explor_sexual,
        criancas_adltes_usua_drogas,
        pes_adultas_usua_drogas,
        migrantes
    ))


def extract_vol_abordagens_reali(post_dict):
    qtd_total_aborda_realizadas = post_dict['F1']

    return (VolAbordagensRealiCras(
        qtd_total_aborda_realizadas
    ))


def to_json(object):
    return json.dumps(object, default=lambda o: o.__dict__,
                      sort_keys=True, indent=4)


@login_required
def send_form_target(request):
    if not 'select' in request.GET:
        select = None
    else:
        select = request.GET['select']

    if not 'id_list' in request.GET:
        id_list = None
    else:
        id_list = request.GET['id_list']
        print("entrouuuuuuuuuuuuuuuuuuuuuuuuu")
    print("id_________________________________list")

    id_list = list(id_list.split(' '))
    print(id_list)
    for id in id_list:
        print(id)
        select = select.lower()
    # mes_referencia =
    # c
    # .today().strftime('%m') essa linha serve para pegar o mes de referencia atual
    mes_numero = (datetime.now().month)-1
    print("mes_numero_______________________________________________")
    print(mes_numero)
    mes_referencia = data_transform(mes_numero)
    form_data_json = []
    if select == 'cras':
        print("for_____________________________________________")
        for id in id_list:
            print(id)
            id_cras = id
            repositorio_cras = DadosCrasRepositoryImpl()
            caso_de_uso_recuperar = RecuperarDadosCras(repositorio_cras)
            form_data = caso_de_uso_recuperar.run(id_cras, mes_referencia)
            repositorio_enviar = None   # Mudar isso pro repositorio
            # caso_de_uso_enviar = EnviarDadosCrasParaAlvo(repositorio_enviar)
            # caso_de_uso_enviar.run(form_data)
            form_data_json.append(form_data)

            form_data_json = str(json.dumps(
                form_data.__dict__, default=lambda o: o.__dict__))
            all_data += form_data_json

        print("all_data________________________________")
        print(all_data)
        xml_data = json2xml.Json2xml(
            all_data, wrapper="all", pretty=True).to_xml()

        form_data_json = to_json(form_data_json)
        form_data_json = readfromstring(form_data_json)
        print("form_data_json_____________________")
        xml_data = json2xml.Json2xml(
            form_data_json, wrapper="all", pretty=True).to_xml()
        return HttpResponse(xml_data, content_type='text/xml')
        # return HttpResponse(form_data_json, content_type="application/json")   Retorno em json
    elif select == 'creas':
        id_creas = id
        return
    id_centro_pop = id

    return render(request, "error500.html", status=500)


@login_required
@transaction.non_atomic_requests
def get_form_centro_pop(request):
    if not request.user.groups.filter(name='centro_pop').exists():
        return render(request, "unauthorized.html", status=401)
    if request.method != 'POST':
        response = HttpResponse("Há algo errado com o formulário")
        response.status_code = 400
        return render(request, "error500.html", status=400)

    pessoas_sit_rua_paef_m, pessoas_sit_rua_paef_f = extract_pes_situa_rua_atend_serv_mes_Ref(
        request.POST)
    pessoas_sit_rua_paef_m.save()
    pessoas_sit_rua_paef_f.save()

    caracteristicas_especificas_paef = extract_caract_esp_identi_pes_atend_serv_mes_ref(
        request.POST)
    caracteristicas_especificas_paef.save()

    cadastramento_pessoas_situacao_rua = extract_cadastra_pes_situa_rua_mes_ref(
        request.POST)
    cadastramento_pessoas_situacao_rua.save()

    volume_total_atendimentos_realizados = extract_vol_total_atend_reali_mes_ref(
        request.POST)
    volume_total_atendimentos_realizados.save()

    quantidade_perfil_pessoas_abordadas_m, quantidade_perfil_pessoas_abordadas_f = extract_pes_situa_rua_atend_serv_mes_ref(
        request.POST)
    quantidade_perfil_pessoas_abordadas_m.save()
    quantidade_perfil_pessoas_abordadas_f.save()

    situacoes_identificadas_servico_especializado_abordagem_social = extract_situa_identi_serv_esp_aborda_soc_mes_ref(
        request.POST)
    situacoes_identificadas_servico_especializado_abordagem_social.save()

    vol_abordagens_reali = extract_vol_abordagens_reali(request.POST)

    try:
        vol_abordagens_reali.save()

    except:
        response = HttpResponse("Há algo errado com o formulário")
        response.status_code = 500
        return render(request, "error500.html", status=500)

    return render(request, "success.html", status=200)


###############################################################################################################
######CREAS######


def extract_fam_acompanhadas_paif(post_dict):
    total_casos_acompanha_PAEFI = post_dict['A1']
    novos_casos_inseridos_acompanha_PAEFI_mes_ref = post_dict['A2']

    return (FamiliasAcompanhadasPAIF(
        total_casos_acompanha_PAEFI,
        novos_casos_inseridos_acompanha_PAEFI_mes_ref
    ))


def extract_novos_casos_inser_acompanha_paefi_mes_ref(post_dict):
    fam_benef_bolsa_familia = post_dict['B1']
    fam_membros_benef_bpc = post_dict['B2']
    fam_criancas_adltes_trab_infantil = post_dict['B3']
    fam_criancas_adltes_serv_acolhi = post_dict['B4']
    fam_situa_viol_substan_psicoativas = post_dict['B5']
    fam_adltes_med_soceducativas_meio_aberto = post_dict['B7']

    return (NovosCasosAcompanhaPAEFImesRef(
        fam_benef_bolsa_familia,
        fam_membros_benef_bpc,
        fam_criancas_adltes_trab_infantil,
        fam_criancas_adltes_serv_acolhi,
        fam_situa_viol_substan_psicoativas,
        fam_adltes_med_soceducativas_meio_aberto
    ))


def extract_pes_viol_direitos_paefi_mes_ref(post_dict):  # B.6
    de_0_a_12_M = post_dict['B6_M_1']
    de_13_a_17_M = post_dict['B6_M_2']
    de_18_a_59_M = post_dict['B6_M_3']
    de_60_M = post_dict['B6_M_4']

    de_0_a_12_F = post_dict['B6_F_1']
    de_13_a_17_F = post_dict['B6_F_2']
    de_18_a_59_F = post_dict['B6_F_3']
    de_60_F = post_dict['B6_F_4']

    return (PesVitimasViolDireitosPAEFImesRef(
        sexo="MASCULINO",
        de_0_a_12_anos=de_0_a_12_M,
        de_13_a_17_anos=de_13_a_17_M,
        de_18_a_59_anos=de_18_a_59_M,
        de_60_anos_ou_mais=de_60_M
    ), PesVitimasViolDireitosPAEFImesRef(
        sexo="FEMININO",
        de_0_a_12_anos=de_0_a_12_F,
        de_13_a_17_anos=de_13_a_17_F,
        de_18_a_59_anos=de_18_a_59_F,
        de_60_anos_ou_mais=de_60_F
    ))


# C1 (n°4)
def extract_criancas_adltes_viol_ingressa_paefi_mes_ref_c1(post_dict):
    de_0_a_6_M = post_dict['C1_M_1']
    de_7_a_12_M = post_dict['C1_M_2']
    de_13_a_17_M = post_dict['C1_M_3']

    de_0_a_6_F = post_dict['C1_F_1']
    de_7_a_12_F = post_dict['C1_F_2']
    de_13_a_17_F = post_dict['C1_F_3']

    return (CrianAdltesViolIngressaPAEFImesRefC1(
        sexo="MASCULINO",
        de_0_a_6_anos=de_0_a_6_M,
        de_7_a_12_anos=de_7_a_12_M,
        de_13_a_17_anos=de_13_a_17_M
    ), CrianAdltesViolIngressaPAEFImesRefC1(
        sexo="FEMININO",
        de_0_a_6_anos=de_0_a_6_F,
        de_7_a_12_anos=de_7_a_12_F,
        de_13_a_17_anos=de_13_a_17_F
    ))


def extract_criancas_adltes_viol_ingressa_paefi_mes_ref_c2(post_dict):
    de_0_a_6_M = post_dict['C2_M_1']
    de_7_a_12_M = post_dict['C2_M_2']
    de_13_a_17_M = post_dict['C2_M_3']

    de_0_a_6_F = post_dict['C2_F_1']
    de_7_a_12_F = post_dict['C2_F_2']
    de_13_a_17_F = post_dict['C2_F_3']

    return (CrianAdltesViolIngressaPAEFImesRefC2(
        sexo="MASCULINO",
        de_0_a_6_anos=de_0_a_6_M,
        de_7_a_12_anos=de_7_a_12_M,
        de_13_a_17_anos=de_13_a_17_M
    ), CrianAdltesViolIngressaPAEFImesRefC2(
        sexo="FEMININO",
        de_0_a_6_anos=de_0_a_6_F,
        de_7_a_12_anos=de_7_a_12_F,
        de_13_a_17_anos=de_13_a_17_F
    ))


def extract_criancas_adltes_viol_ingressa_paefi_mes_ref_c3(post_dict):
    de_0_a_6_M = post_dict['C3_M_1']
    de_7_a_12_M = post_dict['C3_M_2']
    de_13_a_17_M = post_dict['C3_M_3']

    de_0_a_6_F = post_dict['C3_F_1']
    de_7_a_12_F = post_dict['C3_F_2']
    de_13_a_17_F = post_dict['C3_F_3']

    return (CrianAdltesViolIngressaPAEFImesRefC3(
        sexo="MASCULINO",
        de_0_a_6_anos=de_0_a_6_M,
        de_7_a_12_anos=de_7_a_12_M,
        de_13_a_17_anos=de_13_a_17_M
    ), CrianAdltesViolIngressaPAEFImesRefC3(
        sexo="FEMININO",
        de_0_a_6_anos=de_0_a_6_F,
        de_7_a_12_anos=de_7_a_12_F,
        de_13_a_17_anos=de_13_a_17_F
    ))


def extract_criancas_adltes_viol_ingressa_paefi_mes_ref_c4(post_dict):
    de_0_a_6_M = post_dict['C4_M_1']
    de_7_a_12_M = post_dict['C4_M_2']
    de_13_a_17_M = post_dict['C4_M_3']

    de_0_a_6_F = post_dict['C3_F_1']
    de_7_a_12_F = post_dict['C3_F_2']
    de_13_a_17_F = post_dict['C3_F_3']

    return (CrianAdltesViolIngressaPAEFImesRefC4(
        sexo="MASCULINO",
        de_0_a_6_anos=de_0_a_6_M,
        de_7_a_12_anos=de_7_a_12_M,
        de_13_a_17_anos=de_13_a_17_M
    ), CrianAdltesViolIngressaPAEFImesRefC4(
        sexo="FEMININO",
        de_0_a_6_anos=de_0_a_6_F,
        de_7_a_12_anos=de_7_a_12_F,
        de_13_a_17_anos=de_13_a_17_F
    ))


# C.5 (n°5)
def extract_criancas_adltes_trab_infantil_paefi_mes_ref(post_dict):
    de_0_a_6_M = post_dict['C5_M_1']
    de_7_a_12_M = post_dict['C5_M_2']

    de_0_a_6_F = post_dict['C5_F_1']
    de_7_a_12_F = post_dict['C5_F_2']

    return (CrianAdltesTrabInfantilPAEFImesRef(
        sexo="MASCULINO",
        de_0_a_6_anos=de_0_a_6_M,
        de_7_a_12_anos=de_7_a_12_M
    ), CrianAdltesTrabInfantilPAEFImesRef(
        sexo="FEMININO",
        de_0_a_6_anos=de_0_a_6_F,
        de_7_a_12_anos=de_7_a_12_F
    ))


def extract_idosos_situa_viol_paefi_mes_ref_d1(post_dict):  # D.1
    de_60_M = post_dict['D1_M_1']
    de_60_F = post_dict['D1_F_1']

    return (IdososSituaViolPAEFImesRefD1(
        sexo="MASCULINO",
        de_60_anos_ou_mais=de_60_M
    ), IdososSituaViolPAEFImesRefD1(
        sexo="FEMININO",
        de_60_anos_ou_mais=de_60_F
    ))


def extract_idosos_situa_viol_paefi_mes_ref_d2(post_dict):  # D.2
    de_60_M = post_dict['D2_M_1']
    de_60_F = post_dict['D2_F_1']

    return (IdososSituaViolPAEFImesRefD2(
        sexo="MASCULINO",
        de_60_anos_ou_mais=de_60_M
    ), IdososSituaViolPAEFImesRefD2(
        sexo="FEMININO",
        de_60_anos_ou_mais=de_60_F
    ))


def extract_pes_deficiencia_diol_paefi_mes_ref_e1(post_dict):  # E.1 (n°7)
    de_0_a_12_M = post_dict['E1_M_1']
    de_13_a_17_M = post_dict['E1_M_2']
    de_18_a_59_M = post_dict['E1_M_3']
    de_60_M = post_dict['E1_M_4']

    de_0_a_12_F = post_dict['E1_F_1']
    de_13_a_17_F = post_dict['E1_F_2']
    de_18_a_59_F = post_dict['E1_F_3']
    de_60_F = post_dict['E1_F_4']

    return (PesComDeficienciaViolPAEFImesRefE1(
        sexo="MASCULINO",
        de_0_a_12_anos=de_0_a_12_M,
        de_13_a_17_anos=de_13_a_17_M,
        de_18_a_59_anos=de_18_a_59_M,
        de_60_anos_ou_mais=de_60_M
    ), PesComDeficienciaViolPAEFImesRefE1(
        sexo="FEMININO",
        de_0_a_12_anos=de_0_a_12_F,
        de_13_a_17_anos=de_13_a_17_F,
        de_18_a_59_anos=de_18_a_59_F,
        de_60_anos_ou_mais=de_60_F
    ))


def extract_pes_deficiencia_diol_paefi_mes_ref_e2(post_dict):  # E.2
    de_0_a_12_M = post_dict['E1_M_1']
    de_13_a_17_M = post_dict['E1_M_2']
    de_18_a_59_M = post_dict['E1_M_3']
    de_60_M = post_dict['E1_M_4']

    de_0_a_12_F = post_dict['E1_F_1']
    de_13_a_17_F = post_dict['E1_F_2']
    de_18_a_59_F = post_dict['E1_F_3']
    de_60_F = post_dict['E1_F_4']

    return (PesComDeficienciaViolPAEFImesRefE2(
        sexo="MASCULINO",
        de_0_a_12_anos=de_0_a_12_M,
        de_13_a_17_anos=de_13_a_17_M,
        de_18_a_59_anos=de_18_a_59_M,
        de_60_anos_ou_mais=de_60_M
    ), PesComDeficienciaViolPAEFImesRefE2(
        sexo="FEMININO",
        de_0_a_12_anos=de_0_a_12_F,
        de_13_a_17_anos=de_13_a_17_F,
        de_18_a_59_anos=de_18_a_59_F,
        de_60_anos_ou_mais=de_60_F
    ))


def extract_mulheres_adult_viol_intrafami_paefi_mes_ref(post_dict):  # F  (n°8)
    mulheres_adultas_viol_intrafami = post_dict['F1']
    return (MulheresAdultVitViolIntrafamiliarPAEFImesRef(mulheres_adultas_viol_intrafami)
            )


def extract_pes_trafico_humano_paefi_mes_ref(post_dict):  # G

    de_0_a_12_M = post_dict['G1_M_1']
    de_13_a_17_M = post_dict['G1_M_2']
    de_18_a_59_M = post_dict['G1_M_3']
    de_60_M = post_dict['G1_M_4']

    de_0_a_12_F = post_dict['G1_F_1']
    de_13_a_17_F = post_dict['G1_F_2']
    de_18_a_59_F = post_dict['G1_F_3']
    de_60_F = post_dict['G1_F_4']

    return (PesVitTrafHumanoPAEFImesRef(
        sexo="MASCULINO",
        de_0_a_12_anos=de_0_a_12_M,
        de_13_a_17_anos=de_13_a_17_M,
        de_18_a_59_anos=de_18_a_59_M,
        de_60_anos_ou_mais=de_60_M), PesVitTrafHumanoPAEFImesRef(

        sexo="FEMININO",
        de_0_a_12_anos=de_0_a_12_F,
        de_13_a_17_anos=de_13_a_17_F,
        de_18_a_59_anos=de_18_a_59_F,
        de_60_anos_ou_mais=de_60_F))


def extract_pes_discrimi_orie_sexual_paefi_mes_ref(post_dict):  # H
    pes_discrimi_orie_sexual = post_dict['H1']

    return (PesVitDiscrimiOrieSexualPAEFImesRef
            (pes_discrimi_orie_sexual))


def extract_pes_situa_rua_paefi_mes_ref(post_dict):  # i
    de_0_a_12_M = post_dict['I1_M_1']
    de_13_a_17_M = post_dict['I1_M_2']
    de_18_a_59_M = post_dict['I1_M_3']
    de_60_M = post_dict['I1_M_4']

    de_0_a_12_F = post_dict['I1_F_1']
    de_13_a_17_F = post_dict['I1_F_2']
    de_18_a_59_F = post_dict['I1_F_3']
    de_60_F = post_dict['I1_F_4']

    return (PesSituaRuaPAEFImesRef(
        sexo="MASCULINO",
        de_0_a_12_anos=de_0_a_12_M,
        de_13_a_17_anos=de_13_a_17_M,
        de_18_a_59_anos=de_18_a_59_M,
        de_60_anos_ou_mais=de_60_M), PesSituaRuaPAEFImesRef(

        sexo="FEMININO",
        de_0_a_12_anos=de_0_a_12_F,
        de_13_a_17_anos=de_13_a_17_F,
        de_18_a_59_anos=de_18_a_59_F,
        de_60_anos_ou_mais=de_60_F))


def extract_atend_realizados_mes_ref(post_dict):  # M
    total_atendi_indivi_mes_ref = post_dict['M1']
    total_atendi_grupo_mes_ref = post_dict['M2']
    fam_encaminha_cras_mes_ref = post_dict['M3']
    visitas_domici_mes_ref = post_dict['M4']

    return (AtendRealizadosMesRef(
        total_atendi_indivi_mes_ref,
        total_atendi_grupo_mes_ref,
        fam_encaminha_cras_mes_ref,
        visitas_domici_mes_ref
    ))


def extract_vol_adltes_med_soceducativas(post_dict):  # J
    total_adltes_med_soceduca = post_dict['J1']
    qtd_adltes_liberdade_assisti = post_dict['J2']
    qtd_adltes_presta_serv_comuni = post_dict['J3']

    return (VolAdltesMedSoceduca(
        total_adltes_med_soceduca,
        qtd_adltes_liberdade_assisti,
        qtd_adltes_presta_serv_comuni
    ))


def extract_qtd_novos_adltes_serv_mes_ref_j4(post_dict):  # J.4
    masculino = post_dict['J4_M_1']
    feminino = post_dict['J4_F_1']

    return (QtdNovosAdltesServMesRef(
        masculino,
        feminino))


def extract_novos_adltes_la_mes_ref(post_dict):  # J.5
    masculino = post_dict['J4_M_1']
    feminino = post_dict['J4_F_1']

    return (NovosAdltesLAmesRef(
        masculino,
        feminino))


def extract_novos_adltes_psc_mes_ref(post_dict):  # J.6
    masculino = post_dict['J4_M_1']
    feminino = post_dict['J4_F_1']

    return (NovosAdltesPSCmesRef(
        masculino,
        feminino))


def extract_qtd_pes_aborda_equip_serv_mes_ref(post_dict):  # K
    de_0_a_12_M = post_dict['K1_M_1']
    de_13_a_17_M = post_dict['K1_M_2']
    de_18_a_59_M = post_dict['K1_M_3']
    de_60_M = post_dict['K1_M_4']

    de_0_a_12_F = post_dict['K1_F_1']
    de_13_a_17_F = post_dict['K1_F_2']
    de_18_a_59_F = post_dict['K1_F_3']
    de_60_F = post_dict['K1_F_4']

    return (QtdPesAbdEquipServMesRef(
        sexo="MASCULINO",
        de_0_a_12_anos=de_0_a_12_M,
        de_13_a_17_anos=de_13_a_17_M,
        de_18_a_59_anos=de_18_a_59_M,
        de_60_anos_ou_mais=de_60_M), QtdPesAbdEquipServMesRef(

        sexo="FEMININO",
        de_0_a_12_anos=de_0_a_12_F,
        de_13_a_17_anos=de_13_a_17_F,
        de_18_a_59_anos=de_18_a_59_F,
        de_60_anos_ou_mais=de_60_F))


def extract_situa_ident_serv_esp_aborda_social_mes_ref(post_dict):
    criancas_adltes_trab_infatil_ate_15_anos = post_dict['K2']  # K.02
    criancas_adltes_explo_sexual = post_dict['K3']
    criancas_adltes_usua_drogas = post_dict['K4']
    adultos_usua_drogas = post_dict['K5']
    migrantes = post_dict['K6']

    return (SituaIdentServEspcAbordaSocialMesRef(
        criancas_adltes_trab_infatil_ate_15_anos,
        criancas_adltes_explo_sexual,
        criancas_adltes_usua_drogas,
        adultos_usua_drogas,
        migrantes
    ))


def extract_vol_aborda_realizadas(post_dict):  # L
    qtd_total_aborda_reali_mes_ref = post_dict['L1']

    return (VolAbordagensRealiCras(
        qtd_total_aborda_reali_mes_ref))


@login_required
@transaction.non_atomic_requests
def get_form_creas(request):
    if not request.user.groups.filter(name='creas').exists():
        return render(request, "unauthorized.html", status=401)

    if request.method != 'POST':
        response = HttpResponse("Há algo errado com o formulário")
        response.status_code = 400
        return render(request, "error500.html", status=400)

    login_str = str(request.user)
    login = login_str.split('@sedes.df.gov.br')[0]

    sidsResponsavelImpl = ResponsavelCrasSidsRepositoryImpl()

    responsavel = sidsResponsavelImpl.recuperar_responsavel_cras(login)
    arguments = {p:request.POST[p] for p in request.POST if p in FormCreasModel.__dict__}


    responsavelModel = ResponsavelModel.objects.update_or_create(     
        nome= responsavel.nome,
        matricula = responsavel.matricula,
        email_funcional=responsavel.email_funcional,
        cargo = responsavel.cargo,
        id_unidade = responsavel.id_unidade

    )

    arguments['cod_creas'] = responsavel.id_unidade
    arguments['responsavel_creas'] = responsavelModel[0]

    currentMonth = (datetime.now().month)-1
    mes_referencia = data_transform(currentMonth)
    arguments['mes_ref'] = mes_referencia


    lista_unidades_repo = ListaUnidadesRepositoryImpl()
    list_unidades_creas = lista_unidades_repo.recuperar_unidades_creas()

    nome_creas = 'NÃO ENCONTRADO'
    codigo_creas = '000'
    for creas in (list_unidades_creas):
            if (creas.id_unidade == responsavel.id_unidade):
                nome_creas = creas.nome
                codigo_creas = creas.id_unidade


    arguments['nome_creas'] = nome_creas

    formCreasModel = FormCreasModel(
        **arguments
    )

    try:
       formCreasModel.save()

    except Exception as e:

        print(e)
        response = HttpResponse("Há algo errado com o formulário")
        response.status_code = 500
        return render(request, "error500.html", status=500)

    return render(request, "success.html", status=200)


@login_required
def get_form_cras(request):

    if not request.user.groups.filter(name='cras').exists():
        return render(request, "unauthorized.html", status=401)
    login_str = str(request.user)
    login = login_str.split('@sedes.df.gov.br')[0]

    logger.info(f'Formulário enviado pelo usuário {login_str}')

    if request.method != 'POST':
        response = HttpResponse("Not Allowed")
        response.status_code = 405
        return response

    total_de_familias_acompanhamento_paif = int(request.POST['A1'])
    novas_familias_inseridas_acompanhamento_PAIF = int(request.POST['A2'])

    familias_extrema_pobreza = int(request.POST['B1'])
    familias_bolsa_familia = int(request.POST['B2'])
    familias_bolsa_familia_descumprimento = int(request.POST['B3'])
    familias_bpc = int(request.POST['B4'])
    familias_criancas_adolescentes_trabalho = int(request.POST['B5'])
    familias_criancas_adolescentes_acolhimento = int(request.POST['B6'])

    total_atendimento_particularizado_mes = int(request.POST['C1'])
    familias_encaminhadas_cadastro_unico = int(request.POST['C2'])
    familias_encaminhas_atualizacao_cadastro_unico = int(
        request.POST['C3'])
    individuos_encaminhados_bpc = int(request.POST['C4'])
    familias_encaminhadas_creas = int(request.POST['C5'])
    visitas_domiciliares = int(request.POST['C6'])
    total_auxilio_natalidade = int(request.POST['C7'])
    total_auxilio_funeral = int(request.POST['C8'])
    outros_beneficios = int(request.POST['C9'])

    familias_regularmente_paif = int(request.POST['D1'])
    criancas_0_a_6_anos_no_servico = int(request.POST['D2'])
    criancas_adolescentes_servico_convivencia_fortalecimento = int(
        request.POST['D3'])
    adolescentes_servico_convivencia_fortalecimento = int(
        request.POST['D4'])
    idosos_servico_convivencia_fortalecimento = int(request.POST['D5'])
    pessoas_participacao_palestras_oficinas = int(request.POST['D6'])
    pessoas_deficiencia_servicos_convivencia_grupos_paif = int(
        request.POST['D7'])
    adultos_servicos_convivencia_fortalecimento = int(request.POST['D8'])

    print(VolumeServicosConvivenciaEFortalecimentoVinculosDeFamiliasPAIF.__annotations__)
    volume_servicos_form = VolumeServicosConvivenciaEFortalecimentoVinculosDeFamiliasPAIF(total_de_familias_acompanhamento_paif,
                                                                                          familias_regularmente_paif,
                                                                                          criancas_0_a_6_anos_no_servico,
                                                                                          criancas_adolescentes_servico_convivencia_fortalecimento,
                                                                                          adolescentes_servico_convivencia_fortalecimento,
                                                                                          adultos_servicos_convivencia_fortalecimento,
                                                                                          idosos_servico_convivencia_fortalecimento,
                                                                                          pessoas_participacao_palestras_oficinas,
                                                                                          pessoas_deficiencia_servicos_convivencia_grupos_paif)

    dados_paif_form = DadosPAIF(total_de_familias_acompanhamento_paif, novas_familias_inseridas_acompanhamento_PAIF,
                                familias_extrema_pobreza, familias_bolsa_familia, familias_bolsa_familia_descumprimento, familias_bpc,
                                familias_criancas_adolescentes_trabalho, familias_criancas_adolescentes_acolhimento, volume_servicos_form)

    volume_atendimento_particularizado_form = VolumeAtendimentoParticularizado(total_atendimento_particularizado_mes,
                                                                               familias_encaminhadas_cadastro_unico,
                                                                               familias_encaminhas_atualizacao_cadastro_unico,

                                                                               individuos_encaminhados_bpc,
                                                                               familias_encaminhadas_creas,
                                                                               visitas_domiciliares,
                                                                               total_auxilio_natalidade,
                                                                               total_auxilio_funeral,
                                                                               outros_beneficios)

    responsavel_cras = ResponsavelCrasSidsRepositoryImpl().recuperar_responsavel_cras(login)

    # responsavel_cras = ResponsavelCras(
    # 'Nome do responsavel', '4', 'cargo','igor.costa@sedes.df.gov.br',1)       #Usuário que bate no SIDS caso seja necessário
    nome_cras = 'responsavel_cras'   # Pegar o nome do cras pelo login futuramente
    codigo_cras = responsavel_cras.id_unidade
    # Pegar o mes de referencia futuramente (?) pelo login (?) (?) Automaticamente pela data enviada (?)
    mes_referencia = 'Outubro'
    print(mes_referencia)

    dados_cras = DadosCras(dados_paif_form, volume_atendimento_particularizado_form, volume_servicos_form, responsavel_cras,
                           nome_cras, codigo_cras, mes_referencia)

    try:
        responsavel_cras = ResponsavelCrasSidsRepositoryImpl().recuperar_responsavel_cras(login)
        
        # responsavel_cras = ResponsavelCras(
        # 'Nome do responsavel', '4', 'cargo','igor.costa@sedes.df.gov.br',1) 
        id_unidade = responsavel_cras.id_unidade
        lista_unidades_repo = ListaUnidadesRepositoryImpl()
        list_unidades_cras = lista_unidades_repo.recuperar_unidades_cras()
        nome_cras = "NÃO ENCONTRADO"
        codigo_cras = responsavel_cras.id_unidade
        for cras in (list_unidades_cras):
            if (cras.id_unidade == id_unidade):
                nome_cras = cras.nome
                codigo_cras = cras.id_unidade

        currentMonth = (datetime.now().month)-1
        mes_referencia = data_transform(currentMonth)

        dados_cras = DadosCras(dados_paif_form, volume_atendimento_particularizado_form, volume_servicos_form, responsavel_cras,
                               nome_cras, codigo_cras, mes_referencia)

        repositorio_impl_dados_cras = DadosCrasRepositoryImpl()
        enviar = EnviarDadosCrasParaAlvo(repositorio_impl_dados_cras)
        enviar.run(dados_cras)

        logger.info(f'Formulário enviado com sucesso pelo usuário {login_str}')
    except Exception as e:
        print("exception________________________________")
        logger.error(e)
        response = HttpResponse(
            "Erro interno, por favor tente novamente mais tarde")
        response.status_code = 500
        return render(request, "error500.html", status=500)

    return render(request, "success.html", status=200)


@login_required
def rmaAdmin(request):
    if not request.user.groups.filter(name='rma_admin').exists():
        return render(request, "unauthorized.html", status=401)

    login_str = str(request.user)
    logger.info(
        f'Usuário {login_str} requisitou acesso à página de administrador')

    repository = ListaUnidadesRepositoryImpl()
    result_unidades_cp = repository.recuperar_unidades_centro_pop()
    result_unidades_cras = repository.recuperar_unidades_cras()
    print("result_unidade_cras______________________")
    print(result_unidades_cras)
    result_unidades_creas = repository.recuperar_unidades_creas()

    context = {
        'result_unidades_cp': result_unidades_cp,
        'result_unidades_cras': result_unidades_cras,
        'result_unidades_creas': result_unidades_creas
    }

    currentMonth = (datetime.now().month)-1
    mes_referencia = data_transform(currentMonth)

    repositorio_cras = DadosCrasRepositoryImpl()
    caso_de_uso = RecuperarDadosCras(repositorio_cras)

    delete = []
    for cras in (context['result_unidades_cras']):
        try:
            caso_de_uso.run(cras.id_unidade, mes_referencia)
        except:
            delete.append(cras)
            continue

    print("delete__________________________________________")
    print(delete)

    cras_with_data = [
        x for x in context['result_unidades_cras'] if x not in delete]
    context['result_unidades_cras'] = cras_with_data


    delete = []
    for creas in (context['result_unidades_creas']):
        try:
            FormCreasModel.objects.filter(
            cod_creas=id.unidade, mes_ref=mes_referencia).first()
        except:
            delete.append(creas)


    creas_with_data = [
        x for x in context['result_unidades_creas'] if x not in delete]
    context['result_unidades_creas'] = creas_with_data
        
    
    delete = []

    for centro_pop in (context['result_unidades_cp']):
        try:
            pass
            # FormCreasModel.objects.filter(
            # cod_creas=id.unidade, mes_ref=mes_referencia).first()
        except:
            delete.append(centro_pop)

    centro_pop_with_data = [
        x for x in context['result_unidades_cp'] if x not in delete]
    context['result_unidades_cp'] = centro_pop_with_data


    return render(request, "admin_template.html", context)


@login_required

def read_index(request):

    if not request.user.groups.filter(name='rma_admin').exists():
        return render(request, "unauthorized.html", status=401)

    id_creas, id_cras, id_centro_pop, form_data = None, None, None, None
    login_str = str(request.user)
    print(request)

    if not 'unidade' in request.GET:
        unidade = None
    else:
        unidade = request.GET['unidade']
    if unidade == 'cras':

        if 'id_unid' in request.GET:
            id_cras = request.GET['id_unid']
            print(id_cras)

    elif unidade == 'creas':
        if 'id_unid' in request.GET:
            id_creas = request.GET['id_unid']
            print(id_creas)

    elif unidade == 'centro_pop':
        print("centro_pop")

# Esse Id (cras,creas,centro_pop)(Pego a partir do front no botão do olho) é usado para pegar o codigo_cras no nosso banco.
# O id_cras do nosso banco é != desse id_cras. Esse id_cras é = codigo_cras do nosso banco

    if id_cras is not None:
        id_unidade = id_cras
        currentMonth = (datetime.now().month)-1
        mes_referencia = data_transform(currentMonth)
        repositorio_cras = DadosCrasRepositoryImpl()
        caso_de_uso = RecuperarDadosCras(repositorio_cras)
        form_data = caso_de_uso.run(id_cras, mes_referencia)
        
        print(form_data)

    if id_creas is not None:
        id_unidade = id_creas
        currentMonth = (datetime.now().month)-1
        mes_referencia = data_transform(currentMonth)
        form_data = FormCreasModel.objects.filter(mes_ref = mes_referencia, cod_creas = id_creas).last()


    if id_centro_pop is not None:
        print("Centro_pop")

        response = HttpResponse("Erro interno do servidor")
        response.status_code = 500
        return response

    tipo_unidade = request.GET['unidade']
    if not tipo_unidade:
        tipo_unidade = 'cras'
    print(request.GET)
    logger.info(
        f'Usuário {login_str} requisitou acesso à página do formulário {tipo_unidade}')

    if not request.user.groups.filter(name='rma_admin').exists():
        return render(request, "unauthorized.html", status=401)

    arquivo = open(f'formulario_rma/{tipo_unidade}.json', encoding='UTF-8')
    perguntas_json = json.load(arquivo)
    arquivo.close()

    form_data = json.dumps(form_data.__dict__, default=lambda o: o.__dict__)

    print("form_data______________________________________________________________________________________________________")
    print("form_json______________________________________________________________________________")
    print(type(form_data))

    

    print(type(form_data))

    

    nome_unidade = 'NÃO ENCONTRADO'
    endereco = 'NÃO ENCONTRADO'
    municipio = 'NÃO ENCONTRADO'
    uf = 'DF'

    lista_unidades_repo = ListaUnidadesRepositoryImpl()
    list_unidades_cras = lista_unidades_repo.recuperar_unidades_cras()
    print("list unidades cras_________")
    print(list_unidades_cras)
   

    lista_unidades_repo = ListaUnidadesRepositoryImpl()
    list_unidades_cras = lista_unidades_repo.recuperar_unidades_cras()

    for cras in (list_unidades_cras):

        try:
            if (int(cras.id_unidade) == int(id_unidade)):
                print("entrtou")
                nome_unidade = cras.nome
                endereco = cras.endereco
                municipio = cras.nome
                uf = 'DF'
        except:
            continue

    currentMonth = (datetime.now().month)-1
    mes_referencia = data_transform(currentMonth)
    if (mes_referencia == 'Dezembro'):
        ano_referencia = (datetime.now().year)-1
    else:
        ano_referencia = (datetime.now().year)

    mes_ano_referencia = mes_referencia + '/' + str(ano_referencia)

    
    arquivo = open(f'formulario_rma/{tipo_unidade}.json', encoding='UTF-8')
    perguntas_json = json.load(arquivo)
    arquivo.close()
    return render(request, "index.html",
                {'perguntas_json': perguntas_json, 'tipo_unidade': tipo_unidade,'user_cras': nome_unidade, 'id_cras_user': id_unidade, 'mes_ano_user': mes_ano_referencia, 'endereco_user': endereco,
            'municipio_user': municipio, 'uf_user': uf, 'form_data':form_data})



@login_required
def index(request):


    if not 'unidade' in request.GET:
        tipo_unidade = 'cras'
    else:
        tipo_unidade = request.GET['unidade']

    login_str = str(request.user)

    nome_unidade = 'NÃO ENCONTRADO'
    endereco = 'NÃO ENCONTRADO'
    municipio = 'NÃO ENCONTRADO'
    uf = 'DF'

    logger.info(
        f'Usuário {login_str} requisitou acesso à página do formulário {tipo_unidade}')

  
    if not request.user.groups.filter(name=tipo_unidade).exists():
         return render(request, "unauthorized.html", status=401)
         
    login = login_str.split('@sedes.df.gov.br')[0]

    responsavel_cras = ResponsavelCrasSidsRepositoryImpl().recuperar_responsavel_cras(login)
    
    id_unidade = responsavel_cras.id_unidade

    lista_unidades_repo = ListaUnidadesRepositoryImpl()
    list_unidades_cras = lista_unidades_repo.recuperar_unidades_cras()

    for cras in (list_unidades_cras):
        try:
            if (cras.id_unidade == id_unidade):
                nome_unidade = cras.nome
                endereco = cras.endereco
                municipio = cras.nome
                uf = 'DF'
        except:
            continue

    currentMonth = (datetime.now().month)-1
    mes_referencia = data_transform(currentMonth)
    if (mes_referencia == 'Dezembro'):
        ano_referencia = (datetime.now().year)-1
    else:
        ano_referencia = (datetime.now().year)

    mes_ano_referencia = mes_referencia + '/' + str(ano_referencia)

    arquivo = open(f'formulario_rma/{tipo_unidade}.json', encoding='UTF-8')
    perguntas_json = json.load(arquivo)
    arquivo.close()
    return render(request, "index.html",
                  {'perguntas_json': perguntas_json, 'tipo_unidade': tipo_unidade,'user_cras': nome_unidade, 'id_cras_user': id_unidade, 'mes_ano_user': mes_ano_referencia, 'endereco_user': endereco,
                'municipio_user': municipio, 'uf_user': uf})


def test_unid(request):
    repository = ListaUnidadesRepositoryImpl()

    result_unidades_cp = repository.recuperar_unidades_centro_pop()
    result_unidades_cras = repository.recuperar_unidades_cras()
    result_unidades_creas = repository.recuperar_unidades_creas()

    cras_str = "<h1> CRAS</h1> <br>" + \
        "<br/>".join([r.__str__() for r in result_unidades_cras])
    cp_str = "<h1> CENTRO POP</h1> <br>" + \
        "<br/>".join([r.__str__() for r in result_unidades_cp])
    creas_str = "<h1> CREAS</h1> <br>" + \
        "<br/>".join([r.__str__() for r in result_unidades_creas])

    return HttpResponse(
        cras_str + cp_str + creas_str
    )
