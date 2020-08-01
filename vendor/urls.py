from django.urls import path
from vendor import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexVendor, name="IndexVendor"),
    path('bukatoko/', views.IndexBukaToko, name="IndexBukaToko"),
    path('posting/', views.posting, name="posting"),
    path('manageposting/', views.ManagePosting, name="ManagePosting"),
    path('manageposting/delete/<str:kode>', views.ManageDelete, name="ManageDelete"),
    path('managepembeli/', views.ManagePembeli, name="ManagePembeli"),
    path('managepembeli/konfirmasi/<str:kode>', views.konfirmasi, name="konfirmasi"),
    path('managepembeli/download/<str:path>', views.download , name="download"),
    path('managepembeli/cetak/<str:kode>',views.TestDocument, name='cetakdokumen'),
    path('logout/', views.keluar, name="logout"),
    path('EditPosting/<str:kode>', views.EditPosting, name="EditPosting"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
