from django.urls import path
from . import views

app_name = 'diceroller'
urlpatterns = [
    path('',views.home,name='home'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name = 'results'),
    path('start/', views.InitialView.as_view(), name = 'initial'),
    path('roll/',views.roll,name='roll'),
    ]