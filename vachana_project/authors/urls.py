# authors/urls.py
from django.urls import path
from . import views

app_name = 'authors'  # This defines the namespace for the 'authors' app


urlpatterns = [
    path('<int:author_id>/', views.author_detail, name='author_detail'),
]
