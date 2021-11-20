from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _ # convierte cadenas de texto en texto legible para el humano

# se da acceso al administrador Para editar y crear

from .models.user    import UserProfile
from .models.address import Address

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'fullname']
    fieldsets = ( # son los campos que tenemos
    # Aqui definimos las secciones para nuestros filedsets, create, y change page
        # Cada uno de estos parentesis va ha ser una seccion
        #  el primer elmento va a ser el titulo de la seccion 
        #  el segundo elemento va a ser un diccionario con los campos
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('fullname',)}),
        (
            _('Permissions'),
            {'fields':('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important Dates'), {'fields': ('last_login',)})
    )
    # Agregar usuarios desde el admin
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('email', 'password1', 'password2')
        }),
    )

admin.site.register(UserProfile, UserAdmin)
admin.site.register(Address)
