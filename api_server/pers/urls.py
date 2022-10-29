from django.urls import path

from . import views

urlpatterns = [
    path("parse", views.parse_file, name='parse'),
    path("ce", views.ce_test, name='ca')
]