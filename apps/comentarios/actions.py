# criar action para aprovar
def aprova_comentario(modelAdmin, request, queryset):
    # atualizar o status
    queryset.update(status=True)
    
# criar action para reprovar
def reprova_comentario(modelAdmin, request, queryset):
    # atualizar o status
    queryset.update(status=False)