from django.urls import path
from . import views

urlpatterns = [
    path('results/', views.ResultsView.as_view(), name = 'results'),
    path('', views.InitialView.as_view(), name = 'initial'),
    ]