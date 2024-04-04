import pytest
from ....domain.entities.responsavelCras import ResponsavelCras


def test_email_funcional_dont_accept_more_than_one_at_sign():
    with pytest.raises(Exception):
        ResponsavelCras('Nome', 1, 'Cargo', 'Outlook@@sedes.df.gov.br')


def test_email_funcional_dont_accept_other_email_funcional():
    with pytest.raises(Exception):
        ResponsavelCras('Nome', 1, 'Cargo', 'Sedes@gmail.com')


def test_email_funcional_dont_accept_null():
    with pytest.raises(Exception):
        ResponsavelCras('Nome', 1, 'Cargo', ' ')


def test_nome_dont_accept_null():
    with pytest.raises(Exception):
        ResponsavelCras('', 1, 'Outlook@sedes.df.gov.br')


def test_matricula_dont_accept_zero():
    with pytest.raises(Exception):
        ResponsavelCras('Nome', 0, 'Outlook@sedes.df.gov.br')

def test_cargo_dont_accept_nul():
    with pytest.raises(Exception):
        ResponsavelCras('Nome', 1, ' ', 'Outlook@sedes.df.gov.br')
