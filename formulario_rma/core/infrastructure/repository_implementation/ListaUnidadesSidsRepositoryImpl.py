from ...domain.entities.Unidade import Unidade
from ...domain.repositories.ListaUnidades_repository import ListaUnidadesRepository
from ast import List
from sids_app.models import UNIDADES


class ListaUnidadesRepositoryImpl(ListaUnidadesRepository):

    def recuperar_unidades_cras(self) -> List(Unidade):
        result_unidades = UNIDADES.objects.using(
            'SIDS').filter(id_tipo_unidade=1).exclude(nome='EQUIPE DE PROTEÇÃO SOCIAL MÓVEL').exclude(nome='RECANTO DAS EMAS II').exclude(nome='SOL NASCENTE').exclude(nome='SUGIP')

        unidades = []
        for result_unidade in result_unidades:
            unidade = Unidade(
                result_unidade.id_unidade,
                result_unidade.nome,
                result_unidade.id_tipo_unidade,
                result_unidade.endereco
            )
            unidades.append(unidade)

        return unidades

    def recuperar_unidades_centro_pop(self) -> List(Unidade):
        result_unidades = UNIDADES.objects.using(
            'SIDS').filter(id_tipo_unidade=5)

        unidades = []
        for result_unidade in result_unidades:
            unidade = Unidade(
                result_unidade.id_unidade,
                result_unidade.nome,
                result_unidade.id_tipo_unidade,
                result_unidade.endereco
            )
            unidades.append(unidade)

        return unidades

    def recuperar_unidades_creas(self) -> List(Unidade):
        result_unidades = UNIDADES.objects.using(
            'SIDS').filter(id_tipo_unidade=3).exclude(nome='BRASÍLIA / NAI-UAI').exclude(nome='Unidade de Tecnologia').exclude(nome='SÃO SEBASTIÃO').exclude(nome='IMIGRANTES')

        unidades = []
        for result_unidade in result_unidades:
            unidade = Unidade(
                result_unidade.id_unidade,
                result_unidade.nome,
                result_unidade.id_tipo_unidade,
                result_unidade.endereco
            )
            unidades.append(unidade)

        return unidades
