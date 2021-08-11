from . import views
from django.urls import path

urlpatterns = [
    path('/', view=views.home_view, name="home"),
]