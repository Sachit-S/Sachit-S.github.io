from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('/faq', views.faq),
    path("/policy", views.policy),
    path("/features", views.feature)
]