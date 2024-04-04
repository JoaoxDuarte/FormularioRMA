from core.domain.entities.dadosCras import DadosCras
from core.domain.entities.volume_atendimento_particularizado import VolumeAtendimentoParticularizado
from core.domain.repositories.dadosCras_repository import DadosCrasRepository
from core.infrastructure.repository_implementation.responsavelCrasSidsRepositoryImpl import ResponsavelCrasSidsRepositoryImpl
from main_app.models import DadosCrasModel, DadosPaifModel, ResponsavelModel, VolAtendParticularizado, VolumeServicosConvivenciaEFortalecimentoVinculosDeFamiliasPAIFModel, VolumeServicosConvivenciaEFortalecimentoVinculosDeFamiliasPAIFModel


class DadosCrasRepositoryImpl(DadosCrasRepository):
    def enviar_dados_cras(self, dados_cras: DadosCras):
        print("repositorio___________________________________________________")
        print(dados_cras)
        # responsavel_cras_sids = ResponsavelCrasSidsRepositoryImpl()

        model_volume_servicos = VolumeServicosConvivenciaEFortalecimentoVinculosDeFamiliasPAIFModel.objects.create(
            **dados_cras.volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF.__dict__)

        print("model_volume_servicos__________________________________")
        print(model_volume_servicos)
        # login = dados_cras.responsavel_cras.email_funcional.split("@")[0]

        # dados_cras_sids = responsavel_cras_sids.recuperar_responsavel_cras(login)

        model_responsavel_cras = ResponsavelModel.objects.create(nome=dados_cras.responsavel_cras.nome,
                                                                     matricula=dados_cras.responsavel_cras.matricula,
                                                                     email_funcional=dados_cras.responsavel_cras.email_funcional,
                                                                     id_unidade=dados_cras.responsavel_cras.id_unidade)

        model_volume_convivencia_e_fortalecimento_de_vinculos = (VolumeServicosConvivenciaEFortalecimentoVinculosDeFamiliasPAIFModel.objects.create
                                                                 (
                                                                     total_familias_PAIF=dados_cras.volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF.total_familias_PAIF,
                                                                     familias_participando_regularmente_de_grupos_no_ambito_PAIF=dados_cras.volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF.familias_participando_regularmente_de_grupos_no_ambito_PAIF,
                                                                     criancas_adolescentes_0_6_anos_no_servico=dados_cras.volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF.criancas_adolescentes_0_6_anos_no_servico,
                                                                     criancas_adolescente_7_a_14_no_servico=dados_cras.volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF.criancas_adolescente_7_a_14_no_servico,
                                                                     adolescenete_15_a_17_no_servico=dados_cras.volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF.adolescenete_15_a_17_no_servico,
                                                                     adultos_18_a_59_servicos=dados_cras.volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF.adultos_18_a_59_servicos,
                                                                     idosos_servico=dados_cras.volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF.idosos_servico,
                                                                     pessoas_que_participaram_de_atividades=dados_cras.volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF.pessoas_que_participaram_de_atividades,
                                                                     pessoas_com_deficiencia_servico=dados_cras.volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF.pessoas_com_deficiencia_servico))

        volume = dados_cras.volume_atendimento_particularizado
        print("model_volume_convivencia_e_fortalecimento_de_vinculos_____________________________________")
        print(model_volume_convivencia_e_fortalecimento_de_vinculos)

        model_volume_atendimento_particularizado = VolAtendParticularizado.objects.create(total_atend_particularizado_mes=volume.total_atendimento_particularizado_mes,
                                                                                          fam_encami_inclusao_cad_unico_mes=volume.familias_encaminhadas_inclusao_cadunico_mes,
                                                                                          fam_encami_atuali_cad_unico_mes=volume.familias_encaminhadas_atualizacao_cadunico_mes,
                                                                                          individuos_encami_bpc=volume.individuos_encaminhados_para_bpc,
                                                                                          fam_encami_para_creas=volume.familias_encaminhadas_para_creas,
                                                                                          visitas_domici_reali=volume.visitas_domiciliares_realizadas,
                                                                                          total_aux_natali_concedido=volume._total_auxilio_natalidade_concedido,
                                                                                          total_aux_funeral_concedido=volume.total_auxilio_funeral_concedido,
                                                                                          outros_benef_concedidos=volume.outros_beneficios_concedidos,
                                                                                          fam_encami_inclusao_atuali_cad_unico_mes=volume.individuos_encaminhados_para_bpc)

        print("_____________________________________________________________________________________")
        print("model_volume_atendimento_particularizado________________________________")
        print(model_volume_atendimento_particularizado)
        model_dados_paif = DadosPaifModel.objects.create(total_fam_em_acompanha_PAIF=dados_cras.dados_Paif.total_de_familias_em_acompanhamento_PAIF,
                                                         total_novas_fam_PAIF=dados_cras.dados_Paif.total_de_novas_familias_PAIF,
                                                         novas_fam_em_situa_extre_pobreza=dados_cras.dados_Paif.novas_familias_em_situacao_de_extrema_pobreza,
                                                         novas_fam_bolsa_familia=dados_cras.dados_Paif.novas_familias_bolsa_familia,
                                                         novas_familias_membros_bpc=dados_cras.dados_Paif.novas_familias_membros_bpc,
                                                         novas_familias_bolsa_familia_em_descomprimento=dados_cras.dados_Paif.novas_familias_bolsa_familia_em_descomprimento,
                                                         novas_familias_criancas_adltes_trabalho=dados_cras.dados_Paif.novas_familias_criancas_adolescentes_trabalho,
                                                         novas_familias_criancas_adltes_acolhimento=dados_cras.dados_Paif.novas_familias_criancas_adolescentes_acolhimento,
                                                         volume_convivencia_e_fortalecimento_de_vinculos=model_volume_convivencia_e_fortalecimento_de_vinculos
                                                         )

        model_dados_cras = DadosCrasModel.objects.create(
            DadosPAIF=model_dados_paif,
            vol_atend_particularizado=model_volume_atendimento_particularizado,
            vol_serv_convive_fortale_vinculos_fam_PAIF=model_volume_servicos,
            responsavel_cras=model_responsavel_cras,
            nome_cras=dados_cras.nome_cras,
            cod_cras=dados_cras.codigo_cras,
            mes_ref=dados_cras.mes_referencia)

        print("_____________________________________________________________________________________")
        print("model_dados_cras______________________________________________")
        print(model_dados_cras)
        print("Model_dados_paif____________________")
        print(model_dados_paif)

        try:
            model_volume_convivencia_e_fortalecimento_de_vinculos.save()
            model_responsavel_cras.save()
            model_dados_paif.save()
            model_volume_servicos.save()
            model_volume_atendimento_particularizado.save()
            model_dados_cras.save()
            return 1
        except:
            return 0

    def recuperar_dados_cras_por_id_cras(self, id_cras: int, mes_referencia_arg: str):
        print("id cras dentro do repo")
        print(id_cras)
        print("mes referencia dentro do repo")
        print(mes_referencia_arg)
        model = DadosCrasModel.objects.filter(
            cod_cras=id_cras, mes_ref=mes_referencia_arg).first()
    
        print("Model dados cras_____________________")
        print(model)
        dados_cras_args = DadosCras.__init__.__code__.co_varnames
        modelAgs = [f.name for f in DadosCrasModel._meta.get_fields()]
        arg_values = {el: getattr(
            model, el) for el in modelAgs if el in dados_cras_args and not el == 'self'}
        print("antes do return Dados Cras___________________")
        return DadosCras(dados_Paif=model.DadosPAIF,
                         volume_atendimento_particularizado=model.vol_atend_particularizado,
                         volume_servicoes_convivencia_e_fortalecimentoVinculosDeFamiliasPAIF=model.vol_serv_convive_fortale_vinculos_fam_PAIF,
                         responsavel_cras=model.responsavel_cras,
                         nome_cras=model.nome_cras,
                         codigo_cras=model.cod_cras ,
                         mes_referencia=model.mes_ref 
                         )
