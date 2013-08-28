#encoding:utf-8
from principal.models import Obra, Video
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, User

class UserAdmin(admin.ModelAdmin):
    list_display = (
                    'username',
                    'password',
                    'email',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'last_login',
                    'date_joined',
                    'first_name',
                    'last_name',
                    'sexo',
                    'dni',
                    'fecha_nacimiento',
                    'tipo_usuario',
                    'direccion',
                    'cp',
                    'poblacion',
                    'provincia',
                    'telefono',
                    'foto',
                    'estado',
                    'twitter',
                    'facebook' 
                    )
    fieldsets = (
                    ('Información básica',
                        {
                            'fields': ('username', 'password', 'email')
                        }),
                     ('Información personal',
                        {
                            'fields':('first_name', 'last_name','dni','sexo','fecha_nacimiento','direccion', 'cp', 'poblacion', 'provincia', 'telefono', 'foto')
                        }),
                    ('Información adicional',
                        {
                            'fields':('twitter', 'facebook')
                        }),
                    ('Permisos',
                        {
                            'fields':('is_active', 'is_staff', 'is_superuser', 'tipo_usuario', 'estado')
                        }),
                    ('Otros',
                        {
                            'fields':('date_joined', 'last_login')
                        }),    
                 )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Obra)
admin.site.register(Video)
