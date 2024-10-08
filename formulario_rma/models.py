
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AgAbrangencia(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=4000, blank=True, null=True)
    id_localidades = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_ra = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_cras = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_carga = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ag_abrangencia'


class AgAgendas(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    hora = models.CharField(max_length=5, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)
    obs = models.CharField(max_length=100, blank=True, null=True)
    id_json_agenda = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    hora_fim = models.CharField(max_length=5, blank=True, null=True)
    motivo_event = models.CharField(max_length=100, blank=True, null=True)
    data_update = models.DateField(blank=True, null=True)
    pub_ativo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ag_agendas'


class CvCapacidades(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quant_vagas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=1, blank=True, null=True)
    unidade_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    usuario_s_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cv_capacidades'


class CvDemandas(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=1, blank=True, null=True)
    usuario_s_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    unidade_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    demanda_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ref_nome = models.CharField(max_length=255, blank=True, null=True)
    ref_tel1 = models.CharField(max_length=15, blank=True, null=True)
    ref_tel2 = models.CharField(max_length=15, blank=True, null=True)
    ref_tel3 = models.CharField(max_length=15, blank=True, null=True)
    unidade_nome = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    observacoes = models.CharField(max_length=2000, blank=True, null=True)
    emergencial = models.CharField(max_length=1, blank=True, null=True)
    pontuacao = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cv_demandas'


class CvPerfis(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sexo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    faixa_etaria = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    deficiencia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    acompanhado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    capacidade_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cv_perfis'


class CvProcessos(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ud_usuario_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ud_demanda_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    unidade_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    capacidade_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_status = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cv_processos'


class CvRestricoes(models.Model):
    id_restricao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    data_fim = models.DateField(blank=True, null=True)
    motivo = models.CharField(max_length=100, blank=True, null=True)
    observacoes = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cv_restricoes'


class CvRestricoesMotivos(models.Model):
    id_motivo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    motivo = models.CharField(max_length=100, blank=True, null=True)
    ativo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cv_restricoes_motivos'


class CvStatus(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    valor = models.CharField(max_length=255, blank=True, null=True)
    usuario_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    processo_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    motivo = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cv_status'


class CvUsuariosTDemandas(models.Model):
    demanda_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    usuario_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cv_usuarios_t_demandas'


class FfTbAdicNoturno(models.Model):
    id_adic_noturno = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    matricula = models.CharField(max_length=20, blank=True, null=True)
    mes_ref = models.CharField(max_length=20, blank=True, null=True)
    dias = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ff_tb_adic_noturno'


class FfTbOcorrencia(models.Model):
    id_ocorrencia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    matricula = models.CharField(max_length=20, blank=True, null=True)
    mes_ref = models.CharField(max_length=20, blank=True, null=True)
    quant_dias = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ocorrencia = models.CharField(max_length=100, blank=True, null=True)
    observacao = models.CharField(max_length=4000, blank=True, null=True)
    usuario = models.CharField(max_length=20, blank=True, null=True)
    data_ultima_modif = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    data_inicial = models.DateField(blank=True, null=True)
    data_final = models.DateField(blank=True, null=True)
    unid_responsavel = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ff_tb_ocorrencia'


class FfTbServidores(models.Model):
    id_servidor = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_envio = models.DateField(blank=True, null=True)
    mes_ref = models.CharField(max_length=14, blank=True, null=True)
    mat = models.CharField(max_length=8, blank=True, null=True)
    nome = models.CharField(max_length=80, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    ref_salarial = models.CharField(max_length=10, blank=True, null=True)
    classe_padrao = models.CharField(max_length=10, blank=True, null=True)
    funcao = models.CharField(max_length=40, blank=True, null=True)
    cod_func = models.CharField(max_length=10, blank=True, null=True)
    ref_func = models.CharField(max_length=10, blank=True, null=True)
    lotacao = models.CharField(max_length=12, blank=True, null=True)
    desc_lot = models.CharField(max_length=80, blank=True, null=True)
    carga_horaria = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_upload = models.CharField(max_length=8, blank=True, null=True)
    data_inicio_1 = models.CharField(max_length=50, blank=True, null=True)
    data_fim_1 = models.CharField(max_length=50, blank=True, null=True)
    data_inicio_2 = models.CharField(max_length=50, blank=True, null=True)
    data_fim_2 = models.CharField(max_length=50, blank=True, null=True)
    data_inicio_3 = models.CharField(max_length=50, blank=True, null=True)
    data_fim_3 = models.CharField(max_length=50, blank=True, null=True)
    adic_not = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    afastamento = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    observacoes = models.CharField(max_length=4000, blank=True, null=True)
    lotacao_real = models.CharField(max_length=20, blank=True, null=True)
    desc_lot_real = models.CharField(max_length=80, blank=True, null=True)
    status_lotacao = models.CharField(max_length=80, blank=True, null=True)
    ultimo_status = models.CharField(max_length=80, blank=True, null=True)
    ultimo_user = models.CharField(max_length=20, blank=True, null=True)
    regularizado = models.CharField(max_length=20, blank=True, null=True)
    portaria = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ff_tb_servidores'


class FfTbUnidade(models.Model):
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    unidade = models.CharField(max_length=100, blank=True, null=True)
    quat_serv_lot = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quat_serv_pres = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    observacoes = models.CharField(max_length=4000, blank=True, null=True)
    mes_ref = models.CharField(max_length=20, blank=True, null=True)
    usuario = models.CharField(max_length=20, blank=True, null=True)
    data_ultima_modif = models.DateField(blank=True, null=True)
    quat_serv_cne = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quat_serv_nao_cne = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cod_unidade = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ff_tb_unidade'


class PstAcoesAtendimento(models.Model):
    descricao = models.CharField(max_length=500, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    referencia = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pst_acoes_atendimento'


class PstAtendimentos(models.Model):
    contador_id = models.FloatField(blank=True, null=True)
    id_usuario = models.FloatField(blank=True, null=True)
    nome_beneficiario = models.CharField(max_length=250, blank=True, null=True)
    id_beneficio = models.FloatField(blank=True, null=True)
    id_unidade = models.FloatField(blank=True, null=True)
    tipo_unidade = models.CharField(max_length=150, blank=True, null=True)
    nome_unidade = models.CharField(max_length=150, blank=True, null=True)
    nome_unidade_completo = models.CharField(max_length=301, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    nome_ra = models.CharField(max_length=150, blank=True, null=True)
    ra = models.CharField(max_length=153, blank=True, null=True)
    id_usuario_sistema = models.FloatField(blank=True, null=True)
    servidor = models.CharField(max_length=150, blank=True, null=True)
    data_solicitacao = models.DateTimeField(blank=True, null=True)
    tipo_atendimento = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pst_atendimentos'


class PstBatimentoRacaCor(models.Model):
    uf = models.TextField(blank=True, null=True)
    municÝpio = models.TextField(blank=True, null=True)
    nis = models.FloatField(blank=True, null=True)
    nome = models.TextField(blank=True, null=True)
    data_de_nascimento = models.DateTimeField(db_column='Data de Nascimento', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sexo = models.TextField(blank=True, null=True)
    perfil = models.TextField(blank=True, null=True)
    bpc = models.TextField(blank=True, null=True)
    cod_familiar_fam = models.TextField(blank=True, null=True)
    dta_atualizacao = models.DateTimeField(blank=True, null=True)
    dta_cadastramento = models.DateTimeField(blank=True, null=True)
    nom_pessoa = models.TextField(blank=True, null=True)
    cod_parentesco_rf_pessoa = models.TextField(blank=True, null=True)
    num_nis_pessoa_atual = models.FloatField(blank=True, null=True)
    num_cpf_pessoa = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pst_batimento_raca_cor'


class PstBlocoFolhaPab(models.Model):
    ref_folha = models.CharField(max_length=1024, blank=True, null=True)
    cod_familiar = models.CharField(max_length=1024, blank=True, null=True)
    cpf = models.CharField(max_length=1024, blank=True, null=True)
    nistitular = models.CharField(max_length=1024, blank=True, null=True)
    nome = models.CharField(max_length=1028, blank=True, null=True)
    renda_per_capita = models.DecimalField(max_digits=38, decimal_places=0, blank=True, null=True)
    renda_com_aux_brasil = models.CharField(max_length=1028, blank=True, null=True)
    num_nis_pessoa_atual = models.CharField(max_length=1028, blank=True, null=True)
    nom_pessoa = models.CharField(max_length=1028, blank=True, null=True)
    cod_familiar_fam = models.DecimalField(max_digits=38, decimal_places=0, blank=True, null=True)
    dat_atual_fam = models.CharField(max_length=26, blank=True, null=True)
    vlr_renda_media_fam = models.DecimalField(max_digits=38, decimal_places=0, blank=True, null=True)
    num_cpf_pessoa = models.DecimalField(max_digits=38, decimal_places=0, blank=True, null=True)
    vlrtotal = models.DecimalField(max_digits=38, decimal_places=0, blank=True, null=True)
    sitfam = models.CharField(max_length=1028, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pst_bloco_folha_pab'


class PstCadunicoFamilia(models.Model):
    cod_familia = models.BigIntegerField(blank=True, null=True)
    data_cadastro_familia = models.CharField(max_length=10, blank=True, null=True)
    data_atulizacao_familia = models.CharField(max_length=10, blank=True, null=True)
    situacao_cadastro = models.CharField(max_length=18, blank=True, null=True)
    condicao_cadastro_familia = models.CharField(max_length=13, blank=True, null=True)
    renda_percapita_familia = models.BigIntegerField(blank=True, null=True)
    localidade = models.CharField(max_length=1028, blank=True, null=True)
    tipo_logradouro = models.CharField(max_length=1028, blank=True, null=True)
    titulo_logradouro = models.CharField(max_length=1028, blank=True, null=True)
    logradouro = models.CharField(max_length=1028, blank=True, null=True)
    numero = models.BigIntegerField(blank=True, null=True)
    complemento = models.CharField(max_length=1028, blank=True, null=True)
    complemento_adicional = models.CharField(max_length=1028, blank=True, null=True)
    cep = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pst_cadunico_familia'


class PstCadunicoPessoa(models.Model):
    codigo_familiar = models.CharField(max_length=1028, blank=True, null=True)
    numero_membro = models.CharField(max_length=1028, blank=True, null=True)
    data_cadastro = models.DateField(blank=True, null=True)
    data_atualizaþÒo = models.DateField(db_column='data_atualizaÃ├o', blank=True, null=True)  # Field name made lowercase.
    cod_est_cadastral_memb = models.BigIntegerField(blank=True, null=True)
    situacao_cadastro = models.CharField(max_length=18, blank=True, null=True)
    nome_pessoa = models.CharField(max_length=1028, blank=True, null=True)
    cpf = models.CharField(max_length=1028, blank=True, null=True)
    nis_pessoa = models.BigIntegerField(blank=True, null=True)
    sexo = models.CharField(max_length=9, blank=True, null=True)
    data_nascimento = models.CharField(max_length=10, blank=True, null=True)
    prentesco_rf = models.CharField(max_length=45, blank=True, null=True)
    cod_bpc = models.BigIntegerField(blank=True, null=True)
    bpc = models.CharField(max_length=31, blank=True, null=True)
    descricao_raca_cor_pessoa = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pst_cadunico_pessoa'


class PstCartaoGas(models.Model):
    referencia = models.CharField(max_length=38, blank=True, null=True)
    cod_familiar_novo = models.CharField(max_length=38, blank=True, null=True)
    rf_novo = models.CharField(max_length=1028, blank=True, null=True)
    dta_nasc_rf_novo = models.CharField(max_length=38, blank=True, null=True)
    nis_rf_novo = models.CharField(max_length=38, blank=True, null=True)
    cpf_rf_novo = models.CharField(max_length=38, blank=True, null=True)
    vlr_gas = models.CharField(max_length=260, blank=True, null=True)
    mes_referencia = models.CharField(max_length=260, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pst_cartao_gas'


class PstCefDfPratoCheio(models.Model):
    id = models.FloatField(blank=True, null=True)
    cpf = models.FloatField(blank=True, null=True)
    tx_des = models.TextField(blank=True, null=True)
    nome = models.TextField(blank=True, null=True)
    cpf_cnpj = models.TextField(blank=True, null=True)
    razao_social = models.TextField(blank=True, null=True)
    nome_fantasia = models.TextField(blank=True, null=True)
    ds_tip_con = models.TextField(blank=True, null=True)
    cep = models.TextField(blank=True, null=True)
    ds_cnae_icms = models.TextField(blank=True, null=True)
    ds_cnae_iss = models.TextField(blank=True, null=True)
    ds_sit = models.TextField(blank=True, null=True)
    qtd_cpfs_distintos = models.FloatField(blank=True, null=True)
    qtd_ocorrencias = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pst_cef_df_prato_cheio'


class PstDfSocial(models.Model):
    referencia = models.DecimalField(max_digits=38, decimal_places=0, blank=True, null=True)
    nome = models.CharField(max_length=1028, blank=True, null=True)
    cpf = models.CharField(max_length=38, blank=True, null=True)
    dt_nasc = models.CharField(max_length=26, blank=True, null=True)
    cod_familiar_fam = models.CharField(max_length=38, blank=True, null=True)
    rf_novo = models.CharField(max_length=1028, blank=True, null=True)
    cpf_rf_novo = models.CharField(max_length=38, blank=True, null=True)
    nis_rf_novo = models.CharField(max_length=38, blank=True, null=True)
    pab_df_social = models.CharField(max_length=1028, blank=True, null=True)
    vlr_dfs = models.CharField(max_length=38, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pst_df_social'


class PstFalecidosPcdf(models.Model):
    id_sedes = models.BigIntegerField(blank=True, null=True)
    nome_sedes = models.CharField(max_length=500, blank=True, null=True)
    mae_sedes = models.CharField(max_length=500, blank=True, null=True)
    dt_nascimento_sedes = models.DateField(blank=True, null=True)
    nome_iml = models.CharField(max_length=500, blank=True, null=True)
    mae_iml = models.CharField(max_length=500, blank=True, null=True)
    dt_nascimento_iml = models.DateField(blank=True, null=True)
    dt_cadastro_sedes = models.DateField(blank=True, null=True)
    dt_obito = models.DateField(blank=True, null=True)
    dt_carga = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pst_falecidos_pcdf'


class PstIdentCivilCpfDiferentePcdf(models.Model):
    id_sedes = models.BigIntegerField(blank=True, null=True)
    nome_sedes = models.CharField(max_length=500, blank=True, null=True)
    mae_sedes = models.CharField(max_length=500, blank=True, null=True)
    dt_nascimento_sedes = models.DateField(blank=True, null=True)
    cpf_sedes = models.CharField(max_length=20, blank=True, null=True)
    cid_str_ds_nome = models.CharField(max_length=500, blank=True, null=True)
    cid_str_nm_mae = models.CharField(max_length=500, blank=True, null=True)
    cid_dat_dt_nascimento = models.DateField(blank=True, null=True)
    cid_int_nr_cpf = models.CharField(max_length=20, blank=True, null=True)
    dt_cadastro_sedes = models.DateField(blank=True, null=True)
    dt_carga = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pst_ident_civil_cpf_diferente_pcdf'


class PstIdentCivilCpfPcdf(models.Model):
    id_sedes = models.BigIntegerField(blank=True, null=True)
    nome_sedes = models.CharField(max_length=500, blank=True, null=True)
    mae_sedes = models.CharField(max_length=500, blank=True, null=True)
    dt_nascimento_sedes = models.DateField(blank=True, null=True)
    cpf_sedes = models.CharField(max_length=20, blank=True, null=True)
    cid_str_ds_nome = models.CharField(max_length=500, blank=True, null=True)
    cid_str_nm_mae = models.CharField(max_length=500, blank=True, null=True)
    cid_dat_dt_nascimento = models.DateField(blank=True, null=True)
    cid_int_nr_cpf = models.CharField(max_length=20, blank=True, null=True)
    dt_cadastro_sedes = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pst_ident_civil_cpf_pcdf'


class PstIptuPratoCheioCgdf(models.Model):
    id = models.FloatField(blank=True, null=True)
    nome = models.TextField(blank=True, null=True)
    cpf_iptu = models.TextField(blank=True, null=True)
    nome_propietario_imovel = models.TextField(blank=True, null=True)
    nr_imovel = models.TextField(blank=True, null=True)
    cep_imovel = models.TextField(blank=True, null=True)
    bairro_imovel = models.TextField(blank=True, null=True)
    numero_imovel = models.TextField(blank=True, null=True)
    pr_participacao = models.FloatField(blank=True, null=True)
    contagem_linhas_iptu = models.FloatField(blank=True, null=True)
    contagem_linhas_prato_cheio = models.FloatField(blank=True, null=True)
    quantidade_cpfs_distintos = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pst_iptu_prato_cheio_cgdf'


class PstIpvaPratoCheioCgdf(models.Model):
    id = models.FloatField(blank=True, null=True)
    nome = models.TextField(blank=True, null=True)
    nome_proprietario = models.TextField(blank=True, null=True)
    ano_fabricacao = models.TextField(blank=True, null=True)
    ds_modelo = models.TextField(blank=True, null=True)
    data_aquisicao = models.TextField(blank=True, null=True)
    ds_situacao = models.TextField(blank=True, null=True)
    restricao_ds = models.TextField(blank=True, null=True)
    sit_venda_des = models.TextField(blank=True, null=True)
    contagem_linhas = models.FloatField(blank=True, null=True)
    quantidade_cpf_distintos = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pst_ipva_prato_cheio_cgdf'


class PstRetornoCgdf(models.Model):
    id_retorno = models.IntegerField(blank=True, null=True)
    nome_beneficiario = models.CharField(max_length=-1, blank=True, null=True)
    nis_beneficiario = models.CharField(max_length=-1, blank=True, null=True)
    cpf_beneficiario = models.CharField(max_length=-1, blank=True, null=True)
    ano_mes_referencia_beneficio = models.CharField(max_length=-1, blank=True, null=True)
    beneficio = models.CharField(max_length=-1, blank=True, null=True)
    ocorrencia = models.CharField(max_length=-1, blank=True, null=True)
    observaþÒo = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pst_retorno_cgdf'


class PstServidoresPratoCheio(models.Model):
    id = models.FloatField(blank=True, null=True)
    numero_cpf = models.TextField(blank=True, null=True)
    nome = models.TextField(blank=True, null=True)
    nome_01 = models.TextField(blank=True, null=True)
    matricula = models.TextField(blank=True, null=True)
    dc_grupo_sit_func = models.TextField(blank=True, null=True)
    descricao_cargo = models.TextField(blank=True, null=True)
    admissao = models.TextField(blank=True, null=True)
    descricao_empresa = models.TextField(blank=True, null=True)
    descricao_funcao = models.TextField(blank=True, null=True)
    contagem_linhas_personalizadas = models.FloatField(blank=True, null=True)
    contagem_linhas_prato_cheio = models.FloatField(blank=True, null=True)
    vl_remuneracao_basica = models.FloatField(blank=True, null=True)
    vl_beneficios = models.FloatField(blank=True, null=True)
    vl_funcoes = models.FloatField(blank=True, null=True)
    vl_liquido = models.FloatField(blank=True, null=True)
    vl_seg_social = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pst_servidores_prato_cheio'


class PstTotaisAtendimento(models.Model):
    ano = models.IntegerField(blank=True, null=True)
    descricao_atendimento = models.CharField(max_length=500, blank=True, null=True)
    janeiro = models.IntegerField(blank=True, null=True)
    fevereiro = models.IntegerField(blank=True, null=True)
    marco = models.IntegerField(blank=True, null=True)
    abril = models.IntegerField(blank=True, null=True)
    maio = models.IntegerField(blank=True, null=True)
    junho = models.IntegerField(blank=True, null=True)
    julho = models.IntegerField(blank=True, null=True)
    agosto = models.IntegerField(blank=True, null=True)
    setembro = models.IntegerField(blank=True, null=True)
    outubro = models.IntegerField(blank=True, null=True)
    novembro = models.IntegerField(blank=True, null=True)
    dezembro = models.IntegerField(blank=True, null=True)
    percentual = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pst_totais_atendimento'


class TbAcoesAtendimento(models.Model):
    id_acao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    acao = models.CharField(max_length=500, blank=True, null=True)
    ativo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_acoes_atendimento'


class TbAcoesAtendimentoPerfil(models.Model):
    id_acao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_perfil = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_acoes_atendimento_perfil'


class TbAcompanhante(models.Model):
    id_acompanhante = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_passagem = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    grau_parentesco = models.CharField(max_length=50, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    idade = models.CharField(max_length=20, blank=True, null=True)
    rg = models.CharField(max_length=30, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    cert_nasc = models.CharField(max_length=40, blank=True, null=True)
    emissor = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_acompanhante'


class TbAgendaUnidades(models.Model):
    id_agenda = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema_geracao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema_156 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    hora = models.CharField(max_length=10, blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    id_demanda = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_status = models.DateField(blank=True, null=True)
    hora_status = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=40, blank=True, null=True)
    atendimento = models.CharField(max_length=30, blank=True, null=True)
    observacoes = models.CharField(max_length=1000, blank=True, null=True)
    data_geracao = models.DateField(blank=True, null=True)
    liberacao_gerente = models.CharField(max_length=1, blank=True, null=True)
    data_liberacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agenda_unidades'


class TbAgendaUnidadesAbrangencia(models.Model):
    id_abrangencia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_super_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agenda_unidades_abrangencia'


class TbAgendaUnidadesAtividades(models.Model):
    id_atividade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    atividade = models.CharField(max_length=200, blank=True, null=True)
    ativo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agenda_unidades_atividades'


class TbAgendaUnidadesAtivo156(models.Model):
    id_agenda = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_demanda = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_status = models.DateField(blank=True, null=True)
    hora_status = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    qtde_ligacoes = models.CharField(max_length=20, blank=True, null=True)
    modalidade = models.CharField(max_length=99, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agenda_unidades_ativo_156'


class TbAgendaUnidadesContadorPrioritarios(models.Model):
    qtd_prioritarios = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agenda_unidades_contador_prioritarios'


class TbAgendaUnidadesDemandas(models.Model):
    id_demanda = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    hora = models.CharField(max_length=10, blank=True, null=True)
    tipo_agenda = models.CharField(max_length=100, blank=True, null=True)
    agenda_origem = models.CharField(max_length=10, blank=True, null=True)
    qtd_ligacoes = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_status = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pontuacao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    atendimento_imediato = models.CharField(max_length=10, blank=True, null=True)
    hora_status = models.CharField(max_length=10, blank=True, null=True)
    buscando_cras_para = models.CharField(max_length=200, blank=True, null=True)
    situacao_violencia = models.CharField(max_length=500, blank=True, null=True)
    atendimento = models.CharField(max_length=20, blank=True, null=True)
    preferencial_especialista = models.CharField(max_length=20, blank=True, null=True)
    orgao_demandante = models.CharField(max_length=200, blank=True, null=True)
    processo_sei = models.CharField(max_length=100, blank=True, null=True)
    eixo_atuacao_demandante = models.CharField(max_length=200, blank=True, null=True)
    documento_demanda = models.CharField(max_length=100, blank=True, null=True)
    data_documento_demanda = models.DateField(blank=True, null=True)
    documento_reitero = models.CharField(max_length=100, blank=True, null=True)
    data_reiteracao = models.DateField(blank=True, null=True)
    itens_cadunico = models.CharField(max_length=250, blank=True, null=True)
    observacoes = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agenda_unidades_demandas'


class TbAgendaUnidadesDemandasOrdem(models.Model):
    ordem = models.CharField(max_length=20, blank=True, null=True)
    data_ini = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agenda_unidades_demandas_ordem'


class TbAgendaUnidadesDemandasPontuacao(models.Model):
    id_demanda = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_pontuacao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agenda_unidades_demandas_pontuacao'


class TbAgendaUnidadesPontuacao(models.Model):
    id_pontuacao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    item = models.CharField(max_length=200, blank=True, null=True)
    pontuacao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ativo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    origem = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agenda_unidades_pontuacao'


class TbAgendaUnidadesQtdAtendPrioritarios(models.Model):
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qtd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agenda_unidades_qtd_atend_prioritarios'


class TbAtendimentoManuBenef(models.Model):
    id_atendimento = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    sol_manuten_beneficio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    usuarios_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mens = models.TextField(blank=True, null=True)
    ativo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_atendimento_manu_benef'


class TbAtendimentos(models.Model):
    contador_id = models.FloatField(blank=True, null=True)
    id_usuario = models.FloatField(blank=True, null=True)
    nome_beneficiario = models.CharField(max_length=250, blank=True, null=True)
    id_beneficio = models.FloatField(blank=True, null=True)
    id_unidade = models.FloatField(blank=True, null=True)
    tipo_unidade = models.CharField(max_length=150, blank=True, null=True)
    nome_unidade = models.CharField(max_length=150, blank=True, null=True)
    nome_unidade_completo = models.CharField(max_length=301, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    nome_ra = models.CharField(max_length=150, blank=True, null=True)
    ra = models.CharField(max_length=153, blank=True, null=True)
    id_usuario_sistema = models.FloatField(blank=True, null=True)
    servidor = models.CharField(max_length=150, blank=True, null=True)
    data_solicitacao = models.DateTimeField(blank=True, null=True)
    tipo_atendimento = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_atendimentos'


class TbAvSocioeconomica(models.Model):
    id_avaliacao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    parecer = models.CharField(max_length=2000, blank=True, null=True)
    docs_requeridos = models.CharField(max_length=10, blank=True, null=True)
    pecunia = models.CharField(max_length=50, blank=True, null=True)
    inscrita_programas = models.CharField(max_length=10, blank=True, null=True)
    kit_entregue = models.CharField(max_length=3, blank=True, null=True)
    docs_apresentados = models.CharField(max_length=200, blank=True, null=True)
    data_avaliacao = models.CharField(max_length=100, blank=True, null=True)
    cancelado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_natalidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_assinatura = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_av_socioeconomica'


class TbAvaliacaoSocioassistencialIdoso(models.Model):
    id_avaliacao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    religiao = models.CharField(max_length=20, blank=True, null=True)
    processos_sei_relacionados = models.CharField(max_length=200, blank=True, null=True)
    possui_divida_comprometa_renda = models.CharField(max_length=20, blank=True, null=True)
    violencia_patrimonial = models.CharField(max_length=20, blank=True, null=True)
    familia_recebeu_beneficios_ultimo_ano = models.CharField(max_length=20, blank=True, null=True)
    familia_recebeu_beneficios_ultimo_ano_quais = models.CharField(max_length=200, blank=True, null=True)
    situacao_de_rua = models.CharField(max_length=20, blank=True, null=True)
    processo_perda_moradia_desabrigo_imediato = models.CharField(max_length=20, blank=True, null=True)
    hospitalizado_apos_alta = models.CharField(max_length=20, blank=True, null=True)
    decisao_judiacial_acolhimento = models.CharField(max_length=20, blank=True, null=True)
    acolhido_servico_inadequado = models.CharField(max_length=20, blank=True, null=True)
    apresenta_se_lucida = models.CharField(max_length=20, blank=True, null=True)
    doenca_diagnosticada = models.CharField(max_length=20, blank=True, null=True)
    doenca_diagnosticada_qual = models.CharField(max_length=200, blank=True, null=True)
    uso_sonda = models.CharField(max_length=20, blank=True, null=True)
    uso_sonda_qual = models.CharField(max_length=20, blank=True, null=True)
    dispositivo_ostomia = models.CharField(max_length=20, blank=True, null=True)
    dispositivo_ostomia_qual = models.CharField(max_length=20, blank=True, null=True)
    outras_informacoes_saude = models.TextField(blank=True, null=True)
    inseguranca_alimentar = models.CharField(max_length=20, blank=True, null=True)
    inseguranca_alimentar_motivo = models.CharField(max_length=500, blank=True, null=True)
    inseguranca_superada_acolhimento = models.CharField(max_length=20, blank=True, null=True)
    demandas_apresentadas_relato = models.TextField(blank=True, null=True)
    seguranca_autonomia_relato = models.TextField(blank=True, null=True)
    interditada_judicialmente = models.CharField(max_length=20, blank=True, null=True)
    curador = models.CharField(max_length=100, blank=True, null=True)
    seguranca_convivio_relato = models.TextField(blank=True, null=True)
    cuidadores = models.CharField(max_length=200, blank=True, null=True)
    avaliacao_inicial = models.TextField(blank=True, null=True)
    plano_intervencao_inicial_descricao = models.TextField(blank=True, null=True)
    encaminhamento_acolhimento = models.CharField(max_length=20, blank=True, null=True)
    ciencia_possibilidade_encaminhamento_acolhimento = models.CharField(max_length=20, blank=True, null=True)
    concorda_encaminhamento_acolhimento = models.CharField(max_length=20, blank=True, null=True)
    informadas_regras_acolhimento = models.CharField(max_length=20, blank=True, null=True)
    alguem_precisa_acolhido_junto = models.CharField(max_length=20, blank=True, null=True)
    alguem_precisa_acolhido_junto_quem = models.CharField(max_length=200, blank=True, null=True)
    consideracoes_finais = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_avaliacao_socioassistencial_idoso'


class TbBairro(models.Model):
    id_bairro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=72, blank=True, null=True)
    id_uf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_localidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_ra = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_bairro'


class TbBeneficioCalamidade(models.Model):
    id_calamidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_requerente = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    renda_percapta = models.CharField(max_length=20, blank=True, null=True)
    modalidade = models.CharField(max_length=50, blank=True, null=True)
    observacao = models.CharField(max_length=4000, blank=True, null=True)
    data_solicitacao = models.DateField(blank=True, null=True)
    itens_lei = models.CharField(max_length=4000, blank=True, null=True)
    caracteristica_cal = models.CharField(max_length=200, blank=True, null=True)
    avaliacao_tecnica = models.CharField(max_length=4000, blank=True, null=True)
    valor_beneficio = models.CharField(max_length=20, blank=True, null=True)
    data_avaliacao = models.DateField(blank=True, null=True)
    ass_especialista = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ass_coordenador = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    parecer_tecnico = models.CharField(max_length=4000, blank=True, null=True)
    parecer_seas_url = models.CharField(max_length=200, blank=True, null=True)
    data_liberacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_beneficio_calamidade'


class TbBeneficioCarteiraIdoso(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_dados_cad_unico = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    usuarios_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_solicitacao = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_beneficio_carteira_idoso'


class TbBeneficioExcepcional(models.Model):
    id_excepcional = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_requerente = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    renda_percapta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    observacao = models.CharField(max_length=4000, blank=True, null=True)
    data_solicitacao = models.DateField(blank=True, null=True)
    valor_beneficio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_familia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    data_avaliacao = models.DateField(blank=True, null=True)
    id_especialista = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    itens_lei = models.CharField(max_length=2000, blank=True, null=True)
    habilitado_df = models.CharField(max_length=3, blank=True, null=True)
    habilitado_desde = models.DateField(blank=True, null=True)
    numero_codhab = models.CharField(max_length=30, blank=True, null=True)
    envio_relatorio = models.CharField(max_length=3, blank=True, null=True)
    parecer_tecnico = models.CharField(max_length=20, blank=True, null=True)
    avaliacao_tecnica = models.CharField(max_length=4000, blank=True, null=True)
    relatorio_url = models.CharField(max_length=500, blank=True, null=True)
    parecer_seas_url = models.CharField(max_length=200, blank=True, null=True)
    ass_coordenador = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_beneficio_excepcional'


class TbBeneficioNatalidade(models.Model):
    id_natalidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_responsavel = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_procurador = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_crianca = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_nasc_morto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    renda_percapta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bens_consumo = models.CharField(max_length=3, blank=True, null=True)
    pecunia = models.CharField(max_length=3, blank=True, null=True)
    certidao_nascimento = models.CharField(max_length=100, blank=True, null=True)
    declaracao_vivo = models.CharField(max_length=100, blank=True, null=True)
    grau_parent_procurador = models.CharField(max_length=200, blank=True, null=True)
    docs_apresentados = models.CharField(max_length=10, blank=True, null=True)
    elegivel_kit = models.CharField(max_length=10, blank=True, null=True)
    kit_entregue = models.CharField(max_length=10, blank=True, null=True)
    favoravel = models.CharField(max_length=10, blank=True, null=True)
    data_solicitacao = models.DateField(blank=True, null=True)
    ass_coordenador = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    observacao = models.CharField(max_length=4000, blank=True, null=True)
    cancelado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_maternidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status_bensdeconsumo = models.CharField(max_length=30, blank=True, null=True)
    status_pecunia = models.CharField(max_length=30, blank=True, null=True)
    banco_rejeicao_motivo = models.CharField(max_length=100, blank=True, null=True)
    banco_rejeicao_observacao = models.CharField(max_length=500, blank=True, null=True)
    id_status_servidor_bl = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status_unidade_bl = models.CharField(max_length=90, blank=True, null=True)
    data_status_bl = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_beneficio_natalidade'


class TbBeneficioPorMorte(models.Model):
    id_por_morte = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_falecido = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_req_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_req_procurador = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vinculo = models.CharField(max_length=200, blank=True, null=True)
    renda_percapta = models.CharField(max_length=200, blank=True, null=True)
    data_falecimento = models.DateField(blank=True, null=True)
    hora_falecimento = models.CharField(max_length=6, blank=True, null=True)
    idade_aproximada = models.CharField(max_length=20, blank=True, null=True)
    altura = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    peso = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    natimorto = models.CharField(max_length=3, blank=True, null=True)
    moradia = models.CharField(max_length=200, blank=True, null=True)
    acolhido = models.CharField(max_length=3, blank=True, null=True)
    qual_unidade = models.CharField(max_length=150, blank=True, null=True)
    posic_cadeia_produtiva = models.CharField(max_length=150, blank=True, null=True)
    certidao_obito = models.CharField(max_length=150, blank=True, null=True)
    guia_sepultamento = models.CharField(max_length=150, blank=True, null=True)
    cartorio_expedicao = models.CharField(max_length=200, blank=True, null=True)
    prog_transf_renda = models.CharField(max_length=200, blank=True, null=True)
    qual_prog = models.CharField(max_length=200, blank=True, null=True)
    modalidade = models.CharField(max_length=150, blank=True, null=True)
    valor_ressarcimento = models.CharField(max_length=20, blank=True, null=True)
    preenche_criterios = models.CharField(max_length=3, blank=True, null=True)
    data_solicitacao = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    ass_coordenador = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    causa_morte = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_beneficio_por_morte'


class TbBeneficioVulnerabilidade(models.Model):
    id_vulnerabilidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_requerente = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    renda_percapta = models.CharField(max_length=20, blank=True, null=True)
    modalidade = models.CharField(max_length=50, blank=True, null=True)
    observacao = models.CharField(max_length=4000, blank=True, null=True)
    data_solicitacao = models.DateField(blank=True, null=True)
    itens_lei = models.CharField(max_length=4000, blank=True, null=True)
    caracteristica_vul = models.CharField(max_length=200, blank=True, null=True)
    avaliacao_tecnica = models.CharField(max_length=4000, blank=True, null=True)
    valor_beneficio = models.CharField(max_length=20, blank=True, null=True)
    data_avaliacao = models.DateField(blank=True, null=True)
    ass_especialista = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ass_coordenador = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    id_passagem = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    parecer_tecnico = models.CharField(max_length=20, blank=True, null=True)
    parecer_seas_url = models.CharField(max_length=200, blank=True, null=True)
    id_unidade_old = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_beneficio_vulnerabilidade'


class TbBeneficiosComposicao(models.Model):
    tipo_beneficio = models.CharField(max_length=50, blank=True, null=True)
    id_beneficio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_familia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    renda_usuario = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_beneficios_composicao'


class TbCadUnico(models.Model):
    nome_pessoa = models.CharField(max_length=1028, blank=True, null=True)
    nome_mae = models.CharField(max_length=1028, blank=True, null=True)
    data_nascimento = models.CharField(max_length=1028, blank=True, null=True)
    nis_pessoa = models.BigIntegerField(blank=True, null=True)
    cpf_pessoa = models.CharField(max_length=1028, blank=True, null=True)
    rg_pessoa = models.CharField(max_length=1028, blank=True, null=True)
    endereco = models.CharField(max_length=3086, blank=True, null=True)
    cidade = models.CharField(max_length=1028, blank=True, null=True)
    renda_familiar = models.BigIntegerField(blank=True, null=True)
    num_reg = models.FloatField(blank=True, null=True)
    num_reg_arquivo = models.SmallIntegerField(blank=True, null=True)
    nom_arquivo_hdr = models.CharField(max_length=30, blank=True, null=True)
    cod_versao_layout_hdr = models.CharField(max_length=70, blank=True, null=True)
    dta_posicao_cadastro_hdr = models.DateField(blank=True, null=True)
    dta_extracao_dados_hdr = models.DateField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_cad_unico'


class TbCaixaPostal(models.Model):
    id_caixa_postal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=72, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    id_localidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_caixa_postal'


class TbCarroceiroComposicao(models.Model):
    id_composicao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_carroceiro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_cadastro = models.DateField(blank=True, null=True)
    condicao_membro = models.CharField(max_length=50, blank=True, null=True)
    idade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sabe_ler_escrever = models.CharField(max_length=20, blank=True, null=True)
    frequentando_creche_escola = models.CharField(max_length=30, blank=True, null=True)
    nivel_ensino = models.CharField(max_length=100, blank=True, null=True)
    concluiu = models.CharField(max_length=20, blank=True, null=True)
    trabalha = models.CharField(max_length=20, blank=True, null=True)
    tipo_trabalho = models.CharField(max_length=50, blank=True, null=True)
    quanto_ganha = models.CharField(max_length=20, blank=True, null=True)
    exercia_que_trabalho = models.CharField(max_length=50, blank=True, null=True)
    beneficiario_programa_social = models.CharField(max_length=200, blank=True, null=True)
    possui_deficiencia = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_carroceiro_composicao'


class TbCarroceiros(models.Model):
    id_carroceiro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_cadastro = models.DateField(blank=True, null=True)
    escolaridade_curso = models.CharField(max_length=200, blank=True, null=True)
    qtd_pessoas_casa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qtd_moradores_trabalham = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    idade_inicio_carroceiro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    trabalhou_outra_atividade = models.CharField(max_length=100, blank=True, null=True)
    trabalhou_carteira_assinada = models.CharField(max_length=10, blank=True, null=True)
    ano_inicio_carteira = models.CharField(max_length=10, blank=True, null=True)
    ano_fim_carteira = models.CharField(max_length=10, blank=True, null=True)
    atividade_carteira = models.CharField(max_length=100, blank=True, null=True)
    outras_ativid_alem_carroc = models.CharField(max_length=100, blank=True, null=True)
    qtd_dias_semana_carroceiro = models.CharField(max_length=10, blank=True, null=True)
    qtd_horas_dia_carroceiro = models.CharField(max_length=20, blank=True, null=True)
    tipo_carga = models.CharField(max_length=500, blank=True, null=True)
    equipamentos_protecao = models.CharField(max_length=200, blank=True, null=True)
    avaliacao_local_papaentulho = models.CharField(max_length=40, blank=True, null=True)
    qtd_carrocas = models.CharField(max_length=20, blank=True, null=True)
    qtd_animais = models.CharField(max_length=20, blank=True, null=True)
    local_cavalos = models.CharField(max_length=40, blank=True, null=True)
    renda_medi_diaria_carroceiro = models.CharField(max_length=20, blank=True, null=True)
    renda_mensal = models.CharField(max_length=20, blank=True, null=True)
    valor_mensal_gasto_animal = models.CharField(max_length=20, blank=True, null=True)
    beneficio_social = models.CharField(max_length=500, blank=True, null=True)
    usuario_familiar_cadunico = models.CharField(max_length=10, blank=True, null=True)
    associacao_carroceiros = models.CharField(max_length=200, blank=True, null=True)
    gost_associar_outros_carroc = models.CharField(max_length=20, blank=True, null=True)
    gost_trab_outro_veiculo = models.CharField(max_length=20, blank=True, null=True)
    curso_profissionalizante = models.CharField(max_length=200, blank=True, null=True)
    interesse_retomar_estudos = models.CharField(max_length=20, blank=True, null=True)
    interesse_habilitacao = models.CharField(max_length=50, blank=True, null=True)
    interesse_curso_prof = models.CharField(max_length=200, blank=True, null=True)
    tipo_animal = models.CharField(max_length=500, blank=True, null=True)
    idade_animal = models.CharField(max_length=500, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_carroceiros'


class TbCestaEmergencial(models.Model):
    id_cesta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_requerente = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_requerimento = models.DateField(blank=True, null=True)
    tipo_cesta = models.CharField(max_length=50, blank=True, null=True)
    publico = models.CharField(max_length=200, blank=True, null=True)
    nome_recebimento1 = models.CharField(max_length=200, blank=True, null=True)
    nome_recebimento2 = models.CharField(max_length=200, blank=True, null=True)
    nome_recebimento3 = models.CharField(max_length=200, blank=True, null=True)
    requeisicao_outro_orgao = models.CharField(max_length=30, blank=True, null=True)
    processo = models.CharField(max_length=50, blank=True, null=True)
    meses_processo = models.CharField(max_length=20, blank=True, null=True)
    num_requisicao = models.CharField(max_length=20, blank=True, null=True)
    meses_requisicao = models.CharField(max_length=20, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    parecer = models.CharField(max_length=20, blank=True, null=True)
    relatorio = models.TextField(blank=True, null=True)
    bpc = models.CharField(max_length=20, blank=True, null=True)
    renda_percapta = models.CharField(max_length=20, blank=True, null=True)
    data_visita = models.CharField(max_length=20, blank=True, null=True)
    motivo = models.CharField(max_length=500, blank=True, null=True)
    data_entrega_cesta = models.CharField(max_length=20, blank=True, null=True)
    id_usuario_sistema_parecer = models.CharField(max_length=20, blank=True, null=True)
    id_gerente = models.CharField(max_length=20, blank=True, null=True)
    data_status_solicitada = models.DateField(blank=True, null=True)
    data_status = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    data_parecer = models.DateField(blank=True, null=True)
    data_liberacao_gerente = models.DateField(blank=True, null=True)
    motivo_cancelamento = models.CharField(max_length=500, blank=True, null=True)
    caso_excepcional = models.CharField(max_length=20, blank=True, null=True)
    indicacao_excepcionalidade = models.CharField(max_length=200, blank=True, null=True)
    id_familia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_cesta_emergencial'


class TbCestaEmergencialBkp(models.Model):
    id_cesta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_requerente = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_requerimento = models.DateField(blank=True, null=True)
    tipo_cesta = models.CharField(max_length=50, blank=True, null=True)
    publico = models.CharField(max_length=200, blank=True, null=True)
    nome_recebimento1 = models.CharField(max_length=200, blank=True, null=True)
    nome_recebimento2 = models.CharField(max_length=200, blank=True, null=True)
    nome_recebimento3 = models.CharField(max_length=200, blank=True, null=True)
    requeisicao_outro_orgao = models.CharField(max_length=30, blank=True, null=True)
    processo = models.CharField(max_length=50, blank=True, null=True)
    meses_processo = models.CharField(max_length=20, blank=True, null=True)
    num_requisicao = models.CharField(max_length=20, blank=True, null=True)
    meses_requisicao = models.CharField(max_length=20, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    parecer = models.CharField(max_length=20, blank=True, null=True)
    relatorio = models.TextField(blank=True, null=True)
    bpc = models.CharField(max_length=20, blank=True, null=True)
    renda_percapta = models.CharField(max_length=20, blank=True, null=True)
    data_visita = models.CharField(max_length=20, blank=True, null=True)
    motivo = models.CharField(max_length=500, blank=True, null=True)
    data_entrega_cesta = models.CharField(max_length=20, blank=True, null=True)
    id_usuario_sistema_parecer = models.CharField(max_length=20, blank=True, null=True)
    id_gerente = models.CharField(max_length=20, blank=True, null=True)
    data_status_solicitada = models.DateField(blank=True, null=True)
    data_status = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    data_parecer = models.DateField(blank=True, null=True)
    data_liberacao_gerente = models.DateField(blank=True, null=True)
    motivo_cancelamento = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_cesta_emergencial_bkp'


class TbCestaEmergencialPosExtracao(models.Model):
    id_cesta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=100, blank=True, null=True)
    criterios = models.CharField(max_length=300, blank=True, null=True)
    posicao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_cesta_emergencial_pos_extracao'


class TbCestaRequerimento1(models.Model):
    id_requerimento = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rg = models.CharField(max_length=30, blank=True, null=True)
    expedidor = models.CharField(max_length=30, blank=True, null=True)
    uf = models.CharField(max_length=20, blank=True, null=True)
    nome_recebimento_cesta1 = models.CharField(max_length=200, blank=True, null=True)
    nome_recebimento_cesta2 = models.CharField(max_length=200, blank=True, null=True)
    nome_recebimento_cesta3 = models.CharField(max_length=20, blank=True, null=True)
    processo = models.CharField(max_length=50, blank=True, null=True)
    meses_processo = models.CharField(max_length=2000, blank=True, null=True)
    num_requisicao = models.CharField(max_length=50, blank=True, null=True)
    id_familia = models.CharField(max_length=20, blank=True, null=True)
    id_visita = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    relatorio = models.CharField(max_length=2000, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    tipo_cesta = models.CharField(max_length=20, blank=True, null=True)
    concessao = models.CharField(max_length=20, blank=True, null=True)
    id_servidor = models.CharField(max_length=20, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nis = models.CharField(max_length=20, blank=True, null=True)
    data_nasc = models.CharField(max_length=20, blank=True, null=True)
    data_hora_agenda = models.CharField(max_length=20, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    unidade = models.CharField(max_length=2000, blank=True, null=True)
    data_requerimento = models.CharField(max_length=20, blank=True, null=True)
    local_nasc = models.CharField(max_length=100, blank=True, null=True)
    pai = models.CharField(max_length=200, blank=True, null=True)
    mae = models.CharField(max_length=200, blank=True, null=True)
    bpc = models.CharField(max_length=20, blank=True, null=True)
    forma_requerimento = models.CharField(max_length=20, blank=True, null=True)
    cad_incompleto = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    ra = models.CharField(max_length=150, blank=True, null=True)
    telefone = models.CharField(max_length=30, blank=True, null=True)
    expedidor_uf = models.CharField(max_length=20, blank=True, null=True)
    data_visita = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=20, blank=True, null=True)
    motivo = models.CharField(max_length=2000, blank=True, null=True)
    data_entrega_cesta = models.CharField(max_length=20, blank=True, null=True)
    servidor_nome = models.CharField(max_length=200, blank=True, null=True)
    servidor_matricula = models.CharField(max_length=20, blank=True, null=True)
    telefone_2 = models.CharField(max_length=20, blank=True, null=True)
    complemento = models.CharField(max_length=200, blank=True, null=True)
    evolucao = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_cesta_requerimento_1'


class TbCestaRequerimento1Temp(models.Model):
    id_requerimento = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    id_servidor = models.CharField(max_length=20, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_requerimento = models.CharField(max_length=20, blank=True, null=True)
    unidade = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_cesta_requerimento_1_temp'


class TbCestaStatus(models.Model):
    id_status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_cesta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    data_status = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_cesta_status'


class TbCestaVerdeContador(models.Model):
    mes_ano = models.CharField(max_length=20, blank=True, null=True)
    cesta_convencional_limite = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cesta_convencional_pedidos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cesta_organica_limite = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cesta_organica_pedidos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_cesta_verde_contador'


class TbCestaVerdeReprimida(models.Model):
    id_cesta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tipo_cesta = models.CharField(max_length=100, blank=True, null=True)
    publico = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_cesta_verde_reprimida'


class TbControleRestaurante(models.Model):
    id_controle_restaurante = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mes_ano = models.CharField(max_length=10, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    valor_refeicao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    processo = models.CharField(max_length=100, blank=True, null=True)
    diretor_acomp_contr = models.CharField(max_length=150, blank=True, null=True)
    user_responsavel = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_controle_restaurante'


class TbConvocacao(models.Model):
    id_convocacao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    interesse = models.CharField(max_length=500, blank=True, null=True)
    trazer = models.CharField(max_length=200, blank=True, null=True)
    trazer_outros = models.CharField(max_length=200, blank=True, null=True)
    data_comparecimento = models.DateField(blank=True, null=True)
    hora_comparecimento = models.CharField(max_length=5, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_convocacao'


class TbCupomTotais(models.Model):
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    id_restaurante = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    refeicao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marmita = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pessoas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_cupom_totais = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pessoas_refeicao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pessoas_marmita = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pessoas_marmita_refeicao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pessoas_marmita_marmita = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    refeicao_tr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marmita_tr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cafe = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_cupom_totais'


class TbCuponRestaurante(models.Model):
    id_cupon_restaurante = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    codigo_barra = models.CharField(max_length=200, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    ident_catraca = models.CharField(max_length=200, blank=True, null=True)
    id_restaurante = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_controle_restaurante = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_cupon_restaurante'


class TbDadosCadUnico(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    rg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_expedicao = models.CharField(max_length=10, blank=True, null=True)
    orgao = models.CharField(max_length=100, blank=True, null=True)
    data_nascimento = models.CharField(max_length=10, blank=True, null=True)
    data_atualizacao_v7 = models.CharField(max_length=20, blank=True, null=True)
    naturalidade = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dados_cad_unico'


class TbDadosComplementares(models.Model):
    id_dados_complementares = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    genero = models.CharField(max_length=20, blank=True, null=True)
    orientacao_afetivo_sexual = models.CharField(max_length=20, blank=True, null=True)
    orientacao_afetivo_sex_outro = models.CharField(max_length=30, blank=True, null=True)
    identidade_de_genero = models.CharField(max_length=20, blank=True, null=True)
    identidade_de_genero_outro = models.CharField(max_length=30, blank=True, null=True)
    pessoa_desaparecida = models.CharField(max_length=4, blank=True, null=True)
    mes_ano_desaparecimento = models.CharField(max_length=7, blank=True, null=True)
    mes_ano_retorno = models.CharField(max_length=7, blank=True, null=True)
    situacao_de_rua = models.CharField(max_length=4, blank=True, null=True)
    logradouro = models.CharField(max_length=300, blank=True, null=True)
    id_ra = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ponto_referencia = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    situacao_rua_desde = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qtd_vezes_dorme_na_rua = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quando_nao_rua_onde_dorme = models.CharField(max_length=100, blank=True, null=True)
    pessoa_referencia_contato = models.CharField(max_length=2000, blank=True, null=True)
    telefone_pessoa_referencia = models.CharField(max_length=2000, blank=True, null=True)
    hist_violencia_violacao_dir = models.CharField(max_length=4, blank=True, null=True)
    especificacao_historia = models.CharField(max_length=1000, blank=True, null=True)
    outra_historia_especificacao = models.CharField(max_length=50, blank=True, null=True)
    sp_abuso_violencia_sexual = models.CharField(max_length=4, blank=True, null=True)
    sp_ameaca_morte = models.CharField(max_length=4, blank=True, null=True)
    sp_carcere_privado = models.CharField(max_length=4, blank=True, null=True)
    sp_disc_ident_gen_orient_sex = models.CharField(max_length=4, blank=True, null=True)
    sp_disc_int_religiosa = models.CharField(max_length=4, blank=True, null=True)
    sp_disc_raca_etnia = models.CharField(max_length=4, blank=True, null=True)
    sp_exp_forca_trabalho_escravo = models.CharField(max_length=4, blank=True, null=True)
    sp_exp_forca_trabalho_sexo = models.CharField(max_length=4, blank=True, null=True)
    sp_exp_forca_trabalho_outro = models.CharField(max_length=4, blank=True, null=True)
    sp_exp_sexual = models.CharField(max_length=4, blank=True, null=True)
    sp_negligencia_abandono = models.CharField(max_length=4, blank=True, null=True)
    sp_trab_infant_trafico_drogas = models.CharField(max_length=4, blank=True, null=True)
    sp_trab_infant_exp_sexual = models.CharField(max_length=4, blank=True, null=True)
    sp_trab_infant_reciclaveis = models.CharField(max_length=4, blank=True, null=True)
    sp_trab_infant_trabalho_rua = models.CharField(max_length=4, blank=True, null=True)
    sp_trab_infant_mendicancia = models.CharField(max_length=4, blank=True, null=True)
    sp_trab_infant_outro = models.CharField(max_length=4, blank=True, null=True)
    sp_trafico_pessoas = models.CharField(max_length=4, blank=True, null=True)
    sp_trajetoria_rua = models.CharField(max_length=4, blank=True, null=True)
    sp_violencia_fisica = models.CharField(max_length=4, blank=True, null=True)
    sp_violencia_patrimonial = models.CharField(max_length=4, blank=True, null=True)
    sp_violencia_psicologica = models.CharField(max_length=4, blank=True, null=True)
    sp_violencia_agentes_estatais = models.CharField(max_length=4, blank=True, null=True)
    sp_outras_formas_violacao = models.CharField(max_length=4, blank=True, null=True)
    uso_abusivo_alcool = models.CharField(max_length=4, blank=True, null=True)
    uso_abusivo_drogas_licitas = models.CharField(max_length=4, blank=True, null=True)
    uso_abusivo_drogas_ilicitas = models.CharField(max_length=4, blank=True, null=True)
    pess_depend_atividades_diarias = models.CharField(max_length=4, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    localizacao = models.CharField(max_length=50, blank=True, null=True)
    parentesco_pessoa_referencia = models.CharField(max_length=2000, blank=True, null=True)
    endereco_pessoa_referencia = models.CharField(max_length=4000, blank=True, null=True)
    ad_abuso_violencia_sexual = models.CharField(max_length=4, blank=True, null=True)
    ad_ameaca_morte = models.CharField(max_length=4, blank=True, null=True)
    ad_carcere_privado = models.CharField(max_length=4, blank=True, null=True)
    ad_disc_ident_gen_orient_sex = models.CharField(max_length=4, blank=True, null=True)
    ad_disc_intolerancia_religiosa = models.CharField(max_length=4, blank=True, null=True)
    ad_violencia_fisica = models.CharField(max_length=4, blank=True, null=True)
    ad_violencia_patrimonial = models.CharField(max_length=4, blank=True, null=True)
    ad_violencia_psicologica = models.CharField(max_length=4, blank=True, null=True)
    ad_outras_formas_violacao = models.CharField(max_length=4, blank=True, null=True)
    grau_dependencia = models.CharField(max_length=20, blank=True, null=True)
    ausencia_documentacao_civil = models.CharField(max_length=20, blank=True, null=True)
    necessita_apoio_doc_civil = models.CharField(max_length=350, blank=True, null=True)
    bairro = models.CharField(max_length=300, blank=True, null=True)
    sp_trab_infant_domestico = models.CharField(max_length=4, blank=True, null=True)
    sp_trab_infant_agr_familiar = models.CharField(max_length=4, blank=True, null=True)
    gestante = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dados_complementares'


class TbDadosEntidade(models.Model):
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    razao_social = models.CharField(max_length=200, blank=True, null=True)
    nome_fantasia = models.CharField(max_length=200, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    cep = models.CharField(max_length=20, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    nome_dirigente = models.CharField(max_length=100, blank=True, null=True)
    numero_inscricao_cas = models.CharField(max_length=20, blank=True, null=True)
    numero_convenio_se = models.CharField(max_length=20, blank=True, null=True)
    status_entidade = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dados_entidade'


class TbDemanda(models.Model):
    id_demanda = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    demanda = models.CharField(max_length=2000, blank=True, null=True)
    ativo = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_demanda'


class TbDemandaTipoUnidade(models.Model):
    id_demanda = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_tipo_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_demanda_tipo_unidade'


class TbDepartamentos(models.Model):
    id_departamento = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_departamentos'


class TbEmpresaRestaurantes(models.Model):
    id_empresa_restaurante = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cnpj = models.CharField(max_length=19, blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    contato = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_empresa_restaurantes'


class TbEncaminhamento(models.Model):
    id_encaminhamento = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_responsavel = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tipo_encaminhamento = models.CharField(max_length=200, blank=True, null=True)
    destinatario = models.CharField(max_length=200, blank=True, null=True)
    observacao = models.CharField(max_length=4000, blank=True, null=True)
    entidade = models.CharField(max_length=200, blank=True, null=True)
    faixa_scfv = models.CharField(max_length=30, blank=True, null=True)
    raca_cor = models.CharField(max_length=20, blank=True, null=True)
    situacao_escolar = models.CharField(max_length=20, blank=True, null=True)
    escola = models.CharField(max_length=200, blank=True, null=True)
    frequenta_eja = models.CharField(max_length=20, blank=True, null=True)
    segmento = models.CharField(max_length=20, blank=True, null=True)
    semestre = models.CharField(max_length=20, blank=True, null=True)
    nivel = models.CharField(max_length=20, blank=True, null=True)
    serie = models.CharField(max_length=20, blank=True, null=True)
    turno = models.CharField(max_length=20, blank=True, null=True)
    grau_parentesco = models.CharField(max_length=20, blank=True, null=True)
    recebe_beneficio = models.CharField(max_length=20, blank=True, null=True)
    beneficio = models.CharField(max_length=20, blank=True, null=True)
    inscrita_cad_unico = models.CharField(max_length=20, blank=True, null=True)
    encaminhado_pse = models.CharField(max_length=20, blank=True, null=True)
    instancia_demandante = models.CharField(max_length=100, blank=True, null=True)
    qual_demandante = models.CharField(max_length=200, blank=True, null=True)
    publico_prioritario = models.CharField(max_length=200, blank=True, null=True)
    conhecimento_scfv = models.CharField(max_length=20, blank=True, null=True)
    outro_conhecimento = models.CharField(max_length=200, blank=True, null=True)
    data_encaminhamento = models.DateField(blank=True, null=True)
    acolhido = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    evolucao = models.CharField(max_length=4000, blank=True, null=True)
    situacao_prioritaria = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_encaminhamento'


class TbEntidade(models.Model):
    id_entidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cas = models.CharField(max_length=2, blank=True, null=True)
    se = models.CharField(max_length=2, blank=True, null=True)
    programas_sociais = models.CharField(max_length=2, blank=True, null=True)
    outros = models.CharField(max_length=2, blank=True, null=True)
    nome_fantasia = models.CharField(max_length=200, blank=True, null=True)
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    cep = models.CharField(max_length=20, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    telefone1 = models.CharField(max_length=20, blank=True, null=True)
    telefone2 = models.CharField(max_length=20, blank=True, null=True)
    tel_responsavel = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    nome_responsavel = models.CharField(max_length=200, blank=True, null=True)
    num_inscricao = models.CharField(max_length=20, blank=True, null=True)
    data_inscricao = models.CharField(max_length=20, blank=True, null=True)
    entidade = models.CharField(max_length=20, blank=True, null=True)
    abrigo = models.CharField(max_length=20, blank=True, null=True)
    creche = models.CharField(max_length=20, blank=True, null=True)
    segunda = models.CharField(max_length=20, blank=True, null=True)
    terca = models.CharField(max_length=20, blank=True, null=True)
    quarta = models.CharField(max_length=20, blank=True, null=True)
    quinta = models.CharField(max_length=20, blank=True, null=True)
    sexta = models.CharField(max_length=20, blank=True, null=True)
    sabado = models.CharField(max_length=20, blank=True, null=True)
    domingo = models.CharField(max_length=20, blank=True, null=True)
    arrecada_alimentos = models.CharField(max_length=20, blank=True, null=True)
    prepara_alimentos = models.CharField(max_length=20, blank=True, null=True)
    cafe_manha = models.CharField(max_length=20, blank=True, null=True)
    lanche_manha = models.CharField(max_length=20, blank=True, null=True)
    almoco = models.CharField(max_length=20, blank=True, null=True)
    lanche_tarde = models.CharField(max_length=20, blank=True, null=True)
    jantar = models.CharField(max_length=20, blank=True, null=True)
    ceia = models.CharField(max_length=20, blank=True, null=True)
    geladeira = models.CharField(max_length=20, blank=True, null=True)
    freezer = models.CharField(max_length=20, blank=True, null=True)
    num_convenio = models.CharField(max_length=50, blank=True, null=True)
    razao_social = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_entidade'


class TbEntidadeModalidade(models.Model):
    id_entidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    modalidade = models.CharField(max_length=20, blank=True, null=True)
    crianca_menor_6meses = models.CharField(max_length=20, blank=True, null=True)
    crianca_6meses_2anos = models.CharField(max_length=20, blank=True, null=True)
    crianca_2anos_6anos = models.CharField(max_length=20, blank=True, null=True)
    crianca_6anos_14anos = models.CharField(max_length=20, blank=True, null=True)
    jovens_15anos_20anos = models.CharField(max_length=20, blank=True, null=True)
    adulto_20anos_59anos = models.CharField(max_length=20, blank=True, null=True)
    pessoas_60anos_mais = models.CharField(max_length=20, blank=True, null=True)
    atend_nutrizes = models.CharField(max_length=20, blank=True, null=True)
    atend_gestantes = models.CharField(max_length=20, blank=True, null=True)
    atend_deficiente = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_entidade_modalidade'


class TbEvolucaoAcoes(models.Model):
    id_evolucao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_acao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_evolucao_acoes'


class TbEvolucaoAtendimento(models.Model):
    id_evolucao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_demanda = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    perfil_visualizacao = models.CharField(max_length=20, blank=True, null=True)
    unidade_visualizacao = models.CharField(max_length=20, blank=True, null=True)
    prematricula = models.CharField(max_length=3, blank=True, null=True)
    visita_realizada = models.CharField(max_length=3, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_evolucao_atendimento'


class TbEvolucaoDemanda(models.Model):
    id_evolucao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_demanda = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_evolucao_demanda'


class TbEvolucaoSeas(models.Model):
    id_evolucao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    demanda = models.CharField(max_length=200, blank=True, null=True)
    intervencoes = models.TextField(blank=True, null=True)
    encaminhamentos = models.TextField(blank=True, null=True)
    enc_cras = models.CharField(max_length=100, blank=True, null=True)
    enc_cecon = models.CharField(max_length=100, blank=True, null=True)
    enc_creas = models.CharField(max_length=100, blank=True, null=True)
    enc_centropop = models.CharField(max_length=100, blank=True, null=True)
    enc_servico_acolhimento = models.CharField(max_length=100, blank=True, null=True)
    servico_acolhimento_entidade = models.CharField(max_length=100, blank=True, null=True)
    enc_adm_regional = models.CharField(max_length=100, blank=True, null=True)
    enc_conselho_tutelar = models.CharField(max_length=100, blank=True, null=True)
    poder_judiciario_inst = models.CharField(max_length=100, blank=True, null=True)
    ministerio_publico_inst = models.CharField(max_length=100, blank=True, null=True)
    defensoria_publica_inst = models.CharField(max_length=100, blank=True, null=True)
    delegacias_inst = models.CharField(max_length=100, blank=True, null=True)
    conselho_defesa_direitos_inst = models.CharField(max_length=100, blank=True, null=True)
    regularizacao_doc_civil_inst = models.CharField(max_length=100, blank=True, null=True)
    politica_saude_inst = models.CharField(max_length=100, blank=True, null=True)
    politica_educacao_inst = models.CharField(max_length=100, blank=True, null=True)
    politica_trabalho_inst = models.CharField(max_length=100, blank=True, null=True)
    politica_habitacao_inst = models.CharField(max_length=100, blank=True, null=True)
    politica_esporte_inst = models.CharField(max_length=100, blank=True, null=True)
    politica_mulheres_inst = models.CharField(max_length=100, blank=True, null=True)
    sejus_inst = models.CharField(max_length=100, blank=True, null=True)
    outras_politicas_set_inst = models.CharField(max_length=100, blank=True, null=True)
    org_sociedade_civil_inst = models.CharField(max_length=100, blank=True, null=True)
    grupo_parceiro_unidade_inst = models.CharField(max_length=100, blank=True, null=True)
    outro_encaminhamento_inst = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    ra = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    logradouro = models.CharField(max_length=200, blank=True, null=True)
    complemento = models.CharField(max_length=200, blank=True, null=True)
    ponto_referencia = models.CharField(max_length=200, blank=True, null=True)
    localizacao = models.CharField(max_length=100, blank=True, null=True)
    horario_abordagem = models.CharField(max_length=10, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_evolucao_seas'


class TbEvolucaoSeasEncaminha(models.Model):
    id_evolucao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_encaminhamento = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_evolucao_seas_encaminha'


class TbEvolucaoSeasIntervencao(models.Model):
    id_evolucao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_intervencao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_evolucao_seas_intervencao'


class TbEvolucaoSids1(models.Model):
    id_evolucao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tecnico = models.CharField(max_length=200, blank=True, null=True)
    demanda = models.CharField(max_length=200, blank=True, null=True)
    evolucao = models.CharField(max_length=2000, blank=True, null=True)
    data_criacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_evolucao_sids1'


class TbFamilia(models.Model):
    id_familia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    endereco = models.CharField(max_length=150, blank=True, null=True)
    complemento = models.CharField(max_length=75, blank=True, null=True)
    bairro = models.CharField(max_length=150, blank=True, null=True)
    pt_referencia = models.CharField(max_length=250, blank=True, null=True)
    uf = models.CharField(max_length=20, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    resp_familiar = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sit_dom = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=25, blank=True, null=True)
    ag_abrangencia_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_atualizacao = models.DateField(blank=True, null=True)
    forma_ingresso = models.CharField(max_length=30, blank=True, null=True)
    id_tipo_acesso = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_demanda = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_familia'


class TbFamiliaOld(models.Model):
    id_familia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    endereco = models.CharField(max_length=150, blank=True, null=True)
    complemento = models.CharField(max_length=75, blank=True, null=True)
    bairro = models.CharField(max_length=150, blank=True, null=True)
    pt_referencia = models.CharField(max_length=250, blank=True, null=True)
    uf = models.CharField(max_length=20, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    resp_familiar = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sit_dom = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=25, blank=True, null=True)
    ag_abrangencia_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_atualizacao = models.DateField(blank=True, null=True)
    forma_ingresso = models.CharField(max_length=30, blank=True, null=True)
    id_tipo_acesso = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_demanda = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_familia_old'


class TbFamiliaSei(models.Model):
    id_familia_sei = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_familia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    numero_sei = models.CharField(max_length=200, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_familia_sei'


class TbFolhaAcompanhamento(models.Model):
    id_folha = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    programa = models.CharField(max_length=124, blank=True, null=True)
    mes = models.CharField(max_length=20, blank=True, null=True)
    ano = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    listagem = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    valor_folha = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ne_folha = models.CharField(max_length=11, blank=True, null=True)
    data_ne_folha = models.DateField(blank=True, null=True)
    nl_folha = models.CharField(max_length=11, blank=True, null=True)
    data_nl_folha = models.DateField(blank=True, null=True)
    pp_folha = models.CharField(max_length=11, blank=True, null=True)
    data_pp_folha = models.DateField(blank=True, null=True)
    ob_folha = models.CharField(max_length=11, blank=True, null=True)
    data_ob_folha = models.DateField(blank=True, null=True)
    num_fatura = models.CharField(max_length=20, blank=True, null=True)
    reg_fatura = models.CharField(max_length=20, blank=True, null=True)
    danfe_fatura = models.CharField(max_length=20, blank=True, null=True)
    reg_danfe_fatura = models.CharField(max_length=20, blank=True, null=True)
    valor_tarifa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ne_tarifa = models.CharField(max_length=11, blank=True, null=True)
    data_ne_tarifa = models.DateField(blank=True, null=True)
    nl_tarifa = models.CharField(max_length=11, blank=True, null=True)
    data_nl_tarifa = models.DateField(blank=True, null=True)
    pp_tarifa = models.CharField(max_length=11, blank=True, null=True)
    data_pp_tarifa = models.DateField(blank=True, null=True)
    ob_tarifa = models.CharField(max_length=11, blank=True, null=True)
    data_ob_tarifa = models.DateField(blank=True, null=True)
    data_inicio_pgto = models.DateField(blank=True, null=True)
    data_fim_pgto = models.DateField(blank=True, null=True)
    data_prorrog_pgto = models.DateField(blank=True, null=True)
    agente_pagador = models.CharField(max_length=124, blank=True, null=True)
    num_proc_financeiro = models.CharField(max_length=22, blank=True, null=True)
    num_proc_tarifa = models.CharField(max_length=22, blank=True, null=True)
    id_serv_criacao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_serv_alteracao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_criacao = models.CharField(max_length=30, blank=True, null=True)
    data_alteracao = models.CharField(max_length=30, blank=True, null=True)
    qnt_beneficios = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_folha_acompanhamento'


class TbFolhaBeneficios(models.Model):
    memo = models.CharField(max_length=70, blank=True, null=True)
    nome_usuario = models.CharField(max_length=254, blank=True, null=True)
    cpf = models.CharField(max_length=32, blank=True, null=True)
    endereco = models.CharField(max_length=254, blank=True, null=True)
    unidade_atendimento = models.CharField(max_length=128, blank=True, null=True)
    cidade = models.CharField(max_length=70, blank=True, null=True)
    rg = models.CharField(max_length=70, blank=True, null=True)
    uf = models.CharField(max_length=26, blank=True, null=True)
    nome_crianca = models.CharField(max_length=254, blank=True, null=True)
    data_nascimento_crianca = models.DateField(blank=True, null=True)
    nome_corrigido = models.CharField(max_length=128, blank=True, null=True)
    cpf_corrigido = models.CharField(max_length=26, blank=True, null=True)
    rg_corrigido = models.CharField(max_length=70, blank=True, null=True)
    uf_corrigido = models.CharField(max_length=26, blank=True, null=True)
    valor_auxilio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    renda_per_capita = models.IntegerField(blank=True, null=True)
    auxilio = models.CharField(max_length=70, blank=True, null=True)
    listagem = models.CharField(max_length=128, blank=True, null=True)
    mes = models.CharField(max_length=70, blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    obs = models.CharField(max_length=256, blank=True, null=True)
    numero_conveniencia = models.CharField(max_length=26, blank=True, null=True)
    endereco_conveniencia = models.CharField(max_length=128, blank=True, null=True)
    prestacao_feita = models.CharField(max_length=128, blank=True, null=True)
    pago = models.CharField(max_length=26, blank=True, null=True)
    autorizacao = models.CharField(max_length=26, blank=True, null=True)
    assinatura = models.CharField(max_length=26, blank=True, null=True)
    prestacao_contas = models.CharField(max_length=128, blank=True, null=True)
    id_beneficio = models.CharField(max_length=20, blank=True, null=True)
    id_sids = models.CharField(max_length=64, blank=True, null=True)
    nis = models.CharField(max_length=20, blank=True, null=True)
    data_nasc = models.DateTimeField(blank=True, null=True)
    complemento_endereco = models.CharField(max_length=128, blank=True, null=True)
    bairro = models.CharField(max_length=128, blank=True, null=True)
    pt_referencia = models.CharField(max_length=254, blank=True, null=True)
    natalidade_gemeos = models.CharField(max_length=3, blank=True, null=True)
    cod_seguranca = models.CharField(max_length=20, blank=True, null=True)
    codhab = models.CharField(max_length=128, blank=True, null=True)
    recebeu_beneficio = models.CharField(max_length=128, blank=True, null=True)
    obs_prestacao = models.CharField(max_length=256, blank=True, null=True)
    listagem_especial = models.CharField(max_length=128, blank=True, null=True)
    ptts = models.CharField(max_length=20, blank=True, null=True)
    agencia = models.CharField(max_length=20, blank=True, null=True)
    conta = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_reg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_folha = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_folha_beneficios'


class TbFolhaNaoPagos(models.Model):
    id_beneficio = models.CharField(max_length=20, blank=True, null=True)
    nome = models.CharField(max_length=256, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    valor = models.CharField(max_length=20, blank=True, null=True)
    auxilio = models.CharField(max_length=56, blank=True, null=True)
    listagem = models.CharField(max_length=2, blank=True, null=True)
    ano = models.CharField(max_length=20, blank=True, null=True)
    mes = models.CharField(max_length=20, blank=True, null=True)
    referencia = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_folha_nao_pagos'


class TbFuncionalidades(models.Model):
    id_funcionalidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    referencia = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_funcionalidades'


class TbFuncionalidadesModulos(models.Model):
    id_funcionalidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_modulo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_funcionalidades_modulos'


class TbGestaoBeneficioDibes(models.Model):
    id_gestao_bene_dibes = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome_diretor = models.CharField(max_length=255, blank=True, null=True)
    matricula_diretor = models.CharField(max_length=50, blank=True, null=True)
    num_processo = models.CharField(max_length=30, blank=True, null=True)
    interessado_suag = models.CharField(max_length=255, blank=True, null=True)
    num_listagem = models.CharField(max_length=50, blank=True, null=True)
    coordenador = models.CharField(max_length=255, blank=True, null=True)
    matricula_coordenador = models.CharField(max_length=50, blank=True, null=True)
    subs_assis_social = models.CharField(max_length=255, blank=True, null=True)
    matricula_subs = models.CharField(max_length=50, blank=True, null=True)
    interessado_prov = models.CharField(max_length=255, blank=True, null=True)
    data = models.CharField(db_column='DATA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome_diretoria = models.CharField(max_length=150, blank=True, null=True)
    nome_coordenacao = models.CharField(max_length=150, blank=True, null=True)
    nome_subsecretaria = models.CharField(max_length=150, blank=True, null=True)
    valor = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_gestao_beneficio_dibes'


class TbHistoricoAcessoDemanda(models.Model):
    id_historico = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_familia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_tipo_acesso = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_demanda = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_historico_acesso_demanda'


class TbHistoricoViolencia(models.Model):
    id_historico = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    data_ocorrido = models.DateField(blank=True, null=True)
    relacionamento_envolvidos = models.CharField(max_length=200, blank=True, null=True)
    historico_relacionamento = models.TextField(blank=True, null=True)
    descricao_situacao_encaminhamento = models.TextField(blank=True, null=True)
    voce_procurou_servico_saude = models.CharField(max_length=200, blank=True, null=True)
    outra_parte_procurou_servico_saude = models.CharField(max_length=200, blank=True, null=True)
    quando_houve_primeira_violencia = models.TextField(blank=True, null=True)
    violencia_mais_grave = models.TextField(blank=True, null=True)
    ultima_violencia = models.TextField(blank=True, null=True)
    formas_violencia_cometidas = models.CharField(max_length=200, blank=True, null=True)
    formas_violencia_sofridas = models.CharField(max_length=200, blank=True, null=True)
    situacao_processual = models.CharField(max_length=200, blank=True, null=True)
    medidas_protetivas_concedidas = models.CharField(max_length=200, blank=True, null=True)
    medidas_protetivas = models.CharField(max_length=200, blank=True, null=True)
    medidas_sendo_cumpridas = models.CharField(max_length=200, blank=True, null=True)
    houve_prisao = models.TextField(blank=True, null=True)
    violencia_outros_relacionamentos = models.CharField(max_length=200, blank=True, null=True)
    violencia_outros_relacionamentos_ocorrencia = models.CharField(max_length=200, blank=True, null=True)
    violencia_outros_relacionamentos_detalhar = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    formas_violencia_cometidas_obs = models.TextField(blank=True, null=True)
    formas_violencia_sofridas_obs = models.TextField(blank=True, null=True)
    medidas_protetivas_obs = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_historico_violencia'


class TbIntervencao(models.Model):
    id_intervencao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    intervencao = models.CharField(max_length=200, blank=True, null=True)
    ativo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_intervencao'


class TbLiberacaoDibes(models.Model):
    id_liberacao_dibes = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    data = models.CharField(db_column='DATA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id_natalidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    motivo = models.CharField(max_length=3000, blank=True, null=True)
    exportado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_export = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_liberacao_dibes'


class TbLiberacaoDibesCal(models.Model):
    id_liberacao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_calamidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    motivo = models.CharField(max_length=3000, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    exportado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_export = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_liberacao_dibes_cal'


class TbLiberacaoDibesCesta(models.Model):
    id_liberacao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_cesta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    motivo = models.CharField(max_length=2000, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_liberacao_dibes_cesta'


class TbLiberacaoDibesExcepcional(models.Model):
    id_liberacao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_excepcional = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    motivo = models.CharField(max_length=4000, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    exportado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_export = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_liberacao_dibes_excepcional'


class TbLiberacaoDibesMorte(models.Model):
    id_liberacao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_por_morte = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    motivo = models.CharField(max_length=3000, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    exportado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_export = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_liberacao_dibes_morte'


class TbLiberacaoDibesVul(models.Model):
    id_liberacao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_vulnerabilidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    motivo = models.CharField(max_length=3000, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    exportado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_export = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_liberacao_dibes_vul'


class TbLiberacaoGestaoBeneficio(models.Model):
    data = models.CharField(db_column='DATA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dataini = models.CharField(max_length=50, blank=True, null=True)
    datafim = models.CharField(max_length=50, blank=True, null=True)
    id_liberacao_dibes = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_gestao_bene_dibes = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    grupo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_liberacao_gestao_beneficio'


class TbListagemAreaRisco(models.Model):
    cpf = models.CharField(max_length=26, blank=True, null=True)
    nome = models.CharField(max_length=128, blank=True, null=True)
    origem = models.CharField(max_length=128, blank=True, null=True)
    atualizacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_listagem_area_risco'


class TbListagemCodhab(models.Model):
    nome_usuario = models.CharField(max_length=128, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    situacao_cadastral = models.CharField(max_length=128, blank=True, null=True)
    habilitado = models.CharField(max_length=3, blank=True, null=True)
    data_consulta = models.DateField(blank=True, null=True)
    obs = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_listagem_codhab'


class TbListagemPgto(models.Model):
    id_listagem = models.CharField(max_length=20, blank=True, null=True)
    listagem = models.CharField(max_length=20, blank=True, null=True)
    mes_referencia = models.CharField(max_length=20, blank=True, null=True)
    ano_referencia = models.CharField(max_length=4, blank=True, null=True)
    data_inicio_pgto = models.DateField(blank=True, null=True)
    data_termino_pgto = models.DateField(blank=True, null=True)
    id_usuario_sistema = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_listagem_pgto'


class TbLocalidade(models.Model):
    id_localidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=72, blank=True, null=True)
    cep_localidade = models.CharField(max_length=8, blank=True, null=True)
    tipo = models.CharField(max_length=10, blank=True, null=True)
    cod_ibge = models.CharField(max_length=30, blank=True, null=True)
    id_uf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_localidade'


class TbLogradouro(models.Model):
    id_logradouro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    tipo = models.CharField(max_length=36, blank=True, null=True)
    id_bairro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_localidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_logradouro'


class TbMaternidade(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nm_unidade = models.CharField(max_length=90, blank=True, null=True)
    nome = models.CharField(max_length=99, blank=True, null=True)
    nome_social = models.CharField(max_length=45, blank=True, null=True)
    telefoneresidencia = models.CharField(max_length=45, blank=True, null=True)
    telefonecelular = models.CharField(max_length=45, blank=True, null=True)
    telefonerecado = models.CharField(max_length=45, blank=True, null=True)
    datanascimento = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    sexo = models.CharField(max_length=45, blank=True, null=True)
    nomepai = models.CharField(max_length=99, blank=True, null=True)
    nomemae = models.CharField(max_length=99, blank=True, null=True)
    estadocivil = models.CharField(max_length=45, blank=True, null=True)
    nacionalidade = models.CharField(max_length=45, blank=True, null=True)
    naturalidadeuf = models.CharField(max_length=45, blank=True, null=True)
    naturalidadecidade = models.CharField(max_length=45, blank=True, null=True)
    situacaomercadotrabalho = models.CharField(max_length=90, blank=True, null=True)
    renda = models.CharField(max_length=45, blank=True, null=True)
    cpf = models.CharField(max_length=45, blank=True, null=True)
    rg = models.CharField(max_length=45, blank=True, null=True)
    emissorrg = models.CharField(max_length=45, blank=True, null=True)
    ufrg = models.CharField(max_length=45, blank=True, null=True)
    dataemissaorg = models.CharField(max_length=45, blank=True, null=True)
    endereco = models.CharField(max_length=150, blank=True, null=True)
    numero = models.CharField(max_length=45, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    complemento = models.CharField(max_length=45, blank=True, null=True)
    cidade = models.CharField(max_length=45, blank=True, null=True)
    pontoreferencia = models.CharField(max_length=200, blank=True, null=True)
    situacaodomicilio = models.CharField(max_length=150, blank=True, null=True)
    tempomoradiadf = models.CharField(max_length=45, blank=True, null=True)
    racacor = models.CharField(max_length=45, blank=True, null=True)
    tempogestacao = models.CharField(max_length=45, blank=True, null=True)
    datacadastro = models.CharField(max_length=45, blank=True, null=True)
    criancanasceu = models.CharField(max_length=45, blank=True, null=True)
    hospitalprenatal = models.CharField(max_length=150, blank=True, null=True)
    idcidadeendereco = models.CharField(max_length=20, blank=True, null=True)
    mesanoprovnasc = models.CharField(max_length=20, blank=True, null=True)
    cadastrado = models.CharField(max_length=99, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_maternidade'


class TbMaternidadeMembros(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_pessoa_maternidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)
    nome = models.CharField(max_length=90, blank=True, null=True)
    datanascimento = models.CharField(max_length=45, blank=True, null=True)
    hospitalnascimento = models.CharField(max_length=90, blank=True, null=True)
    certidaonascimento = models.CharField(max_length=90, blank=True, null=True)
    declaracaonascidovivo = models.CharField(max_length=45, blank=True, null=True)
    parentesco = models.CharField(max_length=45, blank=True, null=True)
    situacaomercadotrabalho = models.CharField(max_length=90, blank=True, null=True)
    rendapessoal = models.CharField(max_length=45, blank=True, null=True)
    racacor = models.CharField(max_length=45, blank=True, null=True)
    cadastrado = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_maternidade_membros'


class TbMaternidadePreInscricao(models.Model):
    id_pre_inscricao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cpf = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_maternidade_pre_inscricao'


class TbModulos(models.Model):
    id_modulo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=150, blank=True, null=True)
    referencia = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_modulos'


class TbModulosDepartamentos(models.Model):
    id_modulo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_departamento = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_modulos_departamentos'


class TbMotivosCancelBloq(models.Model):
    id_motivos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    ativo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_motivos_cancel_bloq'


class TbNascMorto(models.Model):
    id_nasc_morto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    certidao_obito = models.CharField(max_length=100, blank=True, null=True)
    identificacao = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    cidade_nasc_obito = models.CharField(max_length=100, blank=True, null=True)
    data_nasc_obito = models.DateField(blank=True, null=True)
    estado_nasc_obito = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_nasc_morto'


class TbNatalidadeAvaliacao(models.Model):
    id_natalidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_avaliacao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_natalidade_avaliacao'


class TbNovidades(models.Model):
    id_novidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    titulo = models.CharField(max_length=200, blank=True, null=True)
    texto = models.CharField(max_length=2000, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    ativo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_novidades'


class TbNucleos(models.Model):
    id_nucleos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    num_atendimento_total = models.CharField(max_length=10, blank=True, null=True)
    num_atendimento_entidade = models.CharField(max_length=10, blank=True, null=True)
    num_atendimento_abrigo = models.CharField(max_length=10, blank=True, null=True)
    num_atendimento_creche = models.CharField(max_length=10, blank=True, null=True)
    crianca_menor_6meses = models.CharField(max_length=10, blank=True, null=True)
    crianca_6meses_2anos = models.CharField(max_length=10, blank=True, null=True)
    crianca_2anos_6anos = models.CharField(max_length=10, blank=True, null=True)
    crianca_6anos_14anos = models.CharField(max_length=10, blank=True, null=True)
    jovens_15anos_20anos = models.CharField(max_length=10, blank=True, null=True)
    adultos_20anos_59anos = models.CharField(max_length=10, blank=True, null=True)
    idosos_60anos_mais = models.CharField(max_length=10, blank=True, null=True)
    atend_gestante = models.CharField(max_length=3, blank=True, null=True)
    atend_deficiente = models.CharField(max_length=3, blank=True, null=True)
    arrecada_alimentos = models.CharField(max_length=10, blank=True, null=True)
    prepara_alimentos = models.CharField(max_length=10, blank=True, null=True)
    refeicao_cafe_manha = models.CharField(max_length=10, blank=True, null=True)
    refeicao_lanche_manha = models.CharField(max_length=10, blank=True, null=True)
    refeicao_almoco = models.CharField(max_length=10, blank=True, null=True)
    refeicao_tarde = models.CharField(max_length=10, blank=True, null=True)
    jantar = models.CharField(max_length=10, blank=True, null=True)
    equip_refrigerado = models.CharField(max_length=3, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_nucleos'


class TbOrgaos(models.Model):
    id_orgaos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=300, blank=True, null=True)
    tb_usuarios_sistema_id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_orgaos'


class TbPainelEspera(models.Model):
    id_espera = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.CharField(db_column='DATA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ativo = models.CharField(max_length=1, blank=True, null=True)
    motivo_remocao = models.CharField(max_length=30, blank=True, null=True)
    unidade_demandante = models.CharField(max_length=200, blank=True, null=True)
    motivo_solicitacao = models.CharField(max_length=200, blank=True, null=True)
    local_residencia_permanencia = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_painel_espera'


class TbPainelReserva(models.Model):
    id_reserva = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_painel_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.CharField(db_column='DATA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_painel_reserva'


class TbPainelUnidades(models.Model):
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    meta_capacidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tipo = models.CharField(max_length=30, blank=True, null=True)
    ativo = models.CharField(max_length=1, blank=True, null=True)
    publico = models.CharField(max_length=20, blank=True, null=True)
    faixa_etaria = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=40, blank=True, null=True)
    ordem = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_painel_unidades'


class TbPainelVagas(models.Model):
    id_vagas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_painel_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    vagas_ocupadas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vagas_disponiveis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_painel_vagas'


class TbPais(models.Model):
    id_pais = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_pais'


class TbParecerTecnicoMorte(models.Model):
    id_parecer = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_pormorte = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    justificativa = models.CharField(max_length=3000, blank=True, null=True)
    parecer_bens = models.CharField(max_length=20, blank=True, null=True)
    parecer_pecunia = models.CharField(max_length=20, blank=True, null=True)
    parecer_ressarcimento = models.CharField(max_length=20, blank=True, null=True)
    numero_boletim = models.CharField(max_length=150, blank=True, null=True)
    data_boletim = models.DateField(blank=True, null=True)
    delegacia = models.CharField(max_length=200, blank=True, null=True)
    data_parecer = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_parecer_tecnico_morte'


class TbParecerTecnicoNatalidade(models.Model):
    id_parecer = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_natalidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    justificativa = models.CharField(max_length=3000, blank=True, null=True)
    parecer_pecunia = models.CharField(max_length=20, blank=True, null=True)
    data_parecer = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_parecer_tecnico_natalidade'


class TbPassagem(models.Model):
    id_passagem = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qtd_passagens = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cidade = models.CharField(max_length=300, blank=True, null=True)
    uf = models.CharField(max_length=30, blank=True, null=True)
    data_viagem = models.DateField(blank=True, null=True)
    horario_embarque = models.CharField(max_length=20, blank=True, null=True)
    numero_bilhete = models.CharField(max_length=200, blank=True, null=True)
    valor_unitario = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    empresa = models.CharField(max_length=300, blank=True, null=True)
    url_pdf_passagem = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_passagem'


class TbPerfil(models.Model):
    id_perfil = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_perfil'


class TbPratoCheio(models.Model):
    id_prato_cheio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_cesta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    renda_percapta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_envio_brb = models.CharField(max_length=26, blank=True, null=True)
    data_requerimento = models.CharField(max_length=26, blank=True, null=True)
    status_programa = models.CharField(max_length=128, blank=True, null=True)
    status_cartao = models.CharField(max_length=260, blank=True, null=True)
    data_status_cartao = models.CharField(max_length=26, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_prato_cheio'


class TbPratoCheioAveriguacao(models.Model):
    cpf = models.CharField(max_length=20, blank=True, null=True)
    historico = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_prato_cheio_averiguacao'


class TbPratoCheioMensagem(models.Model):
    id_prato_cheio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mensagem = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_prato_cheio_mensagem'


class TbPratoCheioParcelas(models.Model):
    id_parcela = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_prato_cheio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_credito = models.CharField(max_length=-1, blank=True, null=True)
    valor_credito = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_prato_cheio_parcelas'


class TbProcurador(models.Model):
    id_procurador = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    endereco = models.CharField(max_length=150, blank=True, null=True)
    rg = models.CharField(max_length=100, blank=True, null=True)
    ctps = models.CharField(max_length=100, blank=True, null=True)
    cnh = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField(max_length=15, blank=True, null=True)
    emissor = models.CharField(max_length=50, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_cadastro = models.DateField(blank=True, null=True)
    uf = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=30, blank=True, null=True)
    numero = models.CharField(max_length=150, blank=True, null=True)
    bairro = models.CharField(max_length=200, blank=True, null=True)
    data_nasc = models.DateField(blank=True, null=True)
    data_emissao = models.DateField(blank=True, null=True)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    telefone_resid = models.CharField(max_length=150, blank=True, null=True)
    telefone_cel = models.CharField(max_length=150, blank=True, null=True)
    telefone_rec = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_procurador'


class TbProntuario(models.Model):
    id_prontuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_familia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    numero = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_prontuario'


class TbProtecaoEspecialAtendimento(models.Model):
    id_atendimento = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    procedencia = models.CharField(max_length=100, blank=True, null=True)
    processo = models.CharField(max_length=50, blank=True, null=True)
    bo = models.CharField(max_length=50, blank=True, null=True)
    prioridade = models.CharField(max_length=20, blank=True, null=True)
    classificacao = models.CharField(max_length=20, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    evolucao = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=60, blank=True, null=True)
    data_conclusao = models.DateField(blank=True, null=True)
    relatorio = models.TextField(blank=True, null=True)
    id_usuario_sistema_conclusao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_protecao_especial_atendimento'


class TbProtocolo(models.Model):
    id_protocolo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tipo_doc = models.CharField(max_length=150, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    dias_resposta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prioridade = models.CharField(max_length=100, blank=True, null=True)
    assunto = models.CharField(max_length=255, blank=True, null=True)
    descricao_demanda = models.CharField(max_length=1000, blank=True, null=True)
    anexo = models.CharField(max_length=255, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    origem = models.CharField(max_length=255, blank=True, null=True)
    destino = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_protocolo'


class TbQuestionarioDemandaQualif(models.Model):
    id_form_demanda_qualif = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q_01_idade = models.CharField(max_length=1000, blank=True, null=True)
    q_02_genero = models.CharField(max_length=1000, blank=True, null=True)
    q_03_escolaridade = models.CharField(max_length=1000, blank=True, null=True)
    q_04_formacao = models.CharField(max_length=1000, blank=True, null=True)
    q_05_vinculo = models.CharField(max_length=1000, blank=True, null=True)
    q_06_carreira = models.CharField(max_length=1000, blank=True, null=True)
    q_07_ocupacao = models.CharField(max_length=1000, blank=True, null=True)
    q_08_id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q_09_tempo_atuacao_sedestmidh = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q_10_tempo_atuacao_serv_atual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q_11_frequenta_acao = models.CharField(max_length=1000, blank=True, null=True)
    q_12_frequenta_acao_contribui = models.CharField(max_length=1000, blank=True, null=True)
    q_13_disponivel_para_acoes = models.CharField(max_length=1000, blank=True, null=True)
    q_14_dificuld_nivel_tecnico = models.CharField(max_length=1000, blank=True, null=True)
    q_15_dificuld_nivel_gestao = models.CharField(max_length=1000, blank=True, null=True)
    q_16_dificuld_nivel_relacao = models.CharField(max_length=1000, blank=True, null=True)
    q_17_tema_1 = models.CharField(max_length=1000, blank=True, null=True)
    q_17_tema_2 = models.CharField(max_length=1000, blank=True, null=True)
    q_17_tema_3 = models.CharField(max_length=1000, blank=True, null=True)
    q_18_tema_1 = models.CharField(max_length=1000, blank=True, null=True)
    q_18_justificativa_1 = models.CharField(max_length=1000, blank=True, null=True)
    q_18_tema_2 = models.CharField(max_length=1000, blank=True, null=True)
    q_18_justificativa_2 = models.CharField(max_length=1000, blank=True, null=True)
    q_18_tema_3 = models.CharField(max_length=1000, blank=True, null=True)
    q_18_justificativa_3 = models.CharField(max_length=1000, blank=True, null=True)
    q_19_importancia_cargo_1 = models.CharField(max_length=1000, blank=True, null=True)
    q_19_importancia_cargo_2 = models.CharField(max_length=1000, blank=True, null=True)
    q_19_importancia_cargo_3 = models.CharField(max_length=1000, blank=True, null=True)
    q_19_importancia_cargo_4 = models.CharField(max_length=1000, blank=True, null=True)
    q_19_importancia_cargo_5 = models.CharField(max_length=1000, blank=True, null=True)
    q_19_importancia_cargo_6 = models.CharField(max_length=1000, blank=True, null=True)
    q_19_importancia_cargo_7 = models.CharField(max_length=1000, blank=True, null=True)
    q_19_importancia_cargo_8 = models.CharField(max_length=1000, blank=True, null=True)
    q_19_importancia_cargo_9 = models.CharField(max_length=1000, blank=True, null=True)
    q_19_importancia_cargo_10 = models.CharField(max_length=1000, blank=True, null=True)
    q_20_preferencia_modalidade = models.CharField(max_length=1000, blank=True, null=True)
    q_21_identidade_genero = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_questionario_demanda_qualif'


class TbRa(models.Model):
    id_ra = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_ra'


class TbRecado(models.Model):
    id_recado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_familia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mensagem = models.TextField(blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    recado_transmitido = models.CharField(max_length=1, blank=True, null=True)
    data_entrega = models.DateField(blank=True, null=True)
    id_usuario_entrega = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_recado'


class TbRedeApoio(models.Model):
    id_rede = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    parentesco = models.CharField(max_length=100, blank=True, null=True)
    escolaridade = models.CharField(max_length=50, blank=True, null=True)
    ocupacao = models.CharField(max_length=50, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_rede_apoio'


class TbRegistroRefeicao(models.Model):
    id_registro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_pessoa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_restaurante = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tipo_refeicao = models.CharField(max_length=50, blank=True, null=True)
    data_refeicao = models.DateField(blank=True, null=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    nis = models.CharField(max_length=20, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_registro_refeicao'


class TbRelEmpresaRestaurante(models.Model):
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    contrato = models.CharField(max_length=100, blank=True, null=True)
    id_empresa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_restaurante = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuarios_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_rel_empresa_restaurante'


class TbRelatoriosViews(models.Model):
    id_relatorios = models.AutoField(primary_key=True)
    nome_view = models.CharField(max_length=100, blank=True, null=True)
    nome_relatorio = models.CharField(max_length=200, blank=True, null=True)
    descricao_relatorio = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    permissoes = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_relatorios_views'


class TbRestaurante(models.Model):
    id_restaurante = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    localizacao = models.CharField(max_length=255, blank=True, null=True)
    datacadastro = models.DateField(blank=True, null=True)
    ativo = models.IntegerField(blank=True, null=True)
    coordenadas = models.CharField(max_length=40, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_restaurante'


class TbRestauranteCardapio(models.Model):
    data = models.CharField(db_column='DATA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    valor_calorico = models.CharField(max_length=20, blank=True, null=True)
    prato_proteico = models.CharField(max_length=200, blank=True, null=True)
    guarnicao = models.CharField(max_length=200, blank=True, null=True)
    salada = models.CharField(max_length=200, blank=True, null=True)
    acompanhamento = models.CharField(max_length=200, blank=True, null=True)
    sobremesa = models.CharField(max_length=200, blank=True, null=True)
    bebida = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_restaurante_cardapio'


class TbRestauranteCartao(models.Model):
    id_cartao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_restaurante = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    numero_cartao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tipo_refeicao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ativo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    utilizado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    reserva = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_extravio = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_restaurante_cartao'


class TbRestauranteRampa(models.Model):
    id_restaurante = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_restaurante_rampa'


class TbRestauranteTotais(models.Model):
    id_totais = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_restaurante = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    pessoas_refeicao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pessoas_marmita = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pessoas_refeicao_marmita = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pessoas_marmita_marmita = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pessoas_refeicao_tr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pessoas_marmita_tr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pessoas_refeicao_marmita_tr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pessoas_marmita_marmita_tr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pessoas_cafe_da_manha = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    leitura_inicial = models.CharField(max_length=10, blank=True, null=True)
    leitura_final = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_restaurante_totais'


class TbRestauranteUsuarioSistema(models.Model):
    id_restaurante = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_restaurante_usuario_sistema'


class TbScfv(models.Model):
    id_scfv = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade_origem = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade_referencia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade_scfv = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_responsavel = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    responsavel_outro = models.CharField(max_length=50, blank=True, null=True)
    telefone_responsavel = models.CharField(max_length=20, blank=True, null=True)
    dependente_atividades_diarias = models.CharField(max_length=20, blank=True, null=True)
    vivencia_situacoes = models.CharField(max_length=500, blank=True, null=True)
    vivencia_situacoes_outra = models.CharField(max_length=50, blank=True, null=True)
    turno_interesse = models.CharField(max_length=30, blank=True, null=True)
    necessita_transporte = models.CharField(max_length=20, blank=True, null=True)
    pontuacao = models.CharField(max_length=20, blank=True, null=True)
    data_solicitacao = models.DateField(blank=True, null=True)
    data_vinculo = models.DateField(blank=True, null=True)
    data_desligamento = models.DateField(blank=True, null=True)
    data_status = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    observacoes = models.CharField(max_length=500, blank=True, null=True)
    id_vaga = models.FloatField(blank=True, null=True)
    id_unidade_scfv_preferencia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_scfv'


class TbScfvSituacao(models.Model):
    id_situacao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    situacao = models.CharField(max_length=150, blank=True, null=True)
    pontuacao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ativo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_scfv_situacao'


class TbScfvStatus(models.Model):
    id_status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_scfv = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    motivo = models.CharField(max_length=400, blank=True, null=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_scfv_status'


class TbScfvUnidadeReferencia(models.Model):
    id_unidade_referencia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade_scfv = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_scfv_unidade_referencia'


class TbScfvVagas(models.Model):
    id_vaga = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    coletivo = models.CharField(max_length=50, blank=True, null=True)
    dias_semana = models.CharField(max_length=500, blank=True, null=True)
    turno = models.CharField(max_length=50, blank=True, null=True)
    qtd_vagas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    idadei = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    idadef = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ciclo_vida = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_scfv_vagas'


class TbSeasEncaminhamento(models.Model):
    id_encaminhamento = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    encaminhamento = models.CharField(max_length=200, blank=True, null=True)
    ativo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_seas_encaminhamento'


class TbServicoFunerario(models.Model):
    id_servico = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_pormorte = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    urna_mortuaria = models.CharField(max_length=20, blank=True, null=True)
    traslado = models.CharField(max_length=20, blank=True, null=True)
    util_capela = models.CharField(max_length=20, blank=True, null=True)
    cova_individual = models.CharField(max_length=20, blank=True, null=True)
    cova_coletiva = models.CharField(max_length=20, blank=True, null=True)
    placa_ident = models.CharField(max_length=20, blank=True, null=True)
    isencao_taxa = models.CharField(max_length=20, blank=True, null=True)
    outros_serv = models.CharField(max_length=20, blank=True, null=True)
    tamanho_urna = models.CharField(max_length=20, blank=True, null=True)
    local_inumacao = models.CharField(max_length=150, blank=True, null=True)
    local_retirada = models.CharField(max_length=150, blank=True, null=True)
    data_remocao = models.DateField(blank=True, null=True)
    hora_espera = models.CharField(max_length=6, blank=True, null=True)
    hora_sepultamento = models.CharField(max_length=6, blank=True, null=True)
    nome_motorista = models.CharField(max_length=50, blank=True, null=True)
    matricula_motorista = models.CharField(max_length=50, blank=True, null=True)
    aux_motorista = models.CharField(max_length=50, blank=True, null=True)
    matricula_aux = models.CharField(max_length=50, blank=True, null=True)
    agendado_com = models.CharField(max_length=50, blank=True, null=True)
    data_agenda = models.DateField(blank=True, null=True)
    hora_agenda = models.CharField(max_length=6, blank=True, null=True)
    codigo_agenda = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quadra_sepultura = models.CharField(max_length=20, blank=True, null=True)
    setor_sepultura = models.CharField(max_length=20, blank=True, null=True)
    sepultura = models.CharField(max_length=20, blank=True, null=True)
    corpo_recebido_por = models.CharField(max_length=50, blank=True, null=True)
    cpf_recebido = models.CharField(max_length=20, blank=True, null=True)
    hora_recebimento = models.CharField(max_length=6, blank=True, null=True)
    resp_retirada_urna = models.CharField(max_length=50, blank=True, null=True)
    rg_resp_retirada = models.CharField(max_length=20, blank=True, null=True)
    emissor_resp = models.CharField(max_length=10, blank=True, null=True)
    data_retirada_urna = models.DateField(blank=True, null=True)
    funeraria = models.CharField(max_length=50, blank=True, null=True)
    placa_veiculo = models.CharField(max_length=10, blank=True, null=True)
    foi_sepultado = models.CharField(max_length=5, blank=True, null=True)
    observacao = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_servico_funerario'


class TbServicosSocioAss(models.Model):
    id_servico = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_servicos_socio_ass'


class TbServidores(models.Model):
    id_servidor = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=150, blank=True, null=True)
    matricula = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_servidores'


class TbServidoresBancoDeLeite(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=128, blank=True, null=True)
    matricula = models.CharField(max_length=26, blank=True, null=True)
    unidade = models.CharField(max_length=26, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    senha = models.CharField(max_length=20, blank=True, null=True)
    ultimavisita = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_servidores_banco_de_leite'


class TbSinopseCras(models.Model):
    id_sinopse = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mes_referencia = models.DateField(blank=True, null=True)
    q1_1_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_22_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_22_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_22_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_22_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_22_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_22_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_22_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_22_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_22_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_22_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_22_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_22_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_22_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_23_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_23_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_23_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_23_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_23_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_23_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_23_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_23_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_23_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_23_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_23_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_23_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_23_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_24_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_24_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_24_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_24_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_24_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_24_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_24_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_24_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_24_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_24_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_24_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_24_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_24_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_25_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_25_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_25_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_25_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_25_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_25_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_25_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_25_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_25_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_25_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_25_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_25_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_25_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q2_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q2_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_17 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_18 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_19 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_20 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_21 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_22 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_23 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_1_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_1_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_1_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_1_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_1_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_1_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_1_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_1_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_1_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_1_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_1_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_1_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_2_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_2_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_2_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_2_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_2_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_2_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_2_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_2_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_2_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_2_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_2_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_2_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_3_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_3_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_3_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_3_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_3_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_3_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_3_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_3_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_3_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_3_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_3_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_3_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_4_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_4_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_4_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_4_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_4_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_4_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_4_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_4_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_4_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_4_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_4_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_4_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_5_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_5_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_5_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_5_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_5_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_5_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_5_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_5_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_5_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_5_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_5_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_5_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_6_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_6_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_6_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_6_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_6_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_6_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_6_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_6_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_6_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_6_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_6_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_6_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_7_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_7_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_7_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_7_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_7_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_7_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_7_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_7_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_7_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_7_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_7_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_7_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_8_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_8_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_8_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_8_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_8_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_8_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_8_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_8_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_8_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_8_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_8_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_8_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_9_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_9_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_9_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_9_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_9_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_9_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_9_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_9_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_9_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_9_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_9_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_9_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_10_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_10_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_10_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_10_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_10_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_10_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_10_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_10_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_10_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_10_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_10_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_10_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_11_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_11_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_11_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_11_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_11_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_11_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_11_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_11_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_11_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_11_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_11_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_11_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_12_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_12_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_12_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_12_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_12_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_12_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_12_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_12_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_12_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_12_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_12_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_12_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_13_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_13_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_13_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_13_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_13_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_13_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_13_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_13_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_13_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_13_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_13_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_13_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_14_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_14_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_14_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_14_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_14_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_14_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_14_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_14_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_14_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_14_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_14_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_14_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_15_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_15_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_15_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_15_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_15_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_15_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_15_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_15_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_15_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_15_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_15_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_15_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_16_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_16_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_16_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_16_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_16_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_16_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_16_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_16_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_16_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_16_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_16_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_16_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_17_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_17_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_17_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_17_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_17_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_17_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_17_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_17_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_17_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_17_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_17_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_17_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_18_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_18_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_18_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_18_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_18_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_18_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_18_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_18_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_18_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_18_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_18_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_18_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_19_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_19_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_19_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_19_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_19_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_19_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_19_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_19_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_19_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_19_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_19_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_19_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_20_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_20_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_20_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_20_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_20_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_20_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_20_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_20_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_20_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_20_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_20_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q7_20_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_17 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_18 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_19 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_20 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_21 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_22 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_23 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_24 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_25 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_26 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q10_27 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_sinopse_cras'


class TbSinopseCreas(models.Model):
    id_sinopse = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mes_referencia = models.DateField(blank=True, null=True)
    q1_1_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_1_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_2_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_3_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_4_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_5_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_6_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_7_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_8_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_9_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_10_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_11_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_12_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_13_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_14_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_15_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_16_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_17_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_18_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_19_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_20_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q1_21_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q2_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q2_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q2_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_3_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_3_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_17 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_18 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_19 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_20 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_21 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_22 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_23 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_24 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q4_25 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_3_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_3_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_17 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_18 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_19 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_20 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_21 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_22 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_23 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_24 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_25 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_26 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_27 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_28 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    q8_29 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_sinopse_creas'


class TbSolManutenBeneficio(models.Model):
    id_sol_manuten_beneficio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_block_cancel = models.DateField(blank=True, null=True)
    cad_unico_atualizado = models.CharField(max_length=3, blank=True, null=True)
    fam_atend_crit_pbf = models.CharField(max_length=3, blank=True, null=True)
    fam_vulneravel = models.CharField(max_length=3, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    unidade_origem = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    id_tipo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_motivo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sbenefpbf = models.CharField(max_length=3, blank=True, null=True)
    sacoubenef = models.CharField(max_length=3, blank=True, null=True)
    indicoper = models.CharField(max_length=3, blank=True, null=True)
    transfuf = models.CharField(max_length=3, blank=True, null=True)
    cartaopbf = models.CharField(max_length=3, blank=True, null=True)
    dataatuacadunico = models.DateField(blank=True, null=True)
    atendente = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_status = models.DateField(blank=True, null=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_sol_manuten_beneficio'


class TbStatusAtendManutBene(models.Model):
    id_status_atend_manut_bene = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_status_atend_manut_bene'


class TbSubFuncionalidades(models.Model):
    id_sub_funcionalidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=150, blank=True, null=True)
    id_funcionalidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    referencia = models.CharField(max_length=200, blank=True, null=True)
    oculto = models.CharField(max_length=1, blank=True, null=True)
    menu = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_sub_funcionalidades'


class TbSubFuncionalidadesPerfil(models.Model):
    id_perfil = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_sub_funcionalidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_sub_funcionalidades_perfil'


class TbTipoAcesso(models.Model):
    id_tipo_acesso = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tipo_acesso = models.CharField(max_length=300, blank=True, null=True)
    ativo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_tipo_acesso'


class TbTipoAcessoTipoUnidade(models.Model):
    id_tipo_acesso = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_tipo_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_tipo_acesso_tipo_unidade'


class TbTipoManutBenef(models.Model):
    id_tipo_manut_benef = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_tipo_manut_benef'


class TbTipoUnidade(models.Model):
    id_tipo_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_tipo_unidade'


class TbTramitacaoDoc(models.Model):
    id_tramitacao_doc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_protocolo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    providencia = models.CharField(max_length=200, blank=True, null=True)
    data = models.CharField(db_column='DATA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    destino_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    destino_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    origem_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    origem_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    obs_atendimento = models.CharField(max_length=255, blank=True, null=True)
    data_atendimento = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_tramitacao_doc'


class TbUf(models.Model):
    id_uf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    cep_inicial = models.CharField(max_length=8, blank=True, null=True)
    cep_final = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_uf'


class TbUnidades(models.Model):
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_ra = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=150, blank=True, null=True)
    id_tipo_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    endereco = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    ag_status = models.CharField(max_length=2, blank=True, null=True)
    ag_localidades_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_super_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sigla = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    imagem = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_unidades'


class TbUnidadesConveniadas(models.Model):
    id_unidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    endereco = models.CharField(max_length=500, blank=True, null=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_unidades_conveniadas'


class TbUnidadesVinculadas(models.Model):
    id_unidade_referencia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_unidade_vinculada = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_unidades_vinculadas'


class TbUsuarios(models.Model):
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_usuario_sistema = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_familia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nome = models.CharField(max_length=250, blank=True, null=True)
    nome_social = models.CharField(max_length=200, blank=True, null=True)
    estado_civil = models.CharField(max_length=30, blank=True, null=True)
    situacao_emprego = models.CharField(max_length=200, blank=True, null=True)
    rg = models.CharField(max_length=30, blank=True, null=True)
    emissor = models.CharField(max_length=50, blank=True, null=True)
    data_emissao = models.DateField(blank=True, null=True)
    nis = models.CharField(max_length=11, blank=True, null=True)
    titulo_eleitor = models.CharField(max_length=30, blank=True, null=True)
    ctps_serie = models.CharField(max_length=30, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=30, blank=True, null=True)
    nacionalidade = models.CharField(max_length=150, blank=True, null=True)
    cidade = models.CharField(max_length=200, blank=True, null=True)
    renda_pessoal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    telefone = models.CharField(max_length=30, blank=True, null=True)
    telefone_recado = models.CharField(max_length=30, blank=True, null=True)
    nome_mae = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    escolaridade = models.CharField(max_length=150, blank=True, null=True)
    portador_deficiencia = models.CharField(max_length=200, blank=True, null=True)
    doenca_grave_degen = models.CharField(max_length=200, blank=True, null=True)
    ocupacao = models.CharField(max_length=150, blank=True, null=True)
    data_cadastro = models.DateField(blank=True, null=True)
    nome_pai = models.CharField(max_length=150, blank=True, null=True)
    celular = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    outro_beneficio = models.CharField(max_length=150, blank=True, null=True)
    cpf = models.CharField(max_length=16, blank=True, null=True)
    mora_temp_df = models.CharField(max_length=40, blank=True, null=True)
    grau_parentesco = models.CharField(max_length=200, blank=True, null=True)
    cnh = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    observacao = models.CharField(max_length=2000, blank=True, null=True)
    nome_recado = models.CharField(max_length=250, blank=True, null=True)
    apelido = models.CharField(max_length=50, blank=True, null=True)
    idade_estimada = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    raca_cor = models.CharField(max_length=20, blank=True, null=True)
    ctps_numero = models.CharField(max_length=30, blank=True, null=True)
    ctps_orgao = models.CharField(max_length=50, blank=True, null=True)
    ctps_data_emissao = models.DateField(blank=True, null=True)
    categoria_deficiencia = models.CharField(max_length=200, blank=True, null=True)
    nome_doenca = models.CharField(max_length=100, blank=True, null=True)
    reside_df_desde = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cnh_validade = models.DateField(blank=True, null=True)
    data_atualizacao = models.DateField(blank=True, null=True)
    foto_url = models.CharField(max_length=200, blank=True, null=True)
    catador_reciclaveis = models.CharField(max_length=10, blank=True, null=True)
    vinculado_cooperativa = models.CharField(max_length=10, blank=True, null=True)
    nome_cooperativa = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_usuarios'


class TbUsuariosBf(models.Model):
    nom_pessoa = models.CharField(max_length=500, blank=True, null=True)
    num_nis_pessoa_atual = models.CharField(max_length=60, blank=True, null=True)
    nu_nis_original = models.CharField(max_length=60, blank=True, null=True)
    num_identidade_pessoa = models.CharField(max_length=60, blank=True, null=True)
    sig_orgao_emissor_pessoa = models.CharField(max_length=60, blank=True, null=True)
    sig_uf_ident_pessoa = models.CharField(max_length=60, blank=True, null=True)
    dta_emissao_ident_pessoa = models.CharField(max_length=60, blank=True, null=True)
    num_cpf_pessoa = models.CharField(max_length=60, blank=True, null=True)
    dta_nasc_pessoa = models.CharField(max_length=60, blank=True, null=True)
    cod_familiar_fam = models.CharField(max_length=60, blank=True, null=True)
    nom_localidade_fam = models.CharField(max_length=200, blank=True, null=True)
    nom_tip_logradouro_fam = models.CharField(max_length=100, blank=True, null=True)
    nom_titulo_logradouro_fam = models.CharField(max_length=100, blank=True, null=True)
    nom_logradouro_fam = models.CharField(max_length=100, blank=True, null=True)
    num_logradouro_fam = models.CharField(max_length=60, blank=True, null=True)
    des_complemento_fam = models.CharField(max_length=100, blank=True, null=True)
    des_complemento_adic_fam = models.CharField(max_length=100, blank=True, null=True)
    num_cep_logradouro_fam = models.CharField(max_length=60, blank=True, null=True)
    cod_unidade_territorial_fam = models.CharField(max_length=60, blank=True, null=True)
    nom_unidade_territorial_fam = models.CharField(max_length=60, blank=True, null=True)
    txt_referencia_local_fam = models.CharField(max_length=260, blank=True, null=True)
    id_pessoa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_usuarios_bf'


class TbUsuariosSistema(models.Model):
    id_usuario = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    login = models.CharField(db_column='LOGIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    senha = models.CharField(max_length=32, blank=True, null=True)
    data_criacao = models.DateField(blank=True, null=True)
    data_ultima_visita = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    id_servidor = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_perfil = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    termo_responsabilidade = models.CharField(max_length=20, blank=True, null=True)
    data_aceite = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_usuarios_sistema'


class TesteJoao(models.Model):
    id_teste = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=35, blank=True, null=True)
    email = models.CharField(max_length=35, blank=True, null=True)
    cidade = models.CharField(max_length=30, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teste_joao'


class VcDemandasOld(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=1, blank=True, null=True)
    usuario_s_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    unidade_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    demanda_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ref_nome = models.CharField(max_length=255, blank=True, null=True)
    ref_tel1 = models.CharField(max_length=15, blank=True, null=True)
    ref_tel2 = models.CharField(max_length=15, blank=True, null=True)
    ref_tel3 = models.CharField(max_length=15, blank=True, null=True)
    unidade_nome = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    observacoes = models.CharField(max_length=2000, blank=True, null=True)
    emergencial = models.CharField(max_length=1, blank=True, null=True)
    data_carga = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vc_demandas_old'
