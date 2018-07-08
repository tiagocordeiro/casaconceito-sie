from django.contrib import admin
from .models import Indicacao


class IndicacaoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'valor', 'data_criacao', 'corretor',)
    # list_filter = ('cliente', 'data_criacao', 'corretor',)
    search_fields = ('cliente', 'corretor',)
    # fieldsets = [(None, {'fields': [('cliente', 'descricao', 'valor')]})]
    readonly_fields = ["corretor"]

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('valor')  # here!
            self.exclude.append('data_criacao')
            self.exclude.append('corretor')
        return super(IndicacaoAdmin, self).get_form(request, obj, **kwargs)

    def get_list_filter(self, request):
        if request.user.is_superuser:
            return ('cliente', 'data_criacao', 'corretor',)
        else:
            return ('cliente',)

    def get_queryset(self, request):
        qs = super(IndicacaoAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(corretor=request.user)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'corretor', None) is None:
            obj.corretor = request.user
        obj.save()


admin.site.register(Indicacao, IndicacaoAdmin)