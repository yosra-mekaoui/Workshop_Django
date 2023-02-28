from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage, name="Home_Page"),
    path('listStatic/', listEventsStatic, name="events_list_static"),
    path('list/', listEvents, name="events_list"),
    path('add/', addEvent, name="events_add"),
    path('details/<int:id>', detailsEvent, name="events_details"),
    path('listEvents/', EventsList.as_view(), name="events_listC"),
    path('eventsDetails/<int:pk>', EventsDetails.as_view(), name="events_DetailsC"),
    path('participate/<int:id>', participateEvent, name="events_participate"),
    path('eventsUpdate/<int:pk>', EventUpdateView.as_view(), name="events_UpdateC"),
    # path('eventsDelete/<int:id>', EventDeleteView, name="events_DeleteC"),
    path('eventsDelete/<int:pk>', EventDeleteView.as_view(), name="events_DeleteC"),
    path('cancelPart/<int:id>', CancelParticipate, name="cancel_Participate"),
]
