from main_app.models import DadosPaifModel
from ...domain.entities.DadosPAIF import DadosPAIF
from ...domain.repositories.DadosPAIF_repository import DadosPAIFRepository


class DadosPaifRepositoryImpl (DadosPAIFRepository):
    def recuperar_dados_familia_PAIF(self,dados_paif_id: int) -> DadosPAIF:
        model = DadosPaifModel.objects.filter(id=dados_paif_id).first() #.first() faz a mesma coisa que [0]
        
        dados_paif_args = DadosPAIF.__init__.__code__.co_varnames
        modelAgs = [f.name for f in DadosPaifModel._meta.get_fields()]
        arg_values = {el:getattr(model, el) for el in modelAgs if el in dados_paif_args and not el == 'self'}
        return DadosPAIF(**arg_values)
        
    def criar_dados_familia_PAIF(self,dados_paif: DadosPAIF) -> DadosPAIF:
        model = DadosPaifModel(
            **dados_paif.__dict__
        )
        try:
            model.save()
            return True
        except:
            return False
