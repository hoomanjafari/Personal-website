from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('search-page/', views.SearchView.as_view(), name='search-page'),
]
