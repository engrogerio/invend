#_*_ coding: utf-8 _*_

from django.db import models
from business_unit.models import BusinessUnitSpecificModel

# Create your models here.
class Cliente(BusinessUnitSpecificModel):
    nome=models.CharField('Nome', max_length=60, default='Cliente Nome')
    endereco = models.CharField('Endereço', max_length=200, blank = True)
    telefone = models.CharField('Telefone', max_length=20,  blank = True)
    celular = models.CharField('Celular', max_length=20,  blank = True, )
    cpf = models.CharField('CPF', max_length=15, blank = True)

    def __unicode__(self):
        return self.nome or u''