from django.contrib import admin, messages
from .models import *


# Register your models here.

#juste design
class ParticipateInline(admin.TabularInline):
    model = Participation
    extra = 1
    readonly_fields =('datePart',)
    can_delete = False

def set_Accept(ModelAdmin, request, queryset)  :
    rows = queryset.update(state=True) 
    if rows == 1:
        message = "One event was "
    else:
        message = f"{rows} events were"
    messages.success(request, message="% successfully accepted" % message)  

set_Accept.short_description = 'Accept'

class ParticipateListFilter(admin.SimpleListFilter):
    title='Participation'
    parameter_name = 'nbrParticipants'

    def lookups(self, request, model_admin):
      return (
        ('0', 'No Participants'),
        ('more', 'There are Participants'),
      )
    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(nbrParticipants__exact=0)
        if self.value() == 'more':
            return queryset.filter(nbrParticipants__gt=0)

# @admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    def set_Refuse(self, request, queryset):
        rows = queryset.filter(state=False)
        if rows.count() > 0:
            messages.error(request,message=f"{rows.count()} events already refused" )
        else:
           rows = queryset.update(state=False)  
           if  rows == 1: 
                message = "One event was "
           else:
                message = f"{rows} events were"
           messages.success(request, message="% successfully refused" % message)  

    set_Refuse.short_description = 'Refuse'
    # l'appel ta3 inlines w l les actions w dima fi west tab [ ]
    actions = [set_Accept, "set_Refuse"]
    inlines = [
            ParticipateInline
    ]
    list_display= (
        'title',
        'category',
        'state'
    )
    ordering = ('title',)
    list_filter = ('state', 'category', ParticipateListFilter)
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

# bch nzid attribut participation tawa  sinon njm nzidha bl decorateur lfou9(  @admin.register(Event)  ) w hwa yapliquili el modification eli sart fl classe event
admin.site.register(Participation)

