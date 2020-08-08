from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add/', views.add, name='add'),
    path('add/add_new', views.add_new, name='add_new'),
]