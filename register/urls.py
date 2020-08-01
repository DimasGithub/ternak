from django.urls import path, include
from register import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns = [
    path('', views.register, name="register"),
    path('edituser/', views.edituser, name="edituser"),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
