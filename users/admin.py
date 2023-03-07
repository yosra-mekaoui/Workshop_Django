from django.contrib import admin, messages
from .models import *

# Register your models here.

# admin.site.register(Person)
class PersonAdmin(admin.ModelAdmin):
    ordering = ('username',)
    list_filter = ('username', 'email')
    # input de recherche
    search_fields = [
        'username',
        'cin'
    ]
    # pagination
    list_per_page = 5

    fieldsets = (
        (
            'STATE',
            {
                'classes' : ('collapse',),
                'fields': (('first_name','last_name'),
                ('date_joined'),
                ('is_active','is_staff'))
            }
        ),
        (
            'ABOUT',
            {
                'fields': (
                    'cin',
                    'username',
                    'email',
                    'password'
                )
            }
        ),
    )

admin.site.register(Person, PersonAdmin)