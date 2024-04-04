class VolumeAtendimentoParticularizado:
    def __init__(self, _total_atendimento_particularizado_mes: int,
                 _familias_encaminhadas_inclusao_cadunico_mes: int,
                 _familias_encaminhadas_atualizacao_cadunico_mes: int,
                 _individuos_encaminhados_para_bpc: int,
                 _familias_encaminhadas_para_creas: int,
                 _visitas_domiciliares_realizadas: int,
                 _total_auxilio_natalidade_concedido: int,
                 _total_auxilio_funeral_concedido: int,
                 _outros_beneficios_concedidos: int):
        self._total_atendimento_particularizado_mes = _total_atendimento_particularizado_mes
        self._familias_encaminhadas_inclusao_cadunico_mes = _familias_encaminhadas_inclusao_cadunico_mes
        self._familias_encaminhadas_atualizacao_cadunico_mes = _familias_encaminhadas_atualizacao_cadunico_mes
        self._individuos_encaminhados_para_bpc = _individuos_encaminhados_para_bpc
        self._familias_encaminhadas_para_creas = _familias_encaminhadas_para_creas
        self._visitas_domiciliares_realizadas = _visitas_domiciliares_realizadas
        self._total_auxilio_natalidade_concedido = _total_auxilio_natalidade_concedido
        self._total_auxilio_funeral_concedido = _total_auxilio_funeral_concedido
        self._outros_beneficios_concedidos = _outros_beneficios_concedidos

        if (self._total_atendimento_particularizado_mes < 0 or
                self._familias_encaminhadas_inclusao_cadunico_mes < 0 or
                self._familias_encaminhadas_atualizacao_cadunico_mes < 0 or
                self._individuos_encaminhados_para_bpc < 0 or
                self._familias_encaminhadas_para_creas < 0 or
                self._visitas_domiciliares_realizadas < 0 or
                self._total_auxilio_natalidade_concedido < 0 or
                self._total_auxilio_funeral_concedido < 0 or
                self._outros_beneficios_concedidos < 0):
            raise ValueError("Nenhum valor deve ser negativo.")

        if _familias_encaminhadas_inclusao_cadunico_mes + _familias_encaminhadas_atualizacao_cadunico_mes > _total_atendimento_particularizado_mes:
            raise ValueError(
                "Erro. A inclusão e atualização de famílias encaminhadas com CadUnico não pode ser menor que a soma.")

        if _individuos_encaminhados_para_bpc > _total_atendimento_particularizado_mes:
            raise ValueError(
                "Erro. O número total de atendimentos deve ser maior comparado aos indivíduos encaminhados ao BPC.")

        if _familias_encaminhadas_para_creas > _total_atendimento_particularizado_mes:
            raise ValueError(
                "Erro. O número total de atendimentos deve ser maior comparado as famílias encaminhadas ao CREAS. ")

        if _visitas_domiciliares_realizadas > _total_atendimento_particularizado_mes:
            raise ValueError(
                "Erro. O número total de atendimentos deve ser maior comparado as visitas domiciliares realizadas.")

        if _total_auxilio_natalidade_concedido > _total_atendimento_particularizado_mes:
            raise ValueError(
                "Erro. O número total de atendimentos deve ser maior comparado ao total de auxílio natalidade concedido.")

        if _total_auxilio_funeral_concedido > _total_atendimento_particularizado_mes:
            raise ValueError(
                "Erro. O número total de atendimentos deve ser maior comparado ao total de auxílio funeral concedido.")

        if _outros_beneficios_concedidos > _total_atendimento_particularizado_mes:
            raise ValueError(
                "Erro. O número total de atendimentos deve ser maior comparado aos outros benefícios concedidos.")

    @property
    def total_atendimento_particularizado_mes(self):
        return self._total_atendimento_particularizado_mes

    @total_atendimento_particularizado_mes.setter
    def total_atendimento_particularizado_mes(self, value):
        raise Exception("Não é possível modificar uma entidade instanciada")

    @property
    def familias_encaminhadas_inclusao_cadunico_mes(self):
        return self._familias_encaminhadas_inclusao_cadunico_mes

    @familias_encaminhadas_inclusao_cadunico_mes.setter
    def familias_encaminhadas_inclusao_cadunico_mes(self, value):
        raise Exception("Não é possível modificar uma entidade instanciada")

    @property
    def familias_encaminhadas_atualizacao_cadunico_mes(self):
        return self._familias_encaminhadas_atualizacao_cadunico_mes

    @familias_encaminhadas_atualizacao_cadunico_mes.setter
    def familias_encaminhadas_atualizacao_cadunico_mes(self, value):
        raise Exception("Não é possível modificar uma entidade instanciada")

    @property
    def individuos_encaminhados_para_bpc(self):
        return self._individuos_encaminhados_para_bpc

    @individuos_encaminhados_para_bpc.setter
    def individuos_encaminhados_para_bpc(self, value):
        raise Exception("Não é possível modificar uma entidade instanciada")

    @property
    def familias_encaminhadas_para_creas(self):
        return self._familias_encaminhadas_para_creas

    @familias_encaminhadas_para_creas.setter
    def familias_encaminhadas_para_creas(self, value):
        raise Exception("Não é possível modificar uma entidade instanciada")

    @property
    def visitas_domiliciares_realizadas(self):
        return self._visitas_domiciliares_realizadas

    @visitas_domiliciares_realizadas.setter
    def visitas_domiciliares_realizadas(self, value):
        raise Exception("Não é possível modificar uma entidade instanciada")

    @property
    def total_auxilio_natalidade_concedido(self):
        return self._total_auxilio_natalidade_concedido

    @total_auxilio_natalidade_concedido.setter
    def total_auxilio_natalidade_concedido(self, value):
        raise Exception("Não é possível modificar uma entidade instanciada")

    @property
    def total_auxilio_funeral_concedido(self):
        return self._total_auxilio_funeral_concedido

    @total_auxilio_funeral_concedido.setter
    def total_auxilio_funeral_concedido(self, value):
        raise Exception("Não é possível modificar uma entidade instanciada")

    @property
    def outros_beneficios_concedidos(self):
        return self._outros_beneficios_concedidos

    @outros_beneficios_concedidos.setter
    def outros_beneficios_concedidos(self, value):
        raise Exception("Não é possível modificar uma entidade instanciada")
