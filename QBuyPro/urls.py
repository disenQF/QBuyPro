from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from QBuyPro import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('active/', include('actives.urls', namespace='active')),
    path('user/', include('user.urls', namespace='user')),
]+static(settings.MEDIA_URL,
         document_root=settings.MEDIA_ROOT)
