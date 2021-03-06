# -*- coding: utf-8 -*-

from django.contrib.contenttypes.models import ContentType
from django.contrib import admin
from django import forms


class InventModelAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_max_show_all = 5000


    def has_change_permission(self, request, obj=None):
        ct = ContentType.objects.get_for_model(self.model)
        saida = False
        if request.user.is_superuser:
            saida = True
        else:
             if request.user.has_perm('%s.view_%s' % (ct.app_label, ct.model)):
                saida = True
             else:
                if request.user.has_perm('%s.change_%s' % (ct.app_label, ct.model)):
                    saida = True
                else:
                    saida = False

        return saida

    def get_readonly_fields(self, request, obj=None):
        ct = ContentType.objects.get_for_model(self.model)
        if not request.user.is_superuser and request.user.has_perm('%s.view_%s' % (ct.app_label, ct.model)):
            readonly = list(self.readonly_fields) + [el.name for el in self.model._meta.fields]
            readonly.remove('business_unit')
            return readonly
        else:
            return self.readonly_fields



#Thanks http://www.ibm.com/developerworks/library/os-django-admin/
    """
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'business_unit', None) is None:
            user = User.objects.get(username=request.user)
            obj.business_unit = user.user_business_unit.business_unit
        obj.save()
    """
    def get_queryset(self, request):
        self.user = request.user
        qs = super(InventModelAdmin, self).get_queryset(request)
        #if request.user.is_superuser:
        #   return qs
        return qs.filter(business_unit=self.user.user_business_unit.business_unit)

    def get_form(self, request, obj=None, **kwargs):
        form = super(InventModelAdmin, self).get_form(request, obj, **kwargs)
        form.user = request.user
        return form

class InventFormAdmin(forms.ModelForm):
    """
        Bring to a form, an invisible business_unit foreign key widget with the unit name already, based on current user logged.
        All Forms specific for a business_unit must extend this form.
    """
    #class Meta:
    #    pass

    def __init__(self, *args, **kwds):
        #Defines initial value for the business_unit
        initial = kwds.get('initial', {})
        initial['business_unit']=self.user.user_business_unit.business_unit
        kwds['initial']=initial
        super(InventFormAdmin, self).__init__(*args, **kwds)
        #self.fields['business_unit'].widget.attrs['readonly'] = True
        #TODO:Admin users should be able to see and change the BusinessUnit of an entity?
        self.fields['business_unit'].widget = forms.HiddenInput()
        try:
            self.unit_name = self.user.user_business_unit.business_unit.unit
        except:
            self.unit_name ='' #TODO: Implementar erro quando não traz o nome da unidade