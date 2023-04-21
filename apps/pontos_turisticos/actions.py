# criar action para aprovar
def aprova_ponto_turistico(modelAdmin, request, queryset):
    # atualizar o status
    queryset.update(status=True)
    
# criar action para reprovar
def reprova_ponto_turistico(modelAdmin, request, queryset):
    # atualizar o status
    queryset.update(status=False)