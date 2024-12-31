
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vachanas/', include('vachanas.urls', namespace='vachanas')),  # Add namespace to 'vachanas' app
    # path('authors/', include('authors.urls')),
    path('users/', include('users.urls')),
    path('authors/', include('authors.urls')),  # Include the authors app's URLs

    path('', TemplateView.as_view(template_name='base.html'), name='base'), 
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
