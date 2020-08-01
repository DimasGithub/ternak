from django.contrib import admin
from django.urls import path, include
from details import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('<str:kodetoko>/<str:kode>', views.index, name="index"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
