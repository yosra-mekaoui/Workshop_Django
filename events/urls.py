#on a ajouter ce fichier manuelement pour les bonnes pratiques de django
from django.urls import path
from .views import *
urlpatterns = [
    path('', homePage, name ="Home_Page"),
    path('listStatic/', listEventsStatic, name="events_list_static"),
    path('list/', listEvents, name="events_list"),

]
