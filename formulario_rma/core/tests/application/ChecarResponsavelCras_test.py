import pytest
from formulario_rma.core.domain.exceptions.ResponsavelNaoEGerenteException import ResponsavelNaoEGerenteException

from formulario_rma.core.domain.exceptions.ResponsavelNaoSeEcontraLotadoNoCrasException import ResponsavelNaoSeEncontraLotadoNoCrasException
from ...domain.entities.responsavelCras import ResponsavelCras
from ...domain.repositories.ResponsavelCrasRepository import ResponsavelCrasRepository
from ...application.use_cases.ChecarResponsavelCras import ChecarResponsavelCras


class MockResponsavelCrasRepositoryGerente (ResponsavelCrasRepository):
    def recuperar_responsavel_cras(self, login: str) -> ResponsavelCras:
        return ResponsavelCras(
            'FAKE',
            '015478',
            "GERENTE DE TUDO",
            "fake.user@sedes.df.gov.br",
            4
        )


class MockResponsavelCrasRepositoryNaoGerente (ResponsavelCrasRepository):
    def recuperar_responsavel_cras(self, login: str) -> ResponsavelCras:
        return ResponsavelCras(
            'FAKE',
            '015478',
            "TECNICO",
            "fake.user@sedes.df.gov.br",
            4
        )


def test_if_id_cras_is_validated():
    caso_de_uso = ChecarResponsavelCras(MockResponsavelCrasRepositoryGerente())
    with pytest.raises(ResponsavelNaoSeEncontraLotadoNoCrasException):
        caso_de_uso.run('', 2)


def test_if_cargo_is_gerente():
    caso_de_uso = ChecarResponsavelCras(
        MockResponsavelCrasRepositoryNaoGerente())
    with pytest.raises(ResponsavelNaoEGerenteException):
        caso_de_uso.run('', 4)


def test_can_be_called():
    caso_de_uso = ChecarResponsavelCras(MockResponsavelCrasRepositoryGerente())
    caso_de_uso.run('', 4)
