import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone
# Create your models here.
# TB_USUARIOS_SISTEMA
# TB_SERVIDORES


class USUARIOS_SISTEMA(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    LOGIN = models.CharField(max_length=50)
    senha = models.CharField(max_length=32)
    data_criacao = models.DateField()
    data_ultima_visita = models.CharField(max_length=20)
    status = models.CharField(max_length=1)
    id_servidor = models.IntegerField()
    id_perfil = models.IntegerField()
    termo_responsabilidade = models.CharField(max_length=20)
    data_aceite = models.CharField(max_length=20)

    class Meta:
        db_table = 'tb_usuarios_sistema'


class SERVIDORES(models.Model):
    id_servidor = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150)
    matricula = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    id_unidade = models.IntegerField()

    class Meta:
        db_table = 'tb_servidores'


class PERFIL(models.Model):
    id_perfil = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150)

    class Meta:
        db_table = 'tb_perfil'


class UNIDADES(models.Model):
    id_unidade = models.IntegerField(primary_key=True)
    id_tipo_unidade = models.IntegerField()
    id_ra = models.IntegerField
    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=150)
    status = models.CharField(max_length=20)
    ag_status = models.CharField(max_length=2)
    ag_localidades_id = models.IntegerField
    id_super_unidades = models.IntegerField
    sigla = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    imagem = models.CharField(max_length=200)

    class Meta:
        db_table = 'tb_unidades'
