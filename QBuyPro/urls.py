from django.contrib import admin
from django.conf.urls.static import static
from django.shortcuts import render
from django.urls import path, include

from api import api_router

from QBuyPro import settings


def to_index(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(api_router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('active/', include('actives.urls', namespace='active')),
    path('user/', include('user.urls', namespace='user')),
    path('', to_index)
]+static(settings.MEDIA_URL,
         document_root=settings.MEDIA_ROOT)
