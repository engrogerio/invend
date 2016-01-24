# -*- coding: utf-8 -*-
from django.contrib import admin
from comanda.models import Comanda,Item
from restaurante.admin import InventFormAdmin, InventModelAdmin
from django.forms.models import ModelForm
from django.db import models
from django.forms import TextInput, Textarea
from django.contrib import messages

class ComandaAdminForm(InventFormAdmin):

    class Meta:
        model = Comanda
        fields = "__all__"
    def __init__(self, *args, **kwds):
        super(ComandaAdminForm, self).__init__(*args, **kwds)
        try:
            self.unit_name = self.user.user_business_unit.business_unit.unit
        except:
            print('Não existe')
        try:
            pass
            #self.fields['funcionario'].queryset = Funcionario.objects.filter(ativo=True).filter(business_unit__unit=self.unit_name).order_by('nome')
            #self.fields['permissao'].queryset = Permissao.objects.filter(funcionario=self.instance.funcionario).filter(Q(validade__gte =datetime.date.today())| Q(definitiva=True)).order_by('permissao_especial')
        except:
            pass

class AlwaysChangedModelForm(ModelForm):
    def has_changed(self):
        """ Should returns True if data differs from initial.
        By always returning true even unchanged inlines will get validated and saved."""
        return True


class ComandaInline(admin.TabularInline):
    extra = 0
    model = Item
    form = AlwaysChangedModelForm

class ComandaAdmin(InventModelAdmin):

    form = ComandaAdminForm
    #list_filter = (StatusListFilter,EventoTipoListFilter)
    fieldsets = (
        ('COMANDA', {
            'fields':(('business_unit'),('cliente','status','metodo_pagto')),
        }),
    )

    inlines = [ComandaInline]

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':100})},
    }

    def save_model(self, request, obj, form, change):
        """for getting rid of messages"""
        messages.set_level(request, messages.ERROR)
        obj.user = request.user
        obj.save()

# Register your models here.
admin.site.register(Comanda, ComandaAdmin)