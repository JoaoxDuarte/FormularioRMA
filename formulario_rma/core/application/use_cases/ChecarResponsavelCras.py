
from ...domain.exceptions.ResponsavelNaoEGerenteException import ResponsavelNaoEGerenteException
from ...domain.exceptions.ResponsavelNaoSeEcontraLotadoNoCrasException import ResponsavelNaoSeEncontraLotadoNoCrasException
from ...domain.repositories.ResponsavelCrasRepository import ResponsavelCrasRepository

'''
Este cado de uso chega se o responsável CRAS é gerente e está lotado no CRAS de interesse.
'''


class ChecarResponsavelCras:
    def __init__(self, responsavel_cras_repository: ResponsavelCrasRepository):
        self.responsavel_cras_repository = responsavel_cras_repository

    def run(self, login: str, id_cras: int):
        # Recuperação de dados (entidades)
        responsavel_cras = self.responsavel_cras_repository.recuperar_responsavel_cras(
            login)

        # Regras de aplicação
        # Validar CRAS
        if (responsavel_cras.id_unidade != id_cras):
            raise ResponsavelNaoSeEncontraLotadoNoCrasException()

        # Validar CARGO
        if ('GERENTE' not in responsavel_cras.cargo):
            raise ResponsavelNaoEGerenteException()
        return responsavel_cras