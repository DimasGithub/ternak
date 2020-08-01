from django.urls import path
from user import views

urlpatterns = [
    path('', views.IndexUser, name="IndexUser"),
    path('checkout', views.IndexCheckout, name="IndexCheckout"),
    path('checkout/<str:kode>', views.ManageDelete, name="ManageDelete"),
    path('checkout/confirm/<str:kode>', views.confirmDelete, name="confirmDelete"),
    path('beli/<str:kode>', views.pembelian, name="beli"),
    path('logout/', views.keluar, name="logout"),
]
