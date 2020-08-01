from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name="index"),
    path('register/',include(('register.urls','register'), namespace='register')),
    path('admin/', admin.site.urls),
    path('login/', include(('login.urls', 'login'), namespace='login')),
    path('user/', include(('user.urls', 'user'), namespace='user')),
    path('<str:cat>', views.indexCat, name="indexCat"),
    # path('search/<str:key>', views.indexSearch, name="indexSearch"),
    path('vendor/', include(('vendor.urls', 'vendor'), namespace='vendor')),
    path('details/',include(('details.urls','details'), namespace='details')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
