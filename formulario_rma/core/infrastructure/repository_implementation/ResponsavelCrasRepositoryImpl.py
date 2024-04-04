from core.domain.repositories.ResponsavelCrasRepository import ResponsavelCrasRepository
from main_app.models import DadosCrasModel, ResponsavelModel
from ...domain.entities.responsavelCras import ResponsavelCras

class ResponsavelCrasRepositoryImpl (ResponsavelCrasRepository):
    def recuperar_responsavel_cras(self, login: str):

        model = ResponsavelModel.objects.filter(email_funcional=f'{login}.sedes.df.gov.br').first() #.first() faz a mesma coisa que [0]

        model_responsavel_args = ResponsavelCras.__init__.__code__.co_varnames
        modelAgs = [f.name for f in ResponsavelModel._meta.get_fields()]
        arg_values = {el:getattr(model, el) for el in modelAgs if el in model_responsavel_args and not el == 'self'}

        return ResponsavelCras(**arg_values)

    def confirmar_se_responsavel_esta_autorizado_no_cras(self,email_funcional: str, cras: str):

        try:
            responsavel_cras_model = ResponsavelModel.objects.filter(email_funcional=email_funcional).first()
            dados_cras_model = DadosCrasModel.objects.filter(responsavel_cras=responsavel_cras_model,nome_cras=cras).first()       
            if(dados_cras_model.responsavel_cras == responsavel_cras_model):
                return True
            else:
                return False
        except:
            return False
