from django.urls import path

from . import views

urlpatterns = [
    path('', views.upload_file),
    path('update/',views.update),
]
