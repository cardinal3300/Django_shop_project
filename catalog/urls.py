from django.urls import path
from catalog.views import HomeView, ContactsView, ProductDetailView, AddProductView


app_name = 'catalog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('add/', AddProductView.as_view(), name='add_product'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
