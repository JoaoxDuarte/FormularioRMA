from core.domain.repositories.dadosCras_repository import DadosCrasRepository


class RecuperarDadosCras:
    def __init__(self, dados_cras: DadosCrasRepository):
        self.dados_cras = dados_cras

    def run(self, id_cras: int, mes_referencia:str):
        return self.dados_cras.recuperar_dados_cras_por_id_cras(id_cras, mes_referencia)
