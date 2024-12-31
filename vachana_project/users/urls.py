from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


app_name = 'users'


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),

    path('logout/', LogoutView.as_view(), name='logout'),  # Logout URL


]
