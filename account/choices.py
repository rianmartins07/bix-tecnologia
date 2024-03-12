from django.db import models

class Sexo (models.TextChoices):
    MASCULINO = 'Masculino'
    FEMININO = 'Feminino'
    PREFIRO_NAO_DIZER = 'Prefiro não dizer'
    
