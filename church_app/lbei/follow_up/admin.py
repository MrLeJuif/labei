from django.contrib import admin
from .models import Role, Bacenta, Basonta, Membre, Branche


# Register your models here.
class FollowUpAdmin(admin.ModelAdmin):
   list_display = ('pk', 'nom_membre', 'prenom_membre', 'numero_membre',
                   'adresse_membre', 'role_membre', 'basonta_membre',
                   'bacenta_membre', 'bapteme_esprit', 'bapteme_eau',
                   'date_ajout_membre')
   search_fields = ['role_membre']


class BasontaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nom_basonta', 'leader_basonta')
    search_fields = ['nom_basonta']


class BacentaAdmin(admin.ModelAdmin):
   list_display = ('pk', 'nom_bacenta', 'leader_bacenta')
   search_fields = ['nom_bacenta']


class RoleAdmin(admin.ModelAdmin):
   list_display = ('pk', 'nom_role')
   search_fields = ['nom_role']


class BrancheAdmin(admin.ModelAdmin):
   list_display = ('pk', 'nom_branche', 'leader_branche')
   search_fields = ['nom_branche']


admin.site.register(Role, RoleAdmin)
admin.site.register(Basonta, BasontaAdmin)
admin.site.register(Bacenta, BacentaAdmin)
admin.site.register(Branche, BrancheAdmin)
admin.site.register(Membre, FollowUpAdmin)

# pip install bcrypt
# pip install django[argon2]
