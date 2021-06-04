from django.urls.conf import path
from . import views

urlpatterns = [
    path('',views.Home,name="home"),
    path('about',views.about,name="about"),
    path('contest',views.contest,name="contest"),
    path('event',views.event,name="event"),
]
