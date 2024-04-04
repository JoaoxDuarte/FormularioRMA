class DadosPAIF:
    def __init__(self, total_de_familias_em_acompanhamento_PAIF: int, total_de_novas_familias_PAIF: int,
                 novas_familias_em_situacao_de_extrema_pobreza: int, novas_familias_bolsa_familia: int,
                 novas_familias_bolsa_familia_em_descomprimento: int, novas_familias_membros_bpc: int,
                 novas_familias_criancas_adolescentes_trabalho: int, novas_familias_criancas_adolescentes_acolhimento: int,
                 volume_convivencia_e_fortalecimento_de_vinculos):
        self.total_de_familias_em_acompanhamento_PAIF = total_de_familias_em_acompanhamento_PAIF
        self.total_de_novas_familias_PAIF = total_de_novas_familias_PAIF
        self.novas_familias_em_situacao_de_extrema_pobreza = novas_familias_em_situacao_de_extrema_pobreza
        self.novas_familias_bolsa_familia = novas_familias_bolsa_familia
        self.novas_familias_bolsa_familia_em_descomprimento = novas_familias_bolsa_familia_em_descomprimento
        self.novas_familias_membros_bpc = novas_familias_membros_bpc
        self.novas_familias_criancas_adolescentes_trabalho = novas_familias_criancas_adolescentes_trabalho
        self.novas_familias_criancas_adolescentes_acolhimento = novas_familias_criancas_adolescentes_acolhimento
        self.volume_convivencia_e_fortalecimento_de_vinculos = volume_convivencia_e_fortalecimento_de_vinculos

        if (total_de_familias_em_acompanhamento_PAIF < 0):
            raise Exception(
                'Total de famílias em acompanhamento não pode ser menor que 0!')

        if (total_de_novas_familias_PAIF > total_de_familias_em_acompanhamento_PAIF):
            raise Exception(
                'Novas famílias não podem ser maior que o total de famílias em acompanhamento!')

        if (novas_familias_em_situacao_de_extrema_pobreza > total_de_novas_familias_PAIF):
            raise Exception(
                'Novas famílias em situação de extrema pobreza não pode ser maior que total de novas famílias!')

        if (novas_familias_bolsa_familia > total_de_novas_familias_PAIF):
            raise Exception(
                'Novas famílias presentes no Bolsa Família não pode ser maior que novas famílias!')

        if (novas_familias_bolsa_familia_em_descomprimento > novas_familias_bolsa_familia):
            raise Exception(
                'Novas famílias presentes no Bolsa Família em DESCOMPRIMENTO não pode ser maior que novas famílias')

        if (novas_familias_membros_bpc > total_de_novas_familias_PAIF):
            raise Exception(
                'Novas famílias membros no BPC não pode ser maior que total de famílias')

        if (novas_familias_criancas_adolescentes_trabalho > total_de_novas_familias_PAIF):
            raise Exception(
                'Novas famílias com crianças e adolescentes trabalho não pode ser maior que o total de novas famílias')

        if (novas_familias_criancas_adolescentes_acolhimento > total_de_novas_familias_PAIF):
            raise Exception(
                'Novas famílias com crianças e adolescentes em acolhimento não pode ser maior que total de novas famílias')


@property
def total_de_familias_em_acompanhamento_PAIF(self):
    return self.total_de_familias_em_acompanhamento_PAIF


@total_de_familias_em_acompanhamento_PAIF.setter
def total_de_familias_em_acompanhamento_PAIF(self, value):

    if (value < 0):
        raise Exception("")
    self.total_de_familias_em_acompanhamento_PAIF = value


@property
def total_de_novas_familias_PAIF(self):
    return self.total_de_novas_familias_PAIF


@total_de_novas_familias_PAIF.setter
def total_de_novas_familias_PAIF(self, value):
    if (value < 0):
        raise Exception("")
    self.total_de_novas_familias_PAIF = value


@property
def novas_familias_em_situacao_de_extrema_pobreza(self):
    return self.novas_familias_em_situacao_de_extrema_pobreza


@novas_familias_em_situacao_de_extrema_pobreza.setter
def novas_familias_em_situacao_de_extrema_pobreza(self, value):
    if (value < 0):
        raise Exception("")
    self.novas_familias_em_situacao_de_extrema_pobreza = value


@property
def novas_familias_bolsa_familia(self):
    return self.novas_familias_bolsa_familia


@novas_familias_bolsa_familia.setter
def novas_familias_bolsa_familia(self, value):
    if (value < 0):
        raise Exception("")
    self.novas_familias_bolsa_familia = value


@property
def novas_familias_bolsa_familia_em_descomprimento(self):
    return self.novas_familias_bolsa_familia_em_descomprimento


@novas_familias_bolsa_familia_em_descomprimento.setter
def novas_familias_bolsa_familia_em_descomprimento(self, value):
    if (value < 0):
        raise Exception("")
    self.novas_familias_bolsa_familia_em_descomprimento = value


@property
def novas_familias_membros_bpc(self):
    return self.novas_familias_membros_bpc


@novas_familias_membros_bpc.setter
def novas_familias_membros_bpc(self, value):
    if (value < 0):
        raise Exception("")
    self.novas_familias_membros_bpc = value


@property
def novas_familias_criancas_adolescentes_trabalho(self):
    return novas_familias_criancas_adolescentes_trabalho


@novas_familias_criancas_adolescentes_trabalho.setter
def novas_familias_criancas_adolescentes_trabalho(self, value):
    if (value < 0):
        raise Exception("")
    self.novas_familias_criancas_adolescentes_trabalho = value


@property
def novas_familias_criancas_adolescentes_acolhimento(self):
    return novas_familias_criancas_adolescentes_acolhimento


@novas_familias_criancas_adolescentes_acolhimento.setter
def novas_familias_criancas_adolescentes_acolhimento(self, value):
    if (value < 0):
        raise Exception("")
    self.novas_familias_criancas_adolescentes_acolhimento = value


@property
def volume_convivencia_e_fortalecimento_de_vinculos(self):
    return volume_convivencia_e_fortalecimento_de_vinculos


@volume_convivencia_e_fortalecimento_de_vinculos.setter
def volume_convivencia_e_fortalecimento_de_vinculos(self, value):
    if (value < 0):
        raise Exception("")
    self.volume_convivencia_e_fortalecimento_de_vinculos = value
