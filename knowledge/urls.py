from django.urls import path

from . import views

urlpatterns = [
    path('knowledgeBase/', views.knowledgeBase, name='knowledgeBase'),
    path('patch/<flag>/', views.patch),
    path('revert/<flag>/', views.revert),
]
