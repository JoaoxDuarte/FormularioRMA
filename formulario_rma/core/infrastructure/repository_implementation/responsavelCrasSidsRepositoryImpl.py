

from sids_app.models import PERFIL
from ...domain.entities.responsavelCras import ResponsavelCras
from ...domain.repositories.ResponsavelCrasRepository import ResponsavelCrasRepository
# from ....sids_app.models import USUARIOS_SISTEMA
from sids_app.models import USUARIOS_SISTEMA, SERVIDORES


class ResponsavelCrasSidsRepositoryImpl(ResponsavelCrasRepository):

    def recuperar_responsavel_cras(self, login: str):
        result = USUARIOS_SISTEMA.objects.using(
            'SIDS').filter(LOGIN=login)
        assert (len(result) == 1)

        dados_usuario = result[0]
        result_servidor = SERVIDORES.objects.using('SIDS').filter(
            id_servidor=dados_usuario.id_servidor)
        assert (len(result_servidor) == 1)
        dados_servidor = result_servidor[0]

        result_perfil = PERFIL.objects.using('SIDS').filter(
            id_perfil=dados_usuario.id_perfil)[0]

        responsavel_cras = ResponsavelCras(
            dados_servidor.nome,
            dados_servidor.matricula,
            result_perfil.nome,
            dados_servidor.email,
            dados_servidor.id_unidade
        )
        return responsavel_cras

    def confirmar_se_responsavel_esta_autorizado_no_cras(self, login: str, cras: int):
        responsavel_cras = self.recuperar_responsavel_cras(login)
        return responsavel_cras.id_unidade == cras
