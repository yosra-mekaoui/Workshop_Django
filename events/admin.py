from django.contrib import admin
from .models import *


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display= (
        'title',
        'category',
        'state'
    )
    ordering = ('title',)
    list_filter = ('state', 'category')
    # input de recherche
    search_fields = [
        'title',
        'category'
    ]
    # pagination
    list_per_page = 5



    # bch nbadl l'ordre ta3 l'affichage de formulaire nhbouch yjini mnadhm kima ena hatitou fl code
    # ('title','description') hedhom hatinhom fard ligne 5ater nhbhom fl formulaire ykounou bjnab b3dhhom

    # bch nhotha fi commentaire 5ater ya nhotha hya ya nhot fieldsets

    # fields = (
    #     'organizer',
    #     'state',
    #     ('title','description'), 
    #     'category',
    #     'eventDate',
    #     'eventImage',
    #     'nbrParticipants',
    #     ('created_at','updated_at')


    # )




    # hedhom juste kif nhb nra el created wl updated puisque houma njmch nbdl fihom donc n3ml readonly w nzidhom fl fields
    readonly_fields =('created_at','updated_at')

    # groupement des fileds
    # 'classes' : ('collapse',),  hedhi zdnha kif ena nhb el fields hadhika ma todhrch direct ela ma ena n3ml show
    fieldsets = (
        (
            'STATE',
            {
                'classes' : ('collapse',),
                'fields': (('state','category'),
                ('created_at','updated_at'))
            }
        ),
        (
            'ABOUT',
            {
                'fields': (
                    'title',
                    'description',
                    'nbrParticipants',
                    'eventImage',
                    'eventDate'
                )
            }
        )
    )


admin.site.register(Event, EventAdmin)
