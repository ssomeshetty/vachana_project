from django.urls import path
from . import views

app_name = 'authors'  # This defines the namespace for the 'authors' app


urlpatterns = [
    path('<int:author_id>/', views.author_detail, name='author_detail'),
]

from django.conf import settings
from django.conf.urls.static import static
# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)