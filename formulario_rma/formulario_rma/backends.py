from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from ldap3 import Server, Connection, ALL


class MyBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        print("_____________________________________________________________________________________")
        print("Chamando")
        # define the server
        # define an unsecure LDAP server, requesting info on DSE and schema
        # comando para aceitar o log mesmo sem o @sedes.df.gov.br
        if "@sedes.df.gov.br" not in username:
            username+="@sedes.df.gov.br"

        s = Server('sedest.gdfnet.df', get_info=ALL)

        # define the connection
        c = Connection(s, user=username, password=password)
        if not c.bind():
            print('login failed')
            return None

        user_model = get_user_model()
        try:
            user = user_model.objects.get(username=username)
            print("got user from database")
        except user_model.DoesNotExist:
            print("Creating new user")
            user, flag = user_model.objects.update_or_create(username=username)

        return user

    def get_user(self, user_id: int):
        user_model = get_user_model()
        print("---------------------------------USER--------------------------")
        print(user_id)
        user = user_model.objects.get(id=user_id)
        print(user)
        return user
