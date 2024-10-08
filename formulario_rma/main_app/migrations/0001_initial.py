# Generated by Django 4.1.1 on 2023-01-30 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtendRealizadosMesRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_atendi_indivi_mes_ref', models.IntegerField()),
                ('total_atendi_grupo_mes_ref', models.IntegerField()),
                ('fam_encaminha_cras_mes_ref', models.IntegerField()),
                ('visitas_domici_mes_ref', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CadastraPesSituaRuaMesRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pes_incluidas_cad_unico_mes_ref', models.IntegerField()),
                ('pes_reali_atuali_cad_unico_mes_ref', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CaractEspIdentiPesAtendServMesRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pes_usua_drogas', models.IntegerField()),
                ('migrantes', models.IntegerField()),
                ('pes_doenca_transt_mental', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CrianAdltesTrabInfantilPAEFImesRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=9)),
                ('de_0_a_6_anos', models.IntegerField()),
                ('de_7_a_12_anos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CrianAdltesViolIngressaPAEFImesRefC1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=9)),
                ('de_0_a_6_anos', models.IntegerField()),
                ('de_7_a_12_anos', models.IntegerField()),
                ('de_13_a_17_anos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CrianAdltesViolIngressaPAEFImesRefC2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=9)),
                ('de_0_a_6_anos', models.IntegerField()),
                ('de_7_a_12_anos', models.IntegerField()),
                ('de_13_a_17_anos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CrianAdltesViolIngressaPAEFImesRefC3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=9)),
                ('de_0_a_6_anos', models.IntegerField()),
                ('de_7_a_12_anos', models.IntegerField()),
                ('de_13_a_17_anos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CrianAdltesViolIngressaPAEFImesRefC4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=9)),
                ('de_0_a_6_anos', models.IntegerField()),
                ('de_7_a_12_anos', models.IntegerField()),
                ('de_13_a_17_anos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DadosCrasModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cras', models.CharField(max_length=100)),
                ('cod_cras', models.IntegerField()),
                ('mes_ref', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='FamiliasAcompanhadasPAIF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_casos_acompanha_PAEFI', models.IntegerField(blank=True, null=True)),
                ('novos_casos_acompanha_PAEFI_mes_ref', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IdososSituaViolPAEFImesRefD1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=9)),
                ('de_60_anos_ou_mais', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IdososSituaViolPAEFImesRefD2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=9)),
                ('de_60_anos_ou_mais', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MulheresAdultVitViolIntrafamiliarPAEFImesRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mulheres_adult_vit_viol_intrafamiliar', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NovosAdltesLAmesRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masculino', models.IntegerField()),
                ('feminino', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NovosAdltesPSCmesRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masculino', models.IntegerField()),
                ('feminino', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NovosCasosAcompanhaPAEFImesRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fam_benef_bolsa_familia', models.IntegerField()),
                ('fam_membros_benef_BPC', models.IntegerField()),
                ('fam_criancas_adltes_trab_infantil', models.IntegerField()),
                ('fam_criancas_adltes_serv_acolhi', models.IntegerField()),
                ('fam_situa_viol_substan_psicoativas', models.IntegerField()),
                ('fam_adltes_med_soceduca_meio_abert', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PesComDeficienciaViolPAEFImesRefE1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=9)),
                ('de_0_a_12_anos', models.IntegerField()),
                ('de_13_a_17_anos', models.IntegerField()),
                ('de_18_a_59_anos', models.IntegerField()),
                ('de_60_anos_ou_mais', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PesComDeficienciaViolPAEFImesRefE2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=9)),
                ('de_0_a_12_anos', models.IntegerField()),
                ('de_13_a_17_anos', models.IntegerField()),
                ('de_18_a_59_anos', models.IntegerField()),
                ('de_60_anos_ou_mais', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PesSituaRuaAtendServMesRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=9)),
                ('de_0_a_12_anos', models.IntegerField()),
                ('de_13_a_17_anos', models.IntegerField()),
                ('de_18_a_39_anos', models.IntegerField()),
                ('de_40_a_59_anos', models.IntegerField()),
                ('de_60_anos_ou_mais', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PesSituaRuaPAEFImesRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=9)),
                ('de_0_a_12_anos', models.IntegerField()),
                ('de_13_a_17_anos', models.IntegerField()),
                ('de_18_a_59_anos', models.IntegerField()),
                ('de_60_anos_ou_mais', models.IntegerField()),
                ('pes_situa_rua', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PesVitDiscrimiOrieSexualPAEFImesRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pes_discrimi_orie_sexual', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PesVitimasViolDireitosPAEFImesRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=9)),
                ('de_0_a_12_anos', models.IntegerField()),
                ('de_13_a_17_anos', models.IntegerField()),
                ('de_18_a_59_anos', models.IntegerField()),
                ('de_60_anos_ou_mais', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PesVitTrafHumanoPAEFImesRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=9)),
                ('de_0_a_12_anos', models.IntegerField()),
                ('de_13_a_17_anos', models.IntegerField()),
                ('de_18_a_59_anos', models.IntegerField()),
                ('de_60_anos_ou_mais', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='QtdNovosAdltesServMesRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masculino', models.IntegerField()),
                ('feminino', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QtdPerfilPesAbordaEquipServMesRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=9)),
                ('de_0_a_12_anos', models.IntegerField()),
                ('de_13_a_17_anos', models.IntegerField()),
                ('de_18_a_59_anos', models.IntegerField()),
                ('de_60_anos_ou_mais', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='QtdPesAbdEquipServMesRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=9)),
                ('de_0_a_12_anos', models.IntegerField()),
                ('de_13_a_17_anos', models.IntegerField()),
                ('de_18_a_59_anos', models.IntegerField()),
                ('de_60_anos_ou_mais', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ResponsavelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('matricula', models.IntegerField()),
                ('email_funcional', models.CharField(max_length=320)),
                ('cargo', models.CharField(max_length=150, null=b'I00\n')),
                ('id_unidade', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='SituaIdentiServEspAbordaSocMesRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criancas_adltes_situa_trab_infantil_ate_15_anos', models.IntegerField()),
                ('criancas_adltes_situa_explor_sexual', models.IntegerField()),
                ('criancas_adltes_usua_drogas', models.IntegerField()),
                ('pes_adultas_usua_drogas', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SituaIdentServEspcAbordaSocialMesRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criancas_adltes_trab_infatil_15_anos', models.IntegerField()),
                ('criancas_adltes_explo_sexual', models.IntegerField()),
                ('criancas_adltes_usua_drogas', models.IntegerField()),
                ('adultos_usua_drogas', models.IntegerField()),
                ('migrantes', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VolAbordagensReali',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtd_total_aborda_reali_mes_ref', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VolAbordagensRealiCras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtd_total_aborda_realizadas', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VolAdltesMedSoceduca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_adltes_med_soceduca', models.IntegerField()),
                ('qtd_adltes_liberdade_assisti', models.IntegerField()),
                ('qtd_adltes_presta_serv_comuni', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VolAtendParticularizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_atend_particularizado_mes', models.IntegerField()),
                ('fam_encami_inclusao_cad_unico_mes', models.IntegerField()),
                ('fam_encami_atuali_cad_unico_mes', models.IntegerField()),
                ('fam_encami_inclusao_atuali_cad_unico_mes', models.IntegerField()),
                ('individuos_encami_bpc', models.IntegerField()),
                ('fam_encami_para_creas', models.IntegerField()),
                ('visitas_domici_reali', models.IntegerField()),
                ('total_aux_natali_concedido', models.IntegerField()),
                ('total_aux_funeral_concedido', models.IntegerField()),
                ('outros_benef_concedidos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VolTotalAtendRealiMesRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtd_total_atend_reali_mes_ref', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VolumeServicosConvivenciaEFortalecimentoVinculosDeFamiliasPAIFModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_familias_PAIF', models.IntegerField()),
                ('familias_participando_regularmente_de_grupos_no_ambito_PAIF', models.IntegerField()),
                ('criancas_adolescentes_0_6_anos_no_servico', models.IntegerField()),
                ('criancas_adolescente_7_a_14_no_servico', models.IntegerField()),
                ('adolescenete_15_a_17_no_servico', models.IntegerField()),
                ('adultos_18_a_59_servicos', models.IntegerField()),
                ('idosos_servico', models.IntegerField()),
                ('pessoas_que_participaram_de_atividades', models.IntegerField()),
                ('pessoas_com_deficiencia_servico', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Save_dadosCrasModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Salvo', models.BooleanField()),
                ('DadosCras', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.dadoscrasmodel')),
            ],
        ),
        migrations.CreateModel(
            name='FormCreasModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A1', models.IntegerField()),
                ('A2', models.IntegerField()),
                ('B1', models.IntegerField()),
                ('B2', models.IntegerField()),
                ('B3', models.IntegerField()),
                ('B4', models.IntegerField()),
                ('B5', models.IntegerField()),
                ('B7', models.IntegerField()),
                ('B6_T', models.IntegerField()),
                ('B6_M_1', models.IntegerField()),
                ('B6_M_2', models.IntegerField()),
                ('B6_M_3', models.IntegerField()),
                ('B6_M_4', models.IntegerField()),
                ('B6_F_1', models.IntegerField()),
                ('B6_F_2', models.IntegerField()),
                ('B6_F_3', models.IntegerField()),
                ('B6_F_4', models.IntegerField()),
                ('C1_T', models.IntegerField()),
                ('C1_M_1', models.IntegerField()),
                ('C1_M_2', models.IntegerField()),
                ('C1_M_3', models.IntegerField()),
                ('C1_F_1', models.IntegerField()),
                ('C1_F_2', models.IntegerField()),
                ('C1_F_3', models.IntegerField()),
                ('C2_T', models.IntegerField()),
                ('C2_M_1', models.IntegerField()),
                ('C2_M_2', models.IntegerField()),
                ('C2_M_3', models.IntegerField()),
                ('C2_F_1', models.IntegerField()),
                ('C2_F_2', models.IntegerField()),
                ('C2_F_3', models.IntegerField()),
                ('C3_T', models.IntegerField()),
                ('C3_M_1', models.IntegerField()),
                ('C3_M_2', models.IntegerField()),
                ('C3_M_3', models.IntegerField()),
                ('C3_F_1', models.IntegerField()),
                ('C3_F_2', models.IntegerField()),
                ('C3_F_3', models.IntegerField()),
                ('C4_T', models.IntegerField()),
                ('C4_M_1', models.IntegerField()),
                ('C4_M_2', models.IntegerField()),
                ('C4_M_3', models.IntegerField()),
                ('C4_F_1', models.IntegerField()),
                ('C4_F_2', models.IntegerField()),
                ('C4_F_3', models.IntegerField()),
                ('C5_T', models.IntegerField()),
                ('C5_M_1', models.IntegerField()),
                ('C5_M_2', models.IntegerField()),
                ('C5_F_1', models.IntegerField()),
                ('C5_F_2', models.IntegerField()),
                ('D1_T', models.IntegerField()),
                ('D1_M_1', models.IntegerField()),
                ('D1_F_1', models.IntegerField()),
                ('D2_T', models.IntegerField()),
                ('D2_M_1', models.IntegerField()),
                ('D2_F_1', models.IntegerField()),
                ('E1_T', models.IntegerField()),
                ('E1_M_1', models.IntegerField()),
                ('E1_M_2', models.IntegerField()),
                ('E1_M_3', models.IntegerField()),
                ('E1_M_4', models.IntegerField()),
                ('E1_F_1', models.IntegerField()),
                ('E1_F_2', models.IntegerField()),
                ('E1_F_3', models.IntegerField()),
                ('E1_F_4', models.IntegerField()),
                ('E2_T', models.IntegerField()),
                ('E2_M_1', models.IntegerField()),
                ('E2_M_2', models.IntegerField()),
                ('E2_M_3', models.IntegerField()),
                ('E2_M_4', models.IntegerField()),
                ('E2_F_1', models.IntegerField()),
                ('E2_F_2', models.IntegerField()),
                ('E2_F_3', models.IntegerField()),
                ('E2_F_4', models.IntegerField()),
                ('F1', models.IntegerField()),
                ('G1_T', models.IntegerField()),
                ('G1_M_1', models.IntegerField()),
                ('G1_M_2', models.IntegerField()),
                ('G1_M_3', models.IntegerField()),
                ('G1_M_4', models.IntegerField()),
                ('G1_F_1', models.IntegerField()),
                ('G1_F_2', models.IntegerField()),
                ('G1_F_3', models.IntegerField()),
                ('G1_F_4', models.IntegerField()),
                ('H1', models.IntegerField()),
                ('I1_T', models.IntegerField()),
                ('I1_M_1', models.IntegerField()),
                ('I1_M_2', models.IntegerField()),
                ('I1_M_3', models.IntegerField()),
                ('I1_M_4', models.IntegerField()),
                ('I1_F_1', models.IntegerField()),
                ('I1_F_2', models.IntegerField()),
                ('I1_F_3', models.IntegerField()),
                ('I1_F_4', models.IntegerField()),
                ('M1', models.IntegerField()),
                ('M2', models.IntegerField()),
                ('M3', models.IntegerField()),
                ('M4', models.IntegerField()),
                ('J1', models.IntegerField()),
                ('J2', models.IntegerField()),
                ('J3', models.IntegerField()),
                ('J4_T', models.IntegerField()),
                ('J4_M_1', models.IntegerField()),
                ('J4_F_1', models.IntegerField()),
                ('J5_T', models.IntegerField()),
                ('J5_M_1', models.IntegerField()),
                ('J5_F_1', models.IntegerField()),
                ('J6_T', models.IntegerField()),
                ('J6_M_1', models.IntegerField()),
                ('J6_F_1', models.IntegerField()),
                ('K1_T', models.IntegerField()),
                ('K1_M_1', models.IntegerField()),
                ('K1_M_2', models.IntegerField()),
                ('K1_M_3', models.IntegerField()),
                ('K1_M_4', models.IntegerField()),
                ('K1_F_1', models.IntegerField()),
                ('K1_F_2', models.IntegerField()),
                ('K1_F_3', models.IntegerField()),
                ('K1_F_4', models.IntegerField()),
                ('K2', models.IntegerField()),
                ('K3', models.IntegerField()),
                ('K4', models.IntegerField()),
                ('K5', models.IntegerField()),
                ('K6', models.IntegerField()),
                ('L1', models.IntegerField()),
                ('nome_creas', models.CharField(max_length=100)),
                ('cod_creas', models.IntegerField()),
                ('mes_ref', models.CharField(max_length=10)),
                ('responsavel_creas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.responsavelmodel')),
            ],
        ),
        migrations.CreateModel(
            name='DadosPaifModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_fam_em_acompanha_PAIF', models.IntegerField()),
                ('total_novas_fam_PAIF', models.IntegerField()),
                ('novas_fam_em_situa_extre_pobreza', models.IntegerField()),
                ('novas_fam_bolsa_familia', models.IntegerField(default='0')),
                ('novas_familias_membros_bpc', models.IntegerField(default='0')),
                ('novas_familias_bolsa_familia_em_descomprimento', models.IntegerField()),
                ('novas_familias_criancas_adltes_trabalho', models.IntegerField()),
                ('novas_familias_criancas_adltes_acolhimento', models.IntegerField()),
                ('volume_convivencia_e_fortalecimento_de_vinculos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.volumeservicosconvivenciaefortalecimentovinculosdefamiliaspaifmodel')),
            ],
        ),
        migrations.AddField(
            model_name='dadoscrasmodel',
            name='DadosPAIF',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.dadospaifmodel'),
        ),
        migrations.AddField(
            model_name='dadoscrasmodel',
            name='responsavel_cras',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.responsavelmodel'),
        ),
        migrations.AddField(
            model_name='dadoscrasmodel',
            name='vol_atend_particularizado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.volatendparticularizado'),
        ),
        migrations.AddField(
            model_name='dadoscrasmodel',
            name='vol_serv_convive_fortale_vinculos_fam_PAIF',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.volumeservicosconvivenciaefortalecimentovinculosdefamiliaspaifmodel'),
        ),
    ]
