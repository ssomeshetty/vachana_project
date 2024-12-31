from django.urls import path
from . import views

app_name = 'vachanas'

urlpatterns = [
    # Define your app's URL patterns here
    path('vachanas/', views.vachana_list, name='vachana_list'),
    path('', views.some_view, name='some_view'),
    path('like/<int:vachana_id>/', views.like_vachana, name='like_vachana'),  # Add this line
    path('post/', views.create_vachana, name='create_vachana'),


]
