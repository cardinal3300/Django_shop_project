from django.urls import path
from catalog.views import (
    ContactsView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
    ProductDeleteView,
    ProductCreateView,
)


app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_confirm_delete')
]
