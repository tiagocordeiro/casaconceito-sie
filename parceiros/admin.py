from django.contrib import admin
from .models import Indicacao


class IndicacaoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'valor', 'data_criacao', 'added_by', 'status')
    # list_filter = ('cliente', 'data_criacao', 'added_by',)
    search_fields = ('cliente', 'added_by',)
    # fieldsets = [(None, {'fields': [('cliente', 'descricao', 'valor')]})]

    def get_list_display(self, request):
        if request.user.is_superuser:
            return ('cliente', 'valor', 'data_criacao', 'added_by', 'status')
        else:
            return ('cliente', 'valor', 'data_criacao', 'status')

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            self.readonly_fields = ["added_by"]
        else:
            self.readonly_fields = ["added_by", "status"]

        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('valor')  # here!
            self.exclude.append('data_criacao')
            self.exclude.append('added_by')
        return super(IndicacaoAdmin, self).get_form(request, obj, **kwargs)

    def get_list_filter(self, request):
        if request.user.is_superuser:
            return ('cliente', 'data_criacao', 'added_by', 'status',)
        else:
            return ('cliente', 'status',)

    def get_queryset(self, request):
        qs = super(IndicacaoAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(added_by=request.user)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'added_by', None) is None:
            obj.added_by = request.user
        obj.save()


admin.site.register(Indicacao, IndicacaoAdmin)
