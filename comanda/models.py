#_*_ coding: utf-8 _*_

from business_unit.models import BusinessUnitSpecificModel
from cliente.models import Cliente
from produto.models import Produto
from django.db import models
# Create your models here.


class Comanda(BusinessUnitSpecificModel):


    DINHEIRO = 1
    CARTAO_DEBITO = 2
    CARTAO_CREDITO = 3
    CHEQUE = 4
    CARTEIRA = 5

    FORMA_PAGTO = (
    (DINHEIRO, 'Dinheiro') ,
    (CARTAO_DEBITO, 'Cartão débito') ,
    (CARTAO_CREDITO, 'Cartão crédito'),
    (CHEQUE, 'Cheque'),
    (CARTEIRA, 'Carteira'),
    )


    ABERTO=1
    ENCERRADO=2
    EXCLUIDO=3

    STATUS = (
    (ABERTO, 'Aberto'),
    (ENCERRADO, 'Encerrado'),
    (EXCLUIDO, 'Excluido'),
    )

    numero = models.CharField('Numero', max_length=5, default ='00000')
    cliente = models.ForeignKey(Cliente, null=True)
    status = models.IntegerField('Status da Comanda', choices=STATUS, default = ABERTO)
    metodo_pagto = models.IntegerField('Metodo de Pagamento', choices=FORMA_PAGTO, default= DINHEIRO)

    def __unicode__(self):
        return self.numero or u''



class Item(models.Model):


    def _get_total_item(self):
        total_item = self.produto.preco_unit * self.quantidade
        return total_item

    def _get_preco_unit(self):
        preco_item = self.produto.preco_unit
        return preco_item

    comanda = models.ForeignKey(Comanda, default=1)
    produto = models.ForeignKey(Produto, default=1)
    quantidade = models.DecimalField('Quantidade', max_digits= 6, decimal_places = 3,default = 0)
    preco_unit = models.DecimalField('Preço Unitário (R$)', max_digits= 6, decimal_places = 2,default = 0)
    total_item = models.DecimalField('Total (R$)', max_digits= 6, decimal_places = 2,default = 0)

    def __unicode__(self):
        return self.produto.descricao or u''

    def save(self):
        self.total_item = self._get_total_item()
        self.preco_unit = self._get_preco_unit()
        super(Item, self).save()