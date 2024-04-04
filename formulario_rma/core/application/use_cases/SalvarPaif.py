from formulario_rma.core.domain.entities.DadosPAIF import DadosPAIF
from formulario_rma.core.domain.repositories.DadosPAIF_repository import DadosPAIFRepository


class SalvarPaif:
    def __init__(self, salvar_paif: DadosPAIFRepository):
        self.salvar_paif = salvar_paif

    def run(self,dados_paif: DadosPAIF):
        return self.salvar_paif.criar_dados_familia_PAIF(dados_paif)
