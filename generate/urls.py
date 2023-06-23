from django.urls import path
from . import views


urlpatterns = [
    path(route='', view=views.generate_view, name="generate-view"),
]