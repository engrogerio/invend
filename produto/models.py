#_*_ coding: utf-8 _*_

from django.db import models
from business_unit.models import BusinessUnitSpecificModel

class Produto (BusinessUnitSpecificModel):
    codigo = models.CharField('Código', default ='000', max_length=10)
    descricao = models.CharField('Descrição', default = 'Produto', max_length=100)
    preco_unit = models.DecimalField('Preço Unitário',max_digits= 9, decimal_places = 2, default = 1)

    def __unicode__(self):
        return self.descricao or u''