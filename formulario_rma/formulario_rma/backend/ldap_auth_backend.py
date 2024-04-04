from django.contrib.auth.backends import BaseBackend
from ldap3 import Server, Connection, ALL
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend


class MyBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        print("_____________________________________________________________________________________")
        # define the server
        s = Server('sedest.gdfnet.df', get_info=ALL)  # define an unsecure LDAP server, requesting info on DSE and schema

        print("Chamando")
        # define the connection
        c = Connection(s, user=username, password=password)
        if c.bind():
            user = User(username=username, password=password)
            user.save()
            return user
        else:
            return None