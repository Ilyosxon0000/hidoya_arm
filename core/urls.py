from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include("users.urls")),
    path('api/v1/', include(router.urls))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
