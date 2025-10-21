from django.urls import path
from . import views


app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('add/', views.add_product, name='add_product'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
]
